import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('"english": {"name": "الإنجليزية", "tutor": "Mr. Shakespeare", "emoji": "🇬🇧"', '"english": {"name": "الإنجليزية", "tutor": "Mr. Shakespeare", "emoji": "🏰"')

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)
