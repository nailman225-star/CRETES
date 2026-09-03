import re
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Revert CSS
css_new = '''        .card { 
            background: var(--card-bg); 
            padding: 30px 20px; 
            border-radius: 15px; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.05); 
            text-align: center; 
            text-decoration: none; 
            color: var(--text);
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .card:hover { 
            transform: translateY(-5px); 
            box-shadow: 0 10px 25px rgba(46, 125, 50, 0.15); 
        }
        .card-icon { 
            font-size: 3.5rem; 
            margin-bottom: 15px; 
            display: inline-block;
            transition: transform 0.3s;
        }
        .card:hover .card-icon { transform: scale(1.1); }
        .card-title { font-size: 1.3rem; color: var(--primary-dark); margin-bottom: 10px; font-weight: bold; }
        .card-desc { font-size: 0.95rem; color: #666; line-height: 1.5; margin: 0; }'''

content = re.sub(r'        \.card \{.*?\.card-desc \{.*?\}', css_new, content, flags=re.DOTALL)

# Revert Grid
grid_new = '''        <div class="grid">
            {% for subject in subjects %}
            <a href="/subject/{{ subject.id }}" class="card">
                <div class="card-icon">{{ subject.emoji }}</div>
                <h3 class="card-title" data-i18n="sub_{{ subject.id }}">{{ subject.name }}</h3>
                <p class="card-desc" data-i18n="desc_{{ subject.id }}">انقر للتحدث مع {{ subject.tutor }}</p>
            </a>
            {% endfor %}
        </div>'''

content = re.sub(r'<div class="grid">.*?</div>', grid_new, content, flags=re.DOTALL)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
