# -*- coding: utf-8 -*-
"""PL — forma: ty, czas teraźniejszy i tryb rozkazujący, bez rodzajowych form przeszłych."""

HEADLINE = "Z lotniska Keflavík do Reykjaviku: który transfer pasuje do twojej godziny lądowania"
TITLE = "Keflavík – Reykjavik: autobus, taksówka czy auto"
DESC = ("Z Keflavíku do Reykjaviku: realne ceny Flybusa, autobusu miejskiego i auta oraz co zrobić z "
        "godzinami między lądowaniem a zameldowaniem w hotelu.")

FAQ = [
 ("Jak najtaniej dojechać z lotniska Keflavík do Reykjaviku?",
  "Autobusem miejskim, linią Strætó 55, za 2400 ISK od osoby dorosłej. Młodzież 12–17 lat, osoby powyżej "
  "67 roku życia i pasażerowie z niepełnosprawnością płacą 1200 ISK, dzieci do 12 lat jadą za darmo. "
  "Kursuje codziennie, ale nie do każdego przylotu, i nie każdy kurs kończy się na BSÍ — część dojeżdża "
  "do Fjörður w Hafnarfjörður, a to nie jest centrum miasta."),
 ("Ile trwa dojazd z Keflavíku do Reykjaviku?",
  "Około 45 minut autokarem na jakieś 50 km, mniej więcej tyle samo autem. Czas nie ucieka na trasie. "
  "Ucieka na czekaniu na autobus, który rusza 35–45 minut po lądowaniu, a potem na drugim czekaniu, bo "
  "pokój będzie gotowy dopiero po południu."),
 ("Czy trzeba rezerwować autobus z wyprzedzeniem?",
  "Zwykle nie. Flybus sprzedaje bilety na lotnisku i online, a odjazdy są dopasowane do przylatujących "
  "samolotów. Bilet online trochę oszczędza, pozwala ominąć kolejkę po długim locie i przydaje się w "
  "oblegane terminy. Przy opóźnieniu lotu przewoźnik przenosi twoje miejsce na kolejny odjazd, zamiast "
  "wstrzymywać autobus."),
 ("Czy Flybus dowozi pod hotel?",
  "Zwykły bilet dowozi na dworzec BSÍ. Flybus+ jedzie dalej minibusem do hoteli z listy, za dopłatą. "
  "Jeśli nocujesz w starym centrum, zwykły bilet plus krótki spacer bywa szybszy niż czekanie na objazd "
  "minibusa."),
 ("Czy opłaca się wynająć auto tylko na transfer?",
  "Samo w sobie nie. Jedna droga, 45 minut, a na końcu auto, które trzeba zaparkować w mieście "
  "przechodzonym pieszo. Wynajem zaczyna mieć sens, gdy lotnisko jest początkiem trasy: Złoty Krąg, "
  "południowe wybrzeże, cokolwiek poza stolicą. Prawdziwe pytanie brzmi, czy wyjeżdżasz z miasta."),
 ("Gdzie zostawić bagaż przed zameldowaniem?",
  "Zacznij od pytania w hotelu: pokój, który nie jest gotowy, to co innego niż hotel, który nie może "
  "pomóc — większość przechowa walizki do zameldowania bez opłat. Jeśli nie, schowki są na lotnisku i na "
  "BSÍ, te na BSÍ czynne całą dobę, 96 skrytek w czterech rozmiarach."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/sec-old-town.webp" width="1024" height="683" alt="Rower oparty przy witrynie sklepowej w starym centrum Reykjaviku" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reykjavik</a> › Z lotniska Keflavík do centrum</p>
    <h1>Z lotniska Keflavík do Reykjaviku: opcje i ta, która pasuje do twojej godziny lądowania</h1>
    <p class="sub">Pięćdziesiąt kilometrów, jedna droga, czterdzieści pięć minut. Transfer to łatwa część — luka między lądowaniem a zameldowaniem już nie.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, autor audioprzewodników TouringBee">
      <span>Eugene · Aktualizacja 5 października 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#options">Porównaj opcje</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Transfery i wycieczki</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">Z Keflavíku do Reykjaviku prowadzi jedna droga i zajmuje około 45 minut. Autokar lotniskowy ustawia odjazdy pod przylatujące samoloty: zwykle rusza 35–45 minut po lądowaniu, według rozkładu, który zaczyna się około 03:30 i trwa do późnego wieczora. Dojazd do miasta to problem rozwiązany.</p>

<p>Nierozwiązana zostaje godzina, o której siadasz. Zameldowanie w hotelach Reykjaviku jest zwykle o 14:00 albo 15:00. Jeśli lądujesz wcześniej, jesteś w mieście z bagażem, zamkniętym pokojem i kilkoma godzinami do zagospodarowania — i to, a nie 50 kilometrów, decyduje, jaki bilet kupić.</p>

<p>Dlatego ta strona robi obie połowy: opcje transferu z cenami, które przewoźnicy naprawdę biorą, i potem co zrobić z luką. Jeśli luka zostawia cię w centrum z wolnym czasem, <a href="{ONEDAY}">nasza trasa na jeden dzień</a> i <a href="#audio">spacer z audio TouringBee</a> są zrobione dokładnie pod te godziny. Układasz cały wyjazd? Zacznij od <a href="{HOME}">pełnego przewodnika po Reykjaviku</a>.</p>

<div class="glance">
  <h2>W skrócie</h2>
  <dl>
    <dt>Odległość</dt><dd>Około 50 km z lotniska do centrum Reykjaviku</dd>
    <dt>Przejazd</dt><dd>Około 45 minut autokarem albo autem</dd>
    <dt>Flybus</dt><dd>Od 3999 ISK w jedną stronę do dworca BSÍ</dd>
    <dt>Autobus miejski</dt><dd>Strætó 55 — 2400 ISK dorosły, 1200 ISK ulgowy, do 12 lat za darmo</dd>
    <dt>Odjazdy</dt><dd>Flybus dopasowuje się do przylotów, mniej więcej od 03:30 do późnego wieczora; Strætó jeździ według stałego rozkładu</dd>
    <dt>Rezerwacja</dt><dd>Zwykle niepotrzebna. Bilety są na lotnisku</dd>
    <dt>Bagaż</dt><dd>Najpierw zapytaj w hotelu; schowki są na lotnisku i na BSÍ</dd>
    <dt>Prawdziwe ograniczenie</dt><dd>Zameldowanie o 14:00–15:00, a nie transfer</dd>
  </dl>
</div>

<div class="minicta">
  <h2>Lądujesz wcześnie? To właśnie okno na spacer</h2>
  <p>Spacer z audio TouringBee to <strong>27 przystanków i 2–2,5 godziny</strong> po starym centrum, z mapą i audio offline. Bagaż załatwiony, a martwe godziny przed zameldowaniem zamieniają się w najlepszą część pierwszego dnia.</p>
  <a {BUY}>Audioprzewodnik po Reykjaviku — 9,99 €</a>
</div>

<h2 id="options">Zacznij od godziny lądowania, a nie od ceny</h2>

<p>Każdy poradnik o tej trasie porównuje taryfy. Ale cena to tylko połowa rachunku: tani bilet przestaje być opłacalny w chwili, w której jego rozkład dokłada ci godzinę czekania.</p>

<p>Zapytaj inaczej: o której koła dotykają pasa i gdzie nocujesz? Lądujesz w południe, pokój gotowy o drugiej — pasuje cokolwiek. Lądujesz o szóstej rano i potrzebujesz planu na bagaż i planu na siebie. Najtańszy autobus nie obsługuje każdego lotu, więc może cię kosztować godzinę, którą wolałbyś spędzić gdzie indziej.</p>

<table class="tbl">
  <tr><th>Opcja</th><th>Cena</th><th>Dowozi do</th><th>Kiedy to twój wybór</th></tr>
  <tr><td><strong>Flybus</strong></td><td>od 3999 ISK w jedną stronę</td><td>Dworzec BSÍ</td><td>Domyślnie. Odjazdy pod przyloty; przy opóźnieniu miejsce przechodzi na następny autobus</td></tr>
  <tr><td><strong>Flybus+</strong></td><td>dopłata</td><td>Hotele z listy</td><td>Dużo bagażu, dzieci, zła pogoda albo nocleg poza centrum</td></tr>
  <tr><td><strong>Airport Direct</strong></td><td>taryfa do sprawdzenia</td><td>Terminal w centrum, premium pod hotel</td><td>Drugi regularny autokar — warto porównać cenę z Flybusem</td></tr>
  <tr><td><strong>Strætó 55</strong></td><td>2400 ISK dorosły</td><td>BSÍ albo Fjörður</td><td>Za dnia, z lekkim bagażem, jeśli rozkład się zgadza</td></tr>
  <tr><td><strong>Taksówka lub transfer</strong></td><td>Według taksometru lub wyceny</td><td>Pod drzwi</td><td>Jest was troje albo czworo, albo godzina jest niewygodna</td></tr>
  <tr><td><strong>Auto z wypożyczalni</strong></td><td>Stawka dobowa</td><td>Gdzie chcesz</td><td>Tylko jeśli potem wyjeżdżasz z miasta</td></tr>
</table>

<h2>Flybus i dlaczego jest opcją domyślną</h2>

<p>To ten autokar lotniskowy, którym jedzie większość, a sprzedaje nie szybkość, tylko pewność. Odjazdy są dopasowane do przylatujących samolotów, a nie do stałego taktu: zwykle 35–45 minut po lądowaniu. Opublikowany rozkład zaczyna się około 03:30 i sięga późnego wieczora, więc przy bardzo wczesnym albo bardzo późnym locie sprawdź rozkład na swoją datę, zamiast ufać ogólnej zasadzie.</p>

<p>Jeśli lot się opóźni, przewoźnik nie wstrzymuje dla ciebie autobusu — gwarantuje miejsce na następnym odjeździe, bez dopłaty. To istotna różnica i lepiej ją znać, zanim zaczniesz się denerwować w kolejce do kontroli paszportowej. W cenie są dwie sztuki bagażu po 23 kg.</p>

<p>Zwykły bilet kończy się na BSÍ, dworcu przy południowym skraju centrum. Flybus+ dokłada za dopłatą przejazd minibusem pod hotele z listy. Opłaca się przy ciężkim bagażu, z dziećmi, przy złej pogodzie i wtedy, gdy nocleg jest na obrzeżach.</p>

<p>Jeśli jedziesz lekko i mieszkasz w starym centrum, warto porównać: minibus objeżdża listę adresów, a twój nie musi być pierwszy. Sprawdź, jak daleko twój hotel jest od BSÍ, i zdecyduj po tym, a nie z automatu.</p>

<h2>Strætó 55, tania opcja i jej haczyk</h2>

<p>Autobus miejski to linia 55 i kosztuje 2400 ISK od osoby dorosłej — 1200 ISK dla osób w wieku 12–17 lat, powyżej 67 roku życia i z niepełnosprawnością, za darmo do 12 lat. Dla rodziny ta różnica to realne pieniądze.</p>

<p>Dwa haczyki. Jeździ według rozkładu, a nie pod twój lot, więc lądowanie o 05:30 może oznaczać długie czekanie. I nie każdy kurs kończy się na BSÍ: część dojeżdża do Fjörður w Hafnarfjörður, gminie na południe od Reykjaviku, która zdecydowanie nie jest centrum. Sprawdź kierunek przed wejściem, a nie po.</p>

<div class="ticketbox">
  <h3>Transfery prywatne i wycieczki</h3>
  <p>Jeśli jest was troje albo czworo, policz cenę autobusu na osobę wobec jednego pojazdu, zanim uznasz, że autokar wychodzi taniej. Transfery prywatne i wycieczki z odbiorem w Keflavíku sprzedaje się z wyprzedzeniem.</p>
  <a class="btn sm" href="{GYG}" {OTA}>Porównaj transfery</a>
  <a class="btn sm outline" href="{TIQETS}" {OTA}>Bilety w Reykjaviku</a>
</div>

<h2>Taksówka i moment, w którym różnica się zmniejsza</h2>

<p>Islandzkie taksówki jeżdżą na taksometr i nie ma opublikowanej stawki ryczałtowej z lotniska, więc traktuj taksówkę jako opcję drogą i poproś o szacunek przed wsiadaniem.</p>

<p>Przy trzech czy czterech osobach weź aktualny szacunek i porównaj go z sumą biletów autobusowych. Taksówka liczy się za pojazd, autobus za pasażera, więc wraz z wielkością grupy różnica się zmniejsza. To nie czyni taksówki tanią, tylko bliższą, niż wygląda dla jednej osoby.</p>

<h2>Wynajem auta, uczciwie</h2>

<p>Na sam transfer nie. To jedna prosta droga, którą przejedziesz raz, a na końcu auto do zaparkowania w mieście przechodzonym pieszo. Wynajem zaczyna mieć sens, gdy lotnisko jest początkiem trasy: Złoty Krąg, południowe wybrzeże, cokolwiek poza stolicą. Decyduj po wyjeździe, nie po transferze.</p>

<figure>
  <img src="{P}img/sec-winter-street.webp" width="1024" height="683" loading="lazy" alt="Jaskrawo pomalowany narożny sklep przy zaśnieżonej ulicy w centrum Reykjaviku">
  <figcaption>BSÍ leży tuż na południe od tego wszystkiego. Większość starego centrum to krótki spacer od dworca.</figcaption>
</figure>

<h2>Luka między lądowaniem a zameldowaniem</h2>

<p>To ta część, której nikt nie planuje i na którą wpadają wszyscy. Pokój będzie gotowy dopiero o drugiej po południu. Samolot wylądował o szóstej rano. O ósmej jesteś w centrum z walizką.</p>

<p>Bagaż to łatwiejsza połowa, a pierwszy ruch jest tym, o którym się zapomina: zapytaj w hotelu. Pokój, który nie jest gotowy, to nie to samo co hotel, który nie może pomóc — większość przechowa walizki do zameldowania bez opłat. Przy okazji walizka ląduje tam, gdzie będziesz spać, a to lepsze niż każda skrytka.</p>

<p>Jeśli odpowiedź brzmi „nie” albo masz apartament bez recepcji, schowki są na lotnisku i na BSÍ. Te na BSÍ działają całą dobę, 96 skrytek w czterech rozmiarach, czyli więcej, niż oferuje większość dworców tej wielkości.</p>

<p>Godziny to lepsza połowa, bo stare centrum przechodzi się w jakieś dwadzieścia minut i nie potrzebuje pokoju hotelowego, żeby się podobać. Luka czterech czy pięciu godzin mieści spacer na 2–2,5 godziny, wokół którego zbudowana jest cała ta strona, i zostawia jeszcze miejsce na śniadanie i długą kawę. Kawiarnie otwierają się dużo wcześniej niż recepcje.</p>

<h2>Trzy warianty godzinowe</h2>

<h3>Jeśli lądujesz wcześnie</h3>
<p>Flybus, bo jego odjazdy idą za przylotami. Bagaż załatwiony, śniadanie w centrum i ruszasz, gdy się rozwidni — w okolicach przesilenia zimowego dzieje się to dopiero koło jedenastej, więc zaplanuj najpierw ciepłą godzinę pod dachem.</p>

<h3>Jeśli lądujesz późno</h3>
<p>Znowu Flybus: jego rozkład sięga późnego wieczora, a ostatnie odjazdy są zgrane z późnymi przylotami, czego autobus miejski nie robi. Sprawdź jednak ostatni kurs na swoją datę. Jeśli siadasz po tym, jak autokary skończyły, taksówka nie jest zbytkiem, tylko jedynym, co zostało.</p>

<h3>Jeśli wylatujesz wcześnie</h3>
<p>Licz wstecz od stanowiska odprawy, a nie od bramki, i dolicz 45 minut plus to, co zabierze odbiór z hotelu. Wczesne wyloty oznaczają autokary wyjeżdżające z miasta w środku nocy: rozkład Flybusa to pokrywa, autobus miejski nie.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>Audioprzewodnik</h2>
    <p class="lead" style="max-width:720px">Będziesz mieć w centrum kilka godzin, zanim ktokolwiek wyda ci klucz. Przejść je to rzecz oczywista. Wiedzieć, dlaczego miasto w ogóle tu stoi i dlaczego spacer zaczyna się akurat na tym wzgórzu — to musisz przynieść ze sobą.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="Aplikacja TouringBee z trasą po Reykjaviku, na tle Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">Audioprzewodnik TouringBee po Reykjaviku</h3>
        <p class="meta" style="margin:0 0 10px">27 przystanków · 2–2,5 godziny · jedna płatność, rok dostępu</p>
        <div class="price">9,99 €<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Trafia w martwe godziny.</strong> Dwie do dwóch i pół, mniej więcej tyle masz przed zameldowaniem</li>
          <li><strong>Po pobraniu działa w pełni offline</strong> — przydatne, zanim ogarniesz internet w nowym kraju</li>
          <li><strong>We własnym tempie.</strong> Przerwij na śniadanie i wróć tam, gdzie skończysz</li>
          <li><strong>Jedna płatność.</strong> Bez grupy, bez rozkładu i bez przewodnika, który czeka</li>
        </ul>
        <a {BUY} style="width:100%">Przejdź Reykjavik z audioprzewodnikiem</a>
        <p class="meta" style="margin:12px 0 0;text-align:center">{CHECKOUTNOTE} <a href="{TBPRODUCT}" rel="noopener" data-no-widget>{OPENSHOP}</a>.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap prose">

<h2>Ceny: transfer, bagaż i spacer</h2>
<table class="tbl">
  <tr><th>Pozycja</th><th>Koszt</th></tr>
  <tr><td>Strætó 55, dorosły</td><td>2400 ISK</td></tr>
  <tr><td>Strætó 55, 12–17 lat, 67+, niepełnosprawność</td><td>1200 ISK</td></tr>
  <tr><td>Strætó 55, do 12 lat</td><td>Za darmo</td></tr>
  <tr><td>Flybus do BSÍ, w jedną stronę</td><td>od 3999 ISK</td></tr>
  <tr><td>Airport Direct</td><td>Sprawdź taryfę u przewoźnika</td></tr>
  <tr><td>Flybus+ z dowozem pod hotel</td><td>Dopłata; sprawdź u przewoźnika</td></tr>
  <tr><td>Taksówka</td><td>Taksometr, brak opublikowanej stawki lotniskowej</td></tr>
  <tr><td>Schowek na bagaż</td><td>Na lotnisku i na BSÍ, całą dobę</td></tr>
  <tr><td>Audioprzewodnik na czas luki</td><td>9,99 €, jedna płatność, rok dostępu</td></tr>
</table>

<h2>Pięć błędów</h2>
<ol>
  <li><strong>Wybór tylko po cenie.</strong> Najpierw sprawdź godzinę lądowania i rozkład: tania opcja potrafi dołożyć długie czekanie.</li>
  <li><strong>Założenie, że autobus miejski obsługuje twój lot.</strong> On jeździ według rozkładu, Flybus pod przyloty.</li>
  <li><strong>Wejście do 55 bez sprawdzenia kierunku.</strong> Część kursów kończy się w Fjörður, a nie na BSÍ.</li>
  <li><strong>Dopłacanie do Flybus+ z automatu.</strong> Jeśli hotel jest blisko BSÍ, a bagaż lekki, porównaj najpierw spacer z objazdem minibusa.</li>
  <li><strong>Wynajem auta na transfer.</strong> Bierz je w dniu wyjazdu poza miasto, a nie w dniu lądowania.</li>
</ol>

<h2>Częste pytania</h2>
<div class="faq">{FAQHTML}</div>

<h2>Czytaj dalej</h2>
<ul>
  <li><a href="{ONEDAY}">Reykjavik w jeden dzień</a> — co zrobić z godzinami, które właśnie się zwolniły</li>
  <li><a href="{TOWER}">Hallgrímskirkja i wieża</a> — bilety, godziny i granica 16:45</li>
  <li><a href="{HOME}">Pełny przewodnik po Reykjaviku</a> — spacer, wycieczki i pory roku</li>
  <li><a href="{GUIDES}">Wszystkie przewodniki po Reykjaviku</a></li>
</ul>

<h2>Najkrócej</h2>
<p>Bierz Flybusa, o ile nie masz powodu, żeby zrobić inaczej: odjazdy idą za lotami, przy opóźnieniu miejsce przechodzi na następny kurs, a wysadza cię na skraju centrum za 3999 ISK. Bierz 55, jeśli rozkład się zgadza i liczysz każdą koronę. Bierz auto tylko wtedy, gdy wyjeżdżasz z miasta.</p>
<p>Potem załatw bagaż i wykorzystaj godziny. Jeśli wolisz rozumieć miasto, niż w nim czekać, weź <a href="#audio">audioprzewodnik TouringBee</a>: 27 przystanków, 2–2,5 godziny, w pełni offline.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">Pokój będzie gotowy dopiero o drugiej</h2>
  <p>Spacer trwa dwie i pół godziny. Rachunek robi się sam.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Zacznij spacer — 9,99 €</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Znajdź hotel w centrum</a>
  </div>
</div>

<p class="disc">Część linków na tej stronie to linki afiliacyjne — jeśli rezerwujesz przez nie, możemy dostać prowizję, bez dodatkowego kosztu dla ciebie. Ceny i godziny sprawdzone na stronach przewoźników w październiku 2026 roku; zmieniają się bez uprzedzenia, potwierdź przed wyjazdem. Flybus: flybus.is. Autobus miejski: straeto.is.</p>

  </div>
</section>
"""
