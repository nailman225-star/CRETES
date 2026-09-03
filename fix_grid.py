import re
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_grid = '''        <div class="grid">
            {% for subject in subjects %}
            <a href="/subject/{{ subject.id }}" class="card">
                {% if subject.image %}
                <div class="card-bg" style="background-image: url('{{ subject.image }}');"></div>
                {% endif %}
                <div class="card-overlay"></div>
                <div class="card-content">
                    <div class="card-icon">{{ subject.emoji }}</div>
                    <h3 class="card-title" data-i18n="sub_{{ subject.id }}">{{ subject.name }}</h3>
                    <p class="card-desc" data-i18n="desc_{{ subject.id }}">انقر للتحدث مع {{ subject.tutor }}</p>
                </div>
            </a>
            {% endfor %}
        </div>'''

content = re.sub(r'<div class="grid">.*?</div>', new_grid, content, flags=re.DOTALL)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
