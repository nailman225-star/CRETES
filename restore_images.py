import re
import os

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add back image mapping logic in index()
old_index = '''@app.route("/dashboard")
def index():
    subjects_list = []
    for i, (sid, info) in enumerate(SUBJECTS.items()):
        subjects_list.append({
            "id": sid,
            "name": info["name"],
            "tutor": info["tutor"],
            "emoji": info["emoji"]
        })
        
    return render_template("index.html", subjects=subjects_list)'''

new_index = '''@app.route("/dashboard")
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
            "image": f"/data/{img_name}" if img_name else ""
        })
        
    return render_template("index.html", subjects=subjects_list)'''

content = content.replace(old_index, new_index)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)
