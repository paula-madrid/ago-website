"""Builds the AGO site.

Edit PROJECTS / INFO below, then run:  python3 build.py
Writes index.html (the real site, self-hosted font) and preview.html (claude.ai preview).
"""
import html, pathlib

ROOT = pathlib.Path(__file__).parent

PROJECTS = [
    dict(slug="mitgera-11", title="Mitgera 11", tags=["Visual Identity", "Editorial Design", "Print Design"],
         text="Identity and sales dossier for Mitgera 11, a twenty-two-home development in Tarragona’s Part Baixa. The name, Catalan for party wall, sets the tone for the wordmark and for a boxed ring binder covering the location, the building, the apartment types and the specifications.",
         year="2026", credit=("Context", "Concept project"), images=11),
    dict(slug="arctic-edge", title="From the Arctic Edge to Ocean Bloom", tags=["Editorial Design", "3D Illustration"],
         text="Editorial design and custom 3D illustrations for the scientific publication documenting the Arctic Edge to Ocean Bloom ocean experiment, translating complex research and experimental setups into accessible visual storytelling.",
         year="2022", credit=("Context", "Extiv Expeditions"), images=13),
    dict(slug="munsell-color-system", title="Munsell Color System", tags=["Infographic Design"],
         text="An infographic of the Munsell Color System, developed by Albert H. Munsell in the early 20th century, which classifies colour by hue, value and chroma. Modelled in Rhinoceros 3D and refined in Illustrator and InDesign.",
         year="2024", credit=("Context", "Self-initiated"), images=5, videos=[1]),
    dict(slug="3daysofdesign", title="3daysofdesign Graphic Identity", tags=["Visual Identity", "3D Illustration"],
         text="Graphic identity for 3daysofdesign 2024, developed at BIG around the theme “Dare to Dream”. The project explored the possibilities of design through an optimistic visual language centred on imagination, inspiration, and the belief that anything is possible.",
         year="2024", credit=("Studio", "BIG"), press=[('Dezeen', 'https://www.dezeen.com/2024/02/27/big-3-days-of-design-2024-visual-identity/'), ('IFDM', 'https://ifdm.design/2024/06/03/dedicated-to-dreamers/'), ('Interior Daily', 'https://www.interiordaily.com/article/9634851/3daysofdesign-2024-has-kicked-off-in-copenhagen/')], images=5),
    dict(slug="formgiving-book", title="Formgiving Book", tags=["Editorial Design"],
         text="Catalogue accompanying the Formgiving exhibition at the Danish Architecture Center in Copenhagen. The publication explores BIG’s ideas on how architecture can respond to the challenges shaping our planet.",
         year="2020", credit=("Studio", "BIG"), press=[('designboom', 'https://www.designboom.com/architecture/big-formgiving-an-architectural-future-history-taschen-12-19-2020/'), ('TASCHEN', 'https://www.taschen.com/en/books/architecture-design/04679/big-formgiving-an-architectural-future-history/'), ('art4d', 'https://art4d.com/en/2021/01/big-formgiving')], images=6),
    dict(slug="architects-guide", title="The Architect’s Guide to the Galaxy", tags=["Editorial Design", "3D Illustration"],
         text="Publication developed alongside BIG’s Mars Science City project, exploring the challenges and opportunities of designing architecture on other planets. Rather than a scientific manual, it presents space exploration through an accessible and engaging visual format.",
         year="2018", credit=("Studio", "BIG"), images=12),
    dict(slug="bhq-signage", title="BHQ Signage & Wayfinding", tags=["Signage & Wayfinding", "Icon Design"],
         text="An iconography and signage system for BIG’s headquarters in Copenhagen, from the floor directory and door signs to the pictograms on them. Every icon is drawn on the same construction grid and line weight, so new ones can be added in the same language.",
         year="2022", credit=("Studio", "BIG"), images=6, videos=[1]),
    dict(slug="formgiving-exhibition", title="Formgiving Exhibition", tags=["Visual Identity", "Print Design", "Exhibition Design"],
         text="Graphic design for BIG’s largest exhibition to date at the Danish Architecture Center in Copenhagen, including posters, flyers, and maps. The exhibition explored the evolution of life from the Big Bang to possible futures through a chronological journey.",
         year="2019", credit=("Studio", "BIG"), press=[('designboom', 'https://www.designboom.com/architecture/bjarke-ingels-group-formgiving-exhibition-copenhagen-06-12-2019/'), ('Floornature', 'https://www.floornature.com/danish-architecture-centre-and-big-exhibition-formgiving-nda-14759/'), ('Scandinavian Design', 'https://scandinaviandesign.com/explore-bigs-world-of-form-and-color-danish-architecture-centre/')], images=6),
]

INFO = [
    "is a design studio founded by Paula Madrid, working at the intersection of architecture and graphic design.",
    "The studio focuses on signage and wayfinding, visual identity and editorial design for architecture studios and spatial practices, locally and internationally. Coming from architecture, it treats graphic design as part of the same process that shapes a building: not something applied afterwards, but a layer of how a project is read, navigated and communicated, from the identity system to the finished space.",
]
EMAIL = "hi@appliedgraphicsoffice.com"
INSTAGRAM = "appliedgraphicsoffice"

e = html.escape


def press(p):
    if not p.get("press"):
        return ""
    links = ", ".join(f'<a href="{e(u)}" target="_blank" rel="noopener">{e(n)}</a>' for n, u in p["press"])
    return f"<br>Press: {links}"


