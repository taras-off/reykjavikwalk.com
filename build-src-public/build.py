#!/usr/bin/env python3
"""reykjavikwalk.com — static site generator.

One markup template, one stylesheet, 8 localized content files.
Copy lives in content/<lang>.py ; nothing user-visible is hard-coded here.

    python3 build.py            # build every language into public/
"""
import importlib, json, os, pathlib, re, sys

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "public"
SITE = "https://reykjavikwalk.com"

LANGS = ["en", "fr", "de", "es", "it", "pt", "pl", "ru"]
LANG_LABEL = {"en": "EN", "fr": "FR", "de": "DE", "es": "ES",
              "it": "IT", "pt": "PT", "pl": "PL", "ru": "RU"}
OG_LOCALE = {"en": "en_US", "fr": "fr_FR", "de": "de_DE", "es": "es_ES",
             "it": "it_IT", "pt": "pt_PT", "pl": "pl_PL", "ru": "ru_RU"}

BOKUN_UUID = "5861f2ab-0e3f-4a33-a6ef-0adde2b83f67"
BOKUN_PID = "1250141"

# ---- affiliate URLs. Localized storefronts where the partner has them. -------
GYG = ("https://www.getyourguide.{tld}/reykjavik-l30/"
       "?partner_id=0M4BUCG&amp;utm_medium=travel_agent")
GYG_TLD = {"en": "com", "fr": "fr", "de": "de", "es": "es",
           "it": "it", "pt": "com/pt-pt", "pl": "com/pl-pl", "ru": "com"}
TIQETS = ("https://www.tiqets.com/{lc}/reykjavik-attractions-c22/"
          "?partner=touringbee_limited-180893&amp;tq_campaign=reykjavikwalk")
TIQETS_LC = {"en": "en", "fr": "fr", "de": "de", "es": "es",
             "it": "it", "pt": "pt", "pl": "en", "ru": "en"}
BOOKING_CARS = "https://www.booking.com/cars/index.html?aid=1437498"
TB = ("https://touringbee.com/{path}/?wpam_id=40&amp;utm_source=reykjavikwalk"
      "&amp;utm_medium=referral&amp;utm_campaign=landing&amp;utm_content={slot}")


def gyg(lang):
    tld = GYG_TLD[lang]
    return GYG.format(tld=tld) if "/" not in tld else (
        "https://www.getyourguide.com/{sub}/reykjavik-l30/"
        "?partner_id=0M4BUCG&amp;utm_medium=travel_agent".format(sub=tld.split("/", 1)[1]))


def tiqets(lang):
    return TIQETS.format(lc=TIQETS_LC[lang])


def tb(path, slot):
    return TB.format(path=path, slot=slot)


def bokun_attrs():
    return ('class="btn bokunButton" '
            f'href="https://widgets.bokun.io/online-sales/{BOKUN_UUID}/experience/{BOKUN_PID}" '
            f'data-src="https://widgets.bokun.io/online-sales/{BOKUN_UUID}/experience/{BOKUN_PID}?partialView=1"')


def url(lang, path=""):
    base = SITE + ("/" if lang == "en" else f"/{lang}/")
    return base + path


def hreflang_links(path=""):
    out = [f'<link rel="alternate" hreflang="{l}" href="{url(l, path)}">' for l in LANGS]
    out.append(f'<link rel="alternate" hreflang="x-default" href="{url("en", path)}">')
    return "\n".join(out)


def lang_switcher(lang, path=""):
    items = []
    for l in LANGS:
        cls = ' class="on"' if l == lang else ""
        items.append(f'<a{cls} href="{url(l, path).replace(SITE, "") or "/"}">{LANG_LABEL[l]}</a>')
    return '<nav class="lang" aria-label="Language">' + "".join(items) + "</nav>"


CSS = (ROOT / "_css.txt").read_text(encoding="utf8")


