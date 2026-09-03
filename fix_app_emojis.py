import re
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

new_subjects = '''SUBJECTS = {
    "svt": {"name": "علوم الحياة والأرض", "tutor": "الأستاذ ابن سينا", "emoji": "🧬", "tutor_emoji": "👨‍🏫"},
    "math": {"name": "الرياضيات", "tutor": "الأستاذ الخوارزمي", "emoji": "📐", "tutor_emoji": "👨‍🏫"},
    "physics": {"name": "الفيزياء والكيمياء", "tutor": "الأستاذ نيوتن", "emoji": "🧲", "tutor_emoji": "👨‍🔬"},
    "philosophy": {"name": "الفلسفة", "tutor": "الأستاذ ابن رشد", "emoji": "🧠", "tutor_emoji": "🧔"},
    "islamic": {"name": "التربية الإسلامية", "tutor": "الأستاذ مالك", "emoji": "🕌", "tutor_emoji": "👳‍♂️"},
    "arabic": {"name": "اللغة العربية", "tutor": "الأستاذ سيبويه", "emoji": "📖", "tutor_emoji": "👨‍🏫"},
    "french": {"name": "الفرنسية", "tutor": "Prof. Molière", "emoji": "🗼", "tutor_emoji": "👨‍🏫"},
    "english": {"name": "الإنجليزية", "tutor": "Mr. Shakespeare", "emoji": "🇬🇧", "tutor_emoji": "👨‍🏫"},
    "informatique": {"name": "المعلوميات", "tutor": "الأستاذ تورينغ", "emoji": "💻", "tutor_emoji": "👨‍💻"},
    "history": {"name": "الاجتماعيات", "tutor": "الأستاذ ابن خلدون", "emoji": "🌍", "tutor_emoji": "🧔"}
}'''

content = re.sub(r'SUBJECTS = \{.*?\n\}', new_subjects, content, flags=re.DOTALL)

# Update tutor_emoji in app.py render_template
content = re.sub(r'tutor_emoji=sub\["emoji"\]\)', 'tutor_emoji=sub["tutor_emoji"])', content)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)
