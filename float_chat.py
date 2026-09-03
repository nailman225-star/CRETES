import re

with open('templates/subject.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update .main-content to center its children
new_main_content = '''        .main-content { flex-grow: 1; display: flex; justify-content: center; align-items: center; padding: 20px; background-color: #f4f6f9; }'''
content = re.sub(r'\.main-content \{.*?\}', new_main_content, content, flags=re.DOTALL)

# Update .chat-container to have max-width, height, and nice shadow
new_chat_container = '''        .chat-container { width: 100%; max-width: 900px; height: 90vh; background-color: var(--chat-bg); border-radius: 15px; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1); display: flex; flex-direction: column; overflow: hidden; }'''
content = re.sub(r'\.chat-container \{.*?\}', new_chat_container, content, flags=re.DOTALL)

with open('templates/subject.html', 'w', encoding='utf-8') as f:
    f.write(content)