# ============================================================ page shell =====
def shell(lang, c, *, path, title, desc, body, extra_css="", head_extra="",
          jsonld=None, sticky=True, og_image=None):
    L = c["ui"]
    sticky_html = ""
    if sticky:
        sticky_html = f'''
<div class="sticky" id="sticky">
  <div class="wrap">
    <div class="txt">{L["sticky_title"]}<small>{L["sticky_sub"]}</small></div>
    <a {bokun_attrs()} style="background:#fff;color:var(--navy);border-color:#fff">{L["sticky_btn"]}</a>
  </div>
</div>'''
    jsonld_html = ""
    if jsonld:
        jsonld_html = ('<script type="application/ld+json">\n'
                       + json.dumps(jsonld, ensure_ascii=False, separators=(",", ":"))
                       + "\n</script>")
    canonical = url(lang, path)
    ogimg = og_image or f"{SITE}/img/hero-1536.webp"
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
{hreflang_links(path)}
<meta property="og:type" content="website">
<meta property="og:site_name" content="reykjavikwalk.com">
<meta property="og:locale" content="{OG_LOCALE[lang]}">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{ogimg}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/favicon-180.png">
{head_extra}
<style>{CSS}{extra_css}</style>
</head>
<body>
{header(lang, c, path)}
<main>
{body}
</main>
{footer(lang, c)}
{sticky_html}
{jsonld_html}
<script>(function(){{var s=document.getElementById('sticky');if(!s)return;window.addEventListener('scroll',function(){{s.classList.toggle('on',window.scrollY>600);}},{{passive:true}});}})();</script>
<script>
(function(){{
  var loaded=0, ready=0;
  var EV=['mouseover','touchstart','scroll','keydown','pointerdown'];
  function load(){{
    if(loaded)return; loaded=1;
    EV.forEach(function(e){{window.removeEventListener(e,onEvt);}});
    var s=document.createElement('script'); s.async=true;
    s.src='https://widgets.bokun.io/assets/javascripts/apps/build/BokunWidgetsLoader.js?bookingChannelUUID={BOKUN_UUID}';
    document.body.appendChild(s);
  }}
  function onEvt(){{ if(ready) load(); }}
  EV.forEach(function(e){{window.addEventListener(e,onEvt,{{passive:true}});}});
  setTimeout(function(){{ready=1;}},1200);
  setTimeout(load,8000);
}})();
</script>
</body>
</html>'''


def header(lang, c, path):
    L = c["ui"]
    home = "/" if lang == "en" else f"/{lang}/"
    guides_home = home + c["slugs"]["guides"] + "/"
    drop = "".join(
        f'<a href="{home}{g["slug"]}/">{g["title"]}</a>'
        for g in c["guides"][:10])
    return f'''<header class="hdr">
  <div class="wrap">
    <a class="brand" href="{home}"><img src="/img/logo.webp" width="34" height="34" alt="reykjavikwalk.com"><b>reykjavik</b><span>walk</span></a>
    <details class="menu">
      <summary>{L["menu"]} ▾</summary>
      <div class="drop">{drop}<a class="all" href="{guides_home}">{L["menu_all"]} →</a></div>
    </details>
    {lang_switcher(lang, path)}
  </div>
</header>'''


def footer(lang, c):
    L = c["ui"]
    home = "/" if lang == "en" else f"/{lang}/"
    s = c["slugs"]
    langs_html = " · ".join(
        f'<a href="{url(l).replace(SITE, "") or "/"}">{c["ui"]["langnames"][l]}</a>' for l in LANGS)
    explore = "".join(f'<li><a href="{home}{g["slug"]}/">{g["title"]}</a></li>'
                      for g in c["guides"][:3])
    return f'''<footer>
  <div class="wrap">
    <div class="grid g4">
      <div>
        <h2>{L["f_explore"]}</h2>
        <ul>{explore}<li><a href="{home}{s["guides"]}/">{L["menu_all"]}</a></li></ul>
      </div>
      <div>
        <h2>{L["f_product"]}</h2>
        <ul>
          <li><a href="{home}#audio">{L["product_name"]}</a></li>
          <li><a href="{tb("shop-tbee", "footer")}" target="_blank" rel="noopener">{L["f_alltours"]}</a></li>
          <li><a href="https://touringbee.com/terms-and-conditions-of-use/" target="_blank" rel="noopener">{L["f_terms"]}</a></li>
        </ul>
      </div>
      <div>
        <h2>{L["f_legal"]}</h2>
        <ul>
          <li><a href="{home}{s["privacy"]}/">{L["privacy_title"]}</a></li>
          <li><a href="{home}{s["affiliate"]}/">{L["affiliate_title"]}</a></li>
          <li><a href="mailto:info@touringbee.com">info@touringbee.com</a></li>
        </ul>
      </div>
      <div>
        <h2>{L["f_langs"]}</h2>
        <p style="margin:0">{langs_html}</p>
      </div>
    </div>
    <p class="disc">{L["disclaimer"]}</p>
  </div>
