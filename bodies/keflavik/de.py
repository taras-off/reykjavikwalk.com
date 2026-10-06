# -*- coding: utf-8 -*-
"""DE — auf Deutsch geschrieben. Anrede: Sie. Logistikseite, nur zwei Haken."""

HEADLINE = "Vom Flughafen Keflavík nach Reykjavík: welcher Transfer zu Ihrer Landezeit passt"
TITLE = "Keflavík nach Reykjavík: Bus, Taxi oder Mietwagen"
DESC = ("Von Keflavík nach Reykjavík: die tatsächlichen Preise für Flybus, Linienbus und Mietwagen, "
        "und was Sie mit den Stunden zwischen Landung und Check-in anfangen.")

FAQ = [
 ("Was ist die günstigste Verbindung vom Flughafen Keflavík nach Reykjavík?",
  "Der Linienbus, Strætó Linie 55, für 2.400 ISK pro Erwachsenem. Jugendliche von 12 bis 17, Reisende ab "
  "67 und Menschen mit Behinderung zahlen 1.200 ISK, Kinder unter 12 fahren frei. Er fährt täglich, aber "
  "nicht zu jedem Flug, und nicht jede Fahrt endet am BSÍ — manche enden in Fjörður in Hafnarfjörður, "
  "und das ist nicht die Innenstadt."),
 ("Wie lange dauert die Fahrt von Keflavík nach Reykjavík?",
  "Rund 45 Minuten im Reisebus für etwa 50 km, im Auto ähnlich. Die Zeit geht nicht auf der Strecke "
  "verloren. Sie geht beim Warten auf den Bus verloren, der 35 bis 45 Minuten nach der Landung fährt, und "
  "danach noch einmal, weil Ihr Zimmer erst am Nachmittag fertig ist."),
 ("Muss man den Flughafenbus vorab buchen?",
  "In der Regel nicht. Flybus verkauft Tickets am Flughafen und online, und die Abfahrten richten sich "
  "nach den ankommenden Flügen. Ein Onlineticket spart etwas Geld, erspart nach einem langen Flug die "
  "Schlange und lohnt sich an stark gebuchten Tagen. Bei Verspätung rückt Ihr Platz auf die nächste "
  "Abfahrt, statt dass der Bus wartet."),
 ("Fährt der Flybus bis zu meinem Hotel?",
  "Das Standardticket bringt Sie zum Terminal BSÍ. Flybus+ fährt gegen Aufpreis im Kleinbus weiter zu "
  "teilnehmenden Hotels. Liegt Ihre Unterkunft im alten Zentrum, ist das Standardticket plus ein kurzer "
  "Fußweg oft schneller, als auf die Kleinbusrunde zu warten."),
 ("Lohnt sich ein Mietwagen nur für den Transfer?",
  "Für sich genommen nicht. Eine Straße, 45 Minuten, und am Ende ein Auto, das Sie in einer zu Fuß "
  "begehbaren Stadt parken müssen. Ein Mietwagen ergibt Sinn, wenn der Flughafen der Anfang einer "
  "Rundreise ist: Golden Circle, Südküste, alles außerhalb der Hauptstadt. Die eigentliche Frage ist, ob "
  "Sie die Stadt verlassen."),
 ("Wo lasse ich das Gepäck bis zum Check-in?",
  "Fragen Sie zuerst im Hotel. Ein Zimmer, das noch nicht fertig ist, heißt nicht, dass das Hotel nicht "
  "helfen kann — die meisten verwahren Koffer bis zum Check-in kostenlos. Sonst gibt es Schließfächer in "
  "Keflavík und am BSÍ, die am BSÍ rund um die Uhr, mit 96 Fächern in vier Größen."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/sec-old-town.webp" width="1024" height="683" alt="Ein Fahrrad vor einem Schaufenster im alten Zentrum von Reykjavík" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reykjavík</a> › Vom Flughafen Keflavík in die Stadt</p>
    <h1>Vom Flughafen Keflavík nach Reykjavík: die Optionen, und welche zu Ihrer Landezeit passt</h1>
    <p class="sub">Fünfzig Kilometer, eine Straße, fünfundvierzig Minuten. Der Transfer ist der einfache Teil — die Lücke zwischen Landung und Check-in nicht.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, Autor der TouringBee-Audioguides">
      <span>Von Eugene · Aktualisiert am 5. Oktober 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#options">Optionen vergleichen</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Transfers und Ausflüge</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">Von Keflavík nach Reykjavík führt eine Straße, und sie dauert etwa 45 Minuten. Der Flughafenbus richtet seine Abfahrten nach den ankommenden Flügen: meist fährt er 35 bis 45 Minuten nach einer Landung, nach einem Fahrplan, der gegen 03:30 beginnt und bis in den späten Abend läuft. In die Stadt zu kommen ist ein gelöstes Problem.</p>

<p>Ungelöst ist die Stunde, zu der Sie aufsetzen. Check-in ist in Reykjavík normalerweise um 14:00 oder 15:00 Uhr. Landen Sie davor, stehen Sie mit Gepäck, verschlossenem Zimmer und mehreren Stunden in der Stadt — und genau das, nicht die 50 km, entscheidet, welches Ticket Sie kaufen sollten.</p>

<p>Diese Seite macht deshalb beide Hälften: die Transferoptionen zu den Preisen, die die Anbieter tatsächlich verlangen, und dann, was Sie mit der Lücke machen. Setzt sie Sie mit Zeit im Zentrum ab, sind <a href="{ONEDAY}">unser Tagesplan</a> und <a href="#audio">der TouringBee-Audiorundgang</a> genau für diese Stunden gebaut. Sie planen die ganze Reise? Starten Sie beim <a href="{HOME}">kompletten Reykjavík-Guide</a>.</p>

<div class="glance">
  <h2>Auf einen Blick</h2>
  <dl>
    <dt>Entfernung</dt><dd>Rund 50 km vom Flughafen ins Zentrum von Reykjavík</dd>
    <dt>Fahrt</dt><dd>Etwa 45 Minuten mit Bus oder Auto</dd>
    <dt>Flybus</dt><dd>Ab 3.999 ISK einfache Fahrt zum Terminal BSÍ</dd>
    <dt>Linienbus</dt><dd>Strætó 55 — 2.400 ISK Erwachsene, 1.200 ISK ermäßigt, unter 12 frei</dd>
    <dt>Abfahrten</dt><dd>Flybus richtet sich nach Ankünften, etwa 03:30 bis später Abend; Strætó fährt nach festem Fahrplan</dd>
    <dt>Buchung</dt><dd>Meist nicht nötig. Tickets gibt es am Flughafen</dd>
    <dt>Gepäck</dt><dd>Zuerst im Hotel fragen; Schließfächer am Flughafen und am BSÍ</dd>
    <dt>Die eigentliche Grenze</dt><dd>Check-in um 14:00–15:00, nicht der Transfer</dd>
  </dl>
</div>

<div class="minicta">
  <h2>Früh gelandet? Das ist das Zeitfenster für den Rundgang</h2>
  <p>Der TouringBee-Audiorundgang sind <strong>27 Stationen, 2 bis 2,5 Stunden</strong> durch das alte Zentrum, Karte und Audio offline. Gepäck verstaut, und die toten Stunden vor dem Check-in werden zum besten Teil von Tag eins.</p>
  <a {BUY}>Reykjavík-Audioguide — 9,99 €</a>
</div>

<h2 id="options">Fangen Sie bei Ihrer Landezeit an, nicht beim Preis</h2>

<p>Jeder Ratgeber zu dieser Strecke vergleicht Tarife. Der Preis ist aber nur die halbe Rechnung: Ein günstiges Ticket ist in dem Moment kein gutes Geschäft mehr, in dem sein Fahrplan Ihnen eine Stunde Wartezeit hinzufügt.</p>

<p>Fragen Sie stattdessen: Wann setzen die Räder auf, und wo schlafen Sie? Landung mittags, Zimmer ab zwei — dann passt alles. Landung um sechs Uhr morgens, und Sie brauchen einen Plan für das Gepäck und für sich selbst. Der günstigste Bus bedient nicht jeden Flug und kann Sie deshalb eine Stunde kosten, die Sie lieber anders verbracht hätten.</p>

<table class="tbl">
  <tr><th>Option</th><th>Preis</th><th>Fährt bis</th><th>Passt, wenn</th></tr>
  <tr><td><strong>Flybus</strong></td><td>ab 3.999 ISK einfach</td><td>Terminal BSÍ</td><td>Standard. Abfahrten nach Ankünften; bei Verspätung rückt Ihr Platz auf den nächsten Bus</td></tr>
  <tr><td><strong>Flybus+</strong></td><td>Aufpreis</td><td>Teilnehmende Hotels</td><td>Viel Gepäck, Kinder, schlechtes Wetter, Unterkunft außerhalb</td></tr>
  <tr><td><strong>Airport Direct</strong></td><td>Preis beim Anbieter prüfen</td><td>Zentrales Terminal, Premium bis zum Hotel</td><td>Der zweite Linienbus — lohnt den Preisvergleich mit Flybus</td></tr>
  <tr><td><strong>Strætó 55</strong></td><td>2.400 ISK Erwachsene</td><td>BSÍ oder Fjörður</td><td>Tagsüber, leichtes Gepäck, wenn der Fahrplan passt</td></tr>
  <tr><td><strong>Taxi oder Privattransfer</strong></td><td>Nach Taxameter oder Angebot</td><td>Ihre Tür</td><td>Sie sind zu dritt oder viert, oder die Uhrzeit ist ungünstig</td></tr>
  <tr><td><strong>Mietwagen</strong></td><td>Tagessatz</td><td>Wohin Sie wollen</td><td>Nur wenn Sie später die Stadt verlassen</td></tr>
</table>

<h2>Der Flybus, und warum er der Standard ist</h2>

<p>Es ist der Flughafenbus, den die meisten nehmen, und er verkauft nicht Tempo, sondern Sicherheit. Die Abfahrten richten sich nach ankommenden Flügen statt nach einem festen Takt: meist 35 bis 45 Minuten nach einer Landung. Der veröffentlichte Fahrplan beginnt gegen 03:30 und läuft bis in den späten Abend — prüfen Sie deshalb bei einem sehr frühen oder sehr späten Flug den Plan für Ihr eigenes Datum, statt sich auf die Faustregel zu verlassen.</p>

<p>Ist Ihr Flug verspätet, hält der Anbieter den Bus nicht für Sie an, sondern garantiert Ihnen ohne Aufpreis einen Platz auf der nächsten Abfahrt. Das ist ein bedeutsamer Unterschied, und man sollte ihn kennen, bevor man in der Schlange an der Passkontrolle nervös wird. Im Tarif enthalten sind zwei Gepäckstücke bis je 23 kg.</p>

<p>Das Standardticket endet am BSÍ, dem Busbahnhof am südlichen Rand des Zentrums. Flybus+ ergänzt gegen Aufpreis eine Kleinbusfahrt zu teilnehmenden Hotels. Sie lohnt sich bei schwerem Gepäck, mit Kindern, bei schlechtem Wetter und wenn Ihre Unterkunft am Stadtrand liegt.</p>

<p>Reisen Sie leicht und wohnen im alten Zentrum, lohnt der Vergleich: Der Kleinbus arbeitet eine Adressliste ab, und Ihre muss nicht die erste sein. Sehen Sie nach, wie weit Ihr Hotel vom BSÍ entfernt ist, und entscheiden Sie danach statt automatisch.</p>

<h2>Strætó 55, die günstige Variante und ihr Haken</h2>

<p>Der Linienbus ist die 55 und kostet 2.400 ISK für Erwachsene — 1.200 ISK für 12- bis 17-Jährige, ab 67 und Menschen mit Behinderung, frei unter 12. Für eine Familie ist dieser Unterschied echtes Geld.</p>

<p>Zwei Haken. Er fährt nach Fahrplan und nicht nach Ihrem Flug, eine Landung um 05:30 kann also langes Warten bedeuten. Und nicht jede Fahrt endet am BSÍ: Manche enden in Fjörður in Hafnarfjörður, einer Stadt südlich von Reykjavík, die ausdrücklich nicht das Zentrum ist. Prüfen Sie das Fahrtziel vor dem Einsteigen, nicht danach.</p>

<div class="ticketbox">
  <h3>Privattransfers und Touren</h3>
  <p>Zu dritt oder viert rechnen Sie den Buspreis pro Kopf gegen ein Fahrzeug, bevor Sie den Bus für günstiger halten. Privattransfers und Touren ab Keflavík werden im Voraus verkauft.</p>
  <a class="btn sm" href="{GYG}" {OTA}>Transfers vergleichen</a>
  <a class="btn sm outline" href="{TIQETS}" {OTA}>Tickets in Reykjavík</a>
</div>

<h2>Taxi, und wann sich der Abstand schließt</h2>

<p>Isländische Taxis fahren nach Taxameter, einen veröffentlichten Flughafenpauschalpreis gibt es nicht. Behandeln Sie das Taxi als die teure Option und lassen Sie sich vorher schätzen.</p>

<p>Zu dritt oder viert holen Sie eine aktuelle Schätzung ein und vergleichen sie mit der Summe Ihrer Bustickets. Ein Taxi rechnet pro Fahrzeug, ein Bus pro Person, der Abstand schließt sich also mit der Gruppengröße. Günstig wird das Taxi dadurch nicht, nur näher, als es für eine einzelne Person aussieht.</p>

<h2>Mietwagen, ehrlich gesagt</h2>

<p>Für den Transfer allein nein. Es ist eine gerade Straße, die Sie einmal fahren, und am Ende ein Auto, das Sie in einer zu Fuß begehbaren Stadt parken müssen. Ein Mietwagen ergibt Sinn, wenn der Flughafen der Anfang einer Rundreise ist: Golden Circle, Südküste, alles außerhalb der Hauptstadt. Entscheiden Sie nach der Reise, nicht nach dem Transfer.</p>

<figure>
  <img src="{P}img/sec-winter-street.webp" width="1024" height="683" loading="lazy" alt="Ein bunt gestrichener Eckladen in einer verschneiten Straße im Zentrum von Reykjavík">
  <figcaption>Das BSÍ liegt direkt südlich davon. Das meiste vom alten Zentrum ist ein kurzer Weg vom Terminal.</figcaption>
</figure>

<h2>Die Lücke zwischen Landung und Check-in</h2>

<p>Das ist der Teil, den niemand plant und in den alle laufen. Ihr Zimmer ist erst um zwei Uhr nachmittags fertig. Ihr Flug ist um sechs gelandet. Um acht stehen Sie mit dem Koffer im Zentrum.</p>

<p>Das Gepäck ist die leichte Hälfte, und der erste Schritt ist der, den man vergisst: Fragen Sie im Hotel. Ein Zimmer, das nicht fertig ist, ist nicht dasselbe wie ein Hotel, das nicht helfen kann — die meisten verwahren Koffer bis zum Check-in kostenlos. Außerdem liegt Ihr Gepäck dann dort, wo Sie schlafen, und das schlägt jedes Schließfach.</p>

<p>Lautet die Antwort nein, oder haben Sie eine Wohnung ohne Rezeption gebucht, gibt es Schließfächer in Keflavík und am BSÍ. Die am BSÍ laufen rund um die Uhr, mit 96 Fächern in vier Größen — mehr, als die meisten Bahnhöfe dieser Größe bieten.</p>

<p>Die Stunden sind die bessere Hälfte, denn das alte Zentrum ist etwa zwanzig Minuten breit und braucht kein Hotelzimmer, um zu gefallen. Eine Lücke von vier bis fünf Stunden fasst den 2 bis 2,5 Stunden langen Rundgang, um den herum diese Seite gebaut ist, und lässt noch Platz für Frühstück und einen langen Kaffee. Die Cafés öffnen deutlich vor den Rezeptionen.</p>

<h2>Drei Zeitpunkte</h2>

<h3>Wenn Sie früh landen</h3>
<p>Der Flybus, weil seine Abfahrten den Ankünften folgen. Gepäck geregelt, Frühstück im Zentrum, und losgehen, sobald es hell wird — um die Wintersonnenwende herum ist das erst gegen elf Uhr vormittags, planen Sie also vorher eine warme Stunde drinnen ein.</p>

<h3>Wenn Sie spät landen</h3>
<p>Wieder der Flybus: Sein Fahrplan reicht bis in den späten Abend, und die letzten Abfahrten sind auf späte Ankünfte abgestimmt, was beim Linienbus nicht der Fall ist. Prüfen Sie aber die letzte Abfahrt für Ihr Datum. Landen Sie, nachdem die Busse eingestellt haben, ist ein Taxi kein Luxus, sondern das Einzige, was bleibt.</p>

<h3>Wenn Sie früh abfliegen</h3>
<p>Rechnen Sie vom Check-in-Schalter zurück, nicht vom Gate, und addieren Sie die 45 Minuten plus das, was die Abholung am Hotel kostet. Frühe Abflüge bedeuten Busse, die mitten in der Nacht aus der Stadt fahren: Der Flybus-Fahrplan deckt das ab, der Linienbus nicht.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>Der Audioguide</h2>
    <p class="lead" style="max-width:720px">Sie haben Stunden im Zentrum, bevor Ihnen jemand einen Schlüssel gibt. Sie zu erlaufen ist naheliegend. Zu wissen, warum die Stadt überhaupt hier steht und warum der Rundgang auf genau diesem Hügel beginnt, müssen Sie mitbringen.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="Die TouringBee-App mit der Reykjavík-Route, vor der Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">TouringBee-Audioguide für Reykjavík</h3>
        <p class="meta" style="margin:0 0 10px">27 Stationen · 2–2,5 Stunden · eine Zahlung, ein Jahr Zugriff</p>
        <div class="price">9,99 €<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Passt genau in die toten Stunden.</strong> Zwei bis zweieinhalb, ungefähr so viel haben Sie vor dem Check-in</li>
          <li><strong>Nach dem Download vollständig offline</strong> — praktisch, bevor Sie Daten im neuen Land geklärt haben</li>
          <li><strong>In Ihrem Tempo.</strong> Fürs Frühstück unterbrechen und dort fortsetzen, wo Sie waren</li>
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

<h2>Preise: Transfer, Gepäck und Rundgang</h2>
<table class="tbl">
  <tr><th>Posten</th><th>Kosten</th></tr>
  <tr><td>Strætó 55, Erwachsene</td><td>2.400 ISK</td></tr>
  <tr><td>Strætó 55, 12–17, ab 67, Menschen mit Behinderung</td><td>1.200 ISK</td></tr>
  <tr><td>Strætó 55, unter 12</td><td>Frei</td></tr>
  <tr><td>Flybus zum BSÍ, einfache Fahrt</td><td>ab 3.999 ISK</td></tr>
  <tr><td>Airport Direct</td><td>Preis beim Anbieter prüfen</td></tr>
  <tr><td>Flybus+ mit Hotelzustellung</td><td>Aufpreis; beim Anbieter prüfen</td></tr>
  <tr><td>Taxi</td><td>Nach Taxameter, kein veröffentlichter Flughafenpauschalpreis</td></tr>
  <tr><td>Gepäckschließfach</td><td>Am Flughafen und am BSÍ, rund um die Uhr</td></tr>
  <tr><td>Audioguide für die Lücke</td><td>9,99 €, eine Zahlung, ein Jahr Zugriff</td></tr>
</table>

<h2>Fünf Fehler</h2>
<ol>
  <li><strong>Allein nach dem Preis wählen.</strong> Prüfen Sie zuerst Landezeit und Fahrplan: Die günstige Option kann langes Warten bedeuten.</li>
  <li><strong>Annehmen, der Linienbus bediene Ihren Flug.</strong> Er fährt nach Fahrplan, der Flybus nach Ankünften.</li>
  <li><strong>In eine 55 steigen, ohne das Ziel zu prüfen.</strong> Manche Fahrten enden in Fjörður, nicht am BSÍ.</li>
  <li><strong>Flybus+ automatisch dazubuchen.</strong> Liegt Ihr Hotel nahe am BSÍ und ist das Gepäck leicht, vergleichen Sie erst Fußweg und Kleinbusrunde.</li>
  <li><strong>Einen Mietwagen für den Transfer nehmen.</strong> Mieten Sie ihn am Tag der Abfahrt aufs Land, nicht am Ankunftstag.</li>
</ol>

<h2>Häufige Fragen</h2>
<div class="faq">{FAQHTML}</div>

<h2>Weiterlesen</h2>
<ul>
  <li><a href="{ONEDAY}">Reykjavík an einem Tag</a> — was Sie mit den eben gewonnenen Stunden anfangen</li>
  <li><a href="{TOWER}">Hallgrímskirkja und der Turm</a> — Tickets, Öffnungszeiten und die Grenze 16:45 Uhr</li>
  <li><a href="{HOME}">Der komplette Reykjavík-Guide</a> — der Rundgang, die Ausflüge und die Jahreszeiten</li>
  <li><a href="{GUIDES}">Alle Reykjavík-Guides</a></li>
</ul>

<h2>Kurz gefasst</h2>
<p>Nehmen Sie den Flybus, wenn nichts dagegen spricht: Seine Abfahrten folgen den Flügen, bei Verspätung rückt Ihr Platz nach, und er setzt Sie für 3.999 ISK am Rand des Zentrums ab. Nehmen Sie die 55, wenn der Fahrplan passt und Sie jede Krone zählen. Nehmen Sie ein Auto nur, wenn Sie die Stadt verlassen.</p>
<p>Dann das Gepäck unterbringen und die Stunden nutzen. Wenn Sie die Stadt lieber verstehen als in ihr warten wollen, nehmen Sie <a href="#audio">den TouringBee-Audioguide</a> mit: 27 Stationen, 2–2,5 Stunden, vollständig offline.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">Ihr Zimmer ist erst um zwei fertig</h2>
  <p>Der Rundgang dauert zweieinhalb Stunden. Die Rechnung macht sich von selbst.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Rundgang starten — 9,99 €</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Hotel im Zentrum finden</a>
  </div>
</div>

<p class="disc">Einige Links auf dieser Seite sind Affiliate-Links — wenn Sie darüber buchen, erhalten wir unter Umständen eine Provision, ohne Aufpreis für Sie. Preise und Zeiten wurden im Oktober 2026 auf den Seiten der Anbieter geprüft und ändern sich ohne Ankündigung; prüfen Sie sie vor der Reise. Flybus: flybus.is. Linienbus: straeto.is.</p>

  </div>
</section>
"""
