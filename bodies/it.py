# -*- coding: utf-8 -*-
"""IT — scritto in italiano, non tradotto. Registro: tu. Le storie restano all'audioguida."""

HEADLINE = "Reykjavik in un giorno: cosa vedere e in che ordine"
TITLE = "Reykjavik in un giorno: cosa vedere e itinerario"
DESC = ("Cosa vedere a Reykjavik in un giorno: un itinerario a piedi costruito sui due limiti "
        "della giornata, le ore di luce e l'ultima salita alla torre alle 16:45.")

FAQ = [
 ("Un giorno basta per Reykjavik?",
  "Per la città in sé sì. Il centro storico si attraversa in venti minuti e il percorso a piedi classico è "
  "di circa 5 km: una giornata lo copre con calma, pause comprese. Un giorno non basta per aggiungerci il "
  "Circolo d'Oro o la costa sud: sono giornate a sé, e gran parte di ciascuna si passa in auto."),
 ("A che ora conviene partire d'inverno?",
  "A dicembre punta a essere fuori per le 10:30 e tratta le 16:45 come un limite rigido: è l'ultima salita "
  "alla torre di Hallgrímskirkja da settembre a maggio. Tutto quello che viene dopo il buio funziona "
  "ancora — il porto, la piscina, la cena. Il panorama e le foto no."),
 ("Mi serve l'audioguida se ho già questo itinerario?",
  "Questa pagina risponde al dove e al quando: orari, prenotazioni e un piano di riserva se il tempo gira. "
  "L'audioguida risponde a che cosa stai guardando e perché è interessante: 27 storie lungo la stessa "
  "linea. L'itinerario ti serve quindi come piano della giornata, TouringBee come racconto lungo la strada."),
 ("Serve l'auto per un giorno a Reykjavik?",
  "No. La giornata in città si fa a piedi ed è pianeggiante, tranne una salita. Gli autobus Strætó coprono "
  "tutto il resto a 690 ISK a corsa. L'auto inizia a convenire quando esci dalla città."),
 ("Quanto costa un giorno a Reykjavik?",
  "Camminare non costa nulla. Le voci fisse sono piccole: 1.500 ISK per la torre e 690 ISK per l'autobus. "
  "A spostare il totale sono la laguna e la cena: insieme possono pesare più di tutto il resto."),
 ("Cosa conviene prenotare prima di partire?",
  "Per una giornata in città, soprattutto la laguna: Sky Lagoon e Blue Lagoon funzionano a fasce orarie e "
  "quelle serali, le più richieste, possono esaurirsi con largo anticipo. D'estate aggiungi l'uscita per "
  "le balene con un giorno di margine. Il resto si decide la mattina stessa."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/hero-1536.webp" width="1536" height="864" alt="Il lungomare di Reykjavik sotto un cielo islandese enorme" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reykjavik</a> › Un giorno a Reykjavik</p>
    <h1>Reykjavik in un giorno: cosa vedere, e un itinerario che regge le ore di luce</h1>
    <p class="sub">Due limiti decidono questa giornata: quante ore di luce ti toccano e le 16:45. Tutto il resto si tratta.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, autore delle audioguide TouringBee">
      <span>Di Eugene · Aggiornato il 23 settembre 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#plan">Vai al piano</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Escursioni in giornata</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">A fine dicembre il sole supera i tetti verso le 11:20 e alle tre e mezza è già sparito. L'ultima salita alla torre di Hallgrímskirkja parte alle 16:45. La tua giornata a Reykjavik sta tutta fra questi due orari.</p>

<p>Quello che segue non è quindi un elenco di monumenti, ma un orario. Il centro storico si attraversa in venti minuti e tutto il percorso a piedi è di circa 5 km. Qui il problema non sono le gambe. Sono la luce e gli orari di chiusura.</p>

<p>La giornata la puoi fare tutta con questa pagina e basta. Se vuoi anche sapere cosa c'è dietro i posti che incontri, <a href="#audio">la passeggiata audio di TouringBee</a> segue la stessa linea. Stai ancora costruendo il viaggio? Parti dalla <a href="{HOME}">nostra guida completa di Reykjavik</a>.</p>

<div class="glance">
  <h2>In breve</h2>
  <dl>
    <dt>A piedi</dt><dd>Circa 5 km, in piano tranne la salita di Skólavörðustígur</dd>
    <dt>Forma della giornata</dt><dd>Centro storico → la chiesa e la sua torre → il lungomare → acqua calda</dd>
    <dt>Orario da non mancare</dt><dd>16:45 — ultima salita alla torre, dal 1° settembre al 31 maggio</dd>
    <dt>Biglietto della torre</dt><dd>1.500 ISK adulti · 200 ISK bambini 7–16 · solo in biglietteria</dd>
    <dt>Autobus</dt><dd>690 ISK a corsa sulla rete Strætó</dd>
    <dt>Da prenotare prima</dt><dd>La laguna — l'unica prenotazione che conviene chiudere prima di partire</dd>
    <dt>Mese peggiore per improvvisare</dt><dd>Dicembre: circa quattro ore di luce utili</dd>
  </dl>
</div>

<div class="minicta">
  <h2>Fai questo percorso con l'audioguida</h2>
  <p>La stessa linea attraverso il centro, raccontata: <strong>27 tappe, 2–2,5 ore</strong>, mappa e audio offline. Ti fermi per la torre, per pranzo o per un museo e riprendi da dove eri rimasto.</p>
  <a {BUY}>Audioguida di Reykjavik — 9,99 €</a>
</div>

<h2 id="plan">Controlla prima due cose: il tramonto e la torre</h2>

<p>Il primo limite è il sole, e non fa sconti. Reykjavik si trova appena sotto il Circolo Polare Artico, quindi lo scarto fra piena estate e pieno inverno è più ampio di quasi ovunque tu sia stato prima.</p>

<table class="tbl">
  <tr><th>Mese</th><th>Luce utile</th><th>Cosa cambia per una sola giornata</th></tr>
  <tr><td>Dicembre – gennaio</td><td>4–5 ore</td><td>Un blocco all'aperto, non due. Il resto succede al buio, e va benissimo così.</td></tr>
  <tr><td>Febbraio – aprile</td><td>Cresce in fretta</td><td>Tutto il percorso con la luce, e notti ancora abbastanza scure per cercare l'aurora.</td></tr>
  <tr><td>Maggio – luglio</td><td>Praticamente tutto il giorno</td><td>Parti a mezzogiorno o alle nove di sera. Il limite della luce sparisce; è anche alta stagione.</td></tr>
  <tr><td>Agosto – novembre</td><td>Cala in fretta</td><td>Settembre e ottobre sono un buon compromesso fra ore di luce e notti abbastanza scure per l'aurora.</td></tr>
</table>

<p>Il secondo limite è la torre. Hallgrímskirkja resta l'unico punto alto del centro e, dal 1° settembre al 31 maggio, la chiesa chiude alle 17:00 con l'ultima salita alle 16:45. D'estate resta aperta fino alle 20:00 e la torre fino alle 19:45. I biglietti non si prenotano e valgono una volta sola nel giorno di acquisto, quindi non è una cosa che puoi incastrare quando ti fa comodo.</p>

<table class="tbl">
  <tr><th>Biglietto della torre</th><th>Prezzo</th></tr>
  <tr><td>Adulti</td><td>1.500 ISK</td></tr>
  <tr><td>Bambini 7–16 anni</td><td>200 ISK</td></tr>
  <tr><td>Studenti, over 67, persone con disabilità</td><td>1.300 ISK</td></tr>
</table>

<p>Funzioni religiose e concerti chiudono la chiesa ai visitatori con poco preavviso, quindi dai un'occhiata al programma del giorno prima di costruirci intorno il pomeriggio.</p>

<figure>
  <img src="{P}img/tile-hallgrimskirkja.webp" width="800" height="600" loading="lazy" alt="Hallgrímskirkja vista dal basso, con la bandiera islandese accanto alla torre">
  <figcaption>L'unica tappa della giornata con un orario di chiusura — e l'unica per cui vale la pena riorganizzare tutto.</figcaption>
</figure>

<h2>Mattina: il centro storico</h2>

<p>Parti da Arnarhóll, la collinetta verde sopra la strada del porto, dove la statua del fondatore della città guarda la baia. Il posto non l'ha scelto lui. Ha lasciato che lo scegliesse qualcos'altro, ed è una storia su cui l'audioguida si prende il suo tempo.</p>

<p>Da lì il centro storico si apre in discesa in tre strade scarse. La piazza Austurvöllur ha il parlamento su un lato. Tjörnin, il laghetto, ha il municipio piantato dentro su palafitte. In mezzo stanno i musei piccoli, compreso quello costruito attorno al muro di una casa lunga scavato sotto il marciapiede. Niente di tutto questo porta via molto tempo. Tutto questo si attraversa gratis.</p>

<p>Due note pratiche. L'Islanda va a carta in modo estremo: puoi passarci una settimana senza toccare contanti, e diversi posti non li accettano più. E l'acqua del rubinetto è ottima e gratuita ovunque, quindi una borraccia ti fa risparmiare più di quanto pensi.</p>

<h2>Mezzogiorno: la strada arcobaleno, poi la torre</h2>

<p>Skólavörðustígur sale dalla via dello shopping fino alla porta della chiesa, e il suo ultimo tratto è dipinto con strisce arcobaleno permanenti. È uno dei posti più fotografati di Reykjavik. Presto o a fine giornata ce l'hai quasi tutta per te; fra le undici e le tre d'estate no.</p>

<p>Sali sulla torre adesso, non tenerla per fine giornata. D'inverno è proprio per questo che la mattina è stata compressa. D'estate hai più margine, anche se di solito è più tranquillo presto o vicino all'ultima salita.</p>

<h2>Pranzo, e la prenotazione di cui occuparsi</h2>

<p>Si mangia su Laugavegur e nelle strade intorno. Il classico economico è la <em>pylsa</em> islandese: un hot dog fatto con un misto di agnello, maiale e manzo. Ordinalo <em>eina með öllu</em>, «uno con tutto». D'inverno una zuppa di agnello fa lo stesso lavoro. I ristoranti con servizio al tavolo sono cari sul serio: è lì che una giornata a Reykjavik smette di essere economica.</p>

<div class="ticketbox">
  <h3>Prenota la laguna prima di partire</h3>
  <p>Sky Lagoon e Blue Lagoon funzionano a fasce orarie, e quelle serali, le più richieste, possono esaurirsi con largo anticipo. Per una normale giornata in città è la prenotazione principale da chiudere prima di arrivare.</p>
  <a class="btn sm" href="{TIQETS}" {OTA}>Vedi i biglietti per la laguna</a>
  <a class="btn sm outline" href="{GYG}" {OTA}>Confronta escursioni e transfer</a>
</div>

<h2>Pomeriggio: il lungomare</h2>

<p>La seconda metà della giornata corre lungo il mare. Harpa, l'auditorium di vetro sul bordo del porto, si visita liberamente e in una giornata limpida vale cinque minuti fermo lì dentro. Più avanti, sul percorso di Sæbraut, c'è il Sun Voyager, la scultura d'acciaio che tutti fotografano come una nave vichinga. Non lo è, e il motivo vero è migliore del mito.</p>

<figure>
  <img src="{P}img/sec-sun-voyager.webp" width="1024" height="683" loading="lazy" alt="Una visitatrice passa davanti alla scultura Sun Voyager sul lungomare di Sæbraut in inverno">
  <figcaption>Fotografata di continuo e quasi sempre chiamata nel modo sbagliato.</figcaption>
</figure>

<p>Poi il porto vecchio: le barche per le balene, i ristoranti di pesce e una nave grigia della guardia costiera ormeggiata, con alle spalle scontri contro una marina molto più grande. Se arrivi fino in fondo, trovi il tumulo d'erba dove finisce il percorso audio.</p>

<p>Qui c'è l'unica vera decisione del pomeriggio. Un'uscita per le balene dal porto vecchio dura circa tre ore e si mangia tutta la luce che ti resta. D'estate ne vale la pena se sei venuto per gli animali; a dicembre è uno scambio sfavorevole, perché quelle tre ore sono tutta la tua luce.</p>

<h2>Sera: prima l'acqua calda, poi la cena</h2>

<p>Gli islandesi chiudono la giornata in acqua invece che al bar, e hai due livelli fra cui scegliere.</p>

<p>Sky Lagoon è la versione curata: affacciata sull'oceano, a quindici minuti dal centro, con un rituale in sette passaggi già compreso nel biglietto. Il pass Saman parte da circa 113 € a testa (57 € per i ragazzi); il Sér, con spogliatoi privati, da circa 136 €.</p>

<p>L'opzione locale è una piscina termale comunale: Sundhöllin in centro, Laugardalslaug per il complesso completo. Scaldate dal sottosuolo, aperte fino a tardi e a una frazione del prezzo della laguna; la tariffa adulti aggiornata è su reykjavik.is. Una regola conta più di tutte le altre: prima di entrare in acqua ci si lava a fondo, senza costume. È scritto in ogni spogliatoio e viene fatto rispettare.</p>

<h2>Tre varianti</h2>

<h3>Uno scalo, non una giornata</h3>
<p>Se sei fra due voli con sei o sette ore in città, taglia la metà sul lungomare. Autobus da Keflavík, centro storico e torre, pranzo su Laugavegur, autobus indietro. Ci sta dentro a uno scalo corto con il transfer da entrambi i lati e ti lascia comunque la vista migliore della città.</p>

<h3>Una giornata di dicembre</h3>
<p>Comprimi tutto quello che è all'aperto fra le 11:00 e le 15:30 e accetta che porto, cena e piscina avvengano al buio. Non è un ripiego: le luci del porto sull'acqua battono la versione diurna. E la lunga metà buia della giornata è la tua occasione per vedere l'aurora, se nuvolosità e attività solare vanno d'accordo. Il tratto scuro del lungomare di Sæbraut è il più comodo dalla città. Il faro di Grótta, un autobus più a ovest, è ancora più buio. Ma nessuno dei due sostituisce una vera uscita lontano dalle luci cittadine.</p>

<h3>Una giornata bagnata e di traverso</h3>
<p>Qui il tempo cambia ogni ora e il danno lo fa il vento. In una giornata storta ribalta il piano: musei e piscina in mezzo alla giornata, la passeggiata nella finestra che si apre. L'ombrello qui serve a poco: una raffica forte lo rovescia. Una giacca impermeabile con cappuccio e un berretto sono più affidabili, in qualsiasi mese.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>L'audioguida</h2>
    <p class="lead" style="max-width:720px">Vedere il percorso è una cosa. Capire perché Reykjavik sia finita proprio qui, che cosa rappresenti davvero il Sun Voyager e come un paese così piccolo sia riuscito a tenere testa ad altri molto più grandi è un'altra.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="L'app TouringBee con il percorso di Reykjavik, davanti a Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">Audioguida TouringBee di Reykjavik</h3>
        <p class="meta" style="margin:0 0 10px">27 tappe · 2–2,5 ore · un anno di accesso</p>
        <div class="rate">{STARS}<b>4,7</b> {RATELABEL}</div>
        <div class="price">9,99 €<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Funziona del tutto offline</strong> una volta scaricata — mappa e illustrazioni incluse, per strada non consumi dati</li>
          <li><strong>Con i tuoi tempi.</strong> Fermati per pranzo o per un museo e riprendi due ore dopo dallo stesso punto</li>
          <li><strong>Raccontata in prima persona</strong> da un pescatore di Reykjavik che ha tempo prima di tornare in mare</li>
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

<h2>Quanto costa la giornata</h2>
<table class="tbl">
  <tr><th>Voce</th><th>Costo</th></tr>
  <tr><td>Girare la città a piedi</td><td>Gratis</td></tr>
  <tr><td>Audioguida, pagamento unico</td><td>9,99 €</td></tr>
  <tr><td>Torre di Hallgrímskirkja, adulti</td><td>1.500 ISK</td></tr>
  <tr><td>Corsa singola Strætó</td><td>690 ISK</td></tr>
  <tr><td>Piscina comunale</td><td>Una frazione del prezzo della laguna</td></tr>
  <tr><td>Sky Lagoon, pass Saman</td><td>da circa 113 €</td></tr>
  <tr><td>Balene, circa 3 ore</td><td>Prezzo dell'operatore; il costo vero è la luce</td></tr>
</table>

<p>La città in sé non è cara. Il budget sale di colpo quando ci aggiungi la laguna, le escursioni fuori e le cene al ristorante.</p>

<h2>Cinque errori che ti costano la giornata</h2>
<ol>
  <li><strong>Lasciare la torre per ultima d'inverno.</strong> Ultima salita alle 16:45, da settembre a maggio, e i biglietti si comprano solo in loco.</li>
  <li><strong>Attaccare il Circolo d'Oro a una giornata in città.</strong> Sono otto ore in auto. Vuole una giornata sua.</li>
  <li><strong>Dare quasi tutta la luce di dicembre a una barca.</strong> Tre ore in mare quando hai quattro ore di luce.</li>
  <li><strong>Contare sull'ombrello.</strong> Il vento lo rovescia. Meglio strati, cappuccio e berretto.</li>
  <li><strong>Trattare la laguna come un posto dove si entra e basta.</strong> Va a fasce orarie, e quelle serali se ne vanno per prime.</li>
</ol>

<h2>Domande frequenti</h2>
<div class="faq">{FAQHTML}</div>

<h2>Continua a leggere</h2>
<ul>
  <li><a href="{HOME}">La guida completa di Reykjavik</a> — la passeggiata, le escursioni e le stagioni</li>
  <li><a href="{GUIDES}">Tutte le guide di Reykjavik</a> — cosa è pubblicato e cosa sta arrivando</li>
</ul>

<h2>In due righe</h2>
<p>Reykjavik dà quasi tutto quello che ha in una giornata a piedi. Le distanze non saranno mai il problema. La luce sì.</p>
<p>Quindi controlla il tramonto, non tenere la torre per la sera e fai il resto con i tuoi tempi. E se vuoi capire la città lungo la strada invece che solo guardarla, portati <a href="#audio">l'audioguida TouringBee di Reykjavik</a>: 27 tappe, 2–2,5 ore, tutto offline.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">Ventisette tappe sulla stessa linea</h2>
  <p>Questa pagina ti porta nel posto giusto all'ora giusta. L'audioguida ti dice cosa hai davanti.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Inizia la passeggiata — 9,99 €</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Trova un hotel in centro</a>
  </div>
</div>

<p class="disc">Alcuni link di questa pagina sono affiliati: se prenoti passando di qui possiamo ricevere una commissione, senza costi aggiuntivi per te. Prezzi e orari verificati sui siti degli operatori a settembre 2026; cambiano senza preavviso, controllali prima di partire. Torre: hallgrimskirkja.is. Autobus: straeto.is. Laguna: skylagoon.com.</p>

  </div>
</section>
"""
