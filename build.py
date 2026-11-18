"""Builds the AGO site.

Edit PROJECTS / INFO below, then run:  python3 build.py
Writes index.html (the real site, self-hosted fonts) and preview.html (claude.ai preview).
"""
import html, pathlib

ROOT = pathlib.Path(__file__).parent

PROJECTS = [
    dict(slug="formgiving-book", title="Formgiving Book", tags=["Editorial Design", "Project Documentation"],
         text="Catalogue accompanying the Formgiving exhibition at the Danish Architecture Center in Copenhagen. The publication explores BIG’s ideas on how architecture can respond to the challenges shaping our planet.",
         year="2020", credit=("Studio", "BIG"), press=[('designboom', 'https://www.designboom.com/architecture/big-formgiving-an-architectural-future-history-taschen-12-19-2020/'), ('TASCHEN', 'https://www.taschen.com/en/books/architecture-design/04679/big-formgiving-an-architectural-future-history/'), ('art4d', 'https://art4d.com/en/2021/01/big-formgiving')], images=6),
    dict(slug="3daysofdesign", title="3daysofdesign Graphic Identity", tags=["Visual Identity", "3D Illustration"],
         text="Graphic identity for 3daysofdesign 2024, developed at BIG around the theme “Dare to Dream”. The project explored the possibilities of design through an optimistic visual language centred on imagination, inspiration, and the belief that anything is possible.",
         year="2024", credit=("Studio", "BIG"), press=[('Dezeen', 'https://www.dezeen.com/2024/02/27/big-3-days-of-design-2024-visual-identity/'), ('IFDM', 'https://ifdm.design/2024/06/03/dedicated-to-dreamers/'), ('Interior Daily', 'https://www.interiordaily.com/article/9634851/3daysofdesign-2024-has-kicked-off-in-copenhagen/')], images=5),
    dict(slug="mitgera-11", title="Mitgera 11", tags=["Visual Identity", "Editorial Design", "Print Design"],
         text="Identity and sales dossier for Mitgera 11, a twenty-two-home development in Tarragona’s Part Baixa. The name, Catalan for party wall, sets the tone for the wordmark and for a boxed ring binder covering the location, the building, the apartment types and the specifications.",
         year="2026", credit=("Context", "Llavor Homes"), images=11),
    dict(slug="bhq-signage", title="BHQ Signage & Wayfinding", tags=["Signage & Wayfinding", "Icon Design"],
         text="An iconography and signage system for BIG’s headquarters in Copenhagen, from the floor directory and door signs to the pictograms on them. One grid, one line weight: every icon belongs to the same family.",
         year="2022", credit=("Studio", "BIG"), images=8, videos=[1]),
    dict(slug="park-residences", title="Park Residences", tags=["Editorial Design", "Print Design", "Project Documentation"],
         text="Sales dossier for two timber buildings by Proforma Studio in an apricot orchard in Goght, Armenia. The architects’ drawings are redrawn as one set, from the site to each apartment.",
         year="2026", credit=("Context", "Proforma Studio"), images=8),
    dict(slug="arctic-edge", title="From the Arctic Edge to Ocean Bloom", tags=["Editorial Design", "3D Illustration"],
         text="Editorial design and custom 3D illustrations for the scientific publication documenting the Arctic Edge to Ocean Bloom ocean experiment, translating complex research and experimental setups into accessible visual storytelling.",
         year="2022", credit=("Context", "Extiv Expeditions"), images=13),
    dict(slug="formgiving-exhibition", title="Formgiving Exhibition", tags=["Visual Identity", "Print Design", "Exhibition Design", "Project Documentation"],
         text="Graphic design for BIG’s largest exhibition to date at the Danish Architecture Center in Copenhagen, including posters, flyers, and maps. The exhibition explored the evolution of life from the Big Bang to possible futures through a chronological journey.",
         year="2019", credit=("Studio", "BIG"), press=[('designboom', 'https://www.designboom.com/architecture/bjarke-ingels-group-formgiving-exhibition-copenhagen-06-12-2019/'), ('DAC', 'https://dac.dk/en/exhibitions/big-presents-formgiving'), ('Scandinavian Design', 'https://scandinaviandesign.com/explore-bigs-world-of-form-and-color-danish-architecture-centre/')], images=7),
    dict(slug="architects-guide", title="The Architect’s Guide to the Galaxy", tags=["Editorial Design", "3D Illustration"],
         text="Publication developed alongside BIG’s Mars Science City project, exploring the challenges and opportunities of designing architecture on other planets. Rather than a scientific manual, it presents space exploration through an accessible and engaging visual format.",
         year="2018", credit=("Studio", "BIG"), images=12),
    dict(slug="pallet-tyre-iroko", title="Pallet, Tyre, Iroko", tags=["Editorial Design", "Print Design", "Project Documentation"],
         text="Publication for a dwelling module in Makeni, Sierra Leone, built from pallets, used tyres and iroko. The construction drawings are redrawn alongside the site, climate and assembly sequence.",
         year="2016", images=17,
         alts=['Open book, close-up of detail D10: the tyre footing, steel core and drainage, with red leader lines', 'The closed book at an angle, kraft cover with a photograph glued on and white type', 'Cover open on the opening page: the finished module drawn above a short paragraph', 'Close-up of the opening page: the module drawing and the text about building from parts already in circulation', 'Spread 5–6: the Context divider and the brief, with climate charts and figures', 'Spread 7–8: Makeni, Sierra Leone, text and three photographs', 'Spread 9–10: full-bleed photograph of market stalls built from round timber poles and metal sheet', 'Spread 13–14: aggregation and growth, the six principles, the roof plan and a field photograph', 'Spread 15–16: pallet, tyre and iroko, each with a photograph, data and a joint drawing', 'Close-up of the D1 tyre footing and D4 truss joint, with the red sewing thread in the gutter', 'Spread 17–18: the assembly sequence in eleven axonometric steps', 'Spread 19–20: sections A-A and B-B', 'Close-up of section B-B: two roofs meeting over the shared gutter, details D9 and D10 marked in red', 'Spread 21–22: quantities per module and the module plan', 'Spread 23–24: details D9 and D10, and water and power', 'Spread 25–26: a path through the palms, and the colophon', 'The closed book from above, kraft cover with a photograph glued on and white type']),
    dict(slug="munsell-color-system", title="Munsell Color System", tags=["Infographic Design"],
         text="An infographic of the Munsell Color System, developed by Albert H. Munsell in the early 20th century, which classifies colour by hue, value and chroma. Modelled in Rhinoceros 3D and refined in Illustrator and InDesign.",
         year="2024", images=5, videos=[1]),
]

