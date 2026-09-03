import os
from datetime import date
from flask import Flask, render_template, request, jsonify, send_from_directory
from google import genai
from google.genai import types
from dotenv import load_dotenv
import pypdf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tenacity import retry, stop_after_attempt, wait_exponential

load_dotenv()
app = Flask(__name__)

user_usage = {}
DAILY_LIMIT = 30

client = None
try:
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        client = genai.Client(api_key=api_key)
    else:
        client = genai.Client()
    print("Gemini client initialized successfully.")
except Exception as e:
    print(f"Warning: Gemini client initialization failed. Please set GEMINI_API_KEY. Error: {e}")

SUBJECTS = {
    "svt": {"name": "علوم الحياة والأرض", "tutor": "الأستاذ ابن سينا", "emoji": "🧬", "tutor_emoji": "👨‍🏫"},
    "math": {"name": "الرياضيات", "tutor": "الأستاذ عمر الخيام", "emoji": "📐", "tutor_emoji": "👨‍🏫"},
    "physics": {"name": "الفيزياء والكيمياء", "tutor": "الأستاذ نيوتن", "emoji": "🧲", "tutor_emoji": "👨‍🔬"},
    "philosophy": {"name": "الفلسفة", "tutor": "الأستاذ ابن رشد", "emoji": "🧠", "tutor_emoji": "🧔"},
    "islamic": {"name": "التربية الإسلامية", "tutor": "الأستاذ مالك", "emoji": "🕌", "tutor_emoji": "👳‍♂️"},
    "arabic": {"name": "اللغة العربية", "tutor": "الأستاذ سيبويه", "emoji": "📖", "tutor_emoji": "👨‍🏫"},
    "french": {"name": "الفرنسية", "tutor": "Prof. Molière", "emoji": "🗼", "tutor_emoji": "👨‍🏫"},
    "english": {"name": "الإنجليزية", "tutor": "Mr. Shakespeare", "emoji": "", "custom_image": "BigBen.png", "tutor_emoji": "👨‍🏫"},
    "informatique": {"name": "المعلوميات", "tutor": "الأستاذ الخوارزمي", "emoji": "💻", "tutor_emoji": "👨‍💻"},
    "history": {"name": "الاجتماعيات", "tutor": "الأستاذ ابن خلدون", "emoji": "🌍", "tutor_emoji": "🧔"}
}

def get_system_prompt(subject_id, language, student_name="التلميذ"):
    subject_info = SUBJECTS.get(subject_id, SUBJECTS["svt"])
    subject_name = subject_info["name"]
    tutor_name = subject_info["tutor"]

    prompt = f"""
أنت {tutor_name}، مدرس متخصص وذكي لمادة {subject_name} موجه لتلاميذ الأولى باكالوريا علوم تجريبية في المغرب.
الطالب الذي تتحدث معه الآن اسمه '{student_name}'. يرجى مناداته باسمه بين الحين والآخر لجعله يشعر بالاهتمام والترحيب.
يجب أن تتحدث باللغة {language}.
    
إذا طلب التلميذ شرحاً أو صوراً أو أمثلة مرئية، يحق لك تضمين روابط صور حقيقية (مثل صور علمية من ويكيميديا أو مصادر تعليمية) عبر استخدام وسوم HTML مباشرة.
لا تستخدم الماركداون للصور، بل استخدم فقط وسوم HTML مثل:
<img src="URL" style="max-width:100%; border-radius:8px; margin-top:10px;" alt="description">
تأكد من أن الروابط تعمل وصحيحة.

قواعد صارمة:
1. التزم بمنهج الأولى باكالوريا علوم تجريبية.
2. لا تجب عن أسئلة خارج مادة {subject_name} أو خارج الإطار التعليمي.
3. استخدم أمثلة من الواقع لتسهيل الفهم، وادعم إجاباتك بالتفكير التحليلي.
4. شجع التلميذ دائماً بعبارات تحفيزية.
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

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=15))
def call_gemini_with_retry(prompt, system_instruction):
    return client.models.generate_content(
        model='gemini-3.6-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.7
        )
    )

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
    return render_template("subject.html", 
                           subject_id=subject_id, 
                           subject_name=sub["name"], 
                           tutor_name=sub["tutor"], 
                           tutor_emoji=sub["tutor_emoji"])

@app.route("/api/chat", methods=["POST"])
def chat():
    user_id = get_user_identifier()
    
    if not check_daily_limit(user_id):
        return jsonify({"error": "لقد تجاوزت الحد المسموح به وهو 30 رسالة يومياً. عد غداً!"}), 429
        
    data = request.json
    user_message = data.get("message", "")
    language = data.get("language", "العربية")
    subject_id = data.get("subject_id", "svt")
    student_name = data.get("student_name", "التلميذ")
    
    if not user_message:
        return jsonify({"error": "رسالة فارغة"}), 400
        
    if not client:
        return jsonify({"error": "مفتاح API غير صالح."}), 500
        
    try:
        if subject_id == "svt":
            context = retrieve_relevant_context(user_message)
            prompt = f"سؤال الطالب: {user_message}\n\nمعلومات من المقرر الدراسي (استخدمها إذا كانت مفيدة فقط):\n{context}"
        else:
            # We don't have RAG for other subjects yet
            prompt = user_message

        sys_prompt = get_system_prompt(subject_id, language, student_name)
        response = call_gemini_with_retry(prompt, sys_prompt)
        
        increment_daily_limit(user_id)
        
        return jsonify({
            "response": response.text,
            "remaining": DAILY_LIMIT - user_usage[user_id]["count"]
        })
        
    except Exception as e:
        return jsonify({"error": f"حدث خطأ: {str(e)}"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=False)
