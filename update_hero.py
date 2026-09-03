import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the old floating language switcher if it exists
content = re.sub(r'<div style="position: absolute; top: 20px; left: 20px; z-index: 1000;">.*?</div>\s*', '', content, flags=re.DOTALL)

# Replace the hero section entirely
new_hero = '''    <!-- Hero Section -->
    <div class="hero" style="position: relative; min-height: 280px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: linear-gradient(135deg, #2E7D32, #4CAF50); padding: 20px; overflow: hidden;">
        
        <!-- TOP LEFT: French Title -->
        <div style="position: absolute; top: 25px; left: 30px; z-index: 10;">
            <span style="font-size: 1.8rem; font-weight: 900; color: white; text-shadow: 0 2px 4px rgba(0,0,0,0.3); letter-spacing: 0.5px;">Plateforme Éducative LES CRETES</span>
        </div>
        
        <!-- TOP RIGHT: Arabic Title -->
        <div style="position: absolute; top: 25px; right: 30px; z-index: 10;">
            <span style="font-size: 2rem; font-weight: 900; color: white; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">منصة قمم التعليمية</span>
        </div>

        <!-- CENTER: Welcome -->
        <h2 id="welcome-student" style="margin: 30px 0 15px 0; font-size: 1.5rem; font-weight: normal; color: rgba(255,255,255,0.95); text-shadow: 0 1px 3px rgba(0,0,0,0.2); z-index: 10;"></h2>
        
        <!-- CENTER: Motto -->
        <div data-i18n="hero_motto" style="font-size: 2.2rem; font-weight: bold; color: white; text-shadow: 0 2px 5px rgba(0,0,0,0.3); z-index: 10;">
            خطاك نحو القمة تبدأ من هنا
        </div>

        <!-- BOTTOM LEFT: Language Switcher -->
        <div style="position: absolute; bottom: 25px; left: 30px; z-index: 10;">
            <select id="ui-lang" onchange="changeLang(this.value)" style="padding: 10px 30px; border-radius: 6px; border: 2px solid rgba(255,255,255,0.3); background: rgba(0,0,0,0.15); color: white; font-weight: bold; font-size: 1.2rem; outline: none; cursor: pointer; box-shadow: 0 2px 5px rgba(0,0,0,0.2); appearance: none; -webkit-appearance: none; -moz-appearance: none;">
                <option value="ar" style="color: black;">العربية</option>
                <option value="fr" style="color: black;">Français</option>
                <option value="en" style="color: black;">English</option>
            </select>
            <!-- Custom arrow for select -->
            <div style="position: absolute; right: 15px; top: 50%; transform: translateY(-50%); pointer-events: none; color: white; font-size: 0.8rem;">▼</div>
        </div>

        <!-- BOTTOM RIGHT: Level Badge -->
        <div data-i18n="hero_subtitle" style="position: absolute; bottom: 25px; right: 30px; background: rgba(0,0,0,0.25); padding: 10px 20px; border-radius: 6px; font-weight: bold; color: white; font-size: 1.1rem; border: 1px solid rgba(255,255,255,0.1); z-index: 10;">
            مستوى: الأولى باكالوريا علوم تجريبية
        </div>

    </div>'''

content = re.sub(r'<div class="hero">.*?</div>', new_hero, content, flags=re.DOTALL)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
