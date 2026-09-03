import re
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

new_subjects = '''SUBJECTS = {
    "svt": {"name": "علوم الحياة والأرض", "tutor": "الأستاذ ابن سينا", "emoji": "🧬"},
    "math": {"name": "الرياضيات", "tutor": "الأستاذ الخوارزمي", "emoji": "📐"},
    "physics": {"name": "الفيزياء والكيمياء", "tutor": "الأستاذ نيوتن", "emoji": "🧲"},
    "philosophy": {"name": "الفلسفة", "tutor": "الأستاذ ابن رشد", "emoji": "🧠"},
    "islamic": {"name": "التربية الإسلامية", "tutor": "الأستاذ مالك", "emoji": "🕌"},
    "arabic": {"name": "اللغة العربية", "tutor": "الأستاذ سيبويه", "emoji": "📖"},
    "french": {"name": "الفرنسية", "tutor": "Prof. Molière", "emoji": "🗼"},
    "english": {"name": "الإنجليزية", "tutor": "Mr. Shakespeare", "emoji": "🇬🇧"},
    "informatique": {"name": "المعلوميات", "tutor": "الأستاذ تورينغ", "emoji": "💻"},
    "history": {"name": "الاجتماعيات", "tutor": "الأستاذ ابن خلدون", "emoji": "🌍"}
}'''

content = re.sub(r'SUBJECTS = \{.*?\n\}', new_subjects, content, flags=re.DOTALL)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)
