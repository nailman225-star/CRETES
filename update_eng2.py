import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Just replace the emoji field for english directly using regex
content = re.sub(r'("english": \{.*?"emoji":\s*)"[^"]+"', r'\1"🕰️"', content)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)
