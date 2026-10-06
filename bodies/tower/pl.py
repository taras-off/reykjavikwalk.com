# -*- coding: utf-8 -*-
"""PL — forma: ty, czas teraźniejszy i tryb rozkazujący, bez rodzajowych form przeszłych."""

HEADLINE = "Wieża Hallgrímskirkja: bilety, godziny i kiedy wchodzić"
TITLE = "Hallgrímskirkja: bilety, godziny i wejście na wieżę"
DESC = ("Bilety i godziny wieży Hallgrímskirkja, granica 16:45 zimą, co naprawdę widać z góry i "
        "kiedy kościół jest zamknięty dla zwiedzających.")

FAQ = [
 ("Ile kosztuje wejście na wieżę Hallgrímskirkja?",
  "1500 ISK dla dorosłego i 200 ISK dla dziecka w wieku 7–16 lat. Studenci i osoby z "
  "niepełnosprawnością płacą 1300 ISK; osoby od 67. roku życia mają zniżkę, choć kościół nie podaje "
  "kwoty. Grupy od dziesięciu osób dostają 10 procent rabatu, a grupy szkolne do 16 lat wchodzą za "
  "darmo. Wejście do samego kościoła nic nie kosztuje — płatna jest tylko wieża."),
 ("Czy da się kupić bilety na wieżę przez internet?",
  "Nie. Kościół pisze wprost, że wieży nie można zarezerwować z wyprzedzeniem. Bilety sprzedaje sklepik "
  "kościelny po lewej stronie zaraz za wejściem i są ważne tylko w dniu zakupu. To, co sprzedaje się "
  "online jako „bilet do Hallgrímskirkja”, to coś innego: wycieczka, która zatrzymuje się przed "
  "kościołem, a nie wstęp na wieżę."),
 ("O której zamyka się wieża Hallgrímskirkja?",
  "Od 1 września do 31 maja kościół zamyka się o 17:00, a ostatni wjazd na wieżę jest o 16:45. Od 1 "
  "czerwca do 31 sierpnia czynne do 20:00, wieża do 19:45. Nabożeństwa, uroczystości i koncerty zamykają "
  "kościół dla zwiedzających także w innych porach, więc sprawdź program dnia, zanim ułożysz wokół tego "
  "całe popołudnie."),
 ("Czy warto?",
  "Dla widoku tak: to jedyny wysoki punkt w starym centrum i jedyny, z którego patrzysz na kolorowe "
  "dachy pionowo z góry. Dwadzieścia minut i 1500 ISK to uczciwa wymiana. Jeśli zależy ci na szerszej "
  "panoramie z całą zatoką i górami, Perlan robi to lepiej, ale kosztuje więcej i zabiera pół dnia."),
 ("Czy winda jedzie na sam szczyt?",
  "Prawie. Winda pokonuje większość wysokości, potem zostaje krótki odcinek schodów do tarasu. Taras "
  "jest zamknięty, z otworami na wszystkie cztery strony zamiast otwartej przestrzeni, więc działa przy "
  "każdej pogodzie. Jest mały, a kościół zamyka go, gdy zrobi się tłoczno."),
 ("Czy kościół można zwiedzać za darmo?",
  "Tak. Hallgrímskirkja to czynna parafia, a wejście, żeby zobaczyć nawę i organy, nic nie kosztuje w "
  "godzinach otwarcia. Płacisz tylko za wjazd na górę. Nabożeństwa są otwarte dla wszystkich, ale w ich "
  "trakcie budynek nie jest punktem turystycznym."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/tile-hallgrimskirkja.webp" width="800" height="600" alt="Hallgrímskirkja widziana z dołu, obok wieży powiewa islandzka flaga" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reykjavik</a> › Hallgrímskirkja</p>
    <h1>Hallgrímskirkja: bilety, godziny i kiedy wchodzić na wieżę</h1>
    <p class="sub">Kościół jest za darmo. Wieża nie, nie da się jej zarezerwować, a zimą przestaje wpuszczać o 16:45.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, autor audioprzewodników TouringBee">
      <span>Eugene · Aktualizacja 29 września 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#hours">Godziny i ceny</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Wycieczki po Reykjaviku</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">Dwie rzeczy zaskakują ludzi przy Hallgrímskirkja. Biletu na wieżę nie kupisz z wyprzedzeniem — nigdzie i za żadne pieniądze. A od września do maja ostatni wjazd rusza o 16:45, czyli w grudniu na długo przed tym, zanim większość zdąży skończyć obiad.</p>

<p>Cała reszta jest prosta. Do kościoła wchodzi się za darmo, stoi on na szczycie ulicy, którą i tak zamierzasz iść pod górę, a cały przystanek zajmuje jakieś pół godziny razem z kolejką.</p>

<p>Ta strona jest o wieży: ile kosztuje, kiedy jest otwarta, kiedy zamykają ją nabożeństwa i czy widok jest wart swojej ceny w porównaniu z alternatywami. Stanowi parę z <a href="{ONEDAY}">naszą trasą na jeden dzień w Reykjaviku</a>, w której ta wieża jest punktem stałym, wokół którego wygina się reszta. Jeśli wolisz historię budynku niż logistykę, tym zajmuje się <a href="#audio">spacer z audio TouringBee</a>.</p>

<div class="glance">
  <h2>W skrócie</h2>
  <dl>
    <dt>Wstęp do kościoła</dt><dd>Bezpłatny</dd>
    <dt>Bilet na wieżę</dt><dd>1500 ISK dorosły · 200 ISK dziecko 7–16 · 1300 ISK student lub osoba z niepełnosprawnością</dd>
    <dt>Rezerwacja</dt><dd>Niemożliwa. Sprzedaż w sklepiku kościelnym, tylko na dany dzień</dd>
    <dt>Godziny zimowe</dt><dd>1 IX – 31 V: kościół 10:00–17:00, ostatni wjazd 16:45</dd>
    <dt>Godziny letnie</dt><dd>1 VI – 31 VIII: kościół 09:00–20:00, wieża do 19:45</dd>
    <dt>Ile to trwa</dt><dd>Około 30 minut razem z kolejką</dd>
    <dt>Jak się wjeżdża</dt><dd>Winda prawie na górę, potem krótki odcinek schodów</dd>
    <dt>Wysokość</dt><dd>73 m według samego kościoła — najwyższy budynek w mieście</dd>
  </dl>
</div>

<div class="minicta">
  <h2>Kościół to jeden przystanek dłuższego spaceru</h2>
  <p>Spacer z audio TouringBee obejmuje Hallgrímskirkja i <strong>26 innych przystanków</strong> w starym centrum: <strong>2–2,5 godziny</strong>, mapa i audio offline, we własnym tempie.</p>
  <a {BUY}>Audioprzewodnik po Reykjaviku — 9,99 €</a>
</div>

<h2 id="hours">Co jest płatne, a co nie</h2>

<p>Hallgrímskirkja to czynna parafia luterańska, nie muzeum, i wstęp w godzinach otwarcia jest bezpłatny. Możesz usiąść w nawie, popatrzeć na organy i wyjść, nie płacąc nic. Bilet dotyczy wyłącznie wieży.</p>

<table class="tbl">
  <tr><th>Bilet na wieżę</th><th>Cena</th></tr>
  <tr><td>Dorośli</td><td>1500 ISK</td></tr>
  <tr><td>Dzieci 7–16 lat</td><td>200 ISK</td></tr>
  <tr><td>Studenci, osoby z niepełnosprawnością (za okazaniem dokumentu)</td><td>1300 ISK</td></tr>
  <tr><td>Osoby 67+</td><td>Zniżka; kościół nie podaje kwoty</td></tr>
  <tr><td>Grupy od 10 osób</td><td>10% rabatu</td></tr>
  <tr><td>Grupy szkolne, uczniowie do 16 lat</td><td>Bezpłatnie</td></tr>
</table>

<p>W sieci znajdziesz inne liczby. Turystyczny portal samego Reykjaviku przy naszym sprawdzeniu we wrześniu 2026 nadal podawał 1400 ISK i ostatnie wejście o 16:30. Wiele przewodników kopiuje też stary cennik, który kościół zostawił na własnej stronie ponad tym aktualnym. Ceny powyżej to te, które obowiązują dziś.</p>

<h2>Godziny i termin graniczny</h2>

<table class="tbl">
  <tr><th>Sezon</th><th>Kościół</th><th>Ostatni wjazd</th></tr>
  <tr><td>1 września – 31 maja</td><td>10:00 – 17:00</td><td>16:45</td></tr>
  <tr><td>1 czerwca – 31 sierpnia</td><td>09:00 – 20:00</td><td>19:45</td></tr>
</table>

<p>To wokół tej 16:45 układa się dzień, bo ta godzina nie przesuwa się razem ze światłem. Pod koniec grudnia słońce i tak znika o wpół do czwartej, więc wieża i użyteczne światło kończą się razem. W lutym o 16:45 jest jeszcze jasno i ludzie właśnie dlatego przegapiają wjazd: niebo nie wygląda na godzinę zamknięcia.</p>

<p>Pozostałe zamknięcia są mniej przewidywalne. Kościół zamyka się dla zwiedzających podczas nabożeństw, ślubów, pogrzebów i koncertów, i mówi o tym wprost: godziny mogą się zmienić. Zamyka też taras przy niektórych wydarzeniach, a przy tłoku wcześniej, niż zapowiada. Niedzielny poranek to najpewniejszy sposób, żeby przyjść pod zamknięte drzwi.</p>

<h2>Kupowanie biletu</h2>

<p>Sklepik jest po lewej, zaraz za wejściem do przedsionka. To jedyne miejsce, w którym bilet na wieżę w ogóle istnieje. Kościół formułuje to tak: rezerwacja wieży z wyprzedzeniem nie jest możliwa. Żadnej sprzedaży online, żadnych okienek czasowych, żadnego pomijania kolejki.</p>

<p>To, co widzisz w sieci jako bilet do Hallgrímskirkja, jest czymś innym: wycieczką, która zatrzymuje się przed wejściem, albo kartą miejską, która może zwróci ci koszt. Bilet jest ważny raz, w dniu zakupu, więc nie kupisz go rano, żeby wykorzystać o zmierzchu.</p>

<h2>Wjazd na górę</h2>

<p>Winda pokonuje prawie całą wysokość, krótki odcinek schodów robi resztę. Taras jest zamknięty, z łukowymi otworami na cztery strony zamiast otwartej przestrzeni — i dlatego działa w dniu, w którym na dole wiatr rozkłada parasole na części.</p>

<p>Taras jest mały. W lipcu wolną częścią jest kolejka na dole, a nie sam wjazd, i kościół woli przytrzymać ludzi niż zatłoczyć platformę. Kwadrans na górze w zupełności wystarczy.</p>

<figure>
  <img src="{P}img/tile-rainbow-street.webp" width="800" height="600" loading="lazy" alt="Skólavörðustígur pomalowana w tęczowe pasy, prowadząca pod górę do Hallgrímskirkja">
  <figcaption>Ulica, którą podchodzisz, żeby tu dotrzeć. Z tarasu schodzisz nią z powrotem wzrokiem.</figcaption>
</figure>

<h2>Co naprawdę widać</h2>

<p>Spójrz na zachód, a masz obraz, po który przyjeżdżają wszyscy. Skólavörðustígur schodzi w tęczowych pasach, dalej kolorowe blaszane dachy starego centrum piętrzą się aż do portu, a za nimi zatoka i góra Esja. To ten widok uzasadnia bilet. Jest też jedyną rzeczą, której Perlan nie da: leży za daleko, żeby patrzeć na dachy z góry.</p>

<p>Na południe i wschód rozciąga się mieszkalny Reykjavik, a w pogodny dzień półwysep Reykjanes. Na północ port i woda. Nie ma złej strony, ale jeśli masz jedną chwilę czystego nieba i aparat, wybierz zachód.</p>

<p>Światło liczy się tu bardziej niż godzina. Latem niskie słońce późnym popołudniem wypada lepiej niż południe. Zimą okno i tak jest wąskie, a zachmurzone niebo spłaszcza dachy w jednolitą szarość — warto to wiedzieć, zanim wydasz 1500 ISK w nieodpowiednie popołudnie.</p>

<h2>W środku, za darmo</h2>

<p>Nawa mieści 1200 osób i jest celowo surowa: biała, bardzo wysoka, prawie bez dekoracji. W głębi stoją organy Klaisa, zbudowane w Bonn i ukończone w 1992 roku — 5275 piszczałek, 15 metrów wysokości, około 25 ton. Są też drugie, mniejsze organy duńskiej firmy Frobenius, przebudowane i ponownie poświęcone w 2024 roku. Na tych dużych nagrywają organiści z całego świata; jeśli przy wejściu trwa próba, zostań.</p>

<p>Budowa trwała długo. Guðjón Samúelsson, architekt państwowy, dostał zlecenie w latach trzydziestych i nie doczekał ukończenia. Prace szły od 1945 roku do konsekracji w 1986, a w międzyczasie parafia przez 26 lat korzystała z krypty. Fasadę opisuje się zwykle jako bazaltowe kolumny; sam kościół porównuje ją do skały słupowej, islandzkich gór i lodowców.</p>

<p>To porównanie podaje każdy przewodnik. Dlaczego architekt państwowy spędził karierę na szukaniu osobnego, islandzkiego stylu, to dłuższa historia — i audioprzewodnik poświęca jej czas.</p>

<p>I jeszcze jedno, na zewnątrz. Pomnik na placu stał tu wcześniej niż kościół, a postawienie go tam nie było pomysłem Islandii.</p>

<h2>Wieża czy Perlan?</h2>

<table class="tbl">
  <tr><th></th><th>Hallgrímskirkja</th><th>Perlan</th></tr>
  <tr><td>Gdzie</td><td>Na szczycie starego centrum, pieszo</td><td>Na wzgórzu poza centrum, autobus albo taksówka</td></tr>
  <tr><td>Widok</td><td>Pionowo na kolorowe dachy i tęczową ulicę</td><td>Szeroka panorama: zatoka, miasto, góry</td></tr>
  <tr><td>Taras</td><td>Zamknięty, mały</td><td>Otwarty taras widokowy plus wystawy</td></tr>
  <tr><td>Bilet</td><td>1500 ISK, tylko na miejscu</td><td>Więcej; sprawdź aktualną cenę, zmienia się</td></tr>
  <tr><td>Czas</td><td>30 minut</td><td>Pół dnia razem z dojazdem</td></tr>
</table>

<p>Przy jednym dniu w mieście wieża wygrywa już samym czasem. Przy dwóch dniach, z których jeden jest deszczowy, Perlan jest lepszym budynkiem na złą pogodę, bo w środku jest co robić.</p>

<div class="ticketbox">
  <h3>Wieży nie zarezerwujesz — tego dookoła tak</h3>
  <p>Do samej Hallgrímskirkja nie ma czego rezerwować. Do tego, co obok, jest: Perlan, laguny i wycieczki z przewodnikiem przechodzące obok kościoła sprzedają wejściówki z wyprzedzeniem.</p>
  <a class="btn sm" href="{TIQETS}" {OTA}>Bilety w Reykjaviku</a>
  <a class="btn sm outline" href="{GYG}" {OTA}>Porównaj wycieczki</a>
</div>

<h2>Trzy sytuacje</h2>

<h3>Masz kilka godzin między lotami</h3>
<p>Wieża to najlepsze wykorzystanie krótkiej przesiadki: dwadzieścia minut pieszo od przystanku w centrum i całe miasto naraz. Najpierw wejdź na górę, a potem zejdź do starego centrum, nie odwrotnie.</p>

<h3>Jest niedziela</h3>
<p>Poranne nabożeństwa zamykają kościół dla zwiedzających. Przyjdź po obiedzie; zimą i tak zostaje ci spokojny zapas przed 16:45.</p>

<h3>Pogoda się załamała</h3>
<p>Nie skreślaj wieży. Taras jest zamknięty, a wiatr, który psuje spacer po ulicy, na górze nie przeszkadza. Prawdziwym problemem są niskie chmury: jeśli z chodnika nie widać Esji, z 73 metrów też wiele nie zobaczysz.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>Audioprzewodnik</h2>
    <p class="lead" style="max-width:720px">Z tarasu widzisz, jak Reykjavik wygląda. Dlaczego miasto wyrosło akurat tutaj, co robi ten pomnik na placu i co architekt naprawdę budował — to zupełnie inne pytania.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="Aplikacja TouringBee z trasą po Reykjaviku, na tle Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">Audioprzewodnik TouringBee po Reykjaviku</h3>
        <p class="meta" style="margin:0 0 10px">27 przystanków · 2–2,5 godziny · rok dostępu</p>
        <div class="rate">{STARS}<b>4,7</b> {RATELABEL}</div>
        <div class="price">9,99 €<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Hallgrímskirkja to jeden z 27 przystanków</strong> — trasa biegnie od wzgórza założyciela do starego portu</li>
          <li><strong>Po pobraniu działa w pełni offline</strong> — mapa i ilustracje w komplecie</li>
          <li><strong>We własnym tempie.</strong> Przerwij na wieżę i wróć tam, gdzie skończysz</li>
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

<h2>Pięć błędów</h2>
<ol>
  <li><strong>Szukanie biletów w internecie.</strong> Nie istnieją. Sklepik w kościele jest jedynym sprzedawcą.</li>
  <li><strong>Zostawianie wieży na późne popołudnie między wrześniem a majem.</strong> Ostatni wjazd 16:45, cokolwiek robi niebo.</li>
  <li><strong>Przyjście w niedzielny poranek.</strong> Nabożeństwa zamykają kościół dla zwiedzających.</li>
  <li><strong>Zaufanie cenie z portalu z listingami.</strong> Kilka nadal pokazuje 1400 ISK i godzinę 16:30.</li>
  <li><strong>Wjazd przy niskich chmurach.</strong> Jeśli z ulicy nie widać Esji, zachowaj bilet na jutro.</li>
</ol>

<h2>Częste pytania</h2>
<div class="faq">{FAQHTML}</div>

<h2>Czytaj dalej</h2>
<ul>
  <li><a href="{ONEDAY}">Reykjavik w jeden dzień</a> — trasa, której ta wieża jest osią</li>
  <li><a href="{KEF}">Z lotniska Keflavík do centrum</a> — jak w ogóle tu dotrzeć</li>
  <li><a href="{HOME}">Pełny przewodnik po Reykjaviku</a> — spacer, wycieczki i pory roku</li>
  <li><a href="{GUIDES}">Wszystkie przewodniki po Reykjaviku</a> — co jest opublikowane, a co dopiero powstaje</li>
</ul>

<h2>Najkrócej</h2>
<p>Wejdź za darmo, zapłać 1500 ISK w sklepiku, jeśli chcesz widok, i zrób to zimą przed 16:45. Patrz na zachód, tam są dachy. Pół godziny, i to najlepsze pół godziny, jakie sprzedaje stare centrum.</p>
<p>A jeśli wolisz rozumieć to, nad czym stoisz, a nie tylko na to patrzeć, weź <a href="#audio">audioprzewodnik TouringBee</a>: 27 przystanków przez centrum, ten w komplecie, w pełni offline.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">Kościół to przystanek pierwszy z dwudziestu siedmiu</h2>
  <p>Ta strona wprowadza cię na wieżę o właściwej godzinie. Audioprzewodnik mówi, czym jest miasto pod tobą.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Zacznij spacer — 9,99 €</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Znajdź hotel w centrum</a>
  </div>
</div>

<p class="disc">Część linków na tej stronie to linki afiliacyjne — jeśli rezerwujesz przez nie, możemy dostać prowizję, bez dodatkowego kosztu dla ciebie. Ceny i godziny sprawdzone na hallgrimskirkja.is we wrześniu 2026 roku; zmieniają się bez uprzedzenia, potwierdź przed wyjazdem.</p>

  </div>
</section>
"""
