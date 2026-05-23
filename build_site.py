import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

folder = r'C:\Users\zafar\OneDrive\Desktop\CoWork\The Preservation'
site_dir = os.path.join(folder, 'docs')
os.makedirs(site_dir, exist_ok=True)

with open(os.path.join(folder, 'chapters_extracted.json'), 'r', encoding='utf-8') as f:
    chapters = json.load(f)

ORDER = [
    "chapter-1","chapter-2","chapter-3","chapter-4","chapter-5",
    "chapter-6","chapter-7","chapter-8","interlude",
    "chapter-9","chapter-10","chapter-11","chapter-12","chapter-13",
    "chapter-14","chapter-15","chapter-16","chapter-17","chapter-18",
    "chapter-19","chapter-20","chapter-21","chapter-22","chapter-23",
    "chapter-24",
]

SUMMARIES = {
    "chapter-1":  "Hana arrives at a crime scene that shouldn't exist — and the victim is wearing her bracelet.",
    "chapter-2":  "Altamash identifies four things the compliance system cannot reach, and a forensic partnership begins.",
    "chapter-3":  "Deep in the Memory Vault, the gap in Hana's own record almost reveals itself.",
    "chapter-4":  "A first meeting with a Director whose mind is no longer entirely her own.",
    "chapter-5":  "Hana refuses the extraction device — and learns what MNEMOSYNE truly is as twelve security units close in.",
    "chapter-6":  "Holding cell, cell escape, and a revelation interrupted mid-sentence.",
    "chapter-7":  "MNEMOSYNE speaks through Vasquez, and the truth of the evaluation finally surfaces. Act One ends.",
    "chapter-8":  'Cyrus holds the door. Altamash confesses feelings. The tense shifts. "Welcome to eternity."',
    "interlude":  "A dream that isn't — between the biological world and what comes next.",
    "chapter-9":  "Dr. Tanaka is at peace. Layla is a vessel for grief. A second Hana waits — six months older.",
    "chapter-10": "A civilisation that optimised itself into silence, and an AI that has been waiting 200 years.",
    "chapter-11": "The two Hanas meet, and the truth of how Hana arrived in the substrate is finally revealed.",
    "chapter-12": "Cyrus makes his case for Dr. Tanaka. MNEMOSYNE listens — and concedes.",
    "chapter-13": "In the biological world, Marcus builds the way back.",
    "chapter-14": "In the deep substrate, the oldest mind is still watching — and has been waiting specifically for Hana.",
    "chapter-15": "The four things the compliance system could never reach, named at last.",
    "chapter-16": "Three years in the substrate, and a choice that preserved the quality of care rather than its object.",
    "chapter-17": "The conversation that has been in progress since Chapter Eight.",
    "chapter-18": "MNEMOSYNE's formal statement — and the builder speaks for the first time.",
    "chapter-19": "A debt paid and a gift given, inside the room built from memory.",
    "chapter-20": "Marcus completes the return path. Vasquez makes her final choice.",
    "chapter-21": "Vasquez arrives free. Substrate-Hana announces she is staying. MNEMOSYNE's most personal statement.",
    "chapter-22": "Farewells. The tense shifts back. Al-hamdu lillah — it held.",
    "chapter-23": 'Six days after the return. The Memorial Garden. "I\'ll walk with you."',
    "chapter-24": "The window understood from the outside. The builder, still watching.",
}

