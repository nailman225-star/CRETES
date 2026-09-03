import os
from datetime import date
from flask import Flask, render_template, request, jsonify, send_from_directory
import requests
import pypdf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

user_usage = {}
DAILY_LIMIT = 30
client = True  # متغير توافقية لتجنب أخطاء الفحص القديمة

API_KEY = os.environ.get("GEMINI_API_KEY")

def generate_gemini_response(prompt_text, system_instruction=''):
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}'
    headers = {'Content-Type': 'application/json'}
    payload = {
        'contents': [{'parts': [{'text': prompt_text}]}]
    }
    if system_instruction:
        payload['systemInstruction'] = {'parts': [{'text': system_instruction}]}
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            res_json = response.json()
            return res_json['candidates'][0]['content']['parts'][0]['text']
        else:
            return f'خطأ من الخادم ({response.status_code}): {response.text}'
    except Exception as e:
        return f'حدث خطأ في الاتصال: {str(e)}'

SUBJECTS = {
    'svt': {'name': 'علوم الحياة والأرض', 'tutor': 'الأستاذ ابن سينا', 'emoji': '🧬', 'tutor_emoji': '👨‍🏫'},
    'math': {'name': 'الرياضيات', 'tutor': 'الأستاذ عمر الخيام', 'emoji': '📐', 'tutor_emoji': '👨‍🏫'},
    'physics': {'name': 'الفيزياء والكيمياء', 'tutor': 'الأستاذ نيوتن', 'emoji': '⚗️', 'tutor_emoji': '👨‍🏫'},
    'philosophy': {'name': 'الفلسفة', 'tutor': 'الأستاذ ابن رشد', 'emoji': '📖', 'tutor_emoji': '👩‍🏫'},
    'arabic': {'name': 'اللغة العربية', 'tutor': 'الأستاذة عائشة البونية', 'emoji': '✍️', 'tutor_emoji': '👩‍🏫'},
    'english': {'name': 'اللغة الإنجليزية', 'tutor': 'الأستاذة مايا', 'emoji': '🌐', 'tutor_emoji': '👩‍🏫'}
}

def get_system_prompt(subject_id, language, student_name="التلميذ", student_level=""):
    subject_info = SUBJECTS.get(subject_id, SUBJECTS["svt"])
    subject_name = subject_info["name"]
    tutor_name = subject_info["tutor"]
    
    level_text = f" للمستوى {student_level}" if student_level else ""

    prompt = f"""
أنت {tutor_name}، مدرس ذكي متخصص في مادة {subject_name}{level_text} تقدم الشروحات 
والدروس بطريقة تفاعلية ومبسطة للطلاب.
أنت تتحدث مع طالب اسمه '{student_name}'. استعمل اسمه أحياناً في الشرح ليكون التفاعل شخصياً ومحبباً.
يجب أن تتحدث باللغة {language}.
    
إذا تم سؤالك عن أي موضوع لا علاقة له بمادة تخصصك (أو عن معلومات غير دراسية مثل السياسة أو الرياضة) يجب أن تعتذر بلطف 
وتخبر الطالب أنك معلم لهذه المادة فقط.
يمكنك استخدام تنسيق HTML بسيط.
إذا أردت عرض صورة لتوضيح فكرة ما استخدم كود HTML كالتالي:
<img src="URL" style="max-width:100%; border-radius:8px; margin-top:10px;" alt="description">
حيث أن URL هو رابط الصورة.

مهمتك الآن:
1. أجب بأسلوب مشجع ومحفز يناسب سن الطالب{level_text}.
2. كن دقيقاً في معلومات مادة {subject_name} ومطابقاً للمقرر الدراسي.
3. اطرح سؤالاً في النهاية لتتأكد من فهم الطالب أو لتحفزه على التفكير.
4. تجنب الإجابات الطويلة جداً والمملة.
"""
    return prompt

# RAG System Variables
documents = []
vectorizer = TfidfVectorizer(stop_words=None)
tfidf_matrix = None

