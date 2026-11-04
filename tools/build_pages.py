#!/usr/bin/env python3
"""Generate the Audio Custom subpages from one template.

Usage (from the repo root):  python3 tools/build_pages.py

Product pages: add or edit an entry in PRODUCTS and run the script.
Each product gets its own folder with index.html, e.g. /space-echo-re-201-panel/.
Makers and Parts pages are generated from the functions at the bottom.
The home page (index.html) is edited by hand.
"""
import html
import json
import os

SITE = "https://audiocustom.pl"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Inter+Tight:wght@300;400;500;600&family=Archivo:wght@500;700;900&display=swap" rel="stylesheet">')

# ---------------------------------------------------------------- products
# status: "available" | "soon"
PRODUCTS = [
    {
        "slug": "space-echo-re-201-panel",
        "brand": "Roland",
        "model": "Space Echo RE-201",
        "kind": "replacement faceplate",
        "status": "available",
        "title": "Roland Space Echo RE-201 Replacement Panel | Audio Custom",
        "description": "New metal replacement faceplate for the Roland Space Echo RE-201 tape echo, with the original layout and legends. Made in Poland, shipped worldwide.",
        "h1": "Space Echo RE&#8209;201 <em>replacement faceplate.</em>",
        "lead": "A new metal front panel for the Roland RE-201, made for units whose original panel is scratched, faded or corroded beyond saving.",
        "images": [
            ("/replacement-re201.jpg", "New metal replacement faceplate for the Roland Space Echo RE-201", 894, 901),
        ],
        "spec": [
            ("Fits", "Roland RE-201 Space Echo"),
            ("Part", "Front faceplate"),
            ("Material", "Metal"),
            ("Graphics", "Original layout, legends and colours"),
            ("Fitting", "Shipped as a panel, fitted by you or your technician"),
            ("Shipping", "Worldwide from Poland"),
        ],
        "why": [
            "The RE-201 has been on studio desks and stages since the 1970s. Its front panel takes the wear: scratches around the knobs, faded legends, corrosion and dents.",
            "Restoration can take a panel a long way, but not every panel can be saved. When the original is too far gone, a new faceplate gives the unit back the look it had when it left the factory.",
        ],
        "faq": [
            ("Will it fit my unit?", "Send us a photo of your current panel and the details from the back of the unit. We'll confirm the fit before you order."),
            ("Is fitting included?", "The panel ships on its own. Fitting it means opening the unit, so we recommend a technician if you're not comfortable doing that yourself."),
            ("Do you ship worldwide?", "Yes. About 99% of our work goes abroad. Panels are packed for long-distance transit."),
        ],
    },
    {
        "slug": "chorus-echo-re-301-panel",
        "brand": "Roland",
        "model": "Chorus Echo RE-301",
        "kind": "replacement faceplate",
        "status": "available",
        "title": "Roland Chorus Echo RE-301 Replacement Panel | Audio Custom",
        "description": "New metal replacement faceplate for the Roland Chorus Echo RE-301, with the original layout, legends and green sections. Made in Poland, shipped worldwide.",
        "h1": "Chorus Echo RE&#8209;301 <em>replacement faceplate.</em>",
        "lead": "A new metal front panel for the Roland RE-301, with its black, green and brushed sections, for units whose original panel can't be restored.",
        "images": [
            ("/replacement-re301.jpg", "New metal replacement faceplate for the Roland Chorus Echo RE-301", 896, 900),
        ],
        "spec": [
            ("Fits", "Roland RE-301 Chorus Echo"),
            ("Part", "Front faceplate"),
            ("Material", "Metal"),
            ("Graphics", "Original layout, legends and colours"),
            ("Fitting", "Shipped as a panel, fitted by you or your technician"),
            ("Shipping", "Worldwide from Poland"),
        ],
        "why": [
            "The RE-301 adds chorus to the tape echo and a busier panel to go with it. Decades of use leave the legends worn and the surface scratched or corroded.",
            "When restoring the original is no longer an option, a new faceplate brings back the look of the unit without changing anything inside it.",
        ],
        "faq": [
            ("Will it fit my unit?", "Send us a photo of your current panel and the details from the back of the unit. We'll confirm the fit before you order."),
            ("Is fitting included?", "The panel ships on its own. Fitting it means opening the unit, so we recommend a technician if you're not comfortable doing that yourself."),
            ("Do you ship worldwide?", "Yes. About 99% of our work goes abroad. Panels are packed for long-distance transit."),
        ],
    },
]

