import re
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove .top-nav CSS
content = re.sub(r'\s*/\* Top Navigation Bar \*/.*?\s*\.hero \{', '\n        .hero {', content, flags=re.DOTALL)
# Remove media query top-nav if exists
content = re.sub(r'\.top-nav \{ flex-direction: column; gap: 15px; padding: 15px; \}', '', content)

# Remove top-nav HTML
content = re.sub(r'    <!-- Clean, separated Top Navigation -->\s*<header class="top-nav">.*?</header>', '', content, flags=re.DOTALL)

# Let's add a subtle language switcher in the hero section or floating
lang_switcher_html = '''    <div style="position: absolute; top: 20px; left: 20px; z-index: 1000;">
        <select id="ui-lang" onchange="changeLang(this.value)" style="padding: 5px 10px; border-radius: 20px; border: none; background: rgba(255,255,255,0.2); color: white; font-weight: bold; outline: none; cursor: pointer;">
            <option value="ar" style="color: black;">العربية</option>
            <option value="fr" style="color: black;">Français</option>
            <option value="en" style="color: black;">English</option>
        </select>
    </div>'''

content = re.sub(r'<body>', '<body>\n' + lang_switcher_html, content)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