</footer>'''


# ============================================================ landing ========
def landing(lang, c):
    L, s = c["ui"], c["slugs"]
    home = "/" if lang == "en" else f"/{lang}/"
    h = c["home"]
    stars = ('<span class="stars" role="img" aria-label="'
             + L["rating_aria"] + '">'
             + '<svg class="st" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M10 1.6l2.47 5.3 5.53.66-4.1 3.9 1.09 5.94L10 14.5l-4.99 2.9L6.1 11.46 2 7.56l5.53-.66L10 1.6z"/></svg>' * 5
             + "</span>")

    tiles = "".join(
        f'''<a class="tile" href="{home}{t["href"]}/"><img src="/img/{t["img"]}.webp" width="800" height="600" loading="lazy" alt="{t["alt"]}"><div class="t"><h3>{t["h"]}</h3><p>{t["p"]}</p></div></a>'''
        for t in h["tiles"])
    steps = "".join(
        f'<div class="step"><b>{i+1}</b><h3>{st["h"]}</h3><p>{st["p"]}</p></div>'
        for i, st in enumerate(h["steps"]))
    facts = "".join(f'<div><div class="k">{k}</div><div class="v">{v}</div></div>'
                    for k, v in h["facts"])
    hl = "".join(f'<div><span>{k}</span>{v}</div>' for k, v in h["highlights"])
    ticks = "".join(f"<li>{t}</li>" for t in h["ticks"])
    faq = "".join(
        f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>'
        for i, (q, a) in enumerate(h["faq"]))
    plan = "".join(
        f'<div class="card"><div class="pad"><h3>{col["h"]}</h3><p>'
        + " · ".join(f'<a href="{home}{sl}/">{tt}</a>' for sl, tt in col["links"])
        + "</p></div></div>" for col in h["plan"])

    partners = f'''
      <div class="card">
        <div class="noimg">Þingvellir · Geysir · Gullfoss</div>
        <div class="pad"><div class="plabel">GetYourGuide</div><h3>{h["p_golden_h"]}</h3><p class="meta">{h["p_golden_p"]}</p>
        <a class="btn sm outline" href="{gyg(lang)}" target="_blank" rel="noopener sponsored">{L["see_tours"]}</a></div>
      </div>
      <div class="card">
        <img src="/img/card-blue-lagoon.webp" width="600" height="450" loading="lazy" alt="{h["p_blue_alt"]}">
        <div class="pad"><div class="plabel">Tiqets</div><h3>Blue Lagoon</h3><p class="meta">{h["p_blue_p"]}</p>
        <a class="btn sm outline" href="{tiqets(lang)}" target="_blank" rel="noopener sponsored">{L["check_tickets"]}</a></div>
      </div>
      <div class="card">
        <img src="/img/card-northern-lights.webp" width="600" height="450" loading="lazy" alt="{h["p_aurora_alt"]}">
        <div class="pad"><div class="plabel">GetYourGuide</div><h3>{h["p_aurora_h"]}</h3><p class="meta">{h["p_aurora_p"]}</p>
        <a class="btn sm outline" href="{gyg(lang)}" target="_blank" rel="noopener sponsored">{L["see_tours"]}</a></div>
      </div>
      <div class="card">
        <img src="/img/card-sky-lagoon.webp" width="600" height="450" loading="lazy" alt="{h["p_sky_alt"]}">
        <div class="pad"><div class="plabel">Tiqets</div><h3>Sky Lagoon</h3><p class="meta">{h["p_sky_p"]}</p>
        <a class="btn sm outline" href="{tiqets(lang)}" target="_blank" rel="noopener sponsored">{L["check_tickets"]}</a></div>
      </div>'''

    cross = "".join(
        f'<div class="card"><div class="pad"><h3>{x["h"]}</h3><p>{x["p"]}</p>'
        f'<a class="btn sm outline" href="{tb(x["path"], "crosssell")}" target="_blank" rel="noopener">{x["cta"]}</a></div></div>'
        for x in h["cross"])

    body = f'''
