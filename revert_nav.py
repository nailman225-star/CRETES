import re

# FIX INDEX.HTML
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

nav_original = '''    <header class="top-nav">
        <div class="nav-right" style="display: flex; align-items: center; gap: 30px;">
            <div class="brand-ar" style="font-size: 1.8rem; font-weight: 900; color: var(--primary-dark); display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 2.2rem;">🎓</span>
                <span>منصة قمم التعليمية</span>
            </div>
            <div class="lang-switch">
                <select id="ui-lang" class="lang-select" onchange="changeLang(this.value)">
                    <option value="ar">العربية</option>
                    <option value="fr">Français</option>
                    <option value="en">English</option>
                </select>
            </div>
        </div>
        
        <div class="nav-left" style="display: flex; flex-direction: column; align-items: flex-end; text-align: right;">
            <span class="brand-fr" style="font-size: 1.2rem; font-weight: bold; color: #2c3e50; letter-spacing: 0.5px;">Plateforme Éducative LES CRETES</span>
        </div>
    </header>'''

content = re.sub(r'<header class="top-nav">.*?</header>', nav_original, content, flags=re.DOTALL)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# FIX SUBJECT.HTML
with open('templates/subject.html', 'r', encoding='utf-8') as f:
    content = f.read()

nav_original_sub = '''    <header class="top-nav">
        <div class="nav-right" style="display: flex; align-items: center; gap: 30px;">
            <div class="brand-ar" style="font-size: 1.6rem; font-weight: 900; color: var(--primary-dark); display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 2rem;">🎓</span>
                <span>منصة قمم التعليمية</span>
            </div>
            <div class="lang-switch">
                <select id="ui-lang" class="lang-select" onchange="changeLang(this.value)" style="padding: 5px 15px; border-radius: 20px; border: 1px solid #ccc;">
                    <option value="ar">العربية</option>
                    <option value="fr">Français</option>
                    <option value="en">English</option>
                </select>
            </div>
        </div>
        
        <div class="nav-left" style="display: flex; flex-direction: column; align-items: flex-end; text-align: right;">
            <span class="brand-fr" style="font-size: 1.1rem; font-weight: bold; color: #2c3e50; letter-spacing: 0.5px;">Plateforme Éducative LES CRETES</span>
        </div>
    </header>'''

content = re.sub(r'<header class="top-nav">.*?</header>', nav_original_sub, content, flags=re.DOTALL)

with open('templates/subject.html', 'w', encoding='utf-8') as f:
    f.write(content)
