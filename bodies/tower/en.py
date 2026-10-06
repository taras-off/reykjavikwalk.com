# -*- coding: utf-8 -*-
"""EN-мастер статьи про Хатльгримскиркью.

Крючки без развязки: почему госархитектор искал «исландский стиль», и откуда
взялась статуя перед церковью. Не дописывать — это товар аудиогида.
"""

HEADLINE = "Hallgrímskirkja tower: tickets, hours and when to go up"
TITLE = "Hallgrímskirkja Tower: Tickets, Hours & When to Go Up"
DESC = ("Hallgrímskirkja tower tickets, opening hours and the 16:45 winter deadline — plus what "
        "the view actually shows and when the church is shut to visitors.")

FAQ = [
 ("How much does it cost to go up Hallgrímskirkja?",
  "1,500 ISK for an adult and 200 ISK for a child aged 7 to 16. Students and disabled visitors pay "
  "1,300 ISK; visitors aged 67 and over get a concession, though the church does not publish that "
  "amount. Groups of ten or more get 10% off, and school groups of under-16s go free. Walking into the "
  "church itself costs nothing — only the tower is ticketed."),
 ("Can I book Hallgrímskirkja tower tickets online?",
  "No. The church states plainly that tower tickets cannot be reserved in advance. They are sold in the "
  "church shop, on your left as you come through the lobby, and they are valid once on the day you buy "
  "them. Anything sold online as a 'Hallgrímskirkja ticket' is a tour built around the church, not "
  "entry to the tower."),
 ("What time does the Hallgrímskirkja tower close?",
  "From 1 September to 31 May the church closes at 17:00 and the last trip up the tower is 16:45. From "
  "1 June to 31 August it is open until 20:00, with the tower until 19:45. Services, ceremonies and "
  "concerts close the church to visitors at other times, so check the day's notices before you build "
  "an afternoon around it."),
 ("Is Hallgrímskirkja worth it?",
  "For the view, yes — it is the only high viewpoint in the old centre, and it is the one that shows you "
  "the coloured roofs from directly above. Twenty minutes and 1,500 ISK is a fair trade. If you want a "
  "wider panorama with the whole bay and the mountains, Perlan on its hill does that better, and it "
  "costs more."),
 ("Do you take a lift all the way up?",
  "Almost. A lift carries you most of the height, then there is a short flight of steps to the viewing "
  "deck itself. The deck is enclosed, with openings on all four sides rather than open air, so it works "
  "in any weather. It is small, and the church closes it when it gets crowded."),
 ("Can you visit the church for free?",
  "Yes. Hallgrímskirkja is a working parish church and walking in to look at the nave and the organ costs "
  "nothing during opening hours. You pay only if you want to go up. Services are open to anyone as well, "
  "but during them the building is not a sightseeing stop."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/tile-hallgrimskirkja.webp" width="800" height="600" alt="Hallgrímskirkja seen from below, with the Icelandic flag flying beside the tower" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reykjavik</a> › Hallgrímskirkja</p>
    <h1>Hallgrímskirkja tower: tickets, hours, and when to go up</h1>
    <p class="sub">The church is free. The tower is not, it cannot be booked ahead, and in winter it stops letting people up at 16:45.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, author of the TouringBee audio tours">
      <span>By Eugene · Updated 29 September 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#hours">Hours &amp; prices</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Tours in Reykjavik</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">Two things about Hallgrímskirkja catch people out. The tower ticket cannot be bought in advance, from anyone, at any price. And from September to May the last trip up leaves at 16:45, which in December is well before most visitors have finished lunch.</p>

<p>Everything else is easy. The church itself is free to walk into, it sits at the top of the street you were going to climb anyway, and the whole stop takes about half an hour including the queue.</p>

<p>This page covers the tower: what it costs, when it is open, when it is shut for services, and whether the view is worth the money against the alternatives. It pairs with our <a href="{ONEDAY}">one-day Reykjavik itinerary</a>, where this tower is the fixed point the rest of the day bends around. If you want the story behind the building rather than the logistics, that is what the <a href="#audio">TouringBee audio walk</a> is for.</p>

<div class="glance">
  <h2>At a glance</h2>
  <dl>
    <dt>Church entry</dt><dd>Free</dd>
    <dt>Tower ticket</dt><dd>1,500 ISK adult · 200 ISK child 7–16 · 1,300 ISK student or disabled visitor</dd>
    <dt>Booking</dt><dd>Not possible. Sold in the church shop, same day only</dd>
    <dt>Winter hours</dt><dd>1 Sep – 31 May: church 10:00–17:00, last tower 16:45</dd>
    <dt>Summer hours</dt><dd>1 Jun – 31 Aug: church 09:00–20:00, tower until 19:45</dd>
    <dt>How long</dt><dd>About 30 minutes including the queue</dd>
    <dt>Getting up</dt><dd>Lift most of the way, then a short flight of steps</dd>
    <dt>Height</dt><dd>73 m by the church's own reckoning — the tallest building in the city</dd>
  </dl>
</div>

<div class="minicta">
  <h2>The church is one stop on a longer walk</h2>
  <p>The TouringBee audio walk takes in Hallgrímskirkja and <strong>26 other stops</strong> across the old centre — <strong>2–2.5 hours</strong>, offline map and audio, at your own pace.</p>
  <a {BUY}>Reykjavik audio guide — €9.99</a>
</div>

<h2 id="hours">What costs money and what doesn't</h2>

<p>Hallgrímskirkja is a working Lutheran parish church, not a museum, and going inside is free during opening hours. You can sit in the nave, look at the organ, and leave without paying anything. The ticket is only for the tower.</p>

<table class="tbl">
  <tr><th>Tower ticket</th><th>Price</th></tr>
  <tr><td>Adults</td><td>1,500 ISK</td></tr>
  <tr><td>Children 7–16</td><td>200 ISK</td></tr>
  <tr><td>Students, disabled visitors (with ID)</td><td>1,300 ISK</td></tr>
  <tr><td>Seniors 67+</td><td>Concession; the church does not publish the rate</td></tr>
  <tr><td>Groups of 10 or more</td><td>10% off</td></tr>
  <tr><td>School groups, pupils 16 and under</td><td>Free</td></tr>
</table>

<p>You will find other numbers online. Reykjavik's own tourist portal was still listing 1,400 ISK and a 16:30 last entry when we checked in September 2026. Plenty of guides copy an older price table too — the church has left it sitting on its own site, above the current one. The figures above are what it charges now.</p>

<h2>The hours, and the deadline</h2>

<table class="tbl">
  <tr><th>Season</th><th>Church</th><th>Last trip up the tower</th></tr>
  <tr><td>1 September – 31 May</td><td>10:00 – 17:00</td><td>16:45</td></tr>
  <tr><td>1 June – 31 August</td><td>09:00 – 20:00</td><td>19:45</td></tr>
</table>

<p>That 16:45 is the number to plan around, because it does not move with the daylight. In late December the sun is gone by half past three anyway, so the tower and the last useful light run out together. In February it is still bright at 16:45 and people miss it because the sky does not look like closing time.</p>

<p>The other closures are less predictable. The church shuts to visitors during services, weddings, funerals and concerts, and it says so plainly: opening hours are subject to change. It also closes the viewing deck during certain events, and earlier than advertised when the deck gets crowded. Sunday mornings are the most reliable way to arrive and be turned away.</p>

<h2>Buying the ticket</h2>

<p>The shop is on your left as you come through the lobby. That is the only place tower tickets exist. The church's own wording is that it is not possible to reserve tickets for the tower in advance — no online sales, no timed slots, no skip-the-line.</p>

<p>Anything you see advertised online as a Hallgrímskirkja ticket is something else: a walking tour that stops outside, or a city pass that may or may not reimburse you. The ticket is valid once, on the day you buy it, so you cannot buy it in the morning and use it at dusk.</p>

<h2>Going up</h2>

<p>A lift takes you most of the way, and a short flight of steps covers the rest. The viewing deck is enclosed, with arched openings on all four sides rather than open air, which is why it still works on a day when the wind is taking umbrellas apart at street level.</p>

<p>The deck is small. In July the queue downstairs is the slow part, not the climb, and the church will hold people back rather than crowd the platform. Fifteen minutes up there is plenty.</p>

<figure>
  <img src="{P}img/tile-rainbow-street.webp" width="800" height="600" loading="lazy" alt="Skólavörðustígur painted in rainbow stripes, leading uphill towards Hallgrímskirkja">
  <figcaption>The street you climb to get here. From the deck you look straight back down it.</figcaption>
</figure>

<h2>What you actually see</h2>

<p>Look west and you get the picture everyone comes for. Skólavörðustígur runs downhill in rainbow stripes, then the coloured metal roofs of the old centre stack up to the harbour, with the bay and Mount Esja behind. That is the view that justifies the ticket. It is also the one thing Perlan cannot give you: it sits too far out to look down on the roofs.</p>

<p>South and east are residential Reykjavik and, on a clear day, the Reykjanes peninsula. North is the harbour and the water. There is no bad side, but if you have one clear moment and a camera, take the west.</p>

<p>Light matters more than time of day here. In summer the low late sun does better than midday. In winter you are working with a narrow window either way, and an overcast day flattens the roofs into grey — which is worth knowing before you spend the 1,500 ISK on the wrong afternoon.</p>

<h2>Inside, which costs nothing</h2>

<p>The nave seats 1,200 and is deliberately plain: white, high, and almost empty of decoration. At the west end stands the Klais organ, built in Bonn and finished in 1992 — 5,275 pipes, 15 metres tall, about 25 tonnes. There is a second, smaller Frobenius organ from Denmark, rebuilt and reconsecrated in 2024. Organists fly in to record on the big one, and if a rehearsal is running when you walk in, stay for it.</p>

<p>The building took a long time. Guðjón Samúelsson, the state architect, won the commission in the 1930s and did not live to see it finished. Construction ran from 1945 to the consecration in 1986, and the congregation used the crypt for 26 years in between. The facade is usually described as basalt columns; the church itself compares it to columnar rock, Icelandic mountains and glaciers.</p>

<p>That comparison is the version every guidebook gives you. Why a state architect spent his career hunting for a specifically Icelandic style is a longer story, and the audio guide takes its time over it.</p>

<p>One more thing, out front. The statue on the plaza was standing here before the church was, and it was not Iceland's idea to put it there.</p>

<h2>Tower or Perlan?</h2>

<table class="tbl">
  <tr><th></th><th>Hallgrímskirkja</th><th>Perlan</th></tr>
  <tr><td>Where</td><td>Top of the old centre, walkable</td><td>On a hill outside the centre, bus or taxi</td></tr>
  <tr><td>The view</td><td>Down onto the coloured roofs and the rainbow street</td><td>Wide panorama: bay, city, mountains</td></tr>
  <tr><td>Deck</td><td>Enclosed, small</td><td>Open observation deck, plus exhibitions</td></tr>
  <tr><td>Ticket</td><td>1,500 ISK, door only</td><td>More; check the current price, it changes</td></tr>
  <tr><td>Time cost</td><td>30 minutes</td><td>Half a day with the trip out</td></tr>
</table>

<p>On a single day in the city, the tower wins on time alone. If you have two days and one of them is wet, Perlan is the better wet-day building, because there is something to do indoors.</p>

<div class="ticketbox">
  <h3>The tower has no tickets to book — these do</h3>
  <p>Nothing can be reserved for Hallgrímskirkja itself. The things around it can be: Perlan, the lagoons and the guided tours that pass the church all sell timed entry in advance.</p>
  <a class="btn sm" href="{TIQETS}" {OTA}>Reykjavik attraction tickets</a>
  <a class="btn sm outline" href="{GYG}" {OTA}>Compare city tours</a>
</div>

<h2>Three situations</h2>

<h3>You have a few hours between flights</h3>
<p>The tower is the single best use of a short stop: it is a twenty-minute walk from the bus stop in the centre, and it gives you the whole city at once. Go straight there, then come down into the old centre rather than the other way round.</p>

<h3>It is a Sunday</h3>
<p>Morning services close the church to visitors. Come after lunch, and in winter that still leaves you comfortably inside the 16:45 deadline.</p>

<h3>The weather has turned</h3>
<p>Do not write the tower off. The deck is enclosed and the wind that ruins the street is not a problem up there. Low cloud is the real spoiler — if you cannot see Esja from ground level, you will not see much from 73 metres either.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>The audio guide</h2>
    <p class="lead" style="max-width:720px">Standing on the deck tells you what Reykjavik looks like. Why the city grew exactly here, what the statue outside is doing on that plaza, and what the architect was really building are different questions.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="The TouringBee app showing the Reykjavik walking route, held up in front of Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">TouringBee Reykjavik audio guide</h3>
        <p class="meta" style="margin:0 0 10px">27 stops · 2–2.5 hours · one year of access</p>
        <div class="rate">{STARS}<b>4,7</b> {RATELABEL}</div>
        <div class="price">€9.99<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Hallgrímskirkja is one of the 27 stops</strong> — the walk runs from the founding hill to the old harbour</li>
          <li><strong>Works fully offline</strong> once downloaded — map and illustrations included</li>
          <li><strong>Go at your own pace.</strong> Break for the tower and pick it up where you left off</li>
          <li><strong>One payment.</strong> No group, no schedule, no guide waiting on you</li>
        </ul>
        <a {BUY} style="width:100%">Walk Reykjavik with the audio guide</a>
        <p class="meta" style="margin:12px 0 0;text-align:center">{CHECKOUTNOTE} <a href="{TBPRODUCT}" rel="noopener" data-no-widget>{OPENSHOP}</a>.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap prose">

<h2>Five mistakes</h2>
<ol>
  <li><strong>Looking for tickets online.</strong> They do not exist. The shop inside the church is the only seller.</li>
  <li><strong>Leaving it until late afternoon between September and May.</strong> 16:45 is the last trip up, whatever the sky is doing.</li>
  <li><strong>Turning up on a Sunday morning.</strong> Services close the church to visitors.</li>
  <li><strong>Trusting a price you read on a listings site.</strong> Several still show 1,400 ISK and a 16:30 cut-off.</li>
  <li><strong>Going up in low cloud.</strong> If Esja is invisible from the street, save the ticket for tomorrow.</li>
</ol>

<h2>Common questions</h2>
<div class="faq">{FAQHTML}</div>

<h2>Continue exploring</h2>
<ul>
  <li><a href="{ONEDAY}">Reykjavik in one day</a> — the itinerary this tower sits in the middle of</li>
  <li><a href="{KEF}">Keflavík airport to the city</a> — how to get in before any of this starts</li>
  <li><a href="{HOME}">The complete Reykjavik guide</a> — the walk, the day trips and the seasons</li>
  <li><a href="{GUIDES}">All Reykjavik guides</a> — what is published and what is in the works</li>
</ul>

<h2>The short version</h2>
<p>Walk in for free, pay 1,500 ISK at the shop if you want the view, and do it before 16:45 in winter. Look west for the roofs. Half an hour, and it is the best thirty minutes the old centre sells.</p>
<p>And if you would rather know what you are standing on top of than just look at it, take the <a href="#audio">TouringBee audio guide</a> along: 27 stops through the centre, this one included, fully offline.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">The church is stop one of twenty-seven</h2>
  <p>This page gets you up the tower at the right hour. The audio guide tells you what the city below you is.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Start the walk — €9.99</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Find a hotel in the centre</a>
  </div>
</div>

<p class="disc">Some links on this page are affiliate links — if you book through them we may earn a commission at no extra cost to you. Prices and opening hours were checked against hallgrimskirkja.is in September 2026 and change without notice; always confirm before you travel.</p>

  </div>
</section>
"""
