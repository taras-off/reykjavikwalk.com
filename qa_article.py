#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Вычитка статьи перед публикацией: спойлеры, регистр, кальки, структура."""
import json, pathlib, re, sys
sys.path.insert(0, ".")
import build as B
from article_build import ARTICLES, CONTENT, art_url, slug as art_slug
KEY = sys.argv[1] if len(sys.argv) > 1 else "one-day"
SLUG = {l: art_slug(l, KEY) for l in B.LANGS}

FAIL = []
def bad(lang, msg): FAIL.append(f"{lang}: {msg}")

# ── что аудиогид рассказывает сам и чего на странице быть не должно ───────────
SPOILERS = [
 r"high[- ]seat", r"\b871\b", r"Ing[oó]lf", r"pots and pans", r"búsáhald",
 r"Leif(ur|r)?\b", r"\b1930\b", r"\b2008\b", r"l[ií]asson", r"Cod War|Kabeljau|guerra del bacalao|guerre de la morue|wojn\w+ dorsz|тресков",
 r"Ó[ðd]inn", r"\b1937\b", r"\b41 (year|ans|Jahre|años|anni|anos|lat|год)", r"Nordal",
 r"Þ[uú]fa|Тюв", r"дым(ная|ной) бухт|smoky bay|bahía humeante|baie fumante|rauchende",
]

REGISTER = {
 "fr": [(r"\b(tu|ton|ta|tes|toi)\b", "ты-форма во французском (должно быть vous)")],
 "de": [(r"\b(du|dein\w*|dir|dich)\b", "du-форма в немецком (должно быть Sie)")],
 "es": [(r"\busted(es)?\b", "usted в испанском (должно быть tú)")],
 "it": [(r"(?<![.!?]\s)(?<!^)\bLei\b", "формальное Lei в итальянском (должно быть tu)")],
 "pt": [(r"\b(tu|teu|tua|teus|tuas|ti|contigo)\b", "ты-форма в португальском (должно быть 3-е лицо)"),
        (r"\bvoc[êe]s?\b", "você в PT-PT — лучше безличная форма"),
        (r"\b(ônibus|trem|celular|banheiro|café da manhã|legal)\b", "бразилизм в PT-PT"),
        (r"<p>(Começa|Sobe|Reserva|Pede|Faz|Vai|Leva|Verifica|Aceita|Confirma) ", "tu-императив в PT-PT")],
 "pl": [(r"\w+(łeś|łaś|liście|łyście)\b", "родовая форма прошедшего времени (нужен наст. вр.)")],
 "ru": [(r"\b(ты|тебе|твой|твоя|твоё|твои|тобой)\b", "ты-форма в русском (должно быть вы)")],
}

# ── кальки и военная метафорика на месте нейтрального глагола ────────────────
# Абсолюты про режим работы транспорта: расписание почти всегда конечно.
SERVICE_ABSOLUTES = (
    r"(bus|buses|coach|Flybus|autocar|Autobus|autob[uú]s|autobus|авто́?бус\w*)"
    r"[^.!?]{0,80}"
    r"(around the clock|24 hours a day|24/7|day or night|rund um die Uhr|jour et nuit|"
    r"24 horas|tutto il giorno|całą dobę|кругл(ые сутки|осуточно))"
)

CALQUE = [
 r"\bвзять башню\b", r"\bprendre la tour\b", r"\bden Turm nehmen\b", r"\btomar la torre\b",
 r"\bprendere la torre\b", r"\btomar a torre\b", r"\bwzi[ąa]ć wie[żz]ę\b", r"\btake the tower\b",
 r"покор(ить|яем)|завоева", r"conquistar|conquérir|erobern|conquistare|podbi[ćj]|conquer",
 r"\bсделать город\b|\bfaire la ville\b|\bdo the city\b|\bhacer la ciudad\b",
 r"не является тем, чем кажется",
 r"в одном автобусе от",
]

