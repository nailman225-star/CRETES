import re
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

correct_container = '''    <div class="container">
        <h2 class="section-title" data-i18n="subjects_title">المواد الدراسية</h2>
        <div class="grid">
            {% for subject in subjects %}
            <a href="/subject/{{ subject.id }}" class="card">
                <div class="card-icon">{{ subject.emoji }}</div>
                <h3 class="card-title" data-i18n="sub_{{ subject.id }}">{{ subject.name }}</h3>
                <p class="card-desc" data-i18n="desc_{{ subject.id }}">انقر للتحدث مع {{ subject.tutor }}</p>
            </a>
            {% endfor %}
        </div>
    </div>'''

content = re.sub(r'<div class="container">.*?</script>', correct_container + '\n\n    <script>', content, flags=re.DOTALL)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
