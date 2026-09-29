# -*- coding: utf-8 -*-
"""IT — scritto in italiano. Registro: tu. Le storie restano all'audioguida."""

HEADLINE = "Torre di Hallgrímskirkja: biglietti, orari e quando salire"
TITLE = "Hallgrímskirkja: biglietti, orari e quando salire"
DESC = ("Biglietti e orari della torre di Hallgrímskirkja, il limite delle 16:45 d'inverno, cosa si "
        "vede davvero da lassù e quando la chiesa è chiusa ai visitatori.")

FAQ = [
 ("Quanto costa salire sulla Hallgrímskirkja?",
  "1.500 ISK per un adulto e 200 ISK per un bambino dai 7 ai 16 anni. Studenti e persone con disabilità "
  "pagano 1.300 ISK; dai 67 anni c'è una riduzione, ma la chiesa non pubblica l'importo. Sconto del 10% "
  "da dieci persone in su, gratis per le scolaresche fino a 16 anni. Entrare in chiesa non costa nulla: "
  "si paga solo la torre."),
 ("Si possono prenotare online i biglietti per la torre?",
  "No. La chiesa dice chiaramente che non è possibile prenotare la torre in anticipo. I biglietti si "
  "comprano nel negozio della chiesa, sulla sinistra appena entri nell'atrio, e valgono solo per il "
  "giorno dell'acquisto. Quello che trovi online come «biglietto per Hallgrímskirkja» è altro: un tour "
  "che si ferma davanti, non l'accesso alla torre."),
 ("A che ora chiude la torre di Hallgrímskirkja?",
  "Dal 1° settembre al 31 maggio la chiesa chiude alle 17:00 e l'ultima salita è alle 16:45. Dal 1° "
  "giugno al 31 agosto è aperta fino alle 20:00, con la torre fino alle 19:45. Funzioni religiose, "
  "cerimonie e concerti chiudono la chiesa ai visitatori anche in altri momenti: controlla il programma "
  "del giorno prima di costruirci intorno il pomeriggio."),
 ("Ne vale la pena?",
  "Per il panorama sì: è l'unico punto alto del centro storico ed è l'unico da cui vedi i tetti colorati "
  "dall'alto, a picco. Venti minuti e 1.500 ISK sono uno scambio onesto. Se cerchi una vista più ampia "
  "su tutta la baia e le montagne, Perlan fa meglio, ma costa di più e si porta via mezza giornata."),
 ("Si sale in ascensore fino in cima?",
  "Quasi. Un ascensore copre gran parte dell'altezza, poi resta una breve rampa di scale fino alla "
  "terrazza. La terrazza è chiusa, con aperture sui quattro lati invece che all'aria aperta, quindi "
  "funziona con qualsiasi tempo. È piccola, e la chiesa la chiude quando si affolla."),
 ("Si può visitare la chiesa gratis?",
  "Sì. Hallgrímskirkja è una parrocchia in attività: entrare a vedere la navata e l'organo non costa "
  "nulla negli orari di apertura. Paghi solo se vuoi salire. Le funzioni sono aperte a tutti, ma mentre "
  "si svolgono l'edificio non è una tappa turistica."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/tile-hallgrimskirkja.webp" width="800" height="600" alt="Hallgrímskirkja vista dal basso, con la bandiera islandese accanto alla torre" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reykjavik</a> › Hallgrímskirkja</p>
    <h1>Hallgrímskirkja: biglietti, orari e quando salire sulla torre</h1>
    <p class="sub">La chiesa è gratis. La torre no, non si prenota, e d'inverno smette di far salire alle 16:45.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, autore delle audioguide TouringBee">
      <span>Di Eugene · Aggiornato il 29 settembre 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#hours">Orari e prezzi</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Tour a Reykjavik</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">Due cose colgono di sorpresa chi arriva a Hallgrímskirkja. Il biglietto della torre non si compra in anticipo, da nessuno e a nessun prezzo. E da settembre a maggio l'ultima salita parte alle 16:45 — a dicembre, cioè ben prima che la maggior parte dei visitatori abbia finito di pranzare.</p>

<p>Il resto è semplice. La chiesa si visita gratis, sta in cima alla strada che saresti salito comunque, e tutta la tappa dura una mezz'ora abbondante con la fila.</p>

<p>Questa pagina parla della torre: quanto costa, quando è aperta, quando chiude per le funzioni e se il panorama vale i soldi rispetto alle alternative. Fa coppia con <a href="{ONEDAY}">il nostro itinerario di un giorno a Reykjavik</a>, dove questa torre è il punto fisso attorno a cui si piega tutto il resto. Se invece vuoi la storia dell'edificio e non la logistica, ci pensa <a href="#audio">la passeggiata audio di TouringBee</a>.</p>

<div class="glance">
  <h2>In breve</h2>
  <dl>
    <dt>Ingresso in chiesa</dt><dd>Gratuito</dd>
    <dt>Biglietto torre</dt><dd>1.500 ISK adulti · 200 ISK bambini 7–16 · 1.300 ISK studenti e persone con disabilità</dd>
    <dt>Prenotazione</dt><dd>Impossibile. Si compra nel negozio della chiesa, solo per la giornata</dd>
    <dt>Orario invernale</dt><dd>1 set – 31 mag: chiesa 10:00–17:00, ultima salita 16:45</dd>
    <dt>Orario estivo</dt><dd>1 giu – 31 ago: chiesa 09:00–20:00, torre fino alle 19:45</dd>
    <dt>Quanto dura</dt><dd>Circa 30 minuti, fila compresa</dd>
    <dt>Come si sale</dt><dd>Ascensore quasi fino in cima, poi una breve rampa di scale</dd>
    <dt>Altezza</dt><dd>73 m secondo la chiesa stessa: l'edificio più alto della città</dd>
  </dl>
</div>

<div class="minicta">
  <h2>La chiesa è una tappa di una passeggiata più lunga</h2>
  <p>La passeggiata audio di TouringBee comprende Hallgrímskirkja e <strong>altre 26 tappe</strong> nel centro storico: <strong>2–2,5 ore</strong>, mappa e audio offline, con i tuoi tempi.</p>
  <a {BUY}>Audioguida di Reykjavik — 9,99 €</a>
</div>

<h2 id="hours">Cosa si paga e cosa no</h2>

<p>Hallgrímskirkja è una parrocchia luterana in attività, non un museo, e l'ingresso è libero negli orari di apertura. Puoi sederti nella navata, guardare l'organo e uscire senza pagare niente. Il biglietto riguarda solo la torre.</p>

<table class="tbl">
  <tr><th>Biglietto torre</th><th>Prezzo</th></tr>
  <tr><td>Adulti</td><td>1.500 ISK</td></tr>
  <tr><td>Bambini 7–16 anni</td><td>200 ISK</td></tr>
  <tr><td>Studenti, persone con disabilità (con documento)</td><td>1.300 ISK</td></tr>
  <tr><td>Over 67</td><td>Tariffa ridotta; la chiesa non pubblica l'importo</td></tr>
  <tr><td>Gruppi da 10 persone</td><td>10% di sconto</td></tr>
  <tr><td>Scolaresche, alunni fino a 16 anni</td><td>Gratis</td></tr>
</table>

<p>Online troverai altri numeri. Il portale turistico della stessa Reykjavik riportava ancora 1.400 ISK e ultimo ingresso alle 16:30 quando abbiamo controllato, a settembre 2026. Molte guide poi ricopiano un vecchio listino che la chiesa ha lasciato sul proprio sito, sopra quello in vigore. I prezzi qui sopra sono quelli che applica adesso.</p>

<h2>Gli orari, e il limite</h2>

<table class="tbl">
  <tr><th>Stagione</th><th>Chiesa</th><th>Ultima salita</th></tr>
  <tr><td>1 settembre – 31 maggio</td><td>10:00 – 17:00</td><td>16:45</td></tr>
  <tr><td>1 giugno – 31 agosto</td><td>09:00 – 20:00</td><td>19:45</td></tr>
</table>

<p>È attorno a quelle 16:45 che si organizza la giornata, perché non si spostano con la luce. A fine dicembre il sole se n'è andato comunque alle tre e mezza: torre e luce utile finiscono insieme. A febbraio invece alle 16:45 c'è ancora chiaro, e la gente perde la salita proprio per questo, perché il cielo non sembra quello dell'orario di chiusura.</p>

<p>Le altre chiusure sono meno prevedibili. La chiesa chiude ai visitatori durante funzioni, matrimoni, funerali e concerti, e lo dice senza giri di parole: gli orari possono cambiare. Chiude anche la terrazza durante certi eventi, e prima del previsto quando si affolla. La domenica mattina è il modo più affidabile per arrivare e trovare chiuso.</p>

<h2>Comprare il biglietto</h2>

<p>Il negozio è sulla sinistra appena entri nell'atrio. È l'unico posto in cui il biglietto della torre esiste. La formula della chiesa è questa: non è possibile prenotare la torre in anticipo. Niente vendita online, niente fasce orarie, niente salta-fila.</p>

<p>Quello che vedi pubblicizzato online come biglietto per Hallgrímskirkja è altro: un tour che si ferma davanti, o una city card che forse te lo rimborsa. Il biglietto vale una volta sola, nel giorno d'acquisto: non puoi comprarlo la mattina e usarlo al tramonto.</p>

<h2>La salita</h2>

<p>Un ascensore copre quasi tutta l'altezza, una breve rampa di scale fa il resto. La terrazza è chiusa, con aperture ad arco sui quattro lati invece che all'aria aperta: per questo funziona anche in una giornata in cui giù in strada il vento sta smontando gli ombrelli.</p>

<p>La terrazza è piccola. A luglio la parte lenta è la fila da basso, non la salita, e la chiesa preferisce far aspettare piuttosto che ammassare gente lassù. Un quarto d'ora è più che sufficiente.</p>

<figure>
  <img src="{P}img/tile-rainbow-street.webp" width="800" height="600" loading="lazy" alt="Skólavörðustígur dipinta a strisce arcobaleno, in salita verso Hallgrímskirkja">
  <figcaption>La strada che sali per arrivare fin qui. Dalla terrazza la ridiscendi con lo sguardo.</figcaption>
</figure>

<h2>Cosa si vede davvero</h2>

<p>Guarda a ovest e hai l'immagine per cui vengono tutti. Skólavörðustígur scende a strisce arcobaleno, poi i tetti di lamiera colorata del centro storico si accatastano fino al porto, con la baia e il monte Esja dietro. È questa vista a giustificare il biglietto. Ed è anche l'unica cosa che Perlan non può darti: sta troppo fuori per guardare i tetti dall'alto.</p>

<p>A sud e a est c'è la Reykjavik residenziale e, in una giornata limpida, la penisola di Reykjanes. A nord il porto e l'acqua. Non c'è un lato sbagliato, ma se hai un solo momento di cielo pulito e una macchina fotografica, prendi ovest.</p>

<p>Qui conta più la luce che l'orario. D'estate il sole basso di fine giornata rende meglio di mezzogiorno. D'inverno la finestra è comunque stretta, e un cielo coperto appiattisce i tetti in un grigio unico: vale la pena saperlo prima di spendere 1.500 ISK nel pomeriggio sbagliato.</p>

<h2>Dentro, che non costa niente</h2>

<p>La navata contiene 1.200 persone ed è volutamente spoglia: bianca, altissima, quasi senza decorazioni. In fondo c'è l'organo Klais, costruito a Bonn e completato nel 1992: 5.275 canne, 15 metri di altezza, circa 25 tonnellate. C'è anche un secondo organo più piccolo, della danese Frobenius, ricostruito e riconsacrato nel 2024. Sul grande vengono a registrare organisti da tutto il mondo; se entrando trovi una prova in corso, fermati.</p>

<p>Il cantiere è stato lungo. Guðjón Samúelsson, architetto di Stato, vinse l'incarico negli anni Trenta e non fece in tempo a vederlo finito. I lavori andarono dal 1945 alla consacrazione del 1986, e nel frattempo la parrocchia usò la cripta per 26 anni. La facciata di solito viene descritta come colonne di basalto; la chiesa stessa la paragona alla roccia colonnare, alle montagne e ai ghiacciai islandesi.</p>

<p>Quel paragone è la versione che danno tutte le guide. Perché un architetto di Stato abbia passato la carriera a cercare uno stile specificamente islandese è una storia più lunga, e l'audioguida si prende il suo tempo per raccontarla.</p>

<p>Un'ultima cosa, fuori. La statua sul piazzale stava qui prima della chiesa, e non è stata l'Islanda a decidere di metterla lì.</p>

<h2>Torre o Perlan?</h2>

<table class="tbl">
  <tr><th></th><th>Hallgrímskirkja</th><th>Perlan</th></tr>
  <tr><td>Dove</td><td>In cima al centro storico, a piedi</td><td>Su una collina fuori centro, bus o taxi</td></tr>
  <tr><td>La vista</td><td>A picco sui tetti colorati e sulla strada arcobaleno</td><td>Panorama ampio: baia, città, montagne</td></tr>
  <tr><td>Terrazza</td><td>Chiusa, piccola</td><td>Terrazza aperta, più le mostre</td></tr>
  <tr><td>Biglietto</td><td>1.500 ISK, solo in loco</td><td>Di più; controlla il prezzo aggiornato, cambia</td></tr>
  <tr><td>Tempo</td><td>30 minuti</td><td>Mezza giornata con lo spostamento</td></tr>
</table>

<p>In una sola giornata in città la torre vince già solo sul tempo. Con due giorni di cui uno piovoso, Perlan è l'edificio migliore da giornata storta, perché dentro c'è qualcosa da fare.</p>

<div class="ticketbox">
  <h3>La torre non si prenota — quello che c'è intorno sì</h3>
  <p>Per Hallgrímskirkja in sé non si prenota nulla. Per quello che la circonda sì: Perlan, le lagune e i tour guidati che passano davanti alla chiesa vendono le fasce orarie in anticipo.</p>
  <a class="btn sm" href="{TIQETS}" {OTA}>Biglietti per Reykjavik</a>
  <a class="btn sm outline" href="{GYG}" {OTA}>Confronta i tour</a>
</div>

<h2>Tre situazioni</h2>

<h3>Hai qualche ora fra due voli</h3>
<p>La torre è il modo migliore di usare uno scalo breve: venti minuti a piedi dalla fermata del bus in centro, e tutta la città in una volta. Sali prima lì, poi scendi verso il centro storico, non il contrario.</p>

<h3>È domenica</h3>
<p>Le funzioni del mattino chiudono la chiesa ai visitatori. Vai dopo pranzo: d'inverno ti resta comunque margine prima delle 16:45.</p>

<h3>Il tempo è girato</h3>
<p>Non cancellare la torre. La terrazza è chiusa e il vento che rovina la strada lassù non dà fastidio. Il problema vero sono le nuvole basse: se dal marciapiede non vedi l'Esja, non vedrai granché nemmeno da 73 metri.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>L'audioguida</h2>
    <p class="lead" style="max-width:720px">Dalla terrazza vedi che aspetto ha Reykjavik. Perché la città sia cresciuta proprio lì, cosa ci faccia quella statua sul piazzale e cosa stesse davvero costruendo l'architetto sono domande diverse.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="L'app TouringBee con il percorso di Reykjavik, davanti a Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">Audioguida TouringBee di Reykjavik</h3>
        <p class="meta" style="margin:0 0 10px">27 tappe · 2–2,5 ore · un anno di accesso</p>
        <div class="rate">{STARS}<b>4,7</b> {RATELABEL}</div>
        <div class="price">9,99 €<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Hallgrímskirkja è una delle 27 tappe</strong>: il percorso va dalla collina del fondatore al porto vecchio</li>
          <li><strong>Funziona del tutto offline</strong> una volta scaricata, mappa e illustrazioni incluse</li>
          <li><strong>Con i tuoi tempi.</strong> Fermati per salire sulla torre e riprendi da dove eri</li>
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

<h2>Cinque errori</h2>
<ol>
  <li><strong>Cercare i biglietti online.</strong> Non esistono. Il negozio dentro la chiesa è l'unico venditore.</li>
  <li><strong>Lasciare la torre al tardo pomeriggio fra settembre e maggio.</strong> Ultima salita alle 16:45, qualunque cosa faccia il cielo.</li>
  <li><strong>Presentarsi di domenica mattina.</strong> Le funzioni chiudono la chiesa ai visitatori.</li>
  <li><strong>Fidarsi di un prezzo letto su un portale.</strong> Diversi mostrano ancora 1.400 ISK e le 16:30.</li>
  <li><strong>Salire con le nuvole basse.</strong> Se l'Esja non si vede dalla strada, tieni il biglietto per domani.</li>
</ol>

<h2>Domande frequenti</h2>
<div class="faq">{FAQHTML}</div>

<h2>Continua a leggere</h2>
<ul>
  <li><a href="{ONEDAY}">Reykjavik in un giorno</a> — l'itinerario di cui questa torre è il perno</li>
  <li><a href="{HOME}">La guida completa di Reykjavik</a> — la passeggiata, le escursioni e le stagioni</li>
  <li><a href="{GUIDES}">Tutte le guide di Reykjavik</a> — cosa è pubblicato e cosa sta arrivando</li>
</ul>

<h2>In due righe</h2>
<p>Entra gratis, paga 1.500 ISK al negozio se vuoi il panorama, e fallo prima delle 16:45 d'inverno. Guarda a ovest per i tetti. Mezz'ora, ed è la migliore mezz'ora che il centro storico metta in vendita.</p>
<p>E se preferisci capire cosa hai sotto invece di limitarti a guardarlo, portati <a href="#audio">l'audioguida TouringBee</a>: 27 tappe per il centro, questa compresa, tutto offline.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">La chiesa è la tappa uno di ventisette</h2>
  <p>Questa pagina ti porta sulla torre all'ora giusta. L'audioguida ti dice cos'è la città sotto di te.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Inizia la passeggiata — 9,99 €</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Trova un hotel in centro</a>
  </div>
</div>

<p class="disc">Alcuni link di questa pagina sono affiliati: se prenoti passando di qui possiamo ricevere una commissione, senza costi aggiuntivi per te. Prezzi e orari verificati su hallgrimskirkja.is a settembre 2026; cambiano senza preavviso, controllali prima di partire.</p>

  </div>
</section>
"""