INFO = [
    "is a design studio founded by Paula Madrid, working at the intersection of space, information and graphic design.",
    "The studio focuses on signage and wayfinding, visual identity and editorial design for studios, institutions and cultural projects, locally and internationally. With a background in architecture, it treats graphic design as part of how things are built and understood: not something applied afterwards, but a layer of how a project is read, navigated and communicated, from the identity system to the finished space.",
]
EMAIL = "hi@appliedgraphicsoffice.com"
INSTAGRAM = "appliedgraphicsoffice"

e = html.escape


def credit(p):
    if not p.get("credit"):
        return ""
    return f'<br>{e(p["credit"][0])}: {e(p["credit"][1])}'


def press(p):
    if not p.get("press"):
        return ""
    links = ", ".join(f'<a href="{e(u)}" target="_blank" rel="noopener">{e(n)}</a>' for n, u in p["press"])
    return f"<br>Press: {links}"


def project(p, i=0):
    def slide(n):
        alt = e(p["alts"][n - 1]) if p.get("alts") else f'{e(p["title"])}, image {n} of {p["images"]}'
        hid = "" if n == 1 else " hidden"
        if n in p.get("videos", ()):  # muted looping video; the .jpg of the same name is its first frame
            return (f'<video src="img/{p["slug"]}-{n}.mp4" poster="img/{p["slug"]}-{n}.jpg" aria-label="{alt}" '
                    f'muted loop playsinline preload="metadata"{hid}></video>')
        return f'<img src="img/{p["slug"]}-{n}.jpg" alt="{alt}" loading="lazy" decoding="async"{hid}>'
    slides = "".join(slide(n) for n in range(1, p["images"] + 1))
    tags = "".join(f'<li><button class="tag" type="button" data-tag="{e(t)}">{e(t)}</button></li>' for t in p["tags"])
    return f'''
  <article class="project" id="{p["slug"]}" data-i="{i}" data-tags="{e("|".join(p["tags"]))}" style="order:{i}">
    <div class="head">
      <h2><a href="#{p["slug"]}">{e(p["title"])}</a></h2>
      <ul class="tags">{tags}</ul>
    </div>
    <div class="body">
      <p>{e(p["text"])}</p>
      <p class="meta">Year: {e(p["year"])}{credit(p)}{press(p)}</p>
    </div>
    <div class="slides" data-count="{p["images"]}">
      <button class="frame" type="button" aria-label="Enlarge {e(p["title"])}">{slides}</button>
      <button class="prev" type="button" aria-label="Previous image"><svg viewBox="0 0 16 16"><path d="M15 8H1M6 3 1 8l5 5"/></svg></button>
      <button class="next" type="button" aria-label="Next image"><svg viewBox="0 0 16 16"><path d="M1 8h14M10 3l5 5-5 5"/></svg></button>
      <span class="enlarge" aria-hidden="true"><svg viewBox="0 0 16 16"><path d="M9 1h6v6M15 1 9 7M7 15H1V9M1 15l6-6"/></svg></span>    </div>
  </article>'''


