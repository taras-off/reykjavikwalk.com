# -*- coding: utf-8 -*-
"""IT — scritto in italiano. Registro: tu. Pagina logistica, solo due ami."""

HEADLINE = "Dall'aeroporto di Keflavík a Reykjavik: quale transfer in base all'ora di atterraggio"
TITLE = "Keflavík–Reykjavik: bus, taxi o auto a noleggio"
DESC = ("Da Keflavík a Reykjavik: i prezzi reali di Flybus, autobus di linea e auto, e cosa fare "
        "delle ore fra l'atterraggio e il check-in in hotel.")

FAQ = [
 ("Qual è il modo più economico per andare da Keflavík a Reykjavik?",
  "L'autobus di linea, Strætó 55, a 2.400 ISK per un adulto. I ragazzi dai 12 ai 17 anni, chi ha più di "
  "67 anni e i passeggeri con disabilità pagano 1.200 ISK, i bambini sotto i 12 viaggiano gratis. Circola "
  "tutti i giorni ma non a ogni arrivo, e non tutte le corse finiscono al BSÍ: alcune terminano a "
  "Fjörður, a Hafnarfjörður, che non è il centro città."),
 ("Quanto ci vuole da Keflavík a Reykjavik?",
  "Circa 45 minuti in pullman per una cinquantina di chilometri, più o meno lo stesso in auto. Il tempo "
  "non se ne va nel viaggio. Se ne va aspettando il bus, che parte 35-45 minuti dopo l'atterraggio, e poi "
  "aspettando di nuovo, perché la camera non sarà pronta prima del pomeriggio."),
 ("Bisogna prenotare il bus in anticipo?",
  "Di solito no. Flybus vende i biglietti in aeroporto oltre che online, e le partenze seguono i voli in "
  "arrivo. Il biglietto online fa risparmiare qualcosa, evita la fila dopo un volo lungo e conviene nelle "
  "date affollate. Se il volo è in ritardo, l'operatore sposta il tuo posto sulla partenza successiva "
  "invece di trattenere il bus."),
 ("Il Flybus arriva fino al mio hotel?",
  "La tariffa base ti porta al terminal BSÍ. Flybus+ prosegue in minibus fino agli hotel convenzionati, "
  "con un supplemento. Se alloggi nel centro storico, il biglietto normale più una breve camminata è "
  "spesso più veloce che aspettare il giro del minibus."),
 ("Vale la pena noleggiare un'auto solo per il transfer?",
  "Da sola no. Una strada, 45 minuti e, in fondo, un'auto da parcheggiare in una città che si attraversa "
  "a piedi. Il noleggio inizia ad avere senso quando l'aeroporto è l'inizio di un viaggio su strada: "
  "Circolo d'Oro, costa sud, qualsiasi cosa fuori dalla capitale. La domanda vera è se esci dalla città."),
 ("Dove lascio i bagagli prima del check-in?",
  "Parti chiedendo in hotel: una camera non pronta non significa un hotel che non può aiutarti, e la "
  "maggior parte tiene le valigie fino al check-in senza farle pagare. Altrimenti ci sono i depositi a "
  "Keflavík e al BSÍ, quelli del BSÍ aperti 24 ore con 96 armadietti di quattro misure."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/sec-old-town.webp" width="1024" height="683" alt="Una bicicletta parcheggiata davanti a una vetrina nel centro storico di Reykjavik" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reykjavik</a> › Dall'aeroporto di Keflavík al centro</p>
    <h1>Dall'aeroporto di Keflavík a Reykjavik: le opzioni e quale sta bene con la tua ora di atterraggio</h1>
    <p class="sub">Cinquanta chilometri, una strada, quarantacinque minuti. Il transfer è la parte facile; il buco fra atterraggio e check-in no.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, autore delle audioguide TouringBee">
      <span>Di Eugene · Aggiornato il 5 ottobre 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#options">Confronta le opzioni</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Transfer ed escursioni</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">Da Keflavík a Reykjavik c'è una sola strada e ci vogliono circa 45 minuti. Il pullman dell'aeroporto regola le partenze sui voli in arrivo: di solito parte 35-45 minuti dopo un atterraggio, con un orario che comincia verso le 03:30 e arriva a tarda sera. Entrare in città è un problema risolto.</p>

<p>Non è risolta l'ora in cui tocchi terra. A Reykjavik il check-in in hotel è di norma alle 14:00 o alle 15:00. Se atterri prima, arrivi in città con le valigie, una camera chiusa e diverse ore da riempire — ed è questo, non i 50 km, a decidere quale biglietto ti conviene.</p>

<p>Perciò questa pagina fa entrambe le metà: le opzioni di transfer con i prezzi che gli operatori fanno davvero, e poi cosa fare del buco. Se il buco ti lascia in centro con del tempo, <a href="{ONEDAY}">il nostro itinerario di un giorno</a> e <a href="#audio">la passeggiata audio di TouringBee</a> sono costruiti esattamente per quelle ore. Stai montando tutto il viaggio? Parti dalla <a href="{HOME}">guida completa di Reykjavik</a>.</p>

<div class="glance">
  <h2>In breve</h2>
  <dl>
    <dt>Distanza</dt><dd>Circa 50 km dall'aeroporto al centro di Reykjavik</dd>
    <dt>Viaggio</dt><dd>Circa 45 minuti in pullman o in auto</dd>
    <dt>Flybus</dt><dd>Da 3.999 ISK a tratta fino al terminal BSÍ</dd>
    <dt>Autobus di linea</dt><dd>Strætó 55 — 2.400 ISK adulti, 1.200 ISK ridotto, gratis sotto i 12 anni</dd>
    <dt>Partenze</dt><dd>Flybus segue gli arrivi, all'incirca dalle 03:30 a tarda sera; Strætó va a orario fisso</dd>
    <dt>Prenotazione</dt><dd>Di solito non serve. I biglietti si comprano in aeroporto</dd>
    <dt>Bagagli</dt><dd>Chiedi prima in hotel; depositi in aeroporto e al BSÍ</dd>
    <dt>Il vincolo vero</dt><dd>Il check-in alle 14:00–15:00, non il transfer</dd>
  </dl>
</div>

<div class="minicta">
  <h2>Atterri presto? Quella è la finestra della passeggiata</h2>
  <p>La passeggiata audio di TouringBee è <strong>27 tappe, 2–2,5 ore</strong> nel centro storico, con mappa e audio offline. Sistemate le valigie, le ore morte prima del check-in diventano la parte migliore del primo giorno.</p>
  <a {BUY}>Audioguida di Reykjavik — 9,99 €</a>
</div>

<h2 id="options">Parti dalla tua ora di atterraggio, non dal prezzo</h2>

<p>Tutte le guide su questa tratta confrontano le tariffe. Ma il prezzo è solo metà del conto: un biglietto economico smette di essere conveniente nel momento in cui il suo orario ti aggiunge un'ora di attesa.</p>

<p>Chiediti piuttosto: a che ora toccano le ruote e dove dormi? Atterri a mezzogiorno con la camera pronta alle due e va bene qualunque cosa. Atterri alle sei del mattino e ti serve un piano per i bagagli e uno per te. L'autobus più economico non copre tutti i voli, quindi può costarti un'ora che avresti preferito spendere altrove.</p>

<table class="tbl">
  <tr><th>Opzione</th><th>Prezzo</th><th>Arriva a</th><th>Quando è la tua</th></tr>
  <tr><td><strong>Flybus</strong></td><td>da 3.999 ISK a tratta</td><td>Terminal BSÍ</td><td>Predefinita. Partenze legate agli arrivi; se sei in ritardo il posto passa al bus successivo</td></tr>
  <tr><td><strong>Flybus+</strong></td><td>supplemento</td><td>Hotel convenzionati</td><td>Tanti bagagli, bambini, maltempo o alloggio fuori centro</td></tr>
  <tr><td><strong>Airport Direct</strong></td><td>tariffa da verificare</td><td>Terminal centrale, premium fino all'hotel</td><td>Il secondo pullman di linea: vale il confronto di prezzo con Flybus</td></tr>
  <tr><td><strong>Strætó 55</strong></td><td>2.400 ISK adulti</td><td>BSÍ o Fjörður</td><td>Di giorno, bagagli leggeri, se l'orario coincide</td></tr>
  <tr><td><strong>Taxi o transfer privato</strong></td><td>A tassametro o su preventivo</td><td>La tua porta</td><td>Siete in tre o quattro, oppure l'ora è scomoda</td></tr>
  <tr><td><strong>Auto a noleggio</strong></td><td>Tariffa giornaliera</td><td>Dove vuoi</td><td>Solo se poi esci dalla città</td></tr>
</table>

<h2>Il Flybus, e perché è l'opzione predefinita</h2>

<p>È il pullman dell'aeroporto che prende la maggior parte delle persone, e quello che vende non è la velocità ma la certezza. Le partenze seguono i voli in arrivo invece di un intervallo fisso: di solito 35-45 minuti dopo un atterraggio. L'orario pubblicato comincia verso le 03:30 e arriva a tarda sera, quindi per un volo molto presto o molto tardi controlla l'orario della tua data invece di affidarti alla regola generale.</p>

<p>Se il volo è in ritardo l'operatore non trattiene il bus per te: ti garantisce un posto sulla partenza successiva, senza costi aggiuntivi. È una differenza che conta, e conviene conoscerla prima di agitarsi in fila al controllo passaporti. La tariffa comprende due bagagli fino a 23 kg ciascuno.</p>

<p>Il biglietto standard finisce al BSÍ, l'autostazione sul margine sud del centro. Flybus+ aggiunge una tratta in minibus fino agli hotel convenzionati, con supplemento. Si ripaga con bagagli pesanti, con bambini, col maltempo e quando l'alloggio è in periferia.</p>

<p>Se viaggi leggero e stai nel centro storico vale la pena confrontare: il minibus percorre una lista di indirizzi e il tuo potrebbe non essere il primo. Guarda quanto dista il tuo hotel dal BSÍ e decidi in base a quello, non per automatismo.</p>

<h2>Strætó 55, l'opzione economica e la sua fregatura</h2>

<p>L'autobus di linea è il 55 e costa 2.400 ISK per un adulto: 1.200 ISK per i 12-17 anni, gli over 67 e i passeggeri con disabilità, gratis sotto i 12. Per una famiglia quella differenza sono soldi veri.</p>

<p>Due fregature. Va a orario e non sul tuo volo, quindi un atterraggio alle 05:30 può significare una lunga attesa. E non tutte le corse finiscono al BSÍ: alcune terminano a Fjörður, a Hafnarfjörður, un comune a sud di Reykjavik che non è decisamente il centro. Controlla il capolinea prima di salire, non dopo.</p>

<div class="ticketbox">
  <h3>Transfer privati ed escursioni</h3>
  <p>Se siete in tre o quattro, calcola la tariffa del bus a testa contro un solo mezzo prima di dare per scontato che il pullman costi meno. I transfer privati e le escursioni che passano da Keflavík si prenotano in anticipo.</p>
  <a class="btn sm" href="{GYG}" {OTA}>Confronta i transfer</a>
  <a class="btn sm outline" href="{TIQETS}" {OTA}>Biglietti a Reykjavik</a>
</div>

<h2>Il taxi, e quando la distanza si accorcia</h2>

<p>I taxi islandesi vanno a tassametro e non esiste una tariffa fissa pubblicata per l'aeroporto: trattalo come l'opzione cara e chiedi una stima prima di salire.</p>

<p>In tre o quattro, fatti dare una stima aggiornata e confrontala con il totale dei biglietti del bus. Il taxi si paga a mezzo, il bus a passeggero, quindi la distanza si accorcia man mano che il gruppo cresce. Questo non rende il taxi economico, solo più vicino di quanto sembri a chi viaggia da solo.</p>

<h2>L'auto a noleggio, onestamente</h2>

<p>Per il solo transfer no. È una strada dritta che farai una volta e, in fondo, un'auto da parcheggiare in una città che si attraversa a piedi. Il noleggio inizia ad avere senso quando l'aeroporto è l'inizio di un viaggio su strada: Circolo d'Oro, costa sud, qualsiasi cosa fuori dalla capitale. Decidi sul viaggio, non sul transfer.</p>

<figure>
  <img src="{P}img/sec-winter-street.webp" width="1024" height="683" loading="lazy" alt="Un negozio d'angolo dai colori accesi in una via innevata del centro di Reykjavik">
  <figcaption>Il BSÍ sta appena a sud di tutto questo. Quasi tutto il centro storico è a pochi minuti a piedi dall'autostazione.</figcaption>
</figure>

<h2>Il buco fra atterraggio e check-in</h2>

<p>Questa è la parte che nessuno pianifica e contro cui finiscono tutti. La camera non è pronta prima delle due del pomeriggio. Il volo è atterrato alle sei del mattino. Alle otto sei in centro con una valigia.</p>

<p>I bagagli sono la metà facile, e la prima mossa è quella che si dimentica: chiedi al tuo hotel. Una camera non pronta non è la stessa cosa di un hotel che non può fare niente, e la maggior parte tiene le valigie fino al check-in senza farle pagare. In più la valigia resta dove dormirai, il che batte qualsiasi armadietto.</p>

<p>Se la risposta è no, o hai preso un appartamento senza reception, ci sono depositi a Keflavík e al BSÍ. Quelli del BSÍ sono aperti 24 ore, con 96 armadietti di quattro misure, più di quanto offrano le stazioni di queste dimensioni.</p>

<p>Le ore sono la metà migliore, perché il centro storico si attraversa in una ventina di minuti e non ha bisogno di una camera d'albergo per piacere. Un buco di quattro o cinque ore contiene la passeggiata da 2 a 2,5 ore attorno a cui è costruito questo sito e lascia ancora spazio per colazione e un caffè lungo. I bar aprono molto prima dei banconi della reception.</p>

<h2>Tre tempistiche</h2>

<h3>Se atterri presto</h3>
<p>Il Flybus, perché le sue partenze seguono gli arrivi. Bagagli sistemati, colazione in centro e cammini appena fa luce: attorno al solstizio d'inverno non succede prima delle undici circa, quindi metti in conto prima un'ora al caldo al chiuso.</p>

<h3>Se atterri tardi</h3>
<p>Ancora il Flybus: l'orario arriva a tarda sera e le ultime partenze sono agganciate agli arrivi tardivi, cosa che l'autobus di linea non fa. Controlla comunque l'ultima corsa della tua data. Se atterri dopo che i pullman hanno chiuso, il taxi non è uno sfizio: è l'unica cosa rimasta.</p>

<h3>Se riparti presto</h3>
<p>Conta all'indietro dal banco del check-in, non dal gate, e aggiungi i 45 minuti più quello che costa il prelievo in hotel. Le partenze all'alba significano pullman che lasciano la città nel cuore della notte: l'orario del Flybus le copre, l'autobus urbano no.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>L'audioguida</h2>
    <p class="lead" style="max-width:720px">Avrai ore in centro prima che qualcuno ti dia una chiave. Camminarle è ovvio. Sapere perché la città stia proprio lì e perché la passeggiata cominci da quella collina è la parte che devi portarti dietro.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="L'app TouringBee con il percorso di Reykjavik, davanti a Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">Audioguida TouringBee di Reykjavik</h3>
        <p class="meta" style="margin:0 0 10px">27 tappe · 2–2,5 ore · pagamento unico, un anno di accesso</p>
        <div class="price">9,99 €<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Entra nelle ore morte.</strong> Due o due ore e mezza, più o meno quello che hai prima del check-in</li>
          <li><strong>Funziona del tutto offline</strong> una volta scaricata, utile prima di aver risolto i dati in un paese nuovo</li>
          <li><strong>Con i tuoi tempi.</strong> Fermati per colazione e riprendi da dove eri</li>
          <li><strong>Un pagamento solo.</strong> Nessun gruppo, nessun orario, nessuna guida che ti aspetta</li>
        </ul>
        <a {BUY} style="width:100%">Fai Reykjavik con l'audioguida</a>
        <p class="meta" style="margin:12px 0 0;text-align:center">{CHECKOUTNOTE} <a href="{TBPRODUCT}" rel="noopener" data-no-widget>{OPENSHOP}</a>.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap prose">

<h2>Prezzi: transfer, bagagli e passeggiata</h2>
<table class="tbl">
  <tr><th>Voce</th><th>Costo</th></tr>
  <tr><td>Strætó 55, adulti</td><td>2.400 ISK</td></tr>
  <tr><td>Strætó 55, 12–17, over 67, disabilità</td><td>1.200 ISK</td></tr>
  <tr><td>Strætó 55, sotto i 12 anni</td><td>Gratis</td></tr>
  <tr><td>Flybus fino al BSÍ, sola andata</td><td>da 3.999 ISK</td></tr>
  <tr><td>Airport Direct</td><td>Verifica la tariffa con l'operatore</td></tr>
  <tr><td>Flybus+ con consegna in hotel</td><td>Supplemento; verifica con l'operatore</td></tr>
  <tr><td>Taxi</td><td>A tassametro, nessuna tariffa fissa pubblicata per l'aeroporto</td></tr>
  <tr><td>Deposito bagagli</td><td>In aeroporto e al BSÍ, 24 ore</td></tr>
  <tr><td>Audioguida per il buco</td><td>9,99 €, pagamento unico, un anno di accesso</td></tr>
</table>

<h2>Cinque errori</h2>
<ol>
  <li><strong>Scegliere solo sulla tariffa.</strong> Controlla prima l'ora di atterraggio e l'orario: l'opzione economica può aggiungere una lunga attesa.</li>
  <li><strong>Dare per scontato che il bus di linea copra il tuo volo.</strong> Va a orario; il Flybus va sugli arrivi.</li>
  <li><strong>Salire su un 55 senza guardare il capolinea.</strong> Alcune corse finiscono a Fjörður, non al BSÍ.</li>
  <li><strong>Pagare Flybus+ per automatismo.</strong> Se l'hotel è vicino al BSÍ e i bagagli sono leggeri, confronta prima la camminata col giro del minibus.</li>
  <li><strong>Noleggiare l'auto per il transfer.</strong> Prendila il giorno in cui esci dalla città, non il giorno in cui atterri.</li>
</ol>

<h2>Domande frequenti</h2>
<div class="faq">{FAQHTML}</div>

<h2>Continua a leggere</h2>
<ul>
  <li><a href="{ONEDAY}">Reykjavik in un giorno</a> — cosa fare delle ore che hai appena liberato</li>
  <li><a href="{TOWER}">Hallgrímskirkja e la torre</a> — biglietti, orari e il limite delle 16:45</li>
  <li><a href="{HOME}">La guida completa di Reykjavik</a> — la passeggiata, le escursioni e le stagioni</li>
  <li><a href="{GUIDES}">Tutte le guide di Reykjavik</a></li>
</ul>

<h2>In due righe</h2>
<p>Prendi il Flybus se non hai motivi per fare altrimenti: le partenze seguono i voli, in caso di ritardo il posto passa alla corsa dopo e ti lascia al margine del centro per 3.999 ISK. Prendi il 55 se l'orario coincide e conti ogni corona. Prendi l'auto solo se esci dalla città.</p>
<p>Poi sistema i bagagli e usa le ore. Se preferisci capire la città invece di aspettarci dentro, portati <a href="#audio">l'audioguida TouringBee</a>: 27 tappe, 2–2,5 ore, tutto offline.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">La camera non sarà pronta prima delle due</h2>
  <p>La passeggiata dura due ore e mezza. Il conto si fa da solo.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Inizia la passeggiata — 9,99 €</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Trova un hotel in centro</a>
  </div>
</div>

<p class="disc">Alcuni link di questa pagina sono affiliati: se prenoti passando di qui possiamo ricevere una commissione, senza costi aggiuntivi per te. Tariffe e orari verificati sui siti degli operatori a ottobre 2026; cambiano senza preavviso, controllali prima di partire. Flybus: flybus.is. Autobus di linea: straeto.is.</p>

  </div>
</section>
"""
