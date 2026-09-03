import re

with open('templates/subject.html', 'r', encoding='utf-8') as f:
    content = f.read()

bad_html = """        <div class="sidebar">
            <h2 id="sb-title">{{ subject_name }}</h2>
            <h3 id="sb-lessons">📚 المقررات والدروس</h3>
            <ul class="sidebar-list">
                <li><a href="#" id="sb-link1">الوحدة الأولى</a></li>
                <li><a href="#" id="sb-link2">الوحدة الثانية</a></li>
                <li><a href="#" id="sb-link3">الوحدة الثالثة</a></li>
            </ul>
        </div>
        
        <div class="sidebar-section">
            <h3 id="sb-exams">📝 التمارين والامتحانات</h3>
            <ul class="sidebar-list">
                <li><a href="#" id="sb-link4">تمارين تطبيقية</a></li>
                <li><a href="#" id="sb-link5">فروض محروسة</a></li>
            </ul>
        </div>
        
        <a href="/dashboard" class="back-btn" id="sb-back">🏠 العودة للرئيسية</a>
    </div>

    <div class="main-content">"""

good_html = """        <div class="sidebar">
            <h2 id="sb-title">{{ subject_name }}</h2>
            <div class="sidebar-section">
                <h3 id="sb-lessons">📚 المقررات والدروس</h3>
                <ul class="sidebar-list">
                    <li><a href="#" id="sb-link1">الوحدة الأولى</a></li>
                    <li><a href="#" id="sb-link2">الوحدة الثانية</a></li>
                    <li><a href="#" id="sb-link3">الوحدة الثالثة</a></li>
                </ul>
            </div>
            
            <div class="sidebar-section">
                <h3 id="sb-exams">📝 التمارين والامتحانات</h3>
                <ul class="sidebar-list">
                    <li><a href="#" id="sb-link4">تمارين تطبيقية</a></li>
                    <li><a href="#" id="sb-link5">فروض محروسة</a></li>
                </ul>
            </div>
            
            <a href="/dashboard" class="back-btn" id="sb-back">🏠 العودة للرئيسية</a>
        </div>

        <div class="main-content">"""

content = content.replace(bad_html, good_html)

# Also need to close layout-container properly at the end!
content = content.replace('    </div>\n\n    <script>', '        </div>\n    </div>\n\n    <script>')

with open('templates/subject.html', 'w', encoding='utf-8') as f:
    f.write(content)
