import re
with open('templates/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace translation keys to match the full id
c = c.replace('sub_phys', 'sub_physics')
c = c.replace('desc_phys', 'desc_physics')
c = c.replace('sub_hist', 'sub_history')
c = c.replace('desc_hist', 'desc_history')
c = c.replace('sub_philo', 'sub_philosophy')
c = c.replace('desc_philo', 'desc_philosophy')
c = c.replace('sub_ar', 'sub_arabic')
c = c.replace('desc_ar', 'desc_arabic')
c = c.replace('sub_fr', 'sub_french')
c = c.replace('desc_fr', 'desc_french')
c = c.replace('sub_en', 'sub_english')
c = c.replace('desc_en', 'desc_english')
c = c.replace('sub_info', 'sub_informatique')
c = c.replace('desc_info', 'desc_informatique')

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(c)