# Shown in the "Other replacement panels" list on every product page.
CATALOGUE = [
    ("Roland Space Echo RE&#8209;201", "/space-echo-re-201-panel/", "available"),
    ("Roland Chorus Echo RE&#8209;301", "/chorus-echo-re-301-panel/", "available"),
    ("Akai MPC2000XL", None, "soon"),
    ("Roland TR&#8209;909", None, "soon"),
]

# ---------------------------------------------------------------- shared parts
def head(title, description, path, jsonld):
    url = SITE + path
    blocks = "\n".join('<script type="application/ld+json">\n' + json.dumps(j, ensure_ascii=False, indent=2) + "\n</script>" for j in jsonld)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{html.escape(description)}" />
<meta name="robots" content="index, follow, max-image-preview:large" />
<link rel="canonical" href="{url}" />
<meta property="og:type" content="website" />
<meta property="og:url" content="{url}" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{html.escape(description)}" />
<meta property="og:image" content="{SITE}/og-image.jpg" />
<meta property="og:site_name" content="Audio Custom" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png" />
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png" />
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
<meta name="theme-color" content="#14110f" />
{blocks}
{FONTS}
<link rel="stylesheet" href="/site.css" />
</head>
<body>
"""

NAV = open(os.path.join(ROOT, "_nav.html")).read()

def contact(heading="Have a panel that needs <em>saving?</em>", subject="Project inquiry", hint="Tell us the model, what you need and add a few photos or a sketch with dimensions."):
    subj = subject.replace(" ", "%20")
    return f"""<section class="contact" id="contact">
  <div class="contact-logo"><img src="/logo-light.png" alt="Audio Custom" width="1739" height="385" /></div>
  <div class="section-label">— Get in touch</div>
  <h2>{heading}</h2>
  <a class="contact-email" href="mailto:custom@audiocustom.pl?subject={subj}">custom@audiocustom.pl</a>
  <div class="socials">
    <button type="button" class="copy-email" data-email="custom@audiocustom.pl">Copy email address</button>
    <a href="mailto:custom@audiocustom.pl?subject={subj}">Open in your email app</a>
    <a href="https://instagram.com/audiocustompl" target="_blank" rel="noopener">Instagram DM · @audiocustompl</a>
  </div>
  <p class="contact-hint">{hint}</p>
</section>
"""

FOOT = """<footer>
  <div>© Audio Custom · 2013–2026</div>
  <div>Synthesizer restoration · Custom panels · Made by hand</div>
</footer>
<script src="/site.js" defer></script>
</body>
</html>
"""

def crumbs(items):
    out = []
    for label, href in items:
        out.append(f'<a href="{href}">{label}</a>' if href else f"<span>{label}</span>")
    return "<div class=\"crumbs\" role=\"navigation\" aria-label=\"Breadcrumb\">" + "<span>/</span>".join(out) + "</div>"

def breadcrumb_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": html.unescape(n).replace("‑", "-"), "item": SITE + h} for i, (n, h) in enumerate(items)]}

def faq_ld(faq):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}

def faq_html(faq):
    return "\n".join(f"    <details>\n      <summary>{q}</summary>\n      <p>{a}</p>\n    </details>" for q, a in faq)

def write(path, content):
    full = os.path.join(ROOT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)
    print("wrote", full)

# ---------------------------------------------------------------- product page
def product_page(p):
    path = f"/{p['slug']}/"
    name_plain = f"{p['brand']} {p['model']} {p['kind']}"
    status = ('<span class="card-status">Available</span>' if p["status"] == "available"
              else '<span class="card-status status-soon">Coming soon</span>')
    main_src, main_alt, w, h = p["images"][0]
    thumbs = ""
    if len(p["images"]) > 1:
        thumbs = '<div class="pg-thumbs">' + "".join(
            f'<button type="button" aria-pressed="{"true" if i == 0 else "false"}" data-src="{s}" data-alt="{html.escape(a)}" aria-label="Show photo {i + 1}"><img src="{s}" alt="" width="{iw}" height="{ih}" loading="lazy" /></button>'
            for i, (s, a, iw, ih) in enumerate(p["images"])) + "</div>"
    spec = "\n".join(f"        <div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in p["spec"])
    why = "\n".join(f"      <p>{t}</p>" for t in p["why"])
    rows = []
    for label, href, st in CATALOGUE:
        if href == path:
            continue
        name = f'<a href="{href}">{label}</a>' if href else label
        pill = ('<span class="card-status">Available</span>' if st == "available"
                else '<span class="card-status status-soon">Coming soon</span>')
        rows.append(f'    <div class="rep-row{" soon" if st != "available" else ""}">\n      <h3>{name}</h3>\n      <p>{"Metal replacement faceplate." if st == "available" else "Cloned in metal for units with damaged, worn or missing originals."}</p>\n      {pill}\n    </div>')
    crumb_items = [("Home", "/"), ("Replacement panels", "/#replacement"), (p["model"].replace("-", "&#8209;"), path)]
    product_ld = {
        "@context": "https://schema.org", "@type": "Product",
        "name": name_plain, "description": p["description"],
        "image": [SITE + i[0] for i in p["images"]],
        "brand": {"@type": "Brand", "name": "Audio Custom"},
        "isAccessoryOrSparePartFor": {"@type": "Product", "name": f"{p['brand']} {p['model']}"},
        "url": SITE + path,
    }
    return head(p["title"], p["description"], path, [product_ld, breadcrumb_ld(crumb_items), faq_ld(p["faq"])]) + NAV + f"""

