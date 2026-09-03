import re
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

grid_new = '''        <div class="grid">
            {% for subject in subjects %}
            <a href="/subject/{{ subject.id }}" class="card">
                {% if subject.image %}
                <img src="{{ subject.image }}" alt="{{ subject.name }}" style="width: 80px; height: 80px; object-fit: contain; margin: 0 auto 15px auto;">
                {% else %}
                <div class="card-icon">{{ subject.emoji }}</div>
                {% endif %}
                <h3 class="card-title" data-i18n="sub_{{ subject.id }}">{{ subject.name }}</h3>
                <p class="card-desc" data-i18n="desc_{{ subject.id }}">انقر للتحدث مع {{ subject.tutor }}</p>
            </a>
            {% endfor %}
        </div>'''

content = re.sub(r'<div class="grid">.*?</div>', grid_new, content, flags=re.DOTALL)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