<div class="hero">
  <img class="bg" src="/img/hero-1536.webp" srcset="/img/hero-600.webp 600w,/img/hero-768.webp 768w,/img/hero-1536.webp 1536w" sizes="100vw" width="1536" height="864" alt="{h["hero_alt"]}" fetchpriority="high">
  <div class="wrap">
    <span class="chip">{stars} {h["chip"]}</span>
    <h1>{h["h1"]}</h1>
    <p class="sub">{h["sub"]}</p>
    <div class="btnrow">
      <a class="btn dark" href="#tour">{h["cta_inside"]}</a>
      <a {bokun_attrs()}>{L["buy"]}</a>
      <a class="btn ghost" href="#preview">{h["cta_preview"]}</a>
      <a class="btn dark" href="{gyg(lang)}" target="_blank" rel="noopener sponsored">{h["cta_daytrips"]}</a>
    </div>
  </div>
</div>

<section id="tour">
  <div class="wrap">
    <p class="lead">{h["intro1"]}</p>
    <p>{h["intro2"]}</p>
    <p>{h["intro3"]}</p>
    <div class="player" id="preview">
      <div><span class="lbl">{h["preview_h"]}</span><p class="mut">{h["preview_p"]}</p></div>
      <audio controls preload="none" src="/audio/reykjavikt1_en_intro.mp3">{L["audio_fallback"]}</audio>
    </div>
    <div class="hl">{hl}</div>
  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>{h["prod_h2"]}</h2>
    <p class="lead" style="max-width:720px">{h["prod_lead"]}</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="/img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="{h["prod_alt"]}"></div>
      <div class="bd">
        <div class="rate">{stars}<b>4,7</b> {L["rating_label"]}</div>
        <div class="price">{L["price_display"]}<small>{L["price_sub"]}</small></div>
        <ul class="ticks">{ticks}</ul>
        <a {bokun_attrs()} style="width:100%">{L["buy"]}</a>
        <p class="meta" style="margin:12px 0 0;text-align:center">{L["checkout_note"]} <a href="{tb("product/reykjavik-city-walking-tour", "product_card")}" target="_blank" rel="noopener">{L["open_shop"]}</a>.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>{h["why_h2"]}</h2>
    <div class="grid g2" style="align-items:center;margin-bottom:34px">
      <div><p>{h["why_p1"]}</p><p>{h["why_p2"]}</p></div>
      <img src="/img/sec-government-house.webp" width="1024" height="683" loading="lazy" alt="{h["why_img1_alt"]}" style="border-radius:14px">
    </div>
    <div class="grid g2" style="align-items:center;margin-bottom:34px">
      <img src="/img/sec-sun-voyager.webp" width="1024" height="683" loading="lazy" alt="{h["why_img2_alt"]}" style="border-radius:14px">
      <div><h3>{h["light_h3"]}</h3><p>{h["light_p1"]}</p><p>{h["light_p2"]}</p>
        <p><a href="{home}{h["light_link"][0]}/">{h["light_link"][1]} →</a></p></div>
    </div>
    <div class="ticketbox">
      <h3>{h["free_h3"]}</h3><p>{h["free_p"]}</p>
      <a class="btn outline sm" href="{home}{h["free_link"][0]}/">{h["free_link"][1]}</a>
    </div>
    <div class="grid g2" style="align-items:center;margin-top:34px">
      <div><h3>{h["weird_h3"]}</h3><p>{h["weird_p1"]}</p><p>{h["weird_p2"]}</p></div>
      <img src="/img/sec-locomotive.webp" width="1024" height="683" loading="lazy" alt="{h["weird_img_alt"]}" style="border-radius:14px">
    </div>
    <div class="btnrow">
      <a {bokun_attrs()}>{L["buy"]}</a>
      <a class="btn outline" href="{home}{h["oneday_link"][0]}/">{h["oneday_link"][1]}</a>
    </div>
  </div>