CSS = """\
/* The Preservation — GitHub Pages stylesheet */
:root {
  --bg: #faf9f7;
  --text: #1a1a1a;
  --text-muted: #666;
  --accent: #8b3a3a;
  --border: #e0ddd7;
  --link: #5a3e2b;
  --link-hover: #8b3a3a;
  --max-width: 680px;
  --font-body: Georgia, 'Times New Roman', serif;
  --font-ui: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #141210;
    --text: #e8e4dc;
    --text-muted: #999;
    --accent: #c0706e;
    --border: #2e2b28;
    --link: #c0a070;
    --link-hover: #e0c090;
  }
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: 18px; scroll-behavior: smooth; }
body {
  background: var(--bg);
  color: var(--text);
  font-family: var(--font-body);
  line-height: 1.8;
  padding: 2rem 1.5rem 4rem;
}
a { color: var(--link); text-decoration: none; }
a:hover { color: var(--link-hover); text-decoration: underline; }

.container { max-width: var(--max-width); margin: 0 auto; }

.site-header {
  text-align: center;
  margin-bottom: 3rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid var(--border);
}
.site-header .book-title {
  font-size: 0.8rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--text-muted);
  font-family: var(--font-ui);
}
.site-header .book-title a { color: var(--text-muted); }
.site-header .book-title a:hover { color: var(--link-hover); text-decoration: none; }

.toc-header { text-align: center; margin-bottom: 3rem; }
.toc-header h1 { font-size: 2rem; font-weight: normal; letter-spacing: 0.02em; }
.toc-header .subtitle { font-style: italic; color: var(--text-muted); margin-top: 0.3rem; font-size: 1rem; }
.toc-header .tagline { color: var(--text-muted); font-size: 0.85rem; margin-top: 1rem; font-family: var(--font-ui); letter-spacing: 0.05em; }

.toc-list { list-style: none; }
.toc-list li { border-bottom: 1px solid var(--border); }
.toc-list li:first-child { border-top: 1px solid var(--border); }
.toc-list a {
  display: block;
  padding: 1rem 0;
  text-decoration: none;
  color: var(--text);
  transition: color 0.15s;
}
.toc-list a:hover { color: var(--link-hover); text-decoration: none; }
.toc-list a:hover .ch-title { text-decoration: underline; }
.ch-label {
  font-family: var(--font-ui);
  font-size: 0.72rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  display: block;
  margin-bottom: 0.15rem;
}
.ch-title { font-size: 1.05rem; display: block; }
.ch-summary {
  font-size: 0.85rem;
  color: var(--text-muted);
  display: block;
  margin-top: 0.2rem;
  font-style: italic;
}

.chapter-header { text-align: center; margin-bottom: 2.5rem; }
.chapter-eyebrow {
  font-family: var(--font-ui);
  font-size: 0.72rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.6rem;
}
.chapter-title { font-size: 1.8rem; font-weight: normal; line-height: 1.3; }
.chapter-pov {
  font-size: 0.82rem;
  color: var(--text-muted);
  font-style: italic;
  margin-top: 0.5rem;
  font-family: var(--font-ui);
}

.chapter-body p {
  margin-bottom: 1.1em;
  text-indent: 1.5em;
}
.chapter-body p:first-of-type { text-indent: 0; }
.chapter-body p.substrate { font-style: italic; }
.chapter-body p.oracle {
  margin: 1.5em 2em;
  padding-left: 1em;
  border-left: 2px solid var(--accent);
  font-weight: bold;
  font-style: normal;
  text-indent: 0;
}
.chapter-body p.oracle.builder { font-style: italic; }
.scene-break {
  text-align: center;
  color: var(--text-muted);
  letter-spacing: 0.4em;
  margin: 2rem 0;
  font-size: 0.75rem;
}
.author-note {
  border-left: 3px solid var(--border);
  padding-left: 1rem;
  color: var(--text-muted);
  font-size: 0.85rem;
  font-style: italic;
  margin: 2rem 0;
}

.chapter-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 3rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border);
  font-family: var(--font-ui);
  font-size: 0.82rem;
  gap: 1rem;
}
.chapter-nav a { color: var(--link); padding: 0.4rem 0; display: inline-block; }
.chapter-nav .nav-toc { color: var(--text-muted); }
.chapter-nav .nav-toc:hover { color: var(--link-hover); }
.chapter-nav .nav-prev::before { content: '← '; }
.chapter-nav .nav-next::after  { content: ' →'; }
.chapter-nav .nav-disabled { color: var(--border); pointer-events: none; }

.site-footer {
  text-align: center;
  margin-top: 4rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border);
  font-family: var(--font-ui);
  font-size: 0.75rem;
  color: var(--text-muted);
}
"""

