# -*- coding: utf-8 -*-
"""DE — auf Deutsch geschrieben. Anrede: Sie. Die Geschichten bleiben beim Audioguide."""

HEADLINE = "Hallgrímskirkja-Turm: Tickets, Öffnungszeiten und wann hinauf"
TITLE = "Hallgrímskirkja: Tickets, Öffnungszeiten und Turmbesuch"
DESC = ("Turmtickets und Öffnungszeiten der Hallgrímskirkja, die Grenze 16:45 Uhr im Winter, was der "
        "Ausblick wirklich zeigt und wann die Kirche geschlossen ist.")

FAQ = [
 ("Was kostet die Auffahrt auf die Hallgrímskirkja?",
  "1.500 ISK für Erwachsene und 200 ISK für Kinder von 7 bis 16 Jahren. Studierende und Menschen mit "
  "Behinderung zahlen 1.300 ISK; ab 67 gibt es eine Ermäßigung, deren Betrag die Kirche allerdings nicht "
  "veröffentlicht. Ab zehn Personen 10 Prozent Nachlass, Schulgruppen bis 16 Jahre frei. Die Kirche "
  "selbst zu betreten kostet nichts — nur der Turm ist kostenpflichtig."),
 ("Kann man Turmtickets online buchen?",
  "Nein. Die Kirche sagt deutlich, dass sich der Turm nicht im Voraus reservieren lässt. Tickets gibt es "
  "im Kirchenladen, links vom Eingangsbereich, und sie gelten einmalig am Kauftag. Was online als "
  "Hallgrímskirkja-Ticket verkauft wird, ist etwas anderes: eine Führung, die vor der Kirche hält, nicht "
  "der Zugang zum Turm."),
 ("Wann schließt der Turm der Hallgrímskirkja?",
  "Vom 1. September bis 31. Mai schließt die Kirche um 17:00 Uhr, die letzte Auffahrt ist um 16:45 Uhr. "
  "Vom 1. Juni bis 31. August ist bis 20:00 Uhr geöffnet, der Turm bis 19:45 Uhr. Gottesdienste, "
  "Amtshandlungen und Konzerte schließen die Kirche zusätzlich für Besucher — schauen Sie ins "
  "Tagesprogramm, bevor Sie den Nachmittag darum herum planen."),
 ("Lohnt sich der Turm?",
  "Für den Ausblick ja: Es ist der einzige hohe Punkt im alten Zentrum und der einzige, von dem aus Sie "
  "senkrecht auf die bunten Dächer sehen. Zwanzig Minuten und 1.500 ISK sind ein fairer Tausch. Für ein "
  "breiteres Panorama über die ganze Bucht und die Berge ist Perlan besser, kostet aber mehr und frisst "
  "einen halben Tag."),
 ("Fährt ein Aufzug bis ganz nach oben?",
  "Fast. Ein Aufzug nimmt den größten Teil der Höhe, danach folgt eine kurze Treppe bis zur "
  "Aussichtsebene. Die ist geschlossen, mit Öffnungen an allen vier Seiten statt unter freiem Himmel, und "
  "funktioniert deshalb bei jedem Wetter. Sie ist klein, und die Kirche schließt sie, wenn es zu voll "
  "wird."),
 ("Kann man die Kirche kostenlos besichtigen?",
  "Ja. Die Hallgrímskirkja ist eine aktive Gemeindekirche; hineinzugehen und sich Kirchenschiff und Orgel "
  "anzusehen kostet während der Öffnungszeiten nichts. Bezahlt wird nur für den Turm. Gottesdienste sind "
  "für alle offen, aber währenddessen ist das Haus keine Sehenswürdigkeit."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/tile-hallgrimskirkja.webp" width="800" height="600" alt="Die Hallgrímskirkja von unten, daneben weht die isländische Flagge" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reykjavík</a> › Hallgrímskirkja</p>
    <h1>Hallgrímskirkja: Tickets, Öffnungszeiten und der richtige Moment für den Turm</h1>
    <p class="sub">Die Kirche ist kostenlos. Der Turm nicht, er lässt sich nicht vorbuchen, und im Winter endet die Auffahrt um 16:45 Uhr.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, Autor der TouringBee-Audioguides">
      <span>Von Eugene · Aktualisiert am 29. September 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#hours">Zeiten und Preise</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Touren in Reykjavík</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">Zwei Dinge überraschen Besucher an der Hallgrímskirkja. Das Turmticket lässt sich nirgends im Voraus kaufen, zu keinem Preis. Und von September bis Mai fährt die letzte Auffahrt um 16:45 Uhr — im Dezember also, bevor die meisten mit dem Mittagessen fertig sind.</p>

<p>Alles andere ist einfach. Die Kirche selbst ist frei zugänglich, sie steht oben an der Straße, die Sie ohnehin hinaufgehen wollten, und der ganze Halt dauert mit Warteschlange etwa eine halbe Stunde.</p>

<p>Diese Seite behandelt den Turm: Preis, Öffnungszeiten, Schließungen wegen Gottesdiensten und die Frage, ob der Blick sein Geld wert ist. Sie ergänzt <a href="{ONEDAY}">unseren Tagesplan für Reykjavík</a>, in dem dieser Turm der feste Punkt ist, um den sich der Rest biegt. Für die Geschichte des Baus statt der Logistik ist <a href="#audio">der TouringBee-Audiorundgang</a> da.</p>

<div class="glance">
  <h2>Auf einen Blick</h2>
  <dl>
    <dt>Eintritt Kirche</dt><dd>Frei</dd>
    <dt>Turmticket</dt><dd>1.500 ISK Erwachsene · 200 ISK Kinder 7–16 · 1.300 ISK Studierende und Menschen mit Behinderung</dd>
    <dt>Buchung</dt><dd>Nicht möglich. Verkauf im Kirchenladen, nur für denselben Tag</dd>
    <dt>Winter</dt><dd>1. Sep. – 31. Mai: Kirche 10:00–17:00, letzte Auffahrt 16:45</dd>
    <dt>Sommer</dt><dd>1. Juni – 31. Aug.: Kirche 09:00–20:00, Turm bis 19:45</dd>
    <dt>Dauer</dt><dd>Etwa 30 Minuten inklusive Warten</dd>
    <dt>Hinauf</dt><dd>Aufzug fast bis oben, dann eine kurze Treppe</dd>
    <dt>Höhe</dt><dd>73 m nach Angabe der Kirche — das höchste Gebäude der Stadt</dd>
  </dl>
</div>

<div class="minicta">
  <h2>Die Kirche ist eine Station eines längeren Rundgangs</h2>
  <p>Der TouringBee-Audiorundgang nimmt die Hallgrímskirkja und <strong>26 weitere Stationen</strong> im alten Zentrum mit — <strong>2 bis 2,5 Stunden</strong>, Karte und Audio offline, in Ihrem Tempo.</p>
  <a {BUY}>Reykjavík-Audioguide — 9,99 €</a>
</div>

<h2 id="hours">Was kostet und was nicht</h2>

<p>Die Hallgrímskirkja ist eine aktive lutherische Gemeindekirche, kein Museum, und der Eintritt ist während der Öffnungszeiten frei. Sie können sich ins Kirchenschiff setzen, die Orgel ansehen und wieder gehen, ohne etwas zu zahlen. Das Ticket gilt nur für den Turm.</p>

<table class="tbl">
  <tr><th>Turmticket</th><th>Preis</th></tr>
  <tr><td>Erwachsene</td><td>1.500 ISK</td></tr>
  <tr><td>Kinder 7–16 Jahre</td><td>200 ISK</td></tr>
  <tr><td>Studierende, Menschen mit Behinderung (mit Nachweis)</td><td>1.300 ISK</td></tr>
  <tr><td>Ab 67 Jahren</td><td>Ermäßigt; die Kirche nennt keinen Betrag</td></tr>
  <tr><td>Gruppen ab 10 Personen</td><td>10 % Nachlass</td></tr>
  <tr><td>Schulgruppen, Schüler bis 16</td><td>Frei</td></tr>
</table>

<p>Im Netz finden Sie andere Zahlen. Reykjavíks eigenes Tourismusportal führte bei unserer Prüfung im September 2026 noch 1.400 ISK und 16:30 Uhr als letzten Einlass. Viele Reiseseiten kopieren zudem eine alte Preistabelle, welche die Kirche auf ihrer eigenen Seite über der aktuellen stehen gelassen hat. Die Preise oben sind die, die sie heute verlangt.</p>

<h2>Die Zeiten und die Grenze</h2>

<table class="tbl">
  <tr><th>Saison</th><th>Kirche</th><th>Letzte Auffahrt</th></tr>
  <tr><td>1. September – 31. Mai</td><td>10:00 – 17:00</td><td>16:45</td></tr>
  <tr><td>1. Juni – 31. August</td><td>09:00 – 20:00</td><td>19:45</td></tr>
</table>

<p>Um diese 16:45 Uhr herum wird geplant, denn sie wandert nicht mit dem Tageslicht. Ende Dezember ist die Sonne ohnehin um halb vier weg, Turm und Licht enden also gemeinsam. Im Februar ist es um 16:45 Uhr noch hell, und genau deshalb verpassen Leute die Auffahrt: Der Himmel sieht nicht nach Feierabend aus.</p>

<p>Die übrigen Schließungen sind weniger planbar. Die Kirche schließt für Besucher bei Gottesdiensten, Trauungen, Beerdigungen und Konzerten, und sie sagt es offen: Die Öffnungszeiten können sich ändern. Auch die Aussichtsebene wird bei bestimmten Veranstaltungen geschlossen, und früher als angekündigt, wenn es dort voll wird. Sonntagvormittag ist der sicherste Weg, vor verschlossener Tür zu stehen.</p>

<h2>Das Ticket kaufen</h2>

<p>Der Laden liegt links, wenn Sie durch den Eingangsbereich kommen. Nur dort existiert das Turmticket. Die Formulierung der Kirche: Eine Reservierung des Turms im Voraus ist nicht möglich. Kein Onlineverkauf, keine Zeitfenster, kein Skip-the-Line.</p>

<p>Was online als Hallgrímskirkja-Ticket angeboten wird, ist etwas anderes: ein Rundgang, der davor hält, oder ein City-Pass, der es vielleicht erstattet. Das Ticket gilt einmal am Kauftag — morgens kaufen und in der Dämmerung nutzen geht nicht.</p>

<h2>Der Weg nach oben</h2>

<p>Ein Aufzug nimmt den größten Teil der Höhe, eine kurze Treppe den Rest. Die Aussichtsebene ist geschlossen, mit Bogenöffnungen an allen vier Seiten statt unter freiem Himmel. Genau deshalb funktioniert sie an einem Tag, an dem unten auf der Straße der Wind Schirme zerlegt.</p>

<p>Die Ebene ist klein. Im Juli ist die Schlange unten der langsame Teil, nicht die Auffahrt, und die Kirche lässt lieber warten, als die Plattform zu überfüllen. Eine Viertelstunde oben reicht.</p>

<figure>
  <img src="{P}img/tile-rainbow-street.webp" width="800" height="600" loading="lazy" alt="Die in Regenbogenstreifen bemalte Skólavörðustígur führt bergauf zur Hallgrímskirkja">
  <figcaption>Die Straße, die Sie hinaufgehen. Von der Plattform blicken Sie sie direkt wieder hinunter.</figcaption>
</figure>

<h2>Was Sie tatsächlich sehen</h2>

<p>Blicken Sie nach Westen, und Sie haben das Bild, für das alle kommen. Die Skólavörðustígur läuft in Regenbogenstreifen bergab, dahinter stapeln sich die bunten Blechdächer des alten Zentrums bis zum Hafen, mit der Bucht und dem Esja im Rücken. Dieser Blick rechtfertigt das Ticket. Er ist auch das Einzige, was Perlan nicht liefern kann: Perlan liegt zu weit draußen, um auf die Dächer hinabzusehen.</p>

<p>Nach Süden und Osten liegt das Wohn-Reykjavík und bei klarer Sicht die Halbinsel Reykjanes. Nach Norden Hafen und Wasser. Es gibt keine schlechte Seite, aber wenn Sie einen klaren Moment und eine Kamera haben, nehmen Sie Westen.</p>

<p>Das Licht zählt mehr als die Uhrzeit. Im Sommer wirkt die tiefe Abendsonne besser als der Mittag. Im Winter ist das Fenster ohnehin schmal, und ein bedeckter Himmel drückt die Dächer zu einem grauen Teppich zusammen — das sollte man wissen, bevor man 1.500 ISK am falschen Nachmittag ausgibt.</p>

<h2>Drinnen, ohne zu zahlen</h2>

<p>Das Kirchenschiff fasst 1.200 Menschen und ist bewusst schlicht: weiß, hoch, fast ohne Schmuck. Am Ende steht die Klais-Orgel, gebaut in Bonn und 1992 fertiggestellt — 5.275 Pfeifen, 15 Meter hoch, rund 25 Tonnen. Dazu kommt eine kleinere Frobenius-Orgel aus Dänemark, umgebaut und 2024 neu geweiht. Organisten reisen aus aller Welt an, um auf der großen aufzunehmen; läuft beim Hineingehen eine Probe, bleiben Sie.</p>

<p>Der Bau dauerte lange. Guðjón Samúelsson, der Staatsarchitekt, erhielt den Auftrag in den 1930er-Jahren und erlebte die Fertigstellung nicht. Gebaut wurde von 1945 bis zur Weihe 1986, und die Gemeinde nutzte dazwischen 26 Jahre lang die Krypta. Die Fassade wird meist als Basaltsäulen beschrieben; die Kirche selbst vergleicht sie mit Säulenfels, isländischen Bergen und Gletschern.</p>

<p>Dieser Vergleich ist die Version, die jeder Reiseführer bringt. Warum ein Staatsarchitekt seine Laufbahn damit verbrachte, einen eigens isländischen Stil zu suchen, ist die längere Geschichte — und der Audioguide nimmt sich Zeit dafür.</p>

<p>Und noch etwas, draußen. Die Statue auf dem Vorplatz stand hier, bevor die Kirche stand, und es war nicht Islands Idee, sie dorthin zu stellen.</p>

<h2>Turm oder Perlan?</h2>

<table class="tbl">
  <tr><th></th><th>Hallgrímskirkja</th><th>Perlan</th></tr>
  <tr><td>Wo</td><td>Oben im alten Zentrum, zu Fuß</td><td>Auf einem Hügel außerhalb, Bus oder Taxi</td></tr>
  <tr><td>Der Blick</td><td>Senkrecht auf die bunten Dächer und die Regenbogenstraße</td><td>Weites Panorama: Bucht, Stadt, Berge</td></tr>
  <tr><td>Plattform</td><td>Geschlossen, klein</td><td>Offene Aussichtsterrasse plus Ausstellungen</td></tr>
  <tr><td>Ticket</td><td>1.500 ISK, nur vor Ort</td><td>Mehr; aktuellen Preis prüfen, er ändert sich</td></tr>
  <tr><td>Zeitaufwand</td><td>30 Minuten</td><td>Ein halber Tag mit Hin- und Rückweg</td></tr>
</table>

<p>An einem einzigen Tag in der Stadt gewinnt der Turm schon über die Zeit. Bei zwei Tagen, von denen einer verregnet ist, ist Perlan das bessere Schlechtwetterhaus, weil es drinnen etwas zu tun gibt.</p>

<div class="ticketbox">
  <h3>Der Turm lässt sich nicht buchen — das drumherum schon</h3>
  <p>Für die Hallgrímskirkja selbst ist nichts reservierbar. Drumherum schon: Perlan, die Lagunen und die Führungen, die an der Kirche vorbeikommen, verkaufen Zeitfenster im Voraus.</p>
  <a class="btn sm" href="{TIQETS}" {OTA}>Tickets für Reykjavík</a>
  <a class="btn sm outline" href="{GYG}" {OTA}>Stadtführungen vergleichen</a>
</div>

<h2>Drei Situationen</h2>

<h3>Sie haben ein paar Stunden zwischen zwei Flügen</h3>
<p>Der Turm ist die beste Verwendung für einen kurzen Aufenthalt: zwanzig Minuten zu Fuß von der Bushaltestelle im Zentrum, und die ganze Stadt auf einmal. Gehen Sie zuerst hinauf und danach hinunter ins alte Zentrum, nicht umgekehrt.</p>

<h3>Es ist Sonntag</h3>
<p>Die Vormittagsgottesdienste schließen die Kirche für Besucher. Kommen Sie nach dem Mittagessen; im Winter bleibt dann immer noch Luft bis 16:45 Uhr.</p>

<h3>Das Wetter ist gekippt</h3>
<p>Schreiben Sie den Turm nicht ab. Die Ebene ist geschlossen, und der Wind, der unten die Straße ruiniert, stört oben nicht. Das eigentliche Problem sind tiefe Wolken: Wenn Sie den Esja vom Gehweg aus nicht sehen, sehen Sie aus 73 Metern auch nicht viel.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>Der Audioguide</h2>
    <p class="lead" style="max-width:720px">Oben auf der Plattform sehen Sie, wie Reykjavík aussieht. Warum die Stadt genau hier gewachsen ist, was die Statue draußen auf diesem Platz soll und was der Architekt wirklich gebaut hat, sind andere Fragen.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="Die TouringBee-App mit der Reykjavík-Route, hochgehalten vor der Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">TouringBee-Audioguide für Reykjavík</h3>
        <p class="meta" style="margin:0 0 10px">27 Stationen · 2–2,5 Stunden · ein Jahr Zugriff</p>
        <div class="rate">{STARS}<b>4,7</b> {RATELABEL}</div>
        <div class="price">9,99 €<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Die Hallgrímskirkja ist eine der 27 Stationen</strong> — der Weg führt vom Gründerhügel zum alten Hafen</li>
          <li><strong>Nach dem Download vollständig offline</strong> — Karte und Illustrationen inklusive</li>
          <li><strong>In Ihrem Tempo.</strong> Unterbrechen Sie für den Turm und setzen Sie dort fort, wo Sie waren</li>
          <li><strong>Eine Zahlung.</strong> Keine Gruppe, kein Zeitplan, kein Guide, der wartet</li>
        </ul>
        <a {BUY} style="width:100%">Reykjavík mit dem Audioguide gehen</a>
        <p class="meta" style="margin:12px 0 0;text-align:center">{CHECKOUTNOTE} <a href="{TBPRODUCT}" rel="noopener" data-no-widget>{OPENSHOP}</a>.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap prose">

<h2>Fünf Fehler</h2>
<ol>
  <li><strong>Online nach Tickets suchen.</strong> Es gibt keine. Der Laden in der Kirche ist der einzige Verkäufer.</li>
  <li><strong>Den Turm zwischen September und Mai auf den späten Nachmittag legen.</strong> 16:45 Uhr ist die letzte Auffahrt, egal wie hell es ist.</li>
  <li><strong>Sonntagvormittag kommen.</strong> Gottesdienste schließen die Kirche für Besucher.</li>
  <li><strong>Einem Preis aus einem Verzeichnis glauben.</strong> Mehrere zeigen weiterhin 1.400 ISK und 16:30 Uhr.</li>
  <li><strong>Bei tiefen Wolken hinauffahren.</strong> Ist der Esja von der Straße unsichtbar, heben Sie das Ticket für morgen auf.</li>
</ol>

<h2>Häufige Fragen</h2>
<div class="faq">{FAQHTML}</div>

<h2>Weiterlesen</h2>
<ul>
  <li><a href="{ONEDAY}">Reykjavík an einem Tag</a> — der Plan, in dessen Mitte dieser Turm steht</li>
  <li><a href="{KEF}">Vom Flughafen Keflavík in die Stadt</a> — wie Sie überhaupt erst ankommen</li>
  <li><a href="{HOME}">Der komplette Reykjavík-Guide</a> — der Rundgang, die Ausflüge und die Jahreszeiten</li>
  <li><a href="{GUIDES}">Alle Reykjavík-Guides</a> — was veröffentlicht ist und was noch kommt</li>
</ul>

<h2>Kurz gefasst</h2>
<p>Gehen Sie kostenlos hinein, zahlen Sie 1.500 ISK im Laden, wenn Sie den Blick wollen, und tun Sie es im Winter vor 16:45 Uhr. Nach Westen schauen wegen der Dächer. Eine halbe Stunde — und es ist die beste halbe Stunde, die das alte Zentrum verkauft.</p>
<p>Und wenn Sie lieber wissen möchten, worauf Sie da stehen, statt es nur anzusehen, nehmen Sie <a href="#audio">den TouringBee-Audioguide</a> mit: 27 Stationen durch das Zentrum, diese eingeschlossen, vollständig offline.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">Die Kirche ist Station eins von siebenundzwanzig</h2>
  <p>Diese Seite bringt Sie zur richtigen Stunde hinauf. Der Audioguide sagt Ihnen, was die Stadt unter Ihnen ist.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Rundgang starten — 9,99 €</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Hotel im Zentrum finden</a>
  </div>
</div>

<p class="disc">Einige Links auf dieser Seite sind Affiliate-Links — wenn Sie darüber buchen, erhalten wir unter Umständen eine Provision, ohne Aufpreis für Sie. Preise und Öffnungszeiten wurden im September 2026 auf hallgrimskirkja.is geprüft und ändern sich ohne Ankündigung; prüfen Sie sie vor der Reise.</p>

  </div>
</section>
"""
