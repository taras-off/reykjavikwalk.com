# -*- coding: utf-8 -*-
"""PL — napisane po polsku, nie tłumaczone.

Forma: ty, czas teraźniejszy i tryb rozkazujący — bez rodzajowych form przeszłych
(«przyjechałeś/przyjechałaś»). Historie zostają w audioprzewodniku.
"""

HEADLINE = "Reykjavik w jeden dzień: co zobaczyć i w jakiej kolejności"
TITLE = "Reykjavik w jeden dzień: co zobaczyć i trasa pieszo"
DESC = ("Co zobaczyć w Reykjaviku w jeden dzień: trasa piesza ułożona wokół dwóch ograniczeń — "
        "światła dziennego i ostatniego wjazdu na wieżę o 16:45.")

FAQ = [
 ("Czy jeden dzień wystarczy na Reykjavik?",
  "Na samo miasto tak. Stare centrum przechodzi się w dwadzieścia minut, a klasyczna trasa piesza ma około "
  "5 km, więc dzień spokojnie ją mieści razem z postojami. Jeden dzień nie wystarczy, żeby dołożyć Złoty "
  "Krąg albo południowe wybrzeże: to osobne dni, a większość każdego z nich spędza się w aucie."),
 ("O której zaczynać zimą?",
  "W grudniu staraj się być na zewnątrz o 10:30 i traktuj 16:45 jak twardy termin: to ostatni wjazd na "
  "wieżę kościoła Hallgrímskirkja od września do maja. Wszystko po zmroku nadal działa — port, basen, "
  "kolacja. Punkt widokowy i zdjęcia już nie."),
 ("Po co mi audioprzewodnik, skoro mam tę trasę?",
  "Ta strona odpowiada na pytanie gdzie i kiedy: godziny, rezerwacje i plan awaryjny na złą pogodę. "
  "Audioprzewodnik odpowiada na pytanie, na co właściwie patrzysz i dlaczego to ciekawe — 27 historii "
  "wzdłuż tej samej linii. Trasa jest więc planem dnia, a TouringBee opowieścią po drodze."),
 ("Czy na jeden dzień w Reykjaviku potrzebny jest samochód?",
  "Nie. Dzień w mieście robi się pieszo i jest płasko, poza jednym podejściem. Wszystko dalej obsługują "
  "autobusy Strætó za 690 ISK od przejazdu. Samochód zaczyna się opłacać dopiero poza miastem."),
 ("Ile kosztuje dzień w Reykjaviku?",
  "Chodzenie nie kosztuje nic. Stałe wydatki są niewielkie: 1500 ISK za wieżę i 690 ISK za autobus. Na "
  "sumę wpływają laguna i kolacja — we dwie potrafią przeważyć całą resztę."),
 ("Co zarezerwować przed przyjazdem?",
  "Przy zwykłym dniu w mieście przede wszystkim lagunę: Sky Lagoon i Blue Lagoon działają na wejściówki "
  "godzinowe, a te najbardziej oblegane, wieczorne, potrafią rozejść się z dużym wyprzedzeniem. Latem "
  "dorzuć rejs na wieloryby z dniem zapasu. Resztę da się ustalić rano."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/hero-1536.webp" width="1536" height="864" alt="Nadbrzeże Reykjaviku pod szerokim islandzkim niebem" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reykjavik</a> › Jeden dzień w Reykjaviku</p>
    <h1>Reykjavik w jeden dzień: co zobaczyć i trasa, która wytrzyma krótkie światło</h1>
    <p class="sub">O tym dniu decydują dwa ograniczenia: ile dostaniesz światła i godzina 16:45. Cała reszta jest do ustalenia.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, autor audioprzewodników TouringBee">
      <span>Eugene · Aktualizacja 23 września 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#plan">Przejdź do planu</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Wycieczki jednodniowe</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">Pod koniec grudnia słońce wychodzi zza dachów około 11:20, a o wpół do czwartej już go nie ma. Ostatni wjazd na wieżę kościoła Hallgrímskirkja rusza o 16:45. Między tymi dwiema godzinami mieści się cały twój dzień w Reykjaviku.</p>

<p>Dlatego dalej nie ma listy zabytków, tylko rozkład godzin. Stare centrum przechodzi się w dwadzieścia minut, a cała trasa piesza ma około 5 km. Nogi nie są tu problemem. Problemem są światło i godziny otwarcia.</p>

<p>Cały dzień da się przejść wyłącznie z tą stroną. A jeśli chcesz też wiedzieć, co kryje się za mijanymi miejscami, <a href="#audio">spacer z audio TouringBee</a> idzie tą samą linią. Układasz jeszcze cały wyjazd? Zacznij od <a href="{HOME}">naszego pełnego przewodnika po Reykjaviku</a>.</p>

<div class="glance">
  <h2>W skrócie</h2>
  <dl>
    <dt>Pieszo</dt><dd>Około 5 km, płasko poza podejściem ulicą Skólavörðustígur</dd>
    <dt>Układ dnia</dt><dd>Stare centrum → kościół i jego wieża → nadbrzeże → gorąca woda</dd>
    <dt>Twardy termin</dt><dd>16:45 — ostatni wjazd na wieżę, od 1 września do 31 maja</dd>
    <dt>Bilet na wieżę</dt><dd>1500 ISK dorośli · 200 ISK dzieci 7–16 lat · tylko w kasie na miejscu</dd>
    <dt>Autobus</dt><dd>690 ISK za przejazd w sieci Strætó</dd>
    <dt>Rezerwacja z wyprzedzeniem</dt><dd>Laguna — główna rezerwacja, którą warto załatwić przed przyjazdem</dd>
    <dt>Najgorszy miesiąc na improwizację</dt><dd>Grudzień: mniej więcej cztery użyteczne godziny światła</dd>
  </dl>
</div>

<div class="minicta">
  <h2>Przejdź tę trasę z audioprzewodnikiem</h2>
  <p>Ta sama linia przez centrum, tylko opowiedziana: <strong>27 przystanków, 2–2,5 godziny</strong>, mapa i audio offline. Przerwij na wieżę, obiad albo muzeum i wróć dokładnie tam, gdzie skończysz.</p>
  <a {BUY}>Audioprzewodnik po Reykjaviku — 9,99 €</a>
</div>

<h2 id="plan">Sprawdź najpierw dwie rzeczy: zachód słońca i wieżę</h2>

<p>Pierwsze ograniczenie to słońce i nie robi taryfy ulgowej. Reykjavik leży tuż poniżej koła podbiegunowego, więc różnica między pełnią lata a pełnią zimy jest większa niż prawie wszędzie, gdzie planuje się wyjazdy.</p>

<table class="tbl">
  <tr><th>Miesiąc</th><th>Użyteczne światło</th><th>Co to zmienia w jednym dniu</th></tr>
  <tr><td>Grudzień – styczeń</td><td>4–5 godzin</td><td>Jeden blok na zewnątrz, nie dwa. Reszta dzieje się po ciemku i to jest w porządku.</td></tr>
  <tr><td>Luty – kwiecień</td><td>Szybko przybywa</td><td>Cała trasa przy świetle, a noce nadal na tyle ciemne, żeby wypatrywać zorzy.</td></tr>
  <tr><td>Maj – lipiec</td><td>Praktycznie całą dobę</td><td>Możesz ruszyć w południe albo o dziewiątej wieczorem. Ograniczenie światła znika; to również szczyt sezonu.</td></tr>
  <tr><td>Sierpień – listopad</td><td>Szybko ubywa</td><td>Wrzesień i październik to niezły kompromis między długością dnia a nocami dość ciemnymi na zorzę.</td></tr>
</table>

<p>Drugie ograniczenie to wieża. Hallgrímskirkja pozostaje jedynym wysokim punktem widokowym w centrum, a od 1 września do 31 maja kościół zamyka się o 17:00, z ostatnim wjazdem o 16:45. Latem jest czynny do 20:00, a wieża do 19:45. Biletów nie da się zarezerwować i są ważne raz, w dniu zakupu, więc nie wciśniesz tego punktu w dowolne okienko.</p>

<table class="tbl">
  <tr><th>Bilet na wieżę</th><th>Cena</th></tr>
  <tr><td>Dorośli</td><td>1500 ISK</td></tr>
  <tr><td>Dzieci 7–16 lat</td><td>200 ISK</td></tr>
  <tr><td>Studenci, seniorzy 67+, osoby z niepełnosprawnością</td><td>1300 ISK</td></tr>
</table>

<p>Nabożeństwa i koncerty zamykają kościół dla zwiedzających bez większego uprzedzenia, więc zerknij na program dnia, zanim ułożysz całe popołudnie wokół wieży.</p>

<figure>
  <img src="{P}img/tile-hallgrimskirkja.webp" width="800" height="600" loading="lazy" alt="Hallgrímskirkja widziana z dołu, obok wieży powiewa islandzka flaga">
  <figcaption>Jedyny punkt tego dnia z godziną zamknięcia — i jedyny, dla którego warto przestawić resztę.</figcaption>
</figure>

<h2>Rano: stare centrum</h2>

<p>Zacznij na Arnarhóll, niskim zielonym wzgórzu nad drogą portową, gdzie pomnik założyciela miasta patrzy na zatokę. Miejsca nie wybrał sam. Pozwolił, żeby wybrało za niego coś innego, a to historia, na którą audioprzewodnik poświęca sporo czasu.</p>

<p>Stamtąd stare centrum rozwija się w dół w jakieś trzy ulice. Plac Austurvöllur ma parlament po jednej stronie. W stawie Tjörnin stoi ratusz na palach. Pomiędzy nimi są małe muzea, w tym to zbudowane wokół odkopanej ściany długiego domu pod chodnikiem. Nic z tego nie zajmuje dużo czasu. Wszystko to przechodzi się za darmo.</p>

<p>Dwie praktyczne uwagi. Islandia jest kartowa do przesady: można tu spędzić tydzień bez dotykania gotówki, a część miejsc już jej nie przyjmuje. A woda z kranu jest wszędzie świetna i darmowa, więc butelka wielorazowa oszczędza więcej, niż się wydaje.</p>

<h2>Południe: tęczowa ulica, potem wieża</h2>

<p>Skólavörðustígur wspina się od ulicy handlowej pod drzwi kościoła, a jej ostatni odcinek jest pomalowany w trwałe tęczowe pasy. To jedno z najczęściej fotografowanych miejsc w Reykjaviku. Wcześnie rano albo pod wieczór masz ją niemal pustą; między jedenastą a trzecią latem już nie.</p>

<p>Wejdź na wieżę teraz, nie zostawiaj jej na koniec dnia. Zimą właśnie po to ściśnięty jest poranek. Latem masz więcej zapasu, choć zwykle spokojniej jest wcześnie albo blisko ostatniego wjazdu.</p>

<h2>Obiad i rezerwacja, o którą warto zadbać</h2>

<p>Je się na Laugavegur i w bocznych uliczkach. Tani klasyk to islandzka <em>pylsa</em>: hot dog z mieszanki jagnięciny, wieprzowiny i wołowiny. Zamawiaj <em>eina með öllu</em>, czyli „jeden ze wszystkim”. Zimą tę samą robotę robi zupa z jagnięciny. Restauracje z obsługą są naprawdę drogie — to tu dzień w Reykjaviku przestaje być tani.</p>

<div class="ticketbox">
  <h3>Zarezerwuj lagunę przed wylotem</h3>
  <p>Sky Lagoon i Blue Lagoon działają na wejściówki godzinowe, a te wieczorne, najbardziej oblegane, potrafią rozejść się z dużym wyprzedzeniem. Przy zwykłym dniu w mieście to główna rezerwacja do załatwienia przed przyjazdem.</p>
  <a class="btn sm" href="{TIQETS}" {OTA}>Zobacz bilety do laguny</a>
  <a class="btn sm outline" href="{GYG}" {OTA}>Porównaj wycieczki i transfery</a>
</div>

<h2>Popołudnie: nadbrzeże</h2>

<p>Druga połowa dnia biegnie wzdłuż morza. Do Harpy, szklanej filharmonii na skraju portu, wchodzi się za darmo i w pogodny dzień warto postać w środku te pięć minut. Dalej przy ścieżce Sæbraut stoi Sun Voyager, stalowa rzeźba, którą wszyscy fotografują jak łódź wikingów. Nie jest nią, a prawdziwy powód jest lepszy od mitu.</p>

<figure>
  <img src="{P}img/sec-sun-voyager.webp" width="1024" height="683" loading="lazy" alt="Zwiedzająca mija zimą rzeźbę Sun Voyager na nadbrzeżu Sæbraut">
  <figcaption>Fotografowana bez przerwy i prawie zawsze nazywana błędnie.</figcaption>
</figure>

<p>Potem stary port: łodzie na wieloryby, restauracje rybne i szary okręt straży przybrzeżnej przy nabrzeżu, z bojowym życiorysem przeciw znacznie większej flocie. Jeśli dojdziesz do samego końca, trafisz na trawiasty kopiec, na którym kończy się trasa audio.</p>

<p>Tu zapada jedyna prawdziwa decyzja popołudnia. Rejs na wieloryby ze starego portu trwa około trzech godzin i zjada całą resztę światła. Latem ma to sens, jeśli przyjeżdżasz tu dla zwierząt; w grudniu to kiepski interes, bo te trzy godziny to całe światło, jakie masz.</p>

<h2>Wieczór: najpierw gorąca woda, potem jedzenie</h2>

<p>Islandczycy kończą dzień w wodzie, a nie w barze, i masz do wyboru dwa poziomy.</p>

<p>Sky Lagoon to wersja dopieszczona: nad oceanem, piętnaście minut od centrum, z siedmiostopniowym rytuałem wliczonym w bilet. Pakiet Saman zaczyna się od około 113 € za osobę dorosłą (57 € dla młodzieży), Sér z prywatnymi przebieralniami od mniej więcej 136 €.</p>

<p>Opcja miejscowa to komunalny basen geotermalny — Sundhöllin w centrum, Laugardalslaug jako pełny kompleks. Grzane spod ziemi, czynne do późna i za ułamek ceny laguny; aktualna stawka dla dorosłych jest na reykjavik.is. Jedna zasada liczy się bardziej niż wszystkie inne: przed wejściem do wody myjesz się dokładnie, bez stroju kąpielowego. Wisi to w każdej przebieralni i jest egzekwowane.</p>

<h2>Trzy warianty</h2>

<h3>Przesiadka, a nie cały dzień</h3>
<p>Jeśli masz między lotami sześć albo siedem godzin w mieście, odpuść część nadbrzeżną. Autobus z Keflavíku, stare centrum i wieża, obiad na Laugavegur, autobus z powrotem. To mieści się w krótkiej przesiadce razem z dojazdem w obie strony i i tak daje najlepszy widok w mieście.</p>

<h3>Grudniowy dzień</h3>
<p>Ściśnij wszystko, co na zewnątrz, między 11:00 a 15:30 i pogódź się z tym, że port, kolacja i basen wypadną po ciemku. To nie jest gorsza wersja: światła portu na wodzie biją wersję dzienną. A długa ciemna połowa doby to twoja szansa na zorzę, o ile zejdą się zachmurzenie i aktywność słoneczna. Ciemny odcinek nadbrzeża Sæbraut jest najprostszy z miasta. Latarnia Grótta, jeden autobus na zachód, jest jeszcze ciemniejsza. Ale żadne z tych miejsc nie zastąpi prawdziwego wyjazdu poza miejskie światła.</p>

<h3>Mokry dzień z wiatrem w bok</h3>
<p>Pogoda zmienia się tu co godzinę, a szkody robi wiatr. W kiepski dzień odwróć plan: muzea i basen w środku dnia, spacer w oknie, które się otworzy. Parasol na niewiele się tu zda: mocny podmuch wywraca go na drugą stronę. Nieprzemakalna kurtka z kapturem i czapka są pewniejsze, w każdym miesiącu.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>Audioprzewodnik</h2>
    <p class="lead" style="max-width:720px">Zobaczyć trasę to jedno. Zrozumieć, dlaczego Reykjavik powstał akurat tutaj, co naprawdę przedstawia Sun Voyager i jak tak mały kraj potrafił postawić się znacznie większym — to zupełnie co innego.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="Aplikacja TouringBee z trasą po Reykjaviku, na tle Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">Audioprzewodnik TouringBee po Reykjaviku</h3>
        <p class="meta" style="margin:0 0 10px">27 przystanków · 2–2,5 godziny · rok dostępu</p>
        <div class="rate">{STARS}<b>4,7</b> {RATELABEL}</div>
        <div class="price">9,99 €<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Po pobraniu działa w pełni offline</strong> — mapa i ilustracje w komplecie, w trasie nie potrzebujesz internetu</li>
          <li><strong>We własnym tempie.</strong> Przerwij na obiad albo muzeum i wróć dwie godziny później w to samo miejsce</li>
          <li><strong>Opowiadany w roli</strong> rybaka z Reykjaviku, który ma czas do następnego wyjścia w morze</li>
          <li><strong>Jedna płatność.</strong> Bez grupy, bez rozkładu i bez przewodnika, który na ciebie czeka</li>
        </ul>
        <a {BUY} style="width:100%">Przejdź Reykjavik z audioprzewodnikiem</a>
        <p class="meta" style="margin:12px 0 0;text-align:center">{CHECKOUTNOTE} <a href="{TBPRODUCT}" rel="noopener" data-no-widget>{OPENSHOP}</a>.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap prose">

<h2>Ile kosztuje ten dzień</h2>
<table class="tbl">
  <tr><th>Pozycja</th><th>Koszt</th></tr>
  <tr><td>Przejście miasta pieszo</td><td>Za darmo</td></tr>
  <tr><td>Audioprzewodnik, jedna płatność</td><td>9,99 €</td></tr>
  <tr><td>Wieża Hallgrímskirkja, dorosły</td><td>1500 ISK</td></tr>
  <tr><td>Pojedynczy przejazd Strætó</td><td>690 ISK</td></tr>
  <tr><td>Basen miejski</td><td>Ułamek ceny laguny</td></tr>
  <tr><td>Sky Lagoon, pakiet Saman</td><td>od około 113 €</td></tr>
  <tr><td>Wieloryby, około 3 godzin</td><td>Cena u operatora; prawdziwym kosztem jest światło</td></tr>
</table>

<p>Samo miasto nie jest drogie. Budżet rośnie gwałtownie dopiero wtedy, gdy dochodzą laguna, wycieczki poza miasto i kolacje w restauracjach.</p>

<h2>Pięć błędów, które kosztują cały dzień</h2>
<ol>
  <li><strong>Zostawianie wieży na koniec dnia zimą.</strong> Ostatni wjazd 16:45, od września do maja, a bilety są tylko w kasie na miejscu.</li>
  <li><strong>Doklejanie Złotego Kręgu do dnia w mieście.</strong> To osiem godzin w aucie. Należy mu się osobny dzień.</li>
  <li><strong>Oddawanie niemal całego grudniowego światła łodzi.</strong> Trzy godziny na morzu przy czterech godzinach światła.</li>
  <li><strong>Liczenie na parasol.</strong> Wiatr wywraca go na drugą stronę. Lepiej warstwy, kaptur i czapka.</li>
  <li><strong>Traktowanie laguny jak miejsca, do którego wchodzi się z marszu.</strong> Są wejściówki godzinowe, a wieczorne schodzą pierwsze.</li>
</ol>

<h2>Częste pytania</h2>
<div class="faq">{FAQHTML}</div>

<h2>Czytaj dalej</h2>
<ul>
  <li><a href="{HOME}">Pełny przewodnik po Reykjaviku</a> — spacer, wycieczki i pory roku</li>
  <li><a href="{GUIDES}">Wszystkie przewodniki po Reykjaviku</a> — co jest opublikowane, a co dopiero powstaje</li>
</ul>

<h2>Najkrócej</h2>
<p>Reykjavik oddaje prawie wszystko, co ma, w jeden dzień na piechotę. Odległości nigdy nie będą tu problemem. Światło będzie.</p>
<p>Sprawdź więc godzinę zachodu, nie zostawiaj wieży na wieczór, a resztę przejdź we własnym tempie. A jeśli chcesz po drodze rozumieć miasto, a nie tylko na nie patrzeć, weź <a href="#audio">audioprzewodnik TouringBee po Reykjaviku</a>: 27 przystanków, 2–2,5 godziny, w pełni offline.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">Dwadzieścia siedem przystanków na tej samej linii</h2>
  <p>Ta strona doprowadza cię we właściwe miejsce o właściwej godzinie. Audioprzewodnik mówi, na co patrzysz.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Zacznij spacer — 9,99 €</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Znajdź hotel w centrum</a>
  </div>
</div>

<p class="disc">Część linków na tej stronie to linki afiliacyjne — jeśli rezerwujesz przez nie, możemy dostać prowizję, bez dodatkowego kosztu dla ciebie. Ceny i godziny sprawdzone na stronach operatorów we wrześniu 2026 roku; zmieniają się bez uprzedzenia, potwierdź je przed wyjazdem. Wieża: hallgrimskirkja.is. Autobusy: straeto.is. Laguna: skylagoon.com.</p>

  </div>
</section>
"""
