import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_grid_css = '''        .grid { 
            display: grid; 
            grid-template-columns: repeat(5, 1fr); 
            gap: 20px; 
            padding: 20px 0;
        }
        @media (max-width: 1400px) {
            .grid { grid-template-columns: repeat(4, 1fr); }
        }
        @media (max-width: 1100px) {
            .grid { grid-template-columns: repeat(3, 1fr); }
        }
        @media (max-width: 800px) {
            .grid { grid-template-columns: repeat(2, 1fr); }
        }
        @media (max-width: 500px) {
            .grid { grid-template-columns: 1fr; }
        }'''

content = re.sub(r'        \.grid \{.*?\}', new_grid_css, content, flags=re.DOTALL)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