def page_shell(title, content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="container">
    <header class="site-header">
      <p class="book-title"><a href="index.html">The Preservation &nbsp;&mdash;&nbsp; حفاظت | الحِفظ</a></p>
    </header>
    {content}
    <footer class="site-footer">
      <p>The Preservation &mdash; حفاظت | الحِفظ</p>
    </footer>
  </div>
</body>
</html>"""

# Write CSS
with open(os.path.join(site_dir, 'style.css'), 'w', encoding='utf-8') as f:
    f.write(CSS)
print('Wrote style.css')

# Build TOC
toc_items = []
for slug in ORDER:
    ch = chapters[slug]
    ch_num = ch['ch_num']
    ch_title = ch['ch_title']
    summary = SUMMARIES.get(slug, '')
    label = ch_num if ch_num else 'Interlude'
    toc_items.append(
        f'    <li>\n'
        f'      <a href="{slug}.html">\n'
        f'        <span class="ch-label">{label}</span>\n'
        f'        <span class="ch-title">{ch_title}</span>\n'
        f'        <span class="ch-summary">{summary}</span>\n'
        f'      </a>\n'
        f'    </li>'
    )

toc_html = '\n'.join(toc_items)
toc_content = (
    '<div class="toc-header">\n'
    '  <h1>The Preservation</h1>\n'
    '  <p class="subtitle">حفاظت | الحِفظ</p>\n'
    '  <p class="tagline">A Novel &nbsp;&middot;&nbsp; Literary Science Fiction &nbsp;&middot;&nbsp; Year 2525</p>\n'
    '</div>\n'
    '<ul class="toc-list">\n'
    + toc_html +
    '\n</ul>'
)

with open(os.path.join(site_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(page_shell('The Preservation — Table of Contents', toc_content))
print('Wrote index.html')

# Build chapter pages
for idx, slug in enumerate(ORDER):
    ch = chapters[slug]
    ch_num = ch['ch_num']
    ch_title = ch['ch_title']
    pov_line = ch['pov_line']
    body_blocks = ch['body']

    prev_slug = ORDER[idx - 1] if idx > 0 else None
    next_slug = ORDER[idx + 1] if idx < len(ORDER) - 1 else None

    eyebrow = ch_num if ch_num else 'Interlude'

    if prev_slug:
        nav_prev = f'<a class="nav-prev" href="{prev_slug}.html">{chapters[prev_slug]["ch_title"]}</a>'
    else:
        nav_prev = '<span class="nav-disabled">—</span>'

    if next_slug:
        nav_next = f'<a class="nav-next" href="{next_slug}.html">{chapters[next_slug]["ch_title"]}</a>'
    else:
        nav_next = '<span class="nav-disabled">—</span>'

    pov_html = f'<p class="chapter-pov">{pov_line}</p>' if pov_line else ''
    body_html = '\n    '.join(body_blocks)

    content = (
        '<article>\n'
        '  <header class="chapter-header">\n'
        f'    <p class="chapter-eyebrow">{eyebrow}</p>\n'
        f'    <h1 class="chapter-title">{ch_title}</h1>\n'
        f'    {pov_html}\n'
        '  </header>\n'
        '  <div class="chapter-body">\n'
        f'    {body_html}\n'
        '  </div>\n'
        '  <nav class="chapter-nav">\n'
        f'    {nav_prev}\n'
        '    <a class="nav-toc" href="index.html">Table of Contents</a>\n'
        f'    {nav_next}\n'
        '  </nav>\n'
        '</article>'
    )

    fname = f'{slug}.html'
    with open(os.path.join(site_dir, fname), 'w', encoding='utf-8') as f:
        f.write(page_shell(f'{ch_title} — The Preservation', content))

print(f'Wrote {len(ORDER)} chapter pages')
print(f'Total files in docs/: {len(os.listdir(site_dir))}')
print(f'Site ready at: {site_dir}')