# цена продукта в местном формате + разделитель тысяч в суммах ISK
NUM = {
 "en": (r"€9\.99", ","), "fr": (r"9,99 €", "\u00a0 "),
 "de": (r"9,99 €", "."),  "es": (r"9,99 €", "."),
 "it": (r"9,99 €", "."),  "pt": (r"9,99 €", "."),
 "pl": (r"9,99 €", ""),   "ru": (r"9,99 €", ""),
}

def strip_tags(h):
    h = re.sub(r"<script.*?</script>", " ", h, flags=re.S)
    h = re.sub(r"<style.*?</style>", " ", h, flags=re.S)
    h = re.sub(r"</(p|li|td|th|h[1-6]|dd|dt|figcaption|summary|div|section)>", ". ", h)
    return re.sub(r"<[^>]+>", " ", h)

print(f"статья: {KEY}")
print(f"{'язык':5} {'слов':>5} {'title':>6} {'desc':>5} {'CTA':>4} {'FAQ':>4} {'макс.предл.':>12}  вердикт")
print("─" * 78)

for lang in B.LANGS:
    p = pathlib.Path("public") / ("" if lang == "en" else lang) / SLUG[lang] / "index.html"
    h = p.read_text(encoding="utf8")
    body = h.split("<main>", 1)[1].split("</main>", 1)[0]
    text = strip_tags(body)

    # 1. спойлеры
    for pat in SPOILERS:
        m = re.search(pat, body, re.I)
        if m: bad(lang, f"СПОЙЛЕР «{m.group(0)}» — это рассказывает гид")

    # 2. регистр
    for pat, why in REGISTER.get(lang, []):
        m = re.search(pat, text, re.I if lang != "it" else 0)
        if m: bad(lang, f"регистр: «{m.group(0)}» — {why}")

    # 2b. посторонние системы письма (CJK, иврит, арабица) — следы опечаток
    stray = re.findall(r"[\u3040-\u30ff\u4e00-\u9fff\u0590-\u05ff\u0600-\u06ff]", text)
    if stray: bad(lang, f"посторонние символы в тексте: {sorted(set(stray))}")
    # кириллица в латинских языках и наоборот
    if lang != "ru" and re.search(r"[А-Яа-яЁё]", text): bad(lang, "кириллица в нелатинском тексте")
    if lang == "ru":
        for w in re.findall(r"\b[A-Za-z]{2,}\b", text):
            pass  # латиница в русском законна: Flybus, Strætó, BSÍ, TouringBee

    # 3a. абсолюты про режим работы транспорта
    m = re.search(SERVICE_ABSOLUTES, text, re.I)
    if m: bad(lang, f"абсолют про режим работы: «{' '.join(m.group(0).split())[:70]}…» — у расписания есть конец")

    # 3. кальки
    for pat in CALQUE:
        m = re.search(pat, text, re.I)
        if m: bad(lang, f"калька/метафора захвата: «{m.group(0)}»")

    # 4. формат чисел
    eur, sep = NUM[lang]
    if not re.search(eur, body): bad(lang, f"нет цены в местном формате ({eur})")
    for amount in set(re.findall(r"\b(\d{1,3}(?:[.,\u00a0 ]\d{3})+|\d{4,})\s?ISK", text)):
        digits = re.sub(r"[^\d]", "", amount)
        if len(digits) < 4: continue
        want = digits if not sep else digits[:-3] + sep[0] + digits[-3:]
        ok = any(amount.strip() == (digits if not s else digits[:-3] + s + digits[-3:])
                 for s in (sep or [""]))
        if not ok: bad(lang, f"разделитель тысяч: «{amount.strip()} ISK», ожидается «{want} ISK»")

    # 5. структура
    title = re.search(r"<title>(.*?)</title>", h).group(1)
    desc = re.search(r'name="description" content="(.*?)"', h).group(1)
    if len(title) > 60: bad(lang, f"title {len(title)} симв. (>60)")
    if len(desc) > 160: bad(lang, f"description {len(desc)} симв. (>160)")
    if h.count("<h1") != 1: bad(lang, f"{h.count('<h1')} тегов h1")
    hs = [int(m.group(1)) for m in re.finditer(r"<h([1-6])", h)]
    for a, b_ in zip(hs, hs[1:]):
        if b_ - a > 1: bad(lang, f"разрыв в иерархии заголовков h{a}→h{b_}")
    if h.count('rel="alternate"') != 9: bad(lang, "hreflang не 8+x-default")
    for l2 in B.LANGS:
        if f'href="{art_url(l2, KEY)}"' not in h: bad(lang, f"нет hreflang на {l2}")
    sw = re.search(r'<nav class="lang".*?</nav>', h, re.S).group(0)
    for l2 in B.LANGS:
        want = B.url(l2, SLUG[l2] + "/").replace(B.SITE, "")
        if f'href="{want}"' not in sw: bad(lang, f"переключатель языков не ведёт на {l2}-версию статьи")
    if 'src="/img/' in h: bad(lang, "абсолютный путь к картинке в статье")

    # 6. FAQ ↔ разметка
    faq_html = len(re.findall(r"<details", h.split('<div class="faq">')[1].split("</div>")[0]))
    ld = json.loads(re.search(r'application/ld\+json">\s*(\{.*?\})\s*</script>', h, re.S).group(1))
    faq_ld = len([g for g in ld["@graph"] if g["@type"] == "FAQPage"][0]["mainEntity"])
    if faq_html != faq_ld: bad(lang, f"FAQ в тексте {faq_html}, в разметке {faq_ld}")
    types = {g["@type"] for g in ld["@graph"]}
    if types != {"Article", "FAQPage", "BreadcrumbList"}: bad(lang, f"JSON-LD: {types}")

    # 7. коммерция
    ctas = [m.start() for m in re.finditer("bokunButton", body)]
    if len(ctas) < 4: bad(lang, f"касаний продукта {len(ctas)} (нужно ≥4)")
    if ctas and 100 * ctas[1] / len(body) > 25:
        bad(lang, "мини-CTA слишком низко на странице")
    paras = re.findall(r"<p[ >].*?</p>", body, re.S)
    first = next((i for i, x in enumerate(paras) if "#audio" in x or "bokunButton" in x), 99)
    if first > 4: bad(lang, f"первое упоминание продукта в абзаце {first + 1}")
    if 'class="minicta"' not in body: bad(lang, "нет мини-CTA после «Коротко»")
    home = "/" if lang == "en" else f"/{lang}/"
    if f'href="{home}"' not in body: bad(lang, "нет ссылки на пиллар в теле")
    if body.count('rel="noopener sponsored"') < 4: bad(lang, "мало размеченных партнёрских ссылок")
    if "BokunWidgets.openModal" not in h: bad(lang, "нет перехватчика Bókun")

    # 8. длина предложений
    sents = [s for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text)) if len(s.split()) > 2]
    longest = max(len(s.split()) for s in sents)
    avg = sum(len(s.split()) for s in sents) / len(sents)
    if longest > 40: bad(lang, f"предложение в {longest} слов")

    errs = [f for f in FAIL if f.startswith(lang + ":")]
    verdict = "OK" if not errs else f"{len(errs)} замечаний"
    words = len(text.split())
    print(f"{lang:5} {words:5} {len(title):6} {len(desc):5} {len(ctas):4} {faq_html:4} "
          f"{longest:>4} (ср.{avg:4.1f})  {verdict}")

print("─" * 78)
if FAIL:
    print(f"\nЗАМЕЧАНИЯ ({len(FAIL)}):")
    for f in FAIL: print(" •", f)
    sys.exit(1)
print("\nВсе проверки пройдены.")
