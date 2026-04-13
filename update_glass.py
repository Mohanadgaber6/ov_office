import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .navbar background to be transparent when un-scrolled
css = css.replace('background: rgba(41,50,135,0.97);', 'background: transparent;')

# 2. Update .about-tabs-container to be glassmorphic
css = css.replace('background: var(--white);', 'background: rgba(255, 255, 255, 0.15);\n  backdrop-filter: blur(15px);\n  -webkit-backdrop-filter: blur(15px);\n  border: 1px solid rgba(255, 255, 255, 0.2);')

# 3. Update borders and text colors inside tabs
css = css.replace('border-bottom: 2px solid var(--light-gray);', 'border-bottom: 2px solid rgba(255, 255, 255, 0.2);')

css = css.replace(
    '.tab-btn {\n    flex: 1;\n    background: none;\n    border: none;\n    padding: 18px 10px;\n    font-family: \'Readex Pro\', \'Cairo\', sans-serif;\n    font-size: 1.15rem;\n    font-weight: 800;\n    color: var(--gray);\n    cursor: pointer;\n    transition: var(--transition);\n    position: relative;\n  }',
    '.tab-btn {\n    flex: 1;\n    background: none;\n    border: none;\n    padding: 18px 10px;\n    font-family: \'Readex Pro\', \'Cairo\', sans-serif;\n    font-size: 1.15rem;\n    font-weight: 800;\n    color: rgba(255,255,255,0.7);\n    cursor: pointer;\n    transition: var(--transition);\n    position: relative;\n  }'
)

css = css.replace('.tab-btn:hover { color: var(--blue); background: var(--off-white); }', '.tab-btn:hover { color: #fff; background: rgba(255,255,255,0.1); }')
css = css.replace('.tab-btn.active { color: var(--blue); }', '.tab-btn.active { color: #fff; }')

css = css.replace('background: var(--blue);\n    border-radius: 3px 3px 0 0;', 'background: #fff;\n    border-radius: 3px 3px 0 0;')

css = css.replace(
    '.tab-pane p {\n    font-size: 1.05rem;\n    color: var(--text-dark);\n    line-height: 1.9;\n    margin-bottom: 16px;\n    text-align: center;\n  }',
    '.tab-pane p {\n    font-size: 1.05rem;\n    color: #fff;\n    line-height: 1.9;\n    margin-bottom: 16px;\n    text-align: center;\n  }'
)

# Replace transparent overlay opacity if we made it too dark
css = css.replace('background: rgba(18, 24, 61, 0.45); /* Transparent dark overly to make text visible */', 'background: rgba(18, 24, 61, 0.35); /* Transparent dark overly to make text visible */')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Done applying glassmorphism and transparency to navbar and tabs.')
