import re
with open('templates/subject.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove .top-nav CSS
content = re.sub(r'\s*/\* Top Navigation Bar \*/.*?flex-shrink: 0;\s*}', '', content, flags=re.DOTALL)

# 2. Remove .top-nav HTML
content = re.sub(r'    <header class="top-nav">.*?</header>', '', content, flags=re.DOTALL)

# 3. Add language switcher to chat header
header_controls = '''                <div class="header-controls">
                    <select id="ui-lang" class="lang-select" onchange="changeLang(this.value)">
                        <option value="ar">العربية</option>
                        <option value="fr">Français</option>
                        <option value="en">English</option>
                    </select>
                    <span class="status-bar" id="remaining-count">الرسائل المتبقية: 30</span>
                </div>'''

content = re.sub(r'                <div class="header-controls">\s*<span class="status-bar".*?</div>', header_controls, content, flags=re.DOTALL)

with open('templates/subject.html', 'w', encoding='utf-8') as f:
    f.write(content)
