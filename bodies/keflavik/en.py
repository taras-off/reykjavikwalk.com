# -*- coding: utf-8 -*-
"""EN-мастер RKV-03 — из Кеблавика в город.

Идея страницы: сам трансфер решается тривиально, а ломается день о разрыв
между посадкой и заселением. Поэтому выбор транспорта — производная от того,
во сколько вы сели, а не от цены.

Страница логистическая, крючков два, а не три-пять: историй здесь просто нет.
"""

HEADLINE = "Keflavík airport to Reykjavik: which transfer fits your landing time"
TITLE = "Keflavík Airport to Reykjavik: Bus, Taxi or Car"
DESC = ("Keflavík airport to Reykjavik: real prices for the Flybus, the public bus and a car, "
        "and what to do with the hours between landing and hotel check-in.")

FAQ = [
 ("What is the cheapest way from Keflavík airport to Reykjavik?",
  "The public bus, Strætó route 55, at 2,400 ISK for an adult. Young people aged 12 to 17, visitors "
  "aged 67 and over and disabled passengers pay 1,200 ISK, and children under 12 travel free. It runs "
  "every day but not on every arrival, and not every trip ends at BSÍ — some finish at Fjörður in "
  "Hafnarfjörður, which is not the city centre."),
 ("How long does it take to get from Keflavík to Reykjavik?",
  "About 45 minutes by coach for the roughly 50 km, and much the same by car. The journey is not where "
  "time goes. Waiting for a bus that leaves 35 to 45 minutes after your flight lands, and then waiting "
  "again because your room is not ready until the afternoon, is where it goes."),
 ("Do I need to book the airport bus in advance?",
  "Usually not. The Flybus sells tickets at the airport as well as online, and departures are timed to "
  "arriving flights. Booking online saves a little, saves queueing after a long flight and is worth doing "
  "on busy dates. If your flight is delayed, the operator moves your seat to the next departure rather "
  "than holding the bus."),
 ("Does the Flybus go to my hotel?",
  "The standard fare takes you to the BSÍ terminal. Flybus+ continues to participating hotels and "
  "guesthouses in a minibus, for a supplement. If your accommodation is in the old centre, the standard "
  "ticket plus a short walk is often faster than waiting for the minibus leg."),
 ("Is a rental car worth it just for the airport transfer?",
  "Not on its own. One road, 45 minutes, and then a car you have to park in a city you can cross on "
  "foot. A rental starts to make sense when the airport is the start of a road trip: the Golden Circle, "
  "the south coast, anything outside the capital. The real question is whether you are leaving town."),
 ("Where can I leave my bags before check-in?",
  "There are lockers at the airport and at the BSÍ terminal, where the Flybus arrives. The BSÍ lockers "
  "run 24 hours with 96 lockers in four sizes, which matters if you land at six in the morning and "
  "cannot get into your room until two in the afternoon."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/sec-old-town.webp" width="1024" height="683" alt="A bicycle parked by a shop window in the old centre of Reykjavik" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reykjavik</a> › Keflavík airport to the city</p>
    <h1>Keflavík airport to Reykjavik: the options, and which one fits your landing time</h1>
    <p class="sub">Fifty kilometres, one road, forty-five minutes. The transfer is the easy part — the gap between landing and check-in is not.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, author of the TouringBee audio tours">
      <span>By Eugene · Updated 5 October 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#options">Compare the options</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Transfers &amp; day trips</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">There is one road from Keflavík to Reykjavik and it takes about 45 minutes. The airport coach times its departures to arriving flights, usually leaving 35 to 45 minutes after a landing, on a timetable that runs from about 03:30 until late evening. Getting into town is a solved problem.</p>

<p>What is not solved is the hour you land. Hotel check-in in Reykjavik is normally 14:00 or 15:00. Land before that and you arrive in the city with your bags, a closed room and several hours to fill — and that, not the 50 km, is what decides which ticket you should buy.</p>

<p>So this page does both halves: every transfer option with the prices the operators actually charge, and then what to do with the gap. If the gap lands you in the centre with time to kill, our <a href="{ONEDAY}">one-day itinerary</a> and the <a href="#audio">TouringBee audio walk</a> are built for exactly those hours. Planning the whole trip? Start from the <a href="{HOME}">complete Reykjavik guide</a>.</p>

<div class="glance">
  <h2>At a glance</h2>
  <dl>
    <dt>Distance</dt><dd>About 50 km from the airport to the city centre</dd>
    <dt>Journey</dt><dd>Around 45 minutes by coach or car</dd>
    <dt>Flybus</dt><dd>From 3,999 ISK one way to the BSÍ terminal</dd>
    <dt>Public bus</dt><dd>Strætó 55 — 2,400 ISK adult, 1,200 ISK reduced, under-12s free</dd>
    <dt>Departures</dt><dd>Flybus times departures to arrivals, roughly 03:30 to late evening; Strætó runs to a fixed timetable</dd>
    <dt>Booking</dt><dd>Not required. Tickets sold at the airport</dd>
    <dt>Luggage</dt><dd>Lockers at the airport and at BSÍ, 24 hours</dd>
    <dt>The real constraint</dt><dd>Check-in at 14:00–15:00, not the transfer</dd>
  </dl>
</div>

<div class="minicta">
  <h2>Landing early? That is the walk's slot</h2>
  <p>The TouringBee audio walk is <strong>27 stops, 2–2.5 hours</strong> through the old centre, offline map and audio. Bags in a locker at BSÍ, and the dead hours before check-in turn into the best part of day one.</p>
  <a {BUY}>Reykjavik audio guide — €9.99</a>
</div>

<h2 id="options">Start with your landing time, not the price</h2>

<p>Every guide to this route compares fares. Price is only half the calculation: a cheap ticket stops being good value the moment its timetable adds an hour of waiting.</p>

<p>Ask instead: what time do the wheels touch down, and where are you sleeping? Land at midday with a room ready at two, and anything works. Land at six in the morning and you need a plan for your bags and for yourself. The cheapest bus does not meet every flight, so it can cost you an hour you would rather have spent elsewhere.</p>

<table class="tbl">
  <tr><th>Option</th><th>Price</th><th>Goes to</th><th>Best when</th></tr>
  <tr><td><strong>Flybus</strong></td><td>from 3,999 ISK one way</td><td>BSÍ terminal</td><td>Default. Departures tied to arrivals; if you are delayed your seat moves to the next bus</td></tr>
  <tr><td><strong>Flybus+</strong></td><td>supplement on top</td><td>Participating hotels</td><td>Lots of luggage, or staying outside the old centre</td></tr>
  <tr><td><strong>Airport Direct</strong></td><td>see operator</td><td>Central terminal, hotels on the premium tier</td><td>The second scheduled coach — worth price-checking against Flybus</td></tr>
  <tr><td><strong>Strætó 55</strong></td><td>2,400 ISK adult</td><td>BSÍ or Fjörður</td><td>Daytime, light bags, timetable fits</td></tr>
  <tr><td><strong>Taxi or private transfer</strong></td><td>Metered or quoted</td><td>Your door</td><td>Three or four of you, or an awkward hour</td></tr>
  <tr><td><strong>Rental car</strong></td><td>Daily rate</td><td>Wherever you want</td><td>Only if you are leaving town later</td></tr>
</table>

<h2>The Flybus, which is the default for a reason</h2>

<p>It is the airport coach most people take, and the thing it sells is not speed but certainty. Departures are tied to arriving flights rather than to a fixed interval, usually going 35 to 45 minutes after a landing. The published timetable starts around 03:30 and runs into the late evening, so for a very early or very late flight check the schedule for your own date rather than assuming.</p>

<p>If your flight is delayed, the operator does not hold the bus for you — it guarantees you a seat on the next departure instead, at no extra cost. That is a meaningful difference and worth knowing before you panic in the immigration queue. The fare includes two bags up to 23 kg each.</p>

<p>The standard ticket ends at BSÍ, the bus terminal on the southern edge of the centre. Flybus+ adds a minibus leg to participating hotels for a supplement. It earns its money with heavy bags, with children, in bad weather, or when your guesthouse is out in the suburbs.</p>

<p>If you are travelling light and staying in the old centre, it is worth comparing: the minibus works through a list of addresses, and yours may not be first. Look up how far your hotel is from BSÍ before you buy the upgrade, and decide on that rather than by default.</p>

<h2>Strætó 55, the cheap one, and its catch</h2>

<p>The public bus is route 55 and it costs 2,400 ISK for an adult — 1,200 ISK for 12 to 17-year-olds, over-67s and disabled passengers, free under 12. For a family that gap is real money.</p>

<p>Two catches. It runs to a timetable rather than to your flight, so a 05:30 landing can mean a long wait. And not every trip ends at BSÍ: some finish at Fjörður in Hafnarfjörður, a town south of Reykjavik, which is emphatically not the city centre. Check which one your departure is before you board, not after.</p>

<div class="ticketbox">
  <h3>Private transfers and tours</h3>
  <p>If there are three or four of you, work out the per-head bus fare against one vehicle before you assume the coach is cheaper. Private transfers and the day trips that collect from Keflavík are sold in advance.</p>
  <a class="btn sm" href="{GYG}" {OTA}>Compare transfers</a>
  <a class="btn sm outline" href="{TIQETS}" {OTA}>Reykjavik tickets</a>
</div>

<h2>Taxi, and when the maths flips</h2>

<p>Icelandic taxis are metered and there is no published flat airport rate, so treat a taxi as the expensive option and ask for an estimate before you get in.</p>

<p>For three or four people, get a current estimate and compare it with the total of your bus tickets. A taxi is charged per vehicle and a bus per passenger, so the gap closes as the group grows — which does not make the taxi cheap, only closer than it looks for one traveller.</p>

<h2>A rental car, honestly</h2>

<p>For the transfer alone, no. It is one straight road you will drive once, and at the other end you have a car to park in a city you can cross on foot. A rental starts to make sense when the airport is the beginning of a road trip — the Golden Circle, the south coast, anything outside the capital. Decide it on the trip, not on the transfer.</p>

<figure>
  <img src="{P}img/sec-winter-street.webp" width="1024" height="683" loading="lazy" alt="A brightly painted corner shop on a snowy street in central Reykjavik">
  <figcaption>BSÍ sits just south of all this. Most of the old centre is a short walk from the terminal door.</figcaption>
</figure>

<h2>The gap between landing and check-in</h2>

<p>This is the part nobody plans and everybody runs into. Your room is not ready until two in the afternoon. Your flight landed at six in the morning. You are in the centre by eight with a suitcase.</p>

<p>The bags are the easy half, and the first move is the one people forget: ask your hotel. A room that is not ready is not the same as a hotel that cannot help, and most will hold luggage until check-in at no charge. That also puts your case where you are sleeping, which beats a locker.</p>

<p>If the answer is no, or you have booked an apartment with no reception, there are lockers at Keflavík and at BSÍ. The BSÍ set runs 24 hours with 96 lockers in four sizes, which is more than most terminals this size manage.</p>

<p>The hours are the better half, because the old centre is about twenty minutes across and does not need a hotel room to be enjoyed. A gap of four or five hours fits the 2 to 2.5-hour walking route this site is built around, with room left for breakfast and a long coffee. The cafés open well before the check-in desks do.</p>

<h2>Three timings</h2>

<h3>If you land early</h3>
<p>The Flybus, because its departures follow the arrivals. Bags dealt with, breakfast in the centre, and start walking when it gets light — around the winter solstice that is not until roughly eleven in the morning, so plan a warm indoor hour first.</p>

<h3>If you land late</h3>
<p>The Flybus again: its timetable runs into the late evening and the last departures are matched to late arrivals, which the public bus is not. Check the last departure for your date, though. If you land after the coaches have stopped, a taxi is not an extravagance, it is the only thing left.</p>

<h3>If you fly out early</h3>
<p>Work backwards from the check-in desk, not the gate, and add the 45 minutes plus whatever the hotel pick-up costs you. Early departures mean coaches leaving the city in the small hours; the Flybus timetable covers them, the city bus does not.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>The audio guide</h2>
    <p class="lead" style="max-width:720px">You will have hours in the centre before anyone gives you a key. Walking it is obvious. Knowing why the city is here at all, and why the walk starts on that particular hill, is the part you have to bring with you.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="The TouringBee app showing the Reykjavik walking route, held up in front of Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">TouringBee Reykjavik audio guide</h3>
        <p class="meta" style="margin:0 0 10px">27 stops · 2–2.5 hours · one payment, one year of access</p>
        <div class="price">€9.99<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Fits the dead hours.</strong> Two to two and a half hours, which is about what you have before check-in</li>
          <li><strong>Works fully offline</strong> once downloaded — useful before you have sorted out data in a new country</li>
          <li><strong>Go at your own pace.</strong> Stop for breakfast and pick it up where you left off</li>
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

<h2>Prices: transfer, luggage and the walk</h2>
<table class="tbl">
  <tr><th>Item</th><th>Cost</th></tr>
  <tr><td>Strætó 55, adult</td><td>2,400 ISK</td></tr>
  <tr><td>Strætó 55, 12–17, 67+, disabled</td><td>1,200 ISK</td></tr>
  <tr><td>Strætó 55, under 12</td><td>Free</td></tr>
  <tr><td>Flybus to BSÍ, one way</td><td>from 3,999 ISK</td></tr>
  <tr><td>Airport Direct</td><td>Check the operator before you choose</td></tr>
  <tr><td>Flybus+ hotel drop-off</td><td>Supplement on top; check the operator</td></tr>
  <tr><td>Taxi</td><td>Metered, no published airport flat rate</td></tr>
  <tr><td>Luggage locker</td><td>Available at the airport and at BSÍ, 24 h</td></tr>
  <tr><td>Audio guide for the gap</td><td>€9.99, one payment, one year of access</td></tr>
</table>

<h2>Five mistakes</h2>
<ol>
  <li><strong>Choosing on fare alone.</strong> Check your landing time and the timetable first: the cheap option can add a long wait.</li>
  <li><strong>Assuming the public bus meets your flight.</strong> It runs to a timetable; the Flybus runs to arrivals.</li>
  <li><strong>Boarding a 55 without checking the destination.</strong> Some trips end at Fjörður, not BSÍ.</li>
  <li><strong>Paying for Flybus+ automatically.</strong> If your hotel is near BSÍ and your bags are light, compare the walk against the minibus round first.</li>
  <li><strong>Renting a car for the transfer.</strong> Rent it the day you leave town, not the day you land.</li>
</ol>

<h2>Common questions</h2>
<div class="faq">{FAQHTML}</div>

<h2>Continue exploring</h2>
<ul>
  <li><a href="{ONEDAY}">Reykjavik in one day</a> — what to do with the hours you just freed up</li>
  <li><a href="{TOWER}">Hallgrímskirkja and the tower</a> — tickets, hours and the 16:45 deadline</li>
  <li><a href="{HOME}">The complete Reykjavik guide</a> — the walk, the day trips and the seasons</li>
  <li><a href="{GUIDES}">All Reykjavik guides</a></li>
</ul>

<h2>The short version</h2>
<p>Take the Flybus unless you have a reason not to: it meets every flight, waits when they are late, and drops you at the edge of the centre for 3,999 ISK. Take the 55 if the timetable fits and you are counting every króna. Take a car only if you are leaving town.</p>
<p>Then put the bags in a locker and use the hours. If you would rather understand the city than simply wait in it, take the <a href="#audio">TouringBee audio guide</a> along: 27 stops, 2–2.5 hours, fully offline.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">Your room is not ready until two</h2>
  <p>The walk is two and a half hours. The arithmetic does itself.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Start the walk — €9.99</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Find a hotel in the centre</a>
  </div>
</div>

<p class="disc">Some links on this page are affiliate links — if you book through them we may earn a commission at no extra cost to you. Fares and timings were checked against the operators' own sites in October 2026 and change without notice; always confirm before you travel. Flybus: flybus.is. Public bus: straeto.is.</p>

  </div>
</section>
"""
