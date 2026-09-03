import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("model='gemini-3.6-flash'", "model='gemini-2.5-flash'")

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)
