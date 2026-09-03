import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will find the end of the hero section:
# "    </div>\n        <div>\n            <span class=\"quote\" ... </div>\n    </div>\n        <p class=\"quote\" ... </p>\n    </div>"
# And replace it with just "    </div>"

bad_html_pattern = r'    </div>\s*<div>\s*<span class="quote" id="quote-text".*?</div>\s*</div>\s*<p class="quote" id="quote-text".*?</p>\s*</div>'

content = re.sub(bad_html_pattern, '    </div>', content, flags=re.DOTALL)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