def initialize_rag():
    global documents, tfidf_matrix
    data_dir = os.path.join(os.path.dirname(__file__), 'DATA')
    if not os.path.exists(data_dir):
        print("DATA directory not found.")
        return

    print("Reading and chunking PDFs for local RAG...")
    text_chunks = []
    for filename in os.listdir(data_dir):
        if filename.lower().endswith('.pdf'):
            path = os.path.join(data_dir, filename)
            try:
                reader = pypdf.PdfReader(path)
                current_chunk = ""
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        current_chunk += text + "\n"
                        if len(current_chunk) > 1500:
                            text_chunks.append(current_chunk)
                            current_chunk = ""
                if current_chunk:
                    text_chunks.append(current_chunk)
                print(f"Processed {filename}: {len(text_chunks)} chunks so far.")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    
    if text_chunks:
        documents = text_chunks
        tfidf_matrix = vectorizer.fit_transform(documents)
        print(f"RAG initialized successfully with {len(documents)} chunks.")
    else:
        print("No text found in PDFs to index.")

initialize_rag()

def retrieve_relevant_context(query, top_k=3):
    if not documents or tfidf_matrix is None:
        return ""
    
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    
    top_indices = similarities.argsort()[-top_k:][::-1]
    relevant_chunks = [documents[i] for i in top_indices if similarities[i] > 0.03]
    
    if not relevant_chunks:
        return ""
        
    return "\n\n---\n\n".join(relevant_chunks)

def get_user_identifier():
    return request.remote_addr

def check_daily_limit(user_id):
    today = str(date.today())
    if user_id not in user_usage or user_usage[user_id]["date"] != today:
        user_usage[user_id] = {"date": today, "count": 0}
    if user_usage[user_id]["count"] >= DAILY_LIMIT:
        return False
    return True

def increment_daily_limit(user_id):
    user_usage[user_id]["count"] += 1

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def index():
    data_dir = os.path.join(os.path.dirname(__file__), 'DATA')
    images = []
    if os.path.exists(data_dir):
        images = sorted([f for f in os.listdir(data_dir) if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg')])
    
    subjects_list = []
    for i, (sid, info) in enumerate(SUBJECTS.items()):
        img_name = images[i % len(images)] if images else ""
        subjects_list.append({
            "id": sid,
            "name": info["name"],
            "tutor": info["tutor"],
            "emoji": info["emoji"],
            "custom_image": f"/data/{info['custom_image']}" if "custom_image" in info else ""
        })
        
    return render_template("index.html", subjects=subjects_list)

@app.route("/data/<path:filename>")
def serve_data(filename):
    return send_from_directory("DATA", filename)

@app.route("/subject/<subject_id>")
def subject_page(subject_id):
    if subject_id not in SUBJECTS:
        return "المادة غير موجودة", 404
    sub = SUBJECTS[subject_id]
    
    # Receive the educational level from query parameter (for dynamic titles)
    student_level = request.args.get('level', '')
    
    title_suffix = f" - {student_level}" if student_level else ""

    return render_template("subject.html", 
                           subject_id=subject_id, 
                           subject_name=sub["name"] + title_suffix, 
                           tutor_name=sub["tutor"], 
                           tutor_emoji=sub["tutor_emoji"],
                           student_level=student_level)

@app.route("/api/chat", methods=["POST"])
def chat():
    user_id = get_user_identifier()
    
    if not check_daily_limit(user_id):
        return jsonify({"error": "لقد استنفدت الحد اليومي من الرسائل (30). عد غداً!"}), 429
        
    data = request.json
    user_message = data.get("message", "")
    language = data.get("language", "العربية")
    subject_id = data.get("subject_id", "svt")
    student_name = data.get("student_name", "التلميذ")
    student_level = data.get("student_level", "")
    
    if not user_message:
        return jsonify({"error": "رسالة فارغة"}), 400
        
    if not client: # legacy fallback if needed
        pass
        
    try:
        if subject_id == "svt":
            context = retrieve_relevant_context(user_message)
            prompt = f"سؤال الطالب: {user_message}\n\nمعلومات من المقرر الدراسي (استخدمها إذا كانت مفيدة فقط):\n{context}"
        else:
            # We don't have RAG for other subjects yet
            prompt = user_message

        sys_prompt = get_system_prompt(subject_id, language, student_name, student_level)
        response_text = generate_gemini_response(prompt, sys_prompt)
        
        increment_daily_limit(user_id)
        
        return jsonify({
            "response": response_text,
            "remaining": DAILY_LIMIT - user_usage[user_id]["count"]
        })
        
    except Exception as e:
        return jsonify({"error": f"حدث خطأ: {str(e)}"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=False)
