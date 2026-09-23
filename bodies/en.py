# -*- coding: utf-8 -*-
"""Тело статьи v3 — по разбору Eugene от 23.09.2026.

Что изменилось против v2:
• H1 под intent «что посмотреть за день», редакционная формула ушла в подзаголовок;
• лид сокращён до трёх абзацев;
• три касания TouringBee вместо одного: лид → мини-CTA после «Коротко» → карточка → финал;
• «Двое часов» → «Сначала проверьте две вещи»;
• вычищены суперлативы и псевдоточные утверждения;
• карточка продукта продаёт результат, а не спецификацию;
• FAQ больше не отговаривает от покупки.

Неизменное правило: интрига без развязки. Крючки не расширять при редактуре.
"""

HEADLINE = "Reykjavik in one day: what to see, and a route that survives the daylight"
TITLE = "Reykjavik in One Day: What to See and a Route | TouringBee"
DESC = ("What to see in Reykjavik in one day: a walking route built around the daylight you get "
        "and the 16:45 last tower lift. Costs, bookings and three variations.")

FAQ = [
 ("Is one day enough for Reykjavik?",
  "For the city itself, yes. The centre is about twenty minutes across and the classic walking line runs "
  "roughly 5 km, so a day covers it with time for stops. One day is not enough to add the Golden Circle "
  "or the South Coast — those are separate days, and most of each one is spent in a vehicle."),
 ("What time should I start in winter?",
  "In December aim to be outside by 10:30 and treat 16:45 as a hard deadline: that is the last lift up "
  "the Hallgrímskirkja tower from September to May. Everything after dark still works — the harbour, a "
  "pool, dinner — but the viewpoint and the photographs do not."),
 ("Do I need the audio guide if I already have this itinerary?",
  "This page answers where and when: the timing, the opening hours, the bookings and a fallback for bad "
  "weather. The audio guide answers what you are looking at and why it is interesting — 27 stories along "
  "the same line. So use the route as the plan for your day, and TouringBee as the commentary along it."),
 ("Do I need a car for a day in Reykjavik?",
  "No. A city day is walkable and flat apart from one climb. Strætó buses cover anything further out at "
  "690 ISK a ride. A car only starts paying for itself when you leave town."),
 ("How much does one day in Reykjavik cost?",
  "The walking costs nothing. The fixed extras are small: 1,500 ISK for the church tower and 690 ISK for a "
  "bus ride. What moves the total is a lagoon ticket and dinner — those two can be more than everything "
  "else combined."),
 ("What should I book before I arrive?",
  "For a standard city day, the lagoon is the main one: Sky Lagoon and the Blue Lagoon both run on timed "
  "entry and the popular evening slots can sell out well ahead. In summer, add a whale-watching boat a "
  "day ahead. Everything else on this day can be decided on the morning."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/hero-1536.webp" width="1536" height="864" alt="The Reykjavik waterfront under a wide Icelandic sky" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reykjavik</a> › One day in Reykjavik</p>
    <h1>Reykjavik in one day: what to see, and a route that survives the daylight</h1>
    <p class="sub">Two limits decide this day: how many hours of light you get, and 16:45. Everything else is negotiable.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, author of the TouringBee audio tours">
      <span>By Eugene · Updated 23 September 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#plan">Jump to the plan</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Day trips &amp; tours</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">In late December the sun clears the rooftops around 11:20 and is gone again by half past three. The last lift up the Hallgrímskirkja tower leaves at 16:45. Between those two numbers sits your entire day in Reykjavik.</p>

<p>So what follows is not a list of sights but a worked timetable. The old centre is twenty minutes across and the whole walking line is about 5 km. Your legs are not the problem here. The light and the closing times are.</p>

<p>You can walk the whole thing from this page alone. If you also want to know what is behind the places you pass, the <a href="#audio">TouringBee audio walk</a> follows the same line. Planning the rest of the trip? Start with our <a href="{HOME}">complete guide to Reykjavik</a>.</p>

<div class="glance">
  <h2>At a glance</h2>
  <dl>
    <dt>Walking</dt><dd>About 5 km, flat except for one climb up Skólavörðustígur</dd>
    <dt>Shape of the day</dt><dd>Old centre → the church and its tower → the waterfront → hot water</dd>
    <dt>Hard deadline</dt><dd>16:45 — last tower lift, 1 September to 31 May</dd>
    <dt>Tower tickets</dt><dd>1,500 ISK adults · 200 ISK children 7–16 · sold on the door only</dd>
    <dt>Bus fare</dt><dd>690 ISK a single ride on Strætó</dd>
    <dt>Book ahead</dt><dd>The lagoon — the one reservation to make before you arrive</dd>
    <dt>Worst month to improvise</dt><dd>December — roughly four usable hours of light</dd>
  </dl>
</div>

<div class="minicta">
  <h2>Walk this route with the audio guide</h2>
  <p>The same line through the centre, narrated: <strong>27 stops, 2–2.5 hours</strong>, offline map and audio. Break for the tower, lunch or a museum and pick it up where you left off.</p>
  <a {BUY}>Reykjavik audio guide — €9.99</a>
</div>

<h2 id="plan">Check two things first: sunset and the tower</h2>

<p>The first limit is the sun, and it is brutal about it. Reykjavik sits just under the Arctic Circle, so the swing between midsummer and midwinter is bigger than anywhere most visitors have planned a trip before.</p>

<table class="tbl">
  <tr><th>Month</th><th>Usable daylight</th><th>What it means for one day</th></tr>
  <tr><td>December – January</td><td>~4–5 hours</td><td>One outdoor block, not two. Everything else happens in the dark, and the dark is fine.</td></tr>
  <tr><td>February – April</td><td>Climbing fast</td><td>Full route in daylight, and nights still dark enough to look for the aurora.</td></tr>
  <tr><td>May – July</td><td>Effectively all day</td><td>Start at noon or at nine in the evening. The daylight limit disappears; this is also the high season.</td></tr>
  <tr><td>August – November</td><td>Shrinking fast</td><td>September and October are a fair compromise between day length and nights dark enough for the aurora.</td></tr>
</table>

<p>The second limit is the tower. Hallgrímskirkja is the only high viewpoint in the centre, and from 1 September to 31 May the church closes at 17:00 with the last lift at 16:45. In summer it runs to 20:00, with the tower until 19:45. Tickets cannot be reserved and are valid once on the day you buy them, so it is not something you can slot in wherever it suits.</p>

<table class="tbl">
  <tr><th>Tower ticket</th><th>Price</th></tr>
  <tr><td>Adults</td><td>1,500 ISK</td></tr>
  <tr><td>Children 7–16</td><td>200 ISK</td></tr>
  <tr><td>Students, seniors 67+, disabled visitors</td><td>1,300 ISK</td></tr>
</table>

<p>Services and concerts close the church to visitors without much warning, so glance at the day's notices before you build the afternoon around it.</p>

<figure>
  <img src="{P}img/tile-hallgrimskirkja.webp" width="800" height="600" loading="lazy" alt="Hallgrímskirkja seen from below, with the Icelandic flag flying beside the tower">
  <figcaption>The one stop on this day with a closing time — and the one worth reorganising around.</figcaption>
</figure>

<h2>Morning: the old centre</h2>

<p>Start on Arnarhóll, the low green hill above the harbour road, where the statue of the city's founder looks out over the bay. He did not pick the spot. He let something else pick it for him, which is a story the audio guide takes its time over.</p>

<p>From there the old centre unfolds downhill in about three streets. Austurvöllur square has the parliament on one side. Tjörnin, the pond, has the city hall standing in it on stilts. Between them sit the small museums, including the one built around an excavated longhouse wall under the pavement. None of it takes long. All of it is free to walk through.</p>

<p>Two practical notes. Iceland is card-first to an extreme degree — you can spend a week here without touching cash, and several places have stopped accepting it. And the tap water is excellent and free everywhere, so a refillable bottle saves you more than you would think.</p>

<h2>Midday: the rainbow street, then up the tower</h2>

<p>Skólavörðustígur climbs from the shopping street to the church door, and its last block is painted in permanent rainbow stripes. It is one of the most photographed spots in Reykjavik. Early or late you get it nearly empty; between eleven and three in summer you will not.</p>

<p>Go up the tower now — do not save it for the end of the day. In winter, compressing the morning is exactly what buys you this. In summer you have more room, though it is usually quieter early or close to the last lift.</p>

<h2>Lunch, and the booking to take care of</h2>

<p>Laugavegur and the streets either side of it are where you eat. The cheap classic is the Icelandic <em>pylsa</em>: a hot dog made from a lamb, pork and beef blend. Order <em>eina með öllu</em> — "one with everything". In winter, a bowl of lamb soup does the same job. Sit-down restaurants are genuinely expensive — this is where a day in Reykjavik stops being cheap.</p>

<div class="ticketbox">
  <h3>Book the lagoon before you land</h3>
  <p>Sky Lagoon and the Blue Lagoon both run on timed entry, and the popular evening slots can sell out well ahead. For a standard city day this is the main reservation to take care of before you arrive.</p>
  <a class="btn sm" href="{TIQETS}" {OTA}>Check lagoon tickets</a>
  <a class="btn sm outline" href="{GYG}" {OTA}>Compare tours &amp; transfers</a>
</div>

<h2>Afternoon: the waterfront</h2>

<p>The second half of the day runs along the sea. Harpa, the glass concert hall on the harbour edge, is free to walk into and worth five minutes of standing still inside on a bright day. Further along the Sæbraut path is the Sun Voyager, the steel sculpture that everyone photographs as a Viking longship. It is not one, and the reason is better than the myth.</p>

<figure>
  <img src="{P}img/sec-sun-voyager.webp" width="1024" height="683" loading="lazy" alt="A visitor walking past the Sun Voyager sculpture on the Sæbraut waterfront in winter">
  <figcaption>Photographed constantly, and almost always labelled wrong.</figcaption>
</figure>

<p>Then the old harbour: whale-watching boats, fish restaurants and a grey coastguard ship at the quay, with a combat record against a much larger navy. Keep walking to the end and you reach the grass mound where the audio route finishes.</p>

<p>Here is the afternoon's one real decision. A whale-watching trip from the old harbour takes about three hours and eats the rest of your daylight. Worth it in summer if wildlife is why you came; a poor trade in December, when those three hours are all the light you have.</p>

<h2>Evening: hot water, then food</h2>

<p>Icelanders end the day in water rather than in a bar, and you have two tiers to choose from.</p>

<p>Sky Lagoon is the polished one: oceanfront, fifteen minutes from downtown, with a seven-step ritual built into the ticket. The Saman pass starts around €113 per adult (€57 for youth); Sér, with private changing rooms, from about €136.</p>

<p>The local option is a municipal geothermal pool — Sundhöllin in the centre, Laugardalslaug for the full complex. Heated from the ground, open late, and a small fraction of the lagoon price; check reykjavik.is for the current adult rate. One rule matters more than any other: you shower thoroughly, without a swimsuit, before you get in. It is posted in every changing room and it is enforced.</p>

<h2>Three variations</h2>

<h3>A stopover, not a day</h3>
<p>If you are between flights with six or seven hours in town, drop the waterfront half. Bus in from Keflavík, do the old centre and the tower, eat on Laugavegur, bus back. That fits inside a short layover with the airport transfer at both ends and still gives you the city's best view.</p>

<h3>A December day</h3>
<p>Compress everything outdoors into 11:00–15:30 and accept that the harbour, dinner and the pool happen in the dark. That is not a downgrade: the harbour lights on the water are better than the daytime version. The long dark half of the day is also your chance at the aurora, if cloud cover and solar activity line up. The dark stretch of the Sæbraut waterfront is the easiest place to look from inside the city. Grótta lighthouse, a bus ride west, is darker. Neither replaces getting properly out of the city's light.</p>

<h3>A wet, sideways day</h3>
<p>The weather here changes by the hour and the wind does most of the damage. On a bad one, invert the plan: museums and the pool in the middle of the day, the walk in whatever window opens. An umbrella is often useless here — a strong gust turns it inside out. A waterproof jacket with a hood and a hat are more reliable, any month of the year.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>The audio guide</h2>
    <p class="lead" style="max-width:720px">Seeing the route is one thing. Knowing why Reykjavik ended up here at all, what the Sun Voyager actually represents, and how a country this small kept arguing with far bigger ones — that is another.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="The TouringBee app showing the Reykjavik walking route, held up in front of Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">TouringBee Reykjavik audio guide</h3>
        <p class="meta" style="margin:0 0 10px">27 stops · 2–2.5 hours · one year of access</p>
        <div class="rate">{STARS}<b>4,7</b> {RATELABEL}</div>
        <div class="price">€9.99<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Works fully offline</strong> once downloaded — map and illustrations included, no data needed on the walk</li>
          <li><strong>Go at your own pace.</strong> Stop for lunch or a museum and pick it up in the same place two hours later</li>
          <li><strong>Narrated in character</strong> by a Reykjavik fisherman with time before his next trip out to sea</li>
          <li><strong>One payment.</strong> No group, no schedule, no guide waiting on you</li>
        </ul>
        <a {BUY} style="width:100%">Walk Reykjavik with the audio guide</a>
        <p class="meta" style="margin:12px 0 0;text-align:center">{CHECKOUTNOTE} <a href="{TBPRODUCT}" rel="noopener">{OPENSHOP}</a>.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap prose">

<h2>What the day costs</h2>
<table class="tbl">
  <tr><th>Item</th><th>Cost</th></tr>
  <tr><td>Walking the city</td><td>Free</td></tr>
  <tr><td>Audio guide, one payment</td><td>€9.99</td></tr>
  <tr><td>Hallgrímskirkja tower, adult</td><td>1,500 ISK</td></tr>
  <tr><td>Strætó single ride</td><td>690 ISK</td></tr>
  <tr><td>Municipal pool</td><td>A small fraction of a lagoon ticket</td></tr>
  <tr><td>Sky Lagoon, Saman pass</td><td>from about €113</td></tr>
  <tr><td>Whale watching, ~3 hours</td><td>Book through an operator; the real cost is the daylight</td></tr>
</table>

<p>The city itself is not expensive. The budget climbs sharply once you add a lagoon, day trips out of town and restaurant dinners.</p>

<h2>Five mistakes that cost people the day</h2>
<ol>
  <li><strong>Leaving the tower until late in winter.</strong> Last lift 16:45, September to May, and tickets are sold on the door only.</li>
  <li><strong>Stacking the Golden Circle onto a city day.</strong> That is eight hours in a vehicle. Give it its own day.</li>
  <li><strong>Giving most of December's daylight to a boat.</strong> Three hours at sea when you have four hours of light.</li>
  <li><strong>Relying on an umbrella.</strong> The wind turns it inside out. Layers, a hood and a hat instead.</li>
  <li><strong>Treating the lagoon as a walk-in.</strong> Timed entry, and the evening slots are the first to go.</li>
</ol>

<h2>Common questions</h2>
<div class="faq">{FAQHTML}</div>

<h2>Continue exploring</h2>
<ul>
  <li><a href="{HOME}">The complete Reykjavik guide</a> — the walk, the day trips and the seasons</li>
  <li><a href="{GUIDES}">All Reykjavik guides</a> — what is published and what is in the works</li>
</ul>

<h2>The short version</h2>
<p>Reykjavik gives up almost everything it has in one day on foot. The distances will never be the problem. The light will.</p>
<p>So check the sunset, do not leave the tower until the evening, and walk the rest at your own pace. And if you want to understand the city on the way rather than just look at it, take the <a href="#audio">TouringBee audio guide</a> with you: 27 stops, 2–2.5 hours, fully offline.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">Twenty-seven stops along the same line</h2>
  <p>This page gets you to the right place at the right hour. The audio guide tells you what you are standing in front of.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Start the walk — €9.99</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Find a hotel in the centre</a>
  </div>
</div>

<p class="disc">Some links on this page are affiliate links — if you book through them we may earn a commission at no extra cost to you. Prices and opening hours were checked against the operators' own sites in September 2026 and change without notice; always confirm before you travel. Tower prices and hours: hallgrimskirkja.is. Bus fares: straeto.is. Lagoon prices: skylagoon.com.</p>

  </div>
</section>
"""
