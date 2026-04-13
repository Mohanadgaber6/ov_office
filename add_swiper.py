import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Swiper CSS in head
if 'swiper-bundle.min.css' not in html:
    html = html.replace('</head>', '  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />\n</head>')

# 2. Add Swiper JS before script.js
if 'swiper-bundle.min.js' not in html:
    html = html.replace('<script src="script.js"></script>', '<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>\n  <script src="script.js"></script>')

# 3. Replace <div class="testimo-grid"> with <div class="swiper testimoSwiper" style="padding-bottom: 50px;"><div class="swiper-wrapper">
html = html.replace('<div class="testimo-grid">', '<div class="swiper testimoSwiper" style="padding-bottom: 50px; overflow: hidden;">\n        <div class="swiper-wrapper">')

# 4. Wrap <div class="testimo-card"> in <div class="swiper-slide">
# There are 6 testimonials. Let's do it cleanly by relying on the structure:
# We find <!-- Review N --> and replace the following <div class="testimo-card"> until </div></div> (which is the end of the card).
# But an easier string replace is this:
html = html.replace('<div class="testimo-card">', '<div class="swiper-slide">\n            <div class="testimo-card" style="height: 100%;">')

# 5. We need to close the <div class="swiper-slide"> after each testimo-card ends.
# A testimo-card ends right before the next <!-- Review X --> OR right before the closing </div> of testimo-grid/wrapper.
# It ends with:
#             </div>
#             <div class="testimo-avatar">.</div>
#           </div>
#         </div>
# So we can replace the boundary:
for num in range(2, 7): # Review 2 to 6
    html = html.replace(f'        <!-- Review {num} -->', f'          </div>\n        <!-- Review {num} -->')
# We need to close the last slide (Review 6) before </div>\n    </div>\n  </section>
html = html.replace('  <!-- ============ SERVICES ============ -->', '</div>\n        <div class="swiper-pagination"></div>\n      </div>\n    </div>\n  </section>\n\n  <!-- ============ SERVICES ============ -->')

with open('index.html.tmp', 'w', encoding='utf-8') as f:
    f.write(html)
