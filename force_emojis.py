import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

grid_old = '''        <div class="grid">
            {% for subject in subjects %}
            <a href="/subject/{{ subject.id }}" class="card">
                <div class="card-icon">
                    {% if subject.image %}
                    <img src="{{ subject.image }}" alt="{{ subject.name }}" style="width: 75px; height: 75px; object-fit: contain;">
                    {% else %}
                    {{ subject.emoji }}
                    {% endif %}
                </div>
                <h3 class="card-title" data-i18n="sub_{{ subject.id }}">{{ subject.name }}</h3>
                <p class="card-desc" data-i18n="desc_{{ subject.id }}">انقر للتحدث مع {{ subject.tutor }}</p>
            </a>
            {% endfor %}
        </div>'''

grid_new = '''        <div class="grid">
            {% for subject in subjects %}
            <a href="/subject/{{ subject.id }}" class="card">
                <div class="card-icon">{{ subject.emoji }}</div>
                <h3 class="card-title" data-i18n="sub_{{ subject.id }}">{{ subject.name }}</h3>
                <p class="card-desc" data-i18n="desc_{{ subject.id }}">انقر للتحدث مع {{ subject.tutor }}</p>
            </a>
            {% endfor %}
        </div>'''

content = content.replace(grid_old, grid_new)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