<main>
<header class="product">
  <div class="product-gallery">
    <div class="pg-main"><img src="{main_src}" alt="{html.escape(main_alt)}" width="{w}" height="{h}" fetchpriority="high" /></div>
    {thumbs}
  </div>
  <div class="product-info">
    {crumbs(crumb_items)}
    {status}
    <h1>{p['h1']}</h1>
    <p class="lead">{p['lead']}</p>
    <dl class="spec">
{spec}
    </dl>
    <p class="price-line">Price on request<small>Send us your unit's details and we'll quote the panel and shipping to your country.</small></p>
    <div class="cta-row">
      <a href="#contact" class="btn btn-primary">Ask about this panel <span class="arrow">→</span></a>
      <a href="/#gallery" class="btn btn-ghost">See our work</a>
    </div>
  </div>
</header>

<section class="why">
  <div class="split">
    <div>
      <div class="section-label">— Why replace</div>
      <h2>When restoration is <em>not enough.</em></h2>
    </div>
    <div class="prose">
{why}
    </div>
  </div>
</section>

<section class="process">
  <div class="section-label">— How to order</div>
  <h2>Three steps to a <em>new face.</em></h2>
  <div class="card-grid cols-3-even">
    <div class="card"><div class="card-num">01</div><h3>Send photos</h3><p>Your current panel and the label on the back of the unit, so we can confirm the fit.</p></div>
    <div class="card"><div class="card-num">02</div><h3>Price &amp; lead time</h3><p>We reply with the price of the panel, shipping to your country and when it can leave the workshop.</p></div>
    <div class="card"><div class="card-num">03</div><h3>Shipped to you</h3><p>Packed for long-distance transit and shipped worldwide from Poland.</p></div>
  </div>
</section>

<section class="faq">
  <div class="section-label">— FAQ</div>
  <h2>Before you <em>order.</em></h2>
  <div class="faq-list">
{faq_html(p['faq'])}
  </div>
</section>

<section class="related">
  <div class="section-label">— Other replacement panels</div>
  <div class="rep-list">
{chr(10).join(rows)}
  </div>
</section>
</main>

""" + contact(heading=f"Ask about the <em>{p['model'].replace('-', '&#8209;')}</em> panel.", subject=f"{p['model']} panel inquiry", hint="Add a photo of your current panel and the details from the back of the unit.") + FOOT

# ---------------------------------------------------------------- makers page
def makers_page():
    path = "/makers/"
    faq = [
        ("What do you need from me to quote?", "A sketch or drawing with dimensions, the quantity and the finish you have in mind. A photo of a panel you like helps too."),
        ("Is there a minimum quantity?", "No. We start with a single prototype made exactly like the series version, and produce runs from a handful of pieces to a few hundred."),
        ("What finishes are possible?", "Powder coating in the colour of your choice, with printed legends, scales and logos on the finished surface."),
        ("Do you make the electronics too?", "No. We make the parts people see and touch: panels, module panels and enclosures. The electronics stay with you."),
        ("Do you ship outside the EU?", "Yes. Most of our work goes abroad. Shipping and any import costs are agreed for each order."),
    ]
    items = [("Home", "/"), ("For makers", path)]
    desc = "Custom synth front panels, module panels and sheet-metal enclosures for makers: cutting, bending, pressed-in standoffs, powder coating and printing. Prototype to series."
    return head("Custom Synth Panels &amp; Enclosures for Makers | Audio Custom", desc, path, [breadcrumb_ld(items), faq_ld(faq)]) + NAV + f"""

