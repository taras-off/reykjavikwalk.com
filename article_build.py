#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сборка статьи «один день в Рейкьявике» на всех 8 языках.

Тексты — в bodies/<lang>.py, каждый написан на своём языке, а не переведён.
Слаги берутся из плана контента (content/<lang>.py, guides[ARTICLE_IDX]).
"""
import importlib, json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import build as B

ARTICLE_IDX = 8
SITE = B.SITE
OTA = 'target="_blank" rel="noopener sponsored"'

CONTENT = {l: importlib.import_module("content." + l).CONTENT for l in B.LANGS}
SLUG = {l: CONTENT[l]["guides"][ARTICLE_IDX]["slug"] for l in B.LANGS}
PATHS = {l: SLUG[l] + "/" for l in B.LANGS}


def art_url(lang):
    return B.url(lang, PATHS[lang])


def tb(path, slot):
    return (f"https://touringbee.com/{path}/?wpam_id=40&amp;utm_source=reykjavikwalk"
            f"&amp;utm_medium=referral&amp;utm_campaign=article&amp;utm_content={slot}")


ART_CSS = """
/* ── статья ── */
.crumb{font-size:14px;color:var(--ink-2);margin-bottom:12px}
.arthero{position:relative;color:#fff;background:var(--navy)}
.arthero:after{content:"";position:absolute;inset:0;background:linear-gradient(105deg,rgba(6,20,38,.88) 0%,rgba(6,20,38,.7) 46%,rgba(6,20,38,.35) 100%)}
.arthero img.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.arthero .wrap{position:relative;z-index:1;padding:58px 20px;max-width:840px}
.arthero .crumb{color:#c3d0e2}.arthero .crumb a{color:#fff}
.arthero h1{font-size:clamp(28px,4.6vw,44px)}
.arthero p.sub{font-size:19px;color:#dbe4f0;max-width:660px}
.byline{display:flex;align-items:center;gap:10px;margin:18px 0 4px;font-size:14.5px;color:#c3d0e2}
.byline img{width:36px;height:36px;border-radius:50%;object-fit:cover}
.wrap.prose{max-width:840px}
.prose{margin:0 auto}
.prose h2{margin-top:1.7em}
.prose h3{margin-top:1.4em;font-size:18px}
.prose ul,.prose ol{padding-left:22px;color:var(--ink-2)}
.prose li{margin-bottom:7px}
.prose figure{margin:26px 0}
.prose figure img{border-radius:14px;width:100%}
.prose figcaption{font-size:14px;color:var(--ink-2);margin-top:8px}
table.tbl{width:100%;border-collapse:collapse;margin:22px 0;font-size:15.5px}
table.tbl th,table.tbl td{border:1px solid var(--line);padding:10px 12px;text-align:left;vertical-align:top}
table.tbl th{background:var(--sand);font-weight:700}
.glance{border:1px solid var(--line);border-left:5px solid var(--teal);background:var(--sand);border-radius:12px;padding:20px 22px;margin:26px 0}
.glance h2{margin-top:0;font-size:21px}
.glance dl{display:grid;grid-template-columns:auto 1fr;gap:8px 16px;margin:0;font-size:15.5px}
.glance dt{font-weight:700}
.glance dd{margin:0;color:var(--ink-2)}
.minicta{border:1px solid var(--line);background:linear-gradient(180deg,#fff 0%,var(--sand) 100%);border-radius:14px;padding:22px 24px;margin:30px 0}
.minicta h2{margin:0 0 8px;font-size:21px}
.minicta p{margin:0 0 16px;color:var(--ink-2)}
.minicta .btn{margin:0}
.disc{font-size:13.5px;color:var(--ink-2);border-top:1px solid var(--line);padding-top:16px;margin-top:34px}
@media(max-width:600px){.glance dl{grid-template-columns:1fr;gap:2px 0}.glance dd{margin-bottom:8px}}
"""


def build(lang):
    C = CONTENT[lang]
    L = C["ui"]
    V = importlib.import_module("bodies." + lang)

    prefix = "../" if lang == "en" else "../../"
    home = "/" if lang == "en" else f"/{lang}/"

    header = B.header(lang, C, PATHS[lang], PATHS).replace('src="/img/', f'src="{prefix}img/')
    footer = B.footer(lang, C).replace('src="/img/', f'src="{prefix}img/')

    stars = ('<span class="stars" role="img" aria-label="' + L["rating_aria"] + '">'
             + '<svg class="st" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true">'
               '<path d="M10 1.6l2.47 5.3 5.53.66-4.1 3.9 1.09 5.94L10 14.5l-4.99 2.9L6.1 11.46 2 7.56l5.53-.66L10 1.6z"/>'
               '</svg>' * 5 + "</span>")

    faqhtml = "".join(
        f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>'
        for i, (q, a) in enumerate(V.FAQ))

    body = V.BODY_TMPL.format(
        P=prefix, HOME=home,
        GUIDES=home + C["slugs"]["guides"] + "/",
        BUY=B.bokun_attrs(), BUYLABEL=L["buy"],
        GYG=B.gyg(lang), TIQETS=B.tiqets(lang), OTA=OTA,
        HOTELS="https://www.booking.com/searchresults.html?ss=Reykjavik&amp;aid=1437498",
        STARS=stars, RATELABEL=L["rating_label"], PRICESUB=L["price_sub"],
        CHECKOUTNOTE=L["checkout_note"], OPENSHOP=L["open_shop"],
        TBPRODUCT=tb("product/reykjavik-city-walking-tour", "article_card"),
        FAQHTML=faqhtml)

    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "@id": art_url(lang) + "#article",
         "headline": V.HEADLINE, "description": V.DESC,
         "image": f"{SITE}/img/hero-1536.webp",
         "datePublished": "2026-09-23", "dateModified": "2026-09-23",
         "inLanguage": lang,
         "author": {"@type": "Person", "name": "Eugene", "description": L["author_bio_plain"]},
         "publisher": {"@type": "Organization", "name": "TouringBee",
                       "logo": {"@type": "ImageObject", "url": f"{SITE}/img/logo.webp"}},
         "mainEntityOfPage": art_url(lang)},
        {"@type": "FAQPage", "@id": art_url(lang) + "#faq",
         "mainEntity": [{"@type": "Question", "name": q,
                         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in V.FAQ]},
        {"@type": "BreadcrumbList", "@id": art_url(lang) + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": C["home"]["h1"] if "h1" in C["home"] else "Reykjavik",
             "item": B.url(lang)},
            {"@type": "ListItem", "position": 2, "name": V.HEADLINE, "item": art_url(lang)}]},
    ]}

    hreflang = "\n".join(
        [f'<link rel="alternate" hreflang="{l}" href="{art_url(l)}">' for l in B.LANGS]
        + [f'<link rel="alternate" hreflang="x-default" href="{art_url("en")}">'])

    sticky = f'''
<div class="sticky" id="sticky">
  <div class="wrap">
    <div class="txt">{L["sticky_title"]}<small>{L["sticky_sub"]}</small></div>
    <a {B.bokun_attrs()} style="background:#fff;color:var(--navy);border-color:#fff">{L["sticky_btn"]}</a>
  </div>
</div>'''

    loader = re.search(r"<script>\n/\* Bókun.*?</script>",
                       B.shell(lang, C, path="", title="x", desc="x", body=""), re.S).group(0)

    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{V.TITLE}</title>
<meta name="description" content="{V.DESC}">
<link rel="canonical" href="{art_url(lang)}">
{hreflang}
<meta property="og:type" content="article">
<meta property="og:site_name" content="reykjavikwalk.com">
<meta property="og:locale" content="{B.OG_LOCALE[lang]}">
<meta property="og:url" content="{art_url(lang)}">
<meta property="og:title" content="{V.TITLE}">
<meta property="og:description" content="{V.DESC}">
<meta property="og:image" content="{SITE}/img/hero-1536.webp">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/favicon-180.png">
<link rel="preconnect" href="https://widgets.bokun.io">
<style>{B.CSS}{ART_CSS}</style>
</head>
<body>
{header}
<main>
{body}
</main>
{footer}
{sticky}
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, separators=(",", ":"))}
</script>
<script>(function(){{var s=document.getElementById('sticky');if(!s)return;window.addEventListener('scroll',function(){{s.classList.toggle('on',window.scrollY>600);}},{{passive:true}});}})();</script>
{loader}
</body>
</html>"""

    out = pathlib.Path("public") / ("" if lang == "en" else lang) / SLUG[lang] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf8")
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    return out, len(html), words


if __name__ == "__main__":
    todo = sys.argv[1:] or B.LANGS
    for l in todo:
        try:
            out, n, w = build(l)
            print(f"{l}: {out}  ({n:,} символов, ~{w} слов)")
        except ModuleNotFoundError as e:
            print(f"{l}: нет bodies/{l}.py — пропущен")