# Wordmark: Britti Sans, outlined from AGO BRITTI.ai (artboard 4). Drawn in currentColor.
WORDMARK = '''<svg class="wordmark" viewBox="76.25 113.75 2521.75 230.00" role="img" aria-label="Applied Graphics Office"><path transform="matrix(1,0,0,-1,189.0685,220.794)" d="M0 0-30 76.5H-31L-60.75 0ZM-43.25 102.25H-17.5L52-72.75H27.75L7-20.25H-67.75L-88.25-72.75H-112.75Z"/><path transform="matrix(1,0,0,-1,353.8156,230.794)" d="M0 0C0 28.75-14.5 47.5-37.75 47.5-61.25 47.5-77.25 28.75-77.25 0-77.25-28.75-61.25-47.75-37.75-47.75-14.5-47.75 0-28.75 0 0M-98.25 62.75H-78.75V40C-70 57-54.5 66.5-34 66.5-.25 66.5 22.25 40.5 22.25 0 22.25-40.5-.25-66.5-34-66.5-53-66.5-67.75-58.5-76.75-43.75V-112.75H-98.25Z"/><path transform="matrix(1,0,0,-1,494.8146,230.794)" d="M0 0C0 28.75-14.5 47.5-37.75 47.5-61.25 47.5-77.25 28.75-77.25 0-77.25-28.75-61.25-47.75-37.75-47.75-14.5-47.75 0-28.75 0 0M-98.25 62.75H-78.75V40C-70 57-54.5 66.5-34 66.5-.25 66.5 22.25 40.5 22.25 0 22.25-40.5-.25-66.5-34-66.5-53-66.5-67.75-58.5-76.75-43.75V-112.75H-98.25Z"/><path transform="matrix(1,0,0,-1,537.3166,269.544)" d="M0 0V151H21.5V-5H32.5V-24H23.25C8.5-24 0-15.5 0 0"/><path transform="matrix(1,0,0,-1,0,461.131)" d="M589.315 293.087H610.815V167.587H589.315ZM586.065 333.837C586.065 341.337 592.065 347.337 600.065 347.337 607.815 347.337 613.815 341.337 613.815 333.837 613.815 326.087 607.815 320.587 600.065 320.587 592.065 320.587 586.065 326.087 586.065 333.837"/><path transform="matrix(1,0,0,-1,725.8146,219.794)" d="M0 0C.75 20.25-11.75 37.25-35.75 37.25-56 37.25-70 23-72.5 0ZM-95-11.25C-95 28.75-71.75 55.5-34.75 55.5 3.75 55.5 26.75 26.5 21.5-17.25H-73C-71.75-43.25-57.75-59-34.25-59-14.5-59-4.5-47.5-1.5-38.25H20C14.25-60.25-4-77.5-34.25-77.5-71.5-77.5-95-51.5-95-11.25"/><path transform="matrix(1,0,0,-1,861.3127,230.794)" d="M0 0C0 28.75-16 47.5-39.25 47.5-62.5 47.5-77 28.75-77 0-77-28.75-62.5-47.5-39.25-47.5-16-47.5 0-28.75 0 0M-99.25 0C-99.25 40.5-76.75 66.5-43 66.5-23.75 66.5-9.25 58.25-.25 43.25V112.25H21.25V-62.75H1.5V-40.5C-7.25-57.25-22.5-66.5-43-66.5-76.75-66.5-99.25-40.5-99.25 0"/><path transform="matrix(1,0,0,-1,966.0617,206.044)" d="M0 0C0 55.25 33 91.25 84 91.25 125 91.25 153.75 67.75 160 31.25H137C132.25 55 111.75 70.5 84.5 70.5 47 70.5 23.75 43 23.75-.25 23.75-42.75 46.5-70.5 83.75-70.5 117.25-70.5 137.5-48.5 139.25-15H85.25V4.75H162.5V-87.5H143.25V-51C134.75-78 111.25-91.25 82-91.25 32.5-91.25 0-55.25 0 0"/><path transform="matrix(1,0,0,-1,1175.8107,168.044)" d="M0 0H39.5V-19H-1.75V-125.5H-23.25V-24C-23.25-8.5-14.75 0 0 0"/><path transform="matrix(1,0,0,-1,1306.8117,238.294)" d="M0 0V4.25L-39 1.75C-57.25 .5-64.25-6.75-64.25-19.25-64.25-34-54.75-40.75-39.75-40.75-17-40.75 0-25.25 0 0M-86.25-20.25C-86.25 1.75-71 15.5-41.75 17.5L-9.75 19.75C-3.75 20.25-.75 22.75-.75 31-.75 48.75-14 55.5-30.25 55.5-48.75 55.5-59.75 46.75-61.75 31H-82.75C-79 59.5-60 74-29.75 74 1.5 74 21.25 58.5 21.25 23.25V-36.25H31.25V-55.25H22C9.5-55.25 2.25-47.5 2.25-33.25V-31.5C-5.25-49-21.25-59-42.75-59-70.25-59-86.25-42.5-86.25-20.25"/><path transform="matrix(1,0,0,-1,1455.3107,230.794)" d="M0 0C0 28.75-14.5 47.5-37.75 47.5-61.25 47.5-77.25 28.75-77.25 0-77.25-28.75-61.25-47.75-37.75-47.75-14.5-47.75 0-28.75 0 0M-98.25 62.75H-78.75V40C-70 57-54.5 66.5-34 66.5-.25 66.5 22.25 40.5 22.25 0 22.25-40.5-.25-66.5-34-66.5-53-66.5-67.75-58.5-76.75-43.75V-112.75H-98.25Z"/><path transform="matrix(1,0,0,-1,1556.0597,183.294)" d="M0 0C-23 0-36.5-16.25-36.5-49V-110.25H-58V64.75H-36.5V-4.5C-29.25 11-15.5 19 3.5 19 32.25 19 49.75 .75 49.75-30.25V-110.25H28.25V-35.25C28.25-11.25 19 0 0 0"/><path transform="matrix(1,0,0,-1,0,461.131)" d="M1631.059 293.087H1652.559V167.587H1631.059ZM1627.809 333.837C1627.809 341.337 1633.809 347.337 1641.809 347.337 1649.559 347.337 1655.559 341.337 1655.559 333.837 1655.559 326.087 1649.559 320.587 1641.809 320.587 1633.809 320.587 1627.809 326.087 1627.809 333.837"/><path transform="matrix(1,0,0,-1,1672.5587,230.794)" d="M0 0C0 40.25 24.5 66.5 60.75 66.5 91.5 66.5 113.5 47.5 117.5 15.75H96C93.25 35 79 47.5 60.5 47.5 37.75 47.5 22.25 28.75 22.25 0 22.25-28.75 38-47.5 60.75-47.5 79.25-47.5 94.75-34.75 97.5-15H118.75C115.25-47 91.75-66.5 60.75-66.5 24.5-66.5 0-40.25 0 0"/><path transform="matrix(1,0,0,-1,1910.5568,259.044)" d="M0 0C0-23.25-19.5-38.25-50.75-38.25-85-38.25-105.75-20.5-106.5 6H-86.5C-84.5-9.5-73.5-20-51-20-33-20-21.75-13-21.75 .5-21.75 10.75-28.5 16-43.75 18.75L-62.75 22C-89.25 26.5-102.75 37.75-102.75 57-102.75 78.5-85.5 94.75-55 94.75-25.25 94.75-5.75 79-4 53H-24.75C-26.25 67.25-36.5 76.75-55.5 76.75-73 76.75-81.25 68.75-81.25 58-81.25 48.5-75 43-57.5 40L-38 36.5C-13.5 32 0 20 0 0"/><path transform="matrix(1,0,0,-1,2130.056,206.044)" d="M0 0C0 42.75-23.75 70.5-60 70.5-96 70.5-120 42.75-120 0-120-42.75-96-70.5-60-70.5-23.75-70.5 0-42.75 0 0M-143.75 0C-143.75 55.25-110.75 91.25-60 91.25-9.25 91.25 24 55.25 24 0 24-55.25-9.25-91.25-60-91.25-110.75-91.25-143.75-55.25-143.75 0"/><path transform="matrix(1,0,0,-1,2212.803,118.54401)" d="M0 0H11.25V-19H-9C-14.5-19-16.5-21-16.5-26.5V-49.5H8V-68.5H-16.25V-175H-37.75V-35.75C-37.75-13.5-25.25 0 0 0"/><path transform="matrix(1,0,0,-1,2278.801,118.54401)" d="M0 0H11.25V-19H-9C-14.5-19-16.5-21-16.5-26.5V-49.5H8V-68.5H-16.25V-175H-37.75V-35.75C-37.75-13.5-25.25 0 0 0"/><path transform="matrix(1,0,0,-1,0,461.131)" d="M2307.301 293.087H2328.801V167.587H2307.301ZM2304.051 333.837C2304.051 341.337 2310.051 347.337 2318.051 347.337 2325.801 347.337 2331.801 341.337 2331.801 333.837 2331.801 326.087 2325.801 320.587 2318.051 320.587 2310.051 320.587 2304.051 326.087 2304.051 333.837"/><path transform="matrix(1,0,0,-1,2348.801,230.794)" d="M0 0C0 40.25 24.5 66.5 60.75 66.5 91.5 66.5 113.5 47.5 117.5 15.75H96C93.25 35 79 47.5 60.5 47.5 37.75 47.5 22.25 28.75 22.25 0 22.25-28.75 38-47.5 60.75-47.5 79.25-47.5 94.75-34.75 97.5-15H118.75C115.25-47 91.75-66.5 60.75-66.5 24.5-66.5 0-40.25 0 0"/><path transform="matrix(1,0,0,-1,2575.802,219.794)" d="M0 0C.75 20.25-11.75 37.25-35.75 37.25-56 37.25-70 23-72.5 0ZM-95-11.25C-95 28.75-71.75 55.5-34.75 55.5 3.75 55.5 26.75 26.5 21.5-17.25H-73C-71.75-43.25-57.75-59-34.25-59-14.5-59-4.5-47.5-1.5-38.25H20C14.25-60.25-4-77.5-34.25-77.5-71.5-77.5-95-51.5-95-11.25"/></svg>'''
CSS = (ROOT / "style.css").read_text()
JS = (ROOT / "script.js").read_text()