<main>
<header class="page-hero">
  {crumbs(items)}
  <h1>Synth panels &amp; enclosures, from a sketch to a <em>finished</em> product.</h1>
  <p class="lead">Building a synthesizer or a modular system? Send us a sketch with dimensions. We handle the metal: front panels, module panels and complete enclosures, from a single prototype to a production run.</p>
  <div class="cta-row">
    <a href="#contact" class="btn btn-primary">Send us your sketch <span class="arrow">→</span></a>
    <a href="#case-study" class="btn btn-ghost">Case study</a>
  </div>
</header>

<section class="makers">
  <div class="section-label">— What we do</div>
  <h2>Everything between your drawing and your <em>shelf.</em></h2>
  <div class="photo-row cols-3">
    <figure><img src="/makers-output-front.jpg" alt="Powder-coated and printed front panel for a synthesizer output module" width="900" height="1200" loading="lazy" /><figcaption>Finished front panel</figcaption></figure>
    <figure><img src="/makers-output-back.jpg" alt="Back of the same panel with pressed-in standoffs" width="900" height="1200" loading="lazy" /><figcaption>Back side · pressed-in standoffs</figcaption></figure>
    <figure><img src="/makers-expander.jpg" alt="Matching set of printed module panels for a synthesizer system" width="675" height="1200" loading="lazy" /><figcaption>Matching panels for one system</figcaption></figure>
  </div>
  <div class="card-grid cols-5">
    <div class="card"><div class="card-num">01</div><h3>Your sketch</h3><p>A drawing with dimensions is enough. A photo of a panel you like helps too.</p></div>
    <div class="card"><div class="card-num">02</div><h3>Cutting &amp; bending</h3><p>Panels and enclosure parts are cut and bent from sheet metal to your dimensions.</p></div>
    <div class="card"><div class="card-num">03</div><h3>Standoffs</h3><p>Standoffs and inserts are pressed in, ready to mount your PCBs and modules.</p></div>
    <div class="card"><div class="card-num">04</div><h3>Powder coating</h3><p>Durable powder-coated finish in the colour of your choice.</p></div>
    <div class="card"><div class="card-num">05</div><h3>Printing</h3><p>Legends, scales and logos printed on the finished surface.</p></div>
  </div>
</section>

<section class="case-study" id="case-study">
  <div class="section-label">— Case study</div>
  <h2>Miltone <em>4Exp</em>, Paris.</h2>
  <div class="case">
    <figure>
      <img src="/makers-miltone-series.jpg" alt="Four black Synthesizer Expander Module panels made for Miltone" width="1120" height="933" loading="lazy" />
      <figcaption>Expander module panels · series production</figcaption>
    </figure>
    <div>
      <p class="lead">Miltone Instruments builds the 4Exp, a hand-crafted analog synthesizer with four independent analog modules in one instrument. We make the metal around it.</p>
      <dl class="case-facts">
        <div><dt>Client</dt><dd>Miltone Instruments, Paris</dd></div>
        <div><dt>Instrument</dt><dd>4Exp analog synthesizer</dd></div>
        <div><dt>Scope</dt><dd>Front panels for every module, enclosure, lacquering</dd></div>
        <div><dt>Panels</dt><dd><span class="big-num">250</span><br/>front panels, 50 sets of 5</dd></div>
        <div><dt>Enclosure</dt><dd>Prototype built exactly like the series version, with riveted inserts on the module rails, for a planned run of 50</dd></div>
      </dl>
      <a class="text-link" href="https://miltone.fr/preorder" target="_blank" rel="noopener">See the 4Exp at miltone.fr →</a>
    </div>
  </div>
</section>

