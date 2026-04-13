import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change title color
html = html.replace('style="color: var(--white); margin-bottom: 50px;">ماذا يقول عملاؤنا عنا</h2>', 'style="color: var(--blue); margin-bottom: 50px; font-weight: 800;">ماذا يقول عملاؤنا عنا</h2>')
# Wait, previously the section title said "ماذا يقول عملاؤنا عنا". The image says "آراء العملاء". Let's change the title to exactly match the image if possible, but actually we can keep the text, just the style needs updating. Also change the section badge color because light badge won't show well on white.
html = html.replace('<div class="section-badge light" style="margin: 0 auto; display: table; margin-bottom: 20px;">آراء العملاء</div>', '<div class="section-badge" style="margin: 0 auto; display: table; margin-bottom: 20px; text-align: right;">آراء العملاء</div>')

# Actually, the picture shows "آراء العملاء" as the H2, aligned to the right!
html = html.replace('<h2 class="section-title center" style="color: var(--blue); margin-bottom: 50px; font-weight: 800;">ماذا يقول عملاؤنا عنا</h2>', '<h2 class="section-title" style="color: var(--blue); margin-bottom: 50px; font-weight: 800; text-align: right; font-size: 2rem;">آراء العملاء</h2>')
html = html.replace('<h2 class="section-title center" style="color: var(--white); margin-bottom: 50px;">ماذا يقول عملاؤنا عنا</h2>', '<h2 class="section-title" style="color: var(--blue); margin-bottom: 50px; font-weight: 800; text-align: right; font-size: 2rem;">آراء العملاء</h2>')

# A regex to match each card and rewrite it
# Match from <div class="testimo-card" ... to the matching </div> at the end of the card setup
# Which is:
# <div class="testimo-card" style="height: 100%;">
#           <div class="testimo-stars">★★★★★</div>
#           <p class="testimo-text">...</p>
#           <hr class="testimo-hr" />
#           <div class="testimo-footer">
#             <div class="testimo-info">
#               <h4>...</h4>
#               <span>...</span>
#             </div>
#             <div class="testimo-avatar">...</div>
#           </div>
#         </div>

pattern = re.compile(
    r'<div class="testimo-card"\s*style="height:\s*100%;">\s*'
    r'<div class="testimo-stars">.*?</div>\s*'
    r'<p class="testimo-text">(.*?)</p>\s*'
    r'<hr class="testimo-hr"\s*/>\s*'
    r'<div class="testimo-footer">\s*'
    r'<div class="testimo-info">\s*'
    r'<h4>(.*?)</h4>\s*'
    r'<span>(.*?)</span>\s*'
    r'</div>\s*'
    r'<div class="testimo-avatar">(.*?)</div>\s*'
    r'</div>\s*'
    r'</div>', flags=re.DOTALL
)

def replace_card(m):
    text = m.group(1).strip()
    name = m.group(2).strip()
    role = m.group(3).strip()
    avatar = m.group(4).strip()
    
    return f"""<div class="testimo-card" style="height: 100%;">
          <div class="testimo-avatar">{avatar}</div>
          <div class="testimo-info">
            <p class="testimo-text">{text}</p>
            <h4>{name}</h4>
            <span>{role}</span>
          </div>
        </div>"""

html = pattern.sub(replace_card, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Finished rewriting index.html!")
