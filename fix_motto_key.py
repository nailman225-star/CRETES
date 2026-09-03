import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('data-i18n="hero_motto"', 'data-i18n="motto"')

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