BODY = f'''
<div id="work-view">
  <header class="top work-top">
    <a class="mark" href="#">{WORDMARK}</a>
    <div class="top-r">
      <a class="nav" href="#information">Information</a>
    </div>
    <div class="filters" aria-live="polite"></div>
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
    <p><a class="mark" href="#">Applied Graphics Office</a> <span class="fade">{e(INFO[0])}</span></p>
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
<meta name="description" content="Applied Graphics Office is a Copenhagen design studio working at the intersection of space, information and graphic design: signage and wayfinding, visual identity and editorial design.">
<meta property="og:title" content="Applied Graphics Office">
<meta property="og:description" content="A design studio working at the intersection of space, information and graphic design. Signage and wayfinding, visual identity and editorial design.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.appliedgraphicsoffice.com/">
<meta property="og:image" content="https://www.appliedgraphicsoffice.com/img/share-munsell-greens.jpg">
<meta property="og:image:width" content="1600">
<meta property="og:image:height" content="997">
<meta name="twitter:card" content="summary_large_image">'''

FONT_LOCAL = '''@font-face{font-family:"Geist";font-style:normal;font-weight:400;font-display:swap;src:url(fonts/geist-latin-400-normal.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Geist";font-style:normal;font-weight:400;font-display:swap;src:url(fonts/geist-latin-ext-400-normal.woff2) format("woff2");unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
@font-face{font-family:"Geist Mono";font-style:normal;font-weight:400;font-display:swap;src:url(fonts/geist-mono-latin-400-normal.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Geist Mono";font-style:normal;font-weight:400;font-display:swap;src:url(fonts/geist-mono-latin-ext-400-normal.woff2) format("woff2");unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
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
<link rel="preload" href="fonts/geist-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/geist-mono-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400&family=Geist+Mono:wght@400&display=swap">
<style>
{CSS}</style>
{BODY}
<script>{JS}</script>
'''
(ROOT / "preview.html").write_text(preview)
print("built index.html and preview.html")