</section>

<section class="soft">
  <div class="wrap">
    <h2>{h["tiles_h2"]}</h2>
    <p class="lead" style="max-width:700px">{h["tiles_lead"]}</p>
    <div class="grid g3" style="margin-top:26px">{tiles}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>{h["how_h2"]}</h2>
    <div class="grid g4" style="margin-top:24px">{steps}</div>
    <p class="meta" style="margin-top:18px">{h["how_note"]}</p>
  </div>
</section>

<section class="soft">
  <div class="wrap">
    <h2>{h["basics_h2"]}</h2>
    <div class="facts" style="margin-top:22px">{facts}</div>
    <div class="ticketbox">
      <h3>{h["book_h3"]}</h3><p>{h["book_p"]}</p>
      <a class="btn sm" href="{tiqets(lang)}" target="_blank" rel="noopener sponsored">{h["book_cta"]}</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>{h["partners_h2"]}</h2>
    <p class="lead" style="max-width:720px">{h["partners_lead"]}</p>
    <div class="grid g4" style="margin-top:26px">{partners}</div>
    <div class="ticketbox">
      <h3>{h["car_h3"]}</h3><p>{h["car_p"]}</p>
      <a class="btn sm" href="{BOOKING_CARS}" target="_blank" rel="noopener sponsored">{h["car_cta"]}</a>
      <a class="btn sm outline" href="{home}{h["car_link"][0]}/" style="margin-left:8px">{h["car_link"][1]}</a>
    </div>
  </div>
</section>

<section class="soft">
  <div class="wrap">
    <h2>{h["cross_h2"]}</h2>
    <p class="lead" style="max-width:680px">{h["cross_lead"]}</p>
    <div class="grid g3" style="margin-top:24px">{cross}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>{h["plan_h2"]}</h2>
    <div class="grid g3" style="margin-top:22px">{plan}</div>
  </div>
</section>

<section class="soft">
  <div class="wrap" style="max-width:820px">
    <h2>{h["faq_h2"]}</h2>
    <div class="faq" style="margin-top:18px">{faq}</div>
  </div>
</section>

<section>
  <div class="wrap" style="max-width:820px">
    <div class="author">
      <img class="av" src="/img/author-eugene.webp" width="96" height="96" loading="lazy" alt="{L["author_alt"]}">
      <div><h2 style="font-size:20px;margin-bottom:.3em">{L["author_h"]}</h2><p>{L["author_bio"]}</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="final">
      <h2 style="color:#fff">{h["final_h2"]}</h2>
      <p>{h["final_p"]}</p>
      <div class="btnrow" style="justify-content:center">
        <a {bokun_attrs()} style="background:#fff;color:var(--navy);border-color:#fff">{L["buy"]}</a>
        <a class="btn ghost" href="{gyg(lang)}" target="_blank" rel="noopener sponsored">{h["final_cta2"]}</a>
      </div>
    </div>
  </div>
