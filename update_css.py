import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .testimonials background
css = re.sub(
    r'\.testimonials \{\s*background:.*?;',
    r'.testimonials {\n  background: var(--white);',
    css,
    flags=re.DOTALL
)

# New CSS for testimo components
new_css = """
.testimoSwiper .swiper-pagination-bullet {
  background: rgba(0,0,0,0.15);
  width: 10px;
  height: 10px;
  opacity: 1;
  transition: all 0.3s ease;
}
.testimoSwiper .swiper-pagination-bullet-active {
  background: var(--teal);
  width: 24px;
  border-radius: 5px;
}
.testimo-card {
  background: #f8f9fa;
  border-radius: 8px;
  border: none;
  padding: 40px 30px;
  display: flex;
  align-items: flex-start;
  gap: 24px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 4px 15px rgba(0,0,0,0.02);
  height: 100%;
}
.testimo-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.06);
}
.testimo-avatar {
  flex-shrink: 0;
  width: 65px;
  height: 65px;
  border-radius: 50%;
  background: #fff;
  border: 1px solid rgba(0,0,0,0.05);
  color: var(--blue);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.8rem;
  font-weight: 800;
  box-shadow: 0 4px 10px rgba(0,0,0,0.03);
}
.testimo-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
}
.testimo-info {
  display: flex;
  flex-direction: column;
  text-align: right;
  flex-grow: 1;
}
.testimo-text {
  color: #444;
  font-size: 1.05rem;
  line-height: 1.8;
  margin-bottom: 24px;
}
.testimo-info h4 {
  color: var(--blue);
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 6px;
}
.testimo-info span {
  color: #777;
  font-size: 0.9rem;
}
"""

# Replace old css with new
pattern = r'\.testimoSwiper \.swiper-pagination-bullet \{.*?\.testimo-avatar \{.*?\}'
# Above pattern is too tricky to match. We'll simply find the index of `.testimoSwiper .swiper-pagination-bullet {` and `/* ================== PACKAGES ================== */` and replace everything in between.

start_idx = css.find('.testimoSwiper .swiper-pagination-bullet {')
end_idx = css.find('/* ================== PACKAGES ================== */')

if start_idx != -1 and end_idx != -1:
    css = css[:start_idx] + new_css + "\n" + css[end_idx:]

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS updated successfully!")
