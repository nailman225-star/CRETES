import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update hero section HTML
new_hero = '''    <div class="hero">
        <h1 data-i18n="hero_title" style="margin: 0 0 10px 0; font-size: 2.8rem; font-weight: 900; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">🎓 منصة قمم التعليمية</h1>
        <h2 id="welcome-student" style="margin: 0 0 20px 0; font-size: 1.5rem; font-weight: normal; color: rgba(255,255,255,0.9);"></h2>
        <div class="level-badge" data-i18n="hero_subtitle" style="display: inline-block; background: rgba(0,0,0,0.2); padding: 8px 20px; border-radius: 20px; font-weight: bold; margin-bottom: 25px;">مستوى: الأولى باكالوريا علوم تجريبية</div>
        <div>
            <span class="quote" id="quote-text" data-i18n="quote" style="display: inline-block; background: rgba(255,255,255,0.2); border: 1px solid rgba(255,255,255,0.3); padding: 12px 25px; border-radius: 30px; font-size: 1.1rem; font-weight: bold; text-shadow: 0 1px 2px rgba(0,0,0,0.2);">"النجاح ليس صدفة، بل هو عمل شاق، مثابرة، وتعلّم مستمر." 🌟</span>
        </div>
    </div>'''

content = re.sub(r'<div class="hero">.*?</div>', new_hero, content, flags=re.DOTALL)

# Update emoji size in .card-icon CSS
content = re.sub(r'\.card-icon \{.*?\}', '.card-icon { font-size: 4.5rem; margin-bottom: 15px; display: inline-block; transition: transform 0.3s; }', content, flags=re.DOTALL)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
