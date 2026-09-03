with open('templates/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if '<div class="grid">' in line:
        start_idx = i
    if '<script>' in line:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    correct_lines = [
        '        <div class="grid">\n',
        '            {% for subject in subjects %}\n',
        '            <a href="/subject/{{ subject.id }}" class="card">\n',
        '                <div class="card-icon">{{ subject.emoji }}</div>\n',
        '                <h3 class="card-title" data-i18n="sub_{{ subject.id }}">{{ subject.name }}</h3>\n',
        '                <p class="card-desc" data-i18n="desc_{{ subject.id }}">انقر للتحدث مع {{ subject.tutor }}</p>\n',
        '            </a>\n',
        '            {% endfor %}\n',
        '        </div>\n',
        '    </div>\n\n'
    ]
    new_lines = lines[:start_idx] + correct_lines + lines[end_idx:]
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