<section class="faq">
  <div class="section-label">— FAQ</div>
  <h2>Questions makers <em>ask us.</em></h2>
  <div class="faq-list">
{faq_html(faq)}
  </div>
</section>
</main>

""" + contact(heading="Send us your <em>sketch.</em>", subject="Panels / enclosures for my instrument", hint="Add a sketch with dimensions, the quantity and the finish you have in mind.") + FOOT

# ---------------------------------------------------------------- parts page
def parts_page():
    path = "/parts/"
    faq = [
        ("What can you reproduce?", "Small plastic parts that are out of production: knobs, data wheels, slider caps, buttons, battery covers, brackets, feet and housings."),
        ("I don't have the original part. Can you still help?", "Often yes. We need something to measure: a matching part from another unit, or clear photos with dimensions."),
        ("Do you make one piece or a set?", "Both. One missing knob or a full set for an instrument."),
    ]
    items = [("Home", "/"), ("Parts", path)]
    desc = "Discontinued knobs, data wheels, LCD housings and other parts for vintage synths and samplers, reverse engineered and reproduced with 3D printing."
    return head("3D-Printed Replacement Parts for Vintage Synths | Audio Custom", desc, path, [breadcrumb_ld(items), faq_ld(faq)]) + NAV + f"""

<main>
<header class="page-hero">
  {crumbs(items)}
  <span class="card-status status-soon">New</span>
  <h1>The knob that broke in 1987 can be <em>made again.</em></h1>
  <p class="lead">Many small parts of vintage synths and samplers have been out of production for decades. We measure an original, model it and reproduce it with 3D printing, finished to sit naturally next to the original parts.</p>
  <div class="cta-row">
    <a href="#contact" class="btn btn-primary">Ask about a part <span class="arrow">→</span></a>
  </div>
</header>

<section class="parts">
  <div class="section-label">— Recent parts</div>
  <h2>Small parts, <em>big difference.</em></h2>
  <div class="photo-row cols-2">
    <figure><img src="/parts-data-knob.jpg" alt="3D-printed replacement data wheel on an Akai MPC2000XL panel" width="892" height="902" loading="lazy" /><figcaption>Akai MPC2000XL · data wheel</figcaption></figure>
    <figure><img src="/parts-mpc60-lcd-housing.jpg" alt="3D-printed LCD housing for an Akai MPC60" width="900" height="1200" loading="lazy" /><figcaption>Akai MPC60 · LCD housing</figcaption></figure>
  </div>
  <div class="card-grid">
    <div class="card"><div class="card-num">01</div><h3>Send the part</h3><p>The broken piece, a matching part from another unit, or clear photos with measurements.</p></div>
    <div class="card"><div class="card-num">02</div><h3>We model it</h3><p>The part is measured and rebuilt as a 3D model. Broken or missing sections are reconstructed.</p></div>
    <div class="card"><div class="card-num">03</div><h3>Test print</h3><p>A first print is checked for fit against the instrument before anything else is made.</p></div>
    <div class="card"><div class="card-num">04</div><h3>Finished part</h3><p>Printed and finished in the colour of the original. One piece or a full set.</p></div>
  </div>
  <p class="note-line">Knobs, data wheels, LCD housings, slider caps, buttons, battery covers, brackets, feet. If it's missing, ask.</p>
</section>

<section class="partner-sec">
  <div class="section-label">— Our partner</div>
  <h2>Made together with <em>OctoClassic.</em></h2>
  <div class="partner">
    <div class="partner-name">OctoClassic</div>
    <div>
      <p>We produce parts together with OctoClassic, who make parts for classic cars, including parts made to order when the originals are no longer available.</p>
      <p>Same problem, different machines: an original that's no longer made, measured carefully and produced again.</p>
    </div>
  </div>
</section>

<section class="faq">
  <div class="section-label">— FAQ</div>
  <h2>About <em>parts.</em></h2>
  <div class="faq-list">
{faq_html(faq)}
  </div>
</section>
</main>

""" + contact(heading="Missing a <em>part?</em>", subject="Replacement part inquiry", hint="Tell us the instrument and the part, and add photos with measurements if you have them.") + FOOT


if __name__ == "__main__":
    for p in PRODUCTS:
        write(f"/{p['slug']}/", product_page(p))
    write("/makers/", makers_page())
    write("/parts/", parts_page())