def project(p, i=0):
    def slide(n):
        alt = f'{e(p["title"])}, image {n} of {p["images"]}'
        hid = "" if n == 1 else " hidden"
        if n in p.get("videos", ()):  # muted looping video; the .jpg of the same name is its first frame
            return (f'<video src="img/{p["slug"]}-{n}.mp4" poster="img/{p["slug"]}-{n}.jpg" aria-label="{alt}" '
                    f'muted loop playsinline preload="metadata"{hid}></video>')
        return f'<img src="img/{p["slug"]}-{n}.jpg" alt="{alt}" loading="lazy" decoding="async"{hid}>'
    slides = "".join(slide(n) for n in range(1, p["images"] + 1))
    tags = "".join(f"<li>{e(t)}</li>" for t in p["tags"])
    return f'''
  <article class="project" id="{p["slug"]}" style="order:{i}">
    <div class="head">
      <h2><a href="#{p["slug"]}">{e(p["title"])}</a></h2>
      <ul class="tags">{tags}</ul>
    </div>
    <div class="body">
      <p>{e(p["text"])}</p>
      <p class="meta">Year: {e(p["year"])}<br>{e(p["credit"][0])}: {e(p["credit"][1])}{press(p)}</p>
    </div>
    <div class="slides" data-count="{p["images"]}">
      <button class="frame" type="button" aria-label="Enlarge {e(p["title"])}">{slides}</button>
      <button class="prev" type="button" aria-label="Previous image"><svg viewBox="0 0 16 16"><path d="M15 8H1M6 3 1 8l5 5"/></svg></button>
      <button class="next" type="button" aria-label="Next image"><svg viewBox="0 0 16 16"><path d="M1 8h14M10 3l5 5-5 5"/></svg></button>
      <span class="enlarge" aria-hidden="true"><svg viewBox="0 0 16 16"><path d="M9 1h6v6M15 1 9 7M7 15H1V9M1 15l6-6"/></svg></span>    </div>
  </article>'''


CSS = (ROOT / "style.css").read_text()
JS = (ROOT / "script.js").read_text()

BODY = f'''
<div id="work-view">
  <header class="top">
    <a class="mark" href="#">Applied Graphics Office</a>
    <a class="nav" href="#information">Information</a>
  </header>
  <main class="grid">
    <div class="col col-left">{"".join(project(p, i) for i, p in enumerate(PROJECTS) if i % 2 == 0)}
    </div>
    <div class="col col-right">{"".join(project(p, i) for i, p in enumerate(PROJECTS) if i % 2 == 1)}
    </div>
  </main>
</div>
<div id="info-view" hidden>
  <div class="top info-top">
  <main class="info">
    <p><a class="mark" href="#">Applied Graphics Office</a> {e(INFO[0])}</p>
    {"".join(f"<p>{e(t)}</p>" for t in INFO[1:])}
    <p class="contact">Email: <a href="mailto:{EMAIL}">{EMAIL}</a><br>Instagram: <a href="https://www.instagram.com/{INSTAGRAM}/" target="_blank" rel="noopener">@{INSTAGRAM}</a></p>
  </main>
  <a class="nav" href="#">Work</a>
  </div>
</div>
<footer class="foot">© 2026 Applied Graphics Office</footer>

<div class="lightbox" id="lightbox" hidden role="dialog" aria-modal="true" aria-label="Enlarged images">
  <button class="lb-close" type="button" aria-label="Close"><svg viewBox="0 0 16 16"><path d="M2 2l12 12M14 2 2 14"/></svg></button>
  <div class="lb-stage">
    <img class="lb-img" alt="">
    <video class="lb-img lb-vid" muted loop playsinline hidden></video>
    <button class="prev" type="button" aria-label="Previous image"><svg viewBox="0 0 16 16"><path d="M15 8H1M6 3 1 8l5 5"/></svg></button>
    <button class="next" type="button" aria-label="Next image"><svg viewBox="0 0 16 16"><path d="M1 8h14M10 3l5 5-5 5"/></svg></button>
  </div>
  <span class="lb-caption"></span>
</div>
'''

META = '''<title>Applied Graphics Office</title>
<meta name="description" content="Applied Graphics Office is a Copenhagen design studio working at the intersection of architecture and graphic design: signage and wayfinding, visual identity and editorial design.">
<meta property="og:title" content="Applied Graphics Office">
<meta property="og:description" content="Signage and wayfinding, visual identity and editorial design for architecture studios and spatial practices.">
<meta property="og:image" content="https://www.appliedgraphicsoffice.com/img/mitgera-11-1.jpg">'''

FONT_LOCAL = '''@font-face{font-family:"Inclusive Sans";font-style:normal;font-weight:400;font-display:swap;src:url(fonts/inclusive-sans-latin-400-normal.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Inclusive Sans";font-style:normal;font-weight:400;font-display:swap;src:url(fonts/inclusive-sans-latin-ext-400-normal.woff2) format("woff2");unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
'''

site = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{META}
<link rel="icon" href="favicon.ico" sizes="32x32">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preload" href="fonts/inclusive-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<style>
{FONT_LOCAL}{CSS}</style>
</head>
<body>{BODY}
<script>{JS}</script>
</body>
</html>
'''
(ROOT / "index.html").write_text(site)

preview = f'''{META}
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inclusive+Sans&display=swap">
<style>
{CSS}</style>
{BODY}
<script>{JS}</script>
'''
(ROOT / "preview.html").write_text(preview)
print("built index.html and preview.html")