</section>'''

    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": f"{SITE}/#org", "name": "TouringBee",
         "url": "https://touringbee.com/", "logo": f"{SITE}/img/logo.webp",
         "sameAs": ["https://www.instagram.com/touringbeeapp",
                    "https://www.youtube.com/@TouringBee",
                    "https://www.facebook.com/TouringBeeru-191755488191134"]},
        {"@type": "WebSite", "@id": f"{url(lang)}#website", "url": url(lang),
         "name": "reykjavikwalk.com", "inLanguage": lang,
         "publisher": {"@id": f"{SITE}/#org"}},
        {"@type": "Person", "@id": f"{SITE}/#author", "name": "Eugene",
         "image": f"{SITE}/img/author-eugene.webp", "description": L["author_bio_plain"]},
        {"@type": "TouristAttraction", "@id": f"{SITE}/#attraction",
         "name": h["city"], "description": h["city_desc"],
         "address": {"@type": "PostalAddress", "addressLocality": "Reykjavík",
                     "addressCountry": "IS"},
         "geo": {"@type": "GeoCoordinates", "latitude": 64.1466, "longitude": -21.9426},
         "isAccessibleForFree": True, "image": f"{SITE}/img/hero-1536.webp"},
        {"@type": "Product", "@id": f"{url(lang)}#product", "name": L["product_name_full"],
         "description": L["product_desc"], "image": f"{SITE}/img/product-reykjavik.webp",
         "brand": {"@type": "Brand", "name": "TouringBee"},
         "category": L["product_category"], "inLanguage": "en",
         "hasMerchantReturnPolicy": {"@type": "MerchantReturnPolicy",
                                     "applicableCountry": "IS",
                                     "returnPolicyCategory": "https://schema.org/MerchantReturnNotPermitted"},
         "offers": {"@type": "Offer", "price": "9.99", "priceCurrency": "EUR",
                    "availability": "https://schema.org/InStock",
                    "url": url(lang) + "#audio"}},
        {"@type": "FAQPage", "@id": f"{url(lang)}#faq", "mainEntity": [
            {"@type": "Question", "name": strip(q),
             "acceptedAnswer": {"@type": "Answer", "text": strip(a)}}
            for q, a in h["faq"]]},
        {"@type": "BreadcrumbList", "@id": f"{url(lang)}#breadcrumb",
         "itemListElement": [{"@type": "ListItem", "position": 1,
                              "name": h["city"], "item": url(lang)}]},
    ]}

    return shell(lang, c, path="", title=h["title"], desc=h["meta"], body=body,
                 jsonld=ld,
                 head_extra='<link rel="preload" as="image" href="/img/hero-1536.webp" '
                            'imagesrcset="/img/hero-600.webp 600w,/img/hero-768.webp 768w,'
                            '/img/hero-1536.webp 1536w" imagesizes="100vw">\n'
                            '<link rel="preconnect" href="https://widgets.bokun.io">')


def strip(html_text):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html_text)).strip()


# ============================================================ guides index ===
GUIDES_CSS = (".crumb{font-size:14px;color:var(--ink-2);margin-bottom:14px}"
              ".gcard .soon{display:inline-block;font-size:13px;font-weight:700;"
              "color:var(--ink-2);background:var(--sand);border:1px solid var(--line);"
              "padding:6px 12px;border-radius:8px}"
              "h1{font-size:clamp(28px,4.4vw,42px)}"
              ".wavehead{margin:38px 0 18px;font-size:22px}")


def guides_page(lang, c):
    L, s = c["ui"], c["slugs"]
    home = "/" if lang == "en" else f"/{lang}/"
    waves = {}
    for g in c["guides"]:
        waves.setdefault(g["wave"], []).append(g)
    blocks = []
    for w in ("P0", "P1", "P2"):
        cards = "".join(
            f'<div class="card gcard"><div class="pad"><h3>{g["title"]}</h3>'
            f'<p class="meta">{g["desc"]}</p><span class="soon">{L["in_production"]}</span></div></div>'
            for g in waves.get(w, []))
        blocks.append(f'<h2 class="wavehead">{L["waves"][w]}</h2>'
                      f'<div class="grid g3">{cards}</div>')
    body = (f'<section><div class="wrap"><p class="crumb"><a href="{home}">{c["home"]["city"]}</a> › '
            f'{L["guides_h1"]}</p><h1>{L["guides_h1"]}</h1>'
            f'<p class="lead" style="max-width:760px">{L["guides_lead"]}</p>'
            + "".join(blocks) + "</div></section>")
    return shell(lang, c, path=s["guides"] + "/", title=L["guides_title"],
                 desc=L["guides_meta"], body=body, extra_css=GUIDES_CSS)


# ============================================================ legal + 404 ====
LEGAL_CSS = (".crumb{font-size:14px;color:var(--ink-2);margin-bottom:14px}"
             "h1{font-size:clamp(28px,4.4vw,42px)}h2{font-size:24px;margin-top:1.6em}")


def legal_page(lang, c, kind):
    L, s = c["ui"], c["slugs"]
    home = "/" if lang == "en" else f"/{lang}/"
    title = L[f"{kind}_title"]
    body = (f'<section><div class="wrap" style="max-width:800px">'
            f'<p class="crumb"><a href="{home}">{c["home"]["city"]}</a> › {title}</p>'
            f'<h1>{title}</h1><p class="lead">{L["updated"]}</p>'
            f'{c["legal"][kind]}</div></section>')
    return shell(lang, c, path=s[kind] + "/", title=f"{title} | reykjavikwalk.com",
                 desc=L[f"{kind}_meta"], body=body, extra_css=LEGAL_CSS, sticky=False)


def notfound_page(lang, c):
    L = c["ui"]
    home = "/" if lang == "en" else f"/{lang}/"
    body = (f'<section><div class="wrap" style="max-width:720px;text-align:center;padding:40px 20px">'
            f'<h1 style="font-size:clamp(30px,5vw,46px)">{L["nf_h1"]}</h1>'
            f'<p class="lead">{L["nf_p"]}</p><div class="btnrow" style="justify-content:center">'
            f'<a class="btn" href="{home}">{L["nf_cta1"]}</a>'
            f'<a class="btn outline" href="{home}{c["slugs"]["guides"]}/">{L["menu_all"]}</a>'
            f'</div></div></section>')
    return shell(lang, c, path="404", title=L["nf_h1"], desc=L["nf_p"],
                 body=body, sticky=False)


# ============================================================ sitemap ========
def sitemap(contents):
    rows = []

    def entry(path_by_lang, prio, freq="monthly"):
        for lang, loc in path_by_lang.items():
            alts = "".join(
                f'<xhtml:link rel="alternate" hreflang="{l}" href="{u}"/>'
                for l, u in path_by_lang.items())
            alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{path_by_lang["en"]}"/>'
            rows.append(f'<url><loc>{loc}</loc><lastmod>2026-08-06</lastmod>'
                        f'<changefreq>{freq}</changefreq><priority>{prio}</priority>{alts}</url>')

    entry({l: url(l) for l in LANGS}, "1.0", "weekly")
    entry({l: url(l, contents[l]["slugs"]["guides"] + "/") for l in LANGS}, "0.6")
    entry({l: url(l, contents[l]["slugs"]["privacy"] + "/") for l in LANGS}, "0.2")
    entry({l: url(l, contents[l]["slugs"]["affiliate"] + "/") for l in LANGS}, "0.2")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + "\n".join(rows) + "\n</urlset>\n")


# ============================================================ main ===========
def write(path, text):
    p = OUT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf8")


def main():
    sys.path.insert(0, str(ROOT))
    contents = {}
    for lang in LANGS:
        contents[lang] = importlib.import_module(f"content.{lang}").CONTENT

    for lang, c in contents.items():
        pre = "" if lang == "en" else f"{lang}/"
        write(f"{pre}index.html", landing(lang, c))
        write(f"{pre}{c['slugs']['guides']}/index.html", guides_page(lang, c))
        write(f"{pre}{c['slugs']['privacy']}/index.html", legal_page(lang, c, "privacy"))
        write(f"{pre}{c['slugs']['affiliate']}/index.html", legal_page(lang, c, "affiliate"))
    write("404.html", notfound_page("en", contents["en"]))
    write("sitemap.xml", sitemap(contents))
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print(f"built {len(LANGS)} languages")


if __name__ == "__main__":
    main()
