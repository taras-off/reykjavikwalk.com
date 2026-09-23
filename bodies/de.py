# -*- coding: utf-8 -*-
"""DE — auf Deutsch geschrieben, nicht übersetzt. Anrede: Sie. Die Geschichten bleiben beim Audioguide."""

HEADLINE = "Reykjavík an einem Tag: was Sie sehen und in welcher Reihenfolge"
TITLE = "Reykjavík an einem Tag: Rundgang mit Zeitplan"
DESC = ("Reykjavík an einem Tag: ein Rundgang entlang der zwei Grenzen, die den Tag entscheiden — "
        "dem Tageslicht und der letzten Turmauffahrt um 16:45 Uhr.")

FAQ = [
 ("Reicht ein Tag für Reykjavík?",
  "Für die Stadt selbst ja. Das alte Zentrum ist rund zwanzig Minuten breit, die klassische Route zu Fuß "
  "etwa 5 km lang — ein Tag deckt das mit Pausen locker ab. Für den Golden Circle oder die Südküste reicht "
  "ein Tag nicht zusätzlich: Das sind eigene Tage, und der größte Teil davon vergeht im Fahrzeug."),
 ("Wann sollte man im Winter starten?",
  "Im Dezember sollten Sie gegen 10:30 Uhr draußen sein und 16:45 Uhr als harte Grenze behandeln: Das ist "
  "von September bis Mai die letzte Auffahrt auf den Turm der Hallgrímskirkja. Alles nach Einbruch der "
  "Dunkelheit funktioniert weiter — Hafen, Schwimmbad, Abendessen. Der Ausblick und die Fotos nicht."),
 ("Brauche ich den Audioguide, wenn ich diesen Tagesplan schon habe?",
  "Diese Seite beantwortet wo und wann: Zeitplan, Öffnungszeiten, Buchungen und einen Plan B für schlechtes "
  "Wetter. Der Audioguide beantwortet, was Sie da eigentlich vor sich haben und warum es interessant ist — "
  "27 Geschichten entlang derselben Linie. Die Route ist also der Tagesplan, TouringBee die Erzählung "
  "unterwegs."),
 ("Braucht man für einen Tag in Reykjavík ein Auto?",
  "Nein. Der Stadttag lässt sich zu Fuß gehen und ist flach, bis auf einen Anstieg. Alles weiter draußen "
  "decken die Strætó-Busse für 690 ISK pro Fahrt ab. Ein Mietwagen lohnt sich erst, wenn Sie die Stadt "
  "verlassen."),
 ("Was kostet ein Tag in Reykjavík?",
  "Das Gehen kostet nichts. Die festen Posten sind klein: 1.500 ISK für den Kirchturm und 690 ISK für eine "
  "Busfahrt. Was die Summe bewegt, sind Lagune und Abendessen — zusammen können die beiden mehr ausmachen "
  "als alles andere."),
 ("Was sollte ich vorab buchen?",
  "Für einen normalen Stadttag vor allem die Lagune: Sky Lagoon und Blue Lagoon arbeiten mit Zeitfenstern, "
  "und die begehrten Abendfenster können früh ausverkauft sein. Im Sommer kommt eine Walbeobachtungstour "
  "dazu, am besten einen Tag vorher. Der Rest entscheidet sich am Morgen."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/hero-1536.webp" width="1536" height="864" alt="Die Uferpromenade von Reykjavík unter weitem isländischem Himmel" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reykjavík</a> › Ein Tag in Reykjavík</p>
    <h1>Reykjavík an einem Tag: was Sie sehen, und ein Plan, der das Tageslicht überlebt</h1>
    <p class="sub">Zwei Grenzen entscheiden diesen Tag: wie viele Stunden Licht Sie bekommen, und 16:45 Uhr. Alles andere ist verhandelbar.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, Autor der TouringBee-Audioguides">
      <span>Von Eugene · Aktualisiert am 23. September 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#plan">Zum Plan</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Tagesausflüge</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">Ende Dezember klettert die Sonne gegen 11:20 Uhr über die Dächer und ist um halb vier wieder verschwunden. Die letzte Auffahrt auf den Turm der Hallgrímskirkja geht um 16:45 Uhr. Zwischen diesen beiden Uhrzeiten liegt Ihr ganzer Tag in Reykjavík.</p>

<p>Was jetzt kommt, ist deshalb keine Liste von Sehenswürdigkeiten, sondern ein Zeitplan. Das alte Zentrum ist zwanzig Minuten breit, die gesamte Gehstrecke rund 5 km. Die Beine sind hier nicht das Problem. Das Licht und die Öffnungszeiten sind es.</p>

<p>Sie können den ganzen Tag allein mit dieser Seite gehen. Wenn Sie zusätzlich wissen wollen, was hinter den Orten unterwegs steckt: <a href="#audio">der TouringBee-Audiorundgang</a> folgt derselben Linie. Sie planen noch die ganze Reise? Beginnen Sie mit <a href="{HOME}">unserem kompletten Reykjavík-Guide</a>.</p>

<div class="glance">
  <h2>Auf einen Blick</h2>
  <dl>
    <dt>Zu Fuß</dt><dd>Rund 5 km, flach bis auf den Anstieg der Skólavörðustígur</dd>
    <dt>Ablauf</dt><dd>Altes Zentrum → Kirche und Turm → Uferpromenade → warmes Wasser</dd>
    <dt>Harte Grenze</dt><dd>16:45 Uhr — letzte Turmauffahrt, 1. September bis 31. Mai</dd>
    <dt>Turmticket</dt><dd>1.500 ISK Erwachsene · 200 ISK Kinder 7–16 · nur vor Ort erhältlich</dd>
    <dt>Busfahrt</dt><dd>690 ISK pro Einzelfahrt bei Strætó</dd>
    <dt>Vorab buchen</dt><dd>Die Lagune — die eine Reservierung, die sich vor der Anreise lohnt</dd>
    <dt>Schlechtester Monat zum Improvisieren</dt><dd>Dezember — etwa vier nutzbare Stunden Licht</dd>
  </dl>
</div>

<div class="minicta">
  <h2>Gehen Sie diese Route mit dem Audioguide</h2>
  <p>Dieselbe Linie durch das Zentrum, erzählt: <strong>27 Stationen, 2 bis 2,5 Stunden</strong>, Karte und Audio offline. Unterbrechen Sie für den Turm, das Mittagessen oder ein Museum und machen Sie dort weiter, wo Sie aufgehört haben.</p>
  <a {BUY}>Reykjavík-Audioguide — 9,99 €</a>
</div>

<h2 id="plan">Prüfen Sie zuerst zwei Dinge: Sonnenuntergang und Turm</h2>

<p>Die erste Grenze ist die Sonne, und sie ist gnadenlos. Reykjavík liegt knapp unter dem Polarkreis, der Unterschied zwischen Hochsommer und Mittwinter ist also größer als fast überall, wo Reisende vorher waren.</p>

<table class="tbl">
  <tr><th>Monat</th><th>Nutzbares Tageslicht</th><th>Was das für einen Tag bedeutet</th></tr>
  <tr><td>Dezember – Januar</td><td>ca. 4–5 Stunden</td><td>Ein Block draußen, nicht zwei. Alles andere passiert im Dunkeln, und das ist in Ordnung.</td></tr>
  <tr><td>Februar – April</td><td>Nimmt schnell zu</td><td>Die ganze Route bei Tageslicht, und die Nächte noch dunkel genug für Polarlichter.</td></tr>
  <tr><td>Mai – Juli</td><td>Praktisch rund um die Uhr</td><td>Start um zwölf oder um neun Uhr abends. Die Lichtgrenze fällt weg; es ist zugleich Hochsaison.</td></tr>
  <tr><td>August – November</td><td>Nimmt schnell ab</td><td>September und Oktober sind ein fairer Kompromiss zwischen Taglänge und Nächten, die dunkel genug fürs Polarlicht sind.</td></tr>
</table>

<p>Die zweite Grenze ist der Turm. Die Hallgrímskirkja bleibt der einzige hohe Aussichtspunkt im Zentrum, und von 1. September bis 31. Mai schließt die Kirche um 17:00 Uhr, letzte Auffahrt 16:45 Uhr. Im Sommer geht es bis 20:00 Uhr, der Turm bis 19:45 Uhr. Tickets lassen sich nicht reservieren und gelten einmalig am Kauftag — einschieben, wann es gerade passt, geht also nicht.</p>

<table class="tbl">
  <tr><th>Turmticket</th><th>Preis</th></tr>
  <tr><td>Erwachsene</td><td>1.500 ISK</td></tr>
  <tr><td>Kinder 7–16 Jahre</td><td>200 ISK</td></tr>
  <tr><td>Studierende, Senioren ab 67, Menschen mit Behinderung</td><td>1.300 ISK</td></tr>
</table>

<p>Gottesdienste und Konzerte schließen die Kirche ohne große Vorwarnung für Besucher. Werfen Sie also einen Blick auf das Tagesprogramm, bevor Sie den Nachmittag um den Turm herum bauen.</p>

<figure>
  <img src="{P}img/tile-hallgrimskirkja.webp" width="800" height="600" loading="lazy" alt="Die Hallgrímskirkja von unten, daneben weht die isländische Flagge">
  <figcaption>Die einzige Station des Tages mit Schließzeit — und die eine, für die sich Umplanen lohnt.</figcaption>
</figure>

<h2>Vormittag: das alte Zentrum</h2>

<p>Beginnen Sie auf dem Arnarhóll, dem niedrigen grünen Hügel über der Hafenstraße, wo die Statue des Stadtgründers über die Bucht blickt. Den Platz hat er nicht selbst ausgesucht. Er hat etwas anderes für sich aussuchen lassen — eine Geschichte, für die sich der Audioguide Zeit nimmt.</p>

<p>Von dort entfaltet sich das alte Zentrum bergab in etwa drei Straßen. Der Austurvöllur hat das Parlament an einer Seite. Im Teich Tjörnin steht das Rathaus auf Stelzen. Dazwischen liegen die kleinen Museen, darunter jenes, das um eine ausgegrabene Langhauswand unter dem Gehweg herum gebaut wurde. Nichts davon dauert lange. Alles davon ist frei zugänglich.</p>

<p>Zwei praktische Hinweise. Island ist extrem kartenorientiert — Sie können eine Woche hier verbringen, ohne Bargeld anzufassen, und einige Stellen nehmen gar keines mehr. Und das Leitungswasser ist überall ausgezeichnet und kostenlos, eine wiederbefüllbare Flasche spart also mehr, als man denkt.</p>

<h2>Mittag: die Regenbogenstraße, dann der Turm</h2>

<p>Die Skólavörðustígur steigt von der Einkaufsstraße bis zur Kirchentür an, und ihr letzter Block ist dauerhaft in Regenbogenstreifen bemalt. Sie gehört zu den meistfotografierten Orten Reykjavíks. Früh oder spät haben Sie sie fast für sich; zwischen elf und drei im Sommer nicht.</p>

<p>Fahren Sie jetzt auf den Turm hinauf und heben Sie ihn sich nicht für das Tagesende auf. Im Winter ist genau das der Grund, warum der Vormittag zusammengedrückt wurde. Im Sommer haben Sie mehr Luft, ruhiger ist es aber meist früh oder kurz vor der letzten Auffahrt.</p>

<h2>Mittagessen und die eine Buchung</h2>

<p>Gegessen wird an der Laugavegur und in den Straßen daneben. Der günstige Klassiker ist die isländische <em>Pylsa</em>: ein Hotdog aus einer Mischung von Lamm, Schwein und Rind. Bestellen Sie <em>eina með öllu</em> — „einen mit allem“. Im Winter erledigt eine Lammsuppe dieselbe Aufgabe. Restaurants mit Bedienung sind wirklich teuer — hier hört ein Tag in Reykjavík auf, günstig zu sein.</p>

<div class="ticketbox">
  <h3>Buchen Sie die Lagune vor dem Abflug</h3>
  <p>Sky Lagoon und Blue Lagoon arbeiten mit Zeitfenstern, und die begehrten Abendfenster können früh ausverkauft sein. Für einen normalen Stadttag ist das die wichtigste Reservierung vor der Anreise.</p>
  <a class="btn sm" href="{TIQETS}" {OTA}>Tickets für die Lagune ansehen</a>
  <a class="btn sm outline" href="{GYG}" {OTA}>Touren und Transfers vergleichen</a>
</div>

<h2>Nachmittag: die Uferpromenade</h2>

<p>Die zweite Tageshälfte verläuft am Meer. Harpa, das gläserne Konzerthaus am Hafenrand, ist frei zugänglich und an einem hellen Tag fünf Minuten Stillstehen im Inneren wert. Weiter am Sæbraut-Weg steht der Sun Voyager, die Stahlskulptur, die alle als Wikingerschiff fotografieren. Sie ist keines, und der wahre Grund ist besser als der Mythos.</p>

<figure>
  <img src="{P}img/sec-sun-voyager.webp" width="1024" height="683" loading="lazy" alt="Eine Besucherin geht im Winter an der Skulptur Sun Voyager an der Sæbraut vorbei">
  <figcaption>Ständig fotografiert und fast immer falsch benannt.</figcaption>
</figure>

<p>Dann der alte Hafen: Boote zur Walbeobachtung, Fischrestaurants und ein graues Schiff der Küstenwache am Kai, mit einer Kampfbilanz gegen eine weit größere Marine. Wer bis ans Ende geht, steht am Grashügel, an dem die Audioroute endet.</p>

<p>Hier fällt die einzige echte Entscheidung des Nachmittags. Eine Walbeobachtungsfahrt ab dem alten Hafen dauert etwa drei Stunden und frisst den Rest Ihres Tageslichts. Im Sommer lohnt sich das, wenn Sie wegen der Tiere gekommen sind; im Dezember ist es ein schlechtes Geschäft, weil diese drei Stunden Ihr ganzes Licht sind.</p>

<h2>Abend: erst warmes Wasser, dann Essen</h2>

<p>Isländer beenden den Tag eher im Wasser als in der Bar, und Sie haben zwei Preisklassen zur Wahl.</p>

<p>Die Sky Lagoon ist die polierte Variante: am Ozean, fünfzehn Minuten vom Zentrum, mit einem siebenstufigen Ritual im Ticket. Der Saman-Pass beginnt bei rund 113 € pro Erwachsenem (57 € für Jugendliche), Sér mit privaten Umkleiden bei etwa 136 €.</p>

<p>Die einheimische Variante ist ein städtisches Thermalbad — Sundhöllin im Zentrum, Laugardalslaug für die volle Anlage. Aus dem Boden geheizt, lange geöffnet und ein Bruchteil des Lagunenpreises; den aktuellen Erwachsenentarif finden Sie auf reykjavik.is. Eine Regel zählt mehr als alle anderen: Vor dem Wasser wird gründlich geduscht, ohne Badekleidung. Das hängt in jeder Umkleide aus, und es wird durchgesetzt.</p>

<h2>Drei Varianten</h2>

<h3>Ein Zwischenstopp, kein ganzer Tag</h3>
<p>Wenn Sie zwischen zwei Flügen sechs oder sieben Stunden in der Stadt haben, lassen Sie die Hälfte am Wasser weg. Mit dem Bus aus Keflavík, altes Zentrum und Turm, Mittagessen an der Laugavegur, Bus zurück. Das passt in einen kurzen Aufenthalt samt Transfer in beide Richtungen und bringt Ihnen trotzdem die beste Aussicht der Stadt.</p>

<h3>Ein Dezembertag</h3>
<p>Drücken Sie alles im Freien in 11:00 bis 15:30 Uhr und nehmen Sie hin, dass Hafen, Abendessen und Schwimmbad im Dunkeln stattfinden. Das ist keine Verschlechterung: Die Hafenlichter auf dem Wasser sind besser als die Tagesversion. Und die lange dunkle Hälfte des Tages ist Ihre Chance auf ein Polarlicht, wenn Bewölkung und Sonnenaktivität mitspielen. Der dunkle Abschnitt der Sæbraut ist aus der Stadt heraus am einfachsten. Der Leuchtturm Grótta, eine Busfahrt weiter westlich, ist noch dunkler. Beides ersetzt aber keine richtige Fahrt weg von den Stadtlichtern.</p>

<h3>Ein nasser Tag mit Wind von der Seite</h3>
<p>Das Wetter wechselt hier stündlich, und den Schaden richtet der Wind an. An einem schlechten Tag drehen Sie den Plan um: Museen und Schwimmbad in die Tagesmitte, der Spaziergang in das Fenster, das sich auftut. Ein Regenschirm nützt hier meist wenig — eine kräftige Bö stülpt ihn um. Eine wasserdichte Jacke mit Kapuze und eine Mütze sind zuverlässiger, in jedem Monat.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>Der Audioguide</h2>
    <p class="lead" style="max-width:720px">Die Route zu sehen ist das eine. Zu verstehen, warum Reykjavík überhaupt hier entstanden ist, was der Sun Voyager wirklich darstellt und wie ein derart kleines Land es mit weit größeren aufnehmen konnte, ist etwas anderes.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="Die TouringBee-App mit der Reykjavík-Route, hochgehalten vor der Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">TouringBee-Audioguide für Reykjavík</h3>
        <p class="meta" style="margin:0 0 10px">27 Stationen · 2–2,5 Stunden · ein Jahr Zugriff</p>
        <div class="rate">{STARS}<b>4,7</b> {RATELABEL}</div>
        <div class="price">9,99 €<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Funktioniert nach dem Download vollständig offline</strong> — Karte und Illustrationen inklusive, unterwegs ist kein Datenvolumen nötig</li>
          <li><strong>In Ihrem Tempo.</strong> Unterbrechen Sie fürs Mittagessen oder ein Museum und setzen Sie zwei Stunden später an derselben Stelle fort</li>
          <li><strong>Aus der Rolle erzählt</strong> — von einem Fischer aus Reykjavík, der noch Zeit bis zur nächsten Ausfahrt hat</li>
          <li><strong>Eine Zahlung.</strong> Keine Gruppe, kein Zeitplan, kein Guide, der auf Sie wartet</li>
        </ul>
        <a {BUY} style="width:100%">Reykjavík mit dem Audioguide gehen</a>
        <p class="meta" style="margin:12px 0 0;text-align:center">{CHECKOUTNOTE} <a href="{TBPRODUCT}" rel="noopener" data-no-widget>{OPENSHOP}</a>.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap prose">

<h2>Was der Tag kostet</h2>
<table class="tbl">
  <tr><th>Posten</th><th>Kosten</th></tr>
  <tr><td>Die Stadt zu Fuß</td><td>Kostenlos</td></tr>
  <tr><td>Audioguide, einmalige Zahlung</td><td>9,99 €</td></tr>
  <tr><td>Turm der Hallgrímskirkja, Erwachsene</td><td>1.500 ISK</td></tr>
  <tr><td>Strætó-Einzelfahrt</td><td>690 ISK</td></tr>
  <tr><td>Städtisches Schwimmbad</td><td>Ein Bruchteil eines Lagunentickets</td></tr>
  <tr><td>Sky Lagoon, Saman-Pass</td><td>ab etwa 113 €</td></tr>
  <tr><td>Walbeobachtung, ca. 3 Stunden</td><td>Preis beim Anbieter; der eigentliche Preis ist das Tageslicht</td></tr>
</table>

<p>Die Stadt selbst ist nicht teuer. Das Budget steigt deutlich, sobald Lagune, Ausflüge aufs Land und Restaurantabende dazukommen.</p>

<h2>Fünf Fehler, die den Tag kosten</h2>
<ol>
  <li><strong>Den Turm im Winter bis zum Schluss aufheben.</strong> Letzte Auffahrt 16:45 Uhr, September bis Mai, und Tickets gibt es nur vor Ort.</li>
  <li><strong>Den Golden Circle auf einen Stadttag draufpacken.</strong> Das sind acht Stunden im Fahrzeug. Er braucht seinen eigenen Tag.</li>
  <li><strong>Im Dezember fast das ganze Tageslicht einem Boot geben.</strong> Drei Stunden auf See bei vier Stunden Licht.</li>
  <li><strong>Sich auf einen Regenschirm verlassen.</strong> Der Wind stülpt ihn um. Lieber Schichten, Kapuze und Mütze.</li>
  <li><strong>Die Lagune für einen Ort halten, an dem man einfach hineingeht.</strong> Es gibt Zeitfenster, und die Abendfenster gehen zuerst.</li>
</ol>

<h2>Häufige Fragen</h2>
<div class="faq">{FAQHTML}</div>

<h2>Weiterlesen</h2>
<ul>
  <li><a href="{HOME}">Der komplette Reykjavík-Guide</a> — der Rundgang, die Ausflüge und die Jahreszeiten</li>
  <li><a href="{GUIDES}">Alle Reykjavík-Guides</a> — was veröffentlicht ist und was noch kommt</li>
</ul>

<h2>Kurz gefasst</h2>
<p>Reykjavík gibt an einem Tag zu Fuß fast alles her, was es hat. Die Entfernungen werden nie das Problem sein. Das Licht schon.</p>
<p>Prüfen Sie also den Sonnenuntergang, heben Sie sich den Turm nicht für den Abend auf und gehen Sie den Rest in Ihrem Tempo. Und wenn Sie die Stadt unterwegs verstehen statt nur ansehen wollen, nehmen Sie <a href="#audio">den TouringBee-Audioguide für Reykjavík</a> mit: 27 Stationen, 2–2,5 Stunden, vollständig offline.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">Siebenundzwanzig Stationen auf derselben Linie</h2>
  <p>Diese Seite bringt Sie zur richtigen Zeit an den richtigen Ort. Der Audioguide sagt Ihnen, wovor Sie stehen.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Rundgang starten — 9,99 €</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Hotel im Zentrum finden</a>
  </div>
</div>

<p class="disc">Einige Links auf dieser Seite sind Affiliate-Links — wenn Sie darüber buchen, erhalten wir unter Umständen eine Provision, ohne Aufpreis für Sie. Preise und Öffnungszeiten wurden im September 2026 auf den Seiten der Anbieter geprüft und ändern sich ohne Ankündigung; prüfen Sie sie vor der Reise. Turm: hallgrimskirkja.is. Busse: straeto.is. Lagune: skylagoon.com.</p>

  </div>
</section>
"""
