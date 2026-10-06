# -*- coding: utf-8 -*-
"""FR — écrit en français. Registre : vous. Page logistique, deux accroches seulement."""

HEADLINE = "De l'aéroport de Keflavík à Reykjavik : quel transfert selon votre heure d'atterrissage"
TITLE = "Keflavík – Reykjavik : bus, taxi ou voiture"
DESC = ("De Keflavík à Reykjavik : les tarifs réels du Flybus, du bus public et de la voiture, et "
        "quoi faire des heures entre l'atterrissage et l'arrivée en chambre.")

FAQ = [
 ("Quel est le moyen le moins cher pour rejoindre Reykjavik depuis Keflavík ?",
  "Le bus public, la ligne Strætó 55, à 2 400 ISK pour un adulte. Les 12-17 ans, les plus de 67 ans et "
  "les personnes handicapées paient 1 200 ISK, et les moins de 12 ans voyagent gratuitement. Il circule "
  "tous les jours mais pas après chaque vol, et tous les trajets ne finissent pas à BSÍ : certains "
  "s'arrêtent à Fjörður, à Hafnarfjörður, qui n'est pas le centre de Reykjavik."),
 ("Combien de temps dure le trajet Keflavík – Reykjavik ?",
  "Environ 45 minutes en autocar pour quelque 50 km, à peu près autant en voiture. Le temps ne part pas "
  "dans le trajet. Il part dans l'attente du bus, qui démarre 35 à 45 minutes après l'atterrissage, puis "
  "dans la seconde attente, parce que votre chambre ne sera prête qu'en début d'après-midi."),
 ("Faut-il réserver le bus à l'avance ?",
  "En général non. Le Flybus vend ses billets à l'aéroport comme en ligne, et ses départs sont calés sur "
  "les vols qui arrivent. Le billet en ligne fait gagner un peu d'argent, évite la file après un long vol "
  "et se justifie sur les dates chargées. Si votre vol a du retard, l'opérateur reporte votre place sur "
  "le départ suivant plutôt que de retenir le bus."),
 ("Le Flybus dépose-t-il à mon hôtel ?",
  "Le tarif standard vous amène au terminal BSÍ. Flybus+ poursuit en minibus jusqu'aux hôtels partenaires, "
  "moyennant un supplément. Si votre hébergement est dans le vieux centre, le billet standard suivi d'une "
  "courte marche est souvent plus rapide que d'attendre la tournée du minibus."),
 ("Louer une voiture vaut-il le coup juste pour le transfert ?",
  "Pas en soi. Une route, 45 minutes, et au bout une voiture à garer dans une ville qui se traverse à "
  "pied. La location commence à avoir du sens quand l'aéroport n'est que le début d'un road trip : le "
  "Cercle d'Or, la côte sud, tout ce qui sort de la capitale. La vraie question est de savoir si vous "
  "quittez la ville."),
 ("Où laisser ses bagages avant l'enregistrement ?",
  "Commencez par demander à votre hôtel : une chambre qui n'est pas prête ne veut pas dire un hôtel qui "
  "ne peut rien faire, et la plupart gardent les valises jusqu'au check-in sans frais. Sinon, il y a des "
  "consignes à Keflavík et à BSÍ, celles de BSÍ ouvertes 24 h avec 96 casiers de quatre tailles."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/sec-old-town.webp" width="1024" height="683" alt="Un vélo garé devant une vitrine du vieux centre de Reykjavik" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reykjavik</a> › De l'aéroport de Keflavík au centre</p>
    <h1>De l'aéroport de Keflavík à Reykjavik : les options, et celle qui colle à votre heure d'atterrissage</h1>
    <p class="sub">Cinquante kilomètres, une route, quarante-cinq minutes. Le transfert est la partie facile — l'écart entre l'atterrissage et l'arrivée en chambre ne l'est pas.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, auteur des audioguides TouringBee">
      <span>Par Eugene · Mis à jour le 5 octobre 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#options">Comparer les options</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Transferts et excursions</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">Une seule route relie Keflavík à Reykjavik, et elle demande environ 45 minutes. L'autocar de l'aéroport cale ses départs sur les vols qui arrivent : il part en général 35 à 45 minutes après un atterrissage, selon un horaire qui court d'environ 3 h 30 jusqu'en fin de soirée. Rejoindre la ville est un problème résolu.</p>

<p>Ce qui ne l'est pas, c'est l'heure à laquelle vous posez. À Reykjavik, l'enregistrement se fait normalement à 14 h ou 15 h. Atterrissez avant, et vous arrivez en ville avec vos bagages, une chambre fermée et plusieurs heures à occuper — et c'est cela, pas les 50 km, qui décide du billet à acheter.</p>

<p>Cette page fait donc les deux moitiés : les options de transfert aux tarifs réellement pratiqués, puis quoi faire de l'écart. S'il vous dépose au centre avec du temps devant vous, <a href="{ONEDAY}">notre itinéraire d'un jour</a> et <a href="#audio">la balade audio TouringBee</a> sont faits pour ces heures-là. Vous préparez tout le séjour ? Partez du <a href="{HOME}">guide complet de Reykjavik</a>.</p>

<div class="glance">
  <h2>L'essentiel</h2>
  <dl>
    <dt>Distance</dt><dd>Environ 50 km de l'aéroport au centre de Reykjavik</dd>
    <dt>Trajet</dt><dd>Environ 45 minutes en autocar comme en voiture</dd>
    <dt>Flybus</dt><dd>À partir de 3 999 ISK l'aller vers le terminal BSÍ</dd>
    <dt>Bus public</dt><dd>Strætó 55 — 2 400 ISK adulte, 1 200 ISK tarif réduit, gratuit avant 12 ans</dd>
    <dt>Départs</dt><dd>Flybus cale ses départs sur les arrivées, environ de 3 h 30 à la fin de soirée ; Strætó suit un horaire fixe</dd>
    <dt>Réservation</dt><dd>Généralement pas nécessaire. Billets vendus à l'aéroport</dd>
    <dt>Bagages</dt><dd>Demandez d'abord à l'hôtel ; consignes à l'aéroport et à BSÍ</dd>
    <dt>La vraie contrainte</dt><dd>L'enregistrement à 14 h–15 h, pas le transfert</dd>
  </dl>
</div>

<div class="minicta">
  <h2>Vous atterrissez tôt ? C'est le créneau de la balade</h2>
  <p>La balade audio TouringBee, c'est <strong>27 étapes, 2 h à 2 h 30</strong> dans le vieux centre, carte et audio hors ligne. Les valises casées, les heures mortes avant l'enregistrement deviennent la meilleure partie du premier jour.</p>
  <a {BUY}>Audioguide de Reykjavik — 9,99 €</a>
</div>

<h2 id="options">Partez de votre heure d'atterrissage, pas du prix</h2>

<p>Tous les guides sur cette liaison comparent les tarifs. Or le prix n'est que la moitié du calcul : un billet bon marché cesse d'être une bonne affaire dès que son horaire vous ajoute une heure d'attente.</p>

<p>Posez plutôt la question autrement : à quelle heure les roues touchent la piste, et où dormez-vous ? Vous atterrissez à midi avec une chambre prête à 14 h, tout marche. Vous atterrissez à six heures du matin, et il vous faut un plan pour vos bagages comme pour vous-même. Le bus le moins cher ne dessert pas tous les vols : il peut donc vous coûter une heure que vous auriez préféré passer ailleurs.</p>

<table class="tbl">
  <tr><th>Option</th><th>Prix</th><th>Dépose à</th><th>À choisir quand</th></tr>
  <tr><td><strong>Flybus</strong></td><td>à partir de 3 999 ISK l'aller</td><td>Terminal BSÍ</td><td>Par défaut. Départs calés sur les arrivées ; en cas de retard votre place passe au bus suivant</td></tr>
  <tr><td><strong>Flybus+</strong></td><td>supplément</td><td>Hôtels partenaires</td><td>Beaucoup de bagages, des enfants, mauvais temps, hébergement en périphérie</td></tr>
  <tr><td><strong>Airport Direct</strong></td><td>tarif à vérifier</td><td>Terminal central, hôtels en formule premium</td><td>Le second autocar régulier — à comparer avec le Flybus</td></tr>
  <tr><td><strong>Strætó 55</strong></td><td>2 400 ISK adulte</td><td>BSÍ ou Fjörður</td><td>En journée, bagages légers, si l'horaire tombe bien</td></tr>
  <tr><td><strong>Taxi ou transfert privé</strong></td><td>Au compteur ou sur devis</td><td>Votre porte</td><td>Vous êtes trois ou quatre, ou l'heure est ingrate</td></tr>
  <tr><td><strong>Voiture de location</strong></td><td>Tarif journalier</td><td>Où vous voulez</td><td>Seulement si vous quittez la ville ensuite</td></tr>
</table>

<h2>Le Flybus, et pourquoi c'est l'option par défaut</h2>

<p>C'est l'autocar que prend la majorité, et ce qu'il vend n'est pas la vitesse mais la certitude. Les départs sont calés sur les vols qui arrivent plutôt que sur un intervalle fixe : en général 35 à 45 minutes après un atterrissage. L'horaire publié commence vers 3 h 30 et court jusqu'en fin de soirée ; pour un vol très matinal ou très tardif, vérifiez donc l'horaire de votre date plutôt que de vous fier à la règle générale.</p>

<p>Si votre vol a du retard, l'opérateur ne retient pas le bus pour vous : il vous garantit une place sur le départ suivant, sans supplément. La nuance compte, et mieux vaut la connaître avant de paniquer dans la file de la police aux frontières. Le tarif comprend deux bagages de 23 kg maximum chacun.</p>

<p>Le billet standard s'arrête à BSÍ, la gare routière en bordure sud du centre. Flybus+ ajoute un trajet en minibus jusqu'aux hôtels partenaires, moyennant supplément. Il se justifie avec des bagages lourds, des enfants, par mauvais temps, ou quand votre hébergement est en périphérie.</p>

<p>Si vous voyagez léger et logez dans le vieux centre, comparez : le minibus enchaîne une liste d'adresses, et la vôtre ne sera pas forcément la première. Regardez la distance entre BSÍ et votre hôtel, puis décidez — plutôt que de prendre le supplément par réflexe.</p>

<h2>Strætó 55, l'option économique et son piège</h2>

<p>Le bus public, c'est la ligne 55, à 2 400 ISK pour un adulte — 1 200 ISK pour les 12-17 ans, les plus de 67 ans et les personnes handicapées, gratuit avant 12 ans. Pour une famille, l'écart est réel.</p>

<p>Deux pièges. Il circule selon un horaire et non selon votre vol : un atterrissage à 5 h 30 peut donc signifier une longue attente. Et tous les trajets ne finissent pas à BSÍ : certains s'arrêtent à Fjörður, à Hafnarfjörður, une commune au sud de Reykjavik qui n'est catégoriquement pas le centre. Vérifiez la destination avant de monter, pas après.</p>

<div class="ticketbox">
  <h3>Transferts privés et excursions</h3>
  <p>À trois ou quatre, calculez le tarif du bus par personne face à un seul véhicule avant de supposer que l'autocar est moins cher. Les transferts privés et les excursions au départ de Keflavík se réservent à l'avance.</p>
  <a class="btn sm" href="{GYG}" {OTA}>Comparer les transferts</a>
  <a class="btn sm outline" href="{TIQETS}" {OTA}>Billets à Reykjavik</a>
</div>

<h2>Le taxi, et quand l'écart se resserre</h2>

<p>Les taxis islandais fonctionnent au compteur et aucun forfait aéroport n'est publié : considérez donc le taxi comme l'option chère et demandez une estimation avant de monter.</p>

<p>À trois ou quatre, demandez une estimation du moment et comparez-la au total de vos billets de bus. Le taxi se facture au véhicule, le bus au passager : l'écart se resserre donc à mesure que le groupe grandit. Cela ne rend pas le taxi bon marché, seulement moins lointain qu'il n'y paraît pour une personne seule.</p>

<h2>La location de voiture, honnêtement</h2>

<p>Pour le seul transfert, non. C'est une route droite que vous ferez une fois, et au bout une voiture à garer dans une ville qui se traverse à pied. La location commence à avoir du sens quand l'aéroport n'est que le début d'un road trip : le Cercle d'Or, la côte sud, tout ce qui sort de la capitale. Décidez sur le voyage, pas sur le transfert.</p>

<figure>
  <img src="{P}img/sec-winter-street.webp" width="1024" height="683" loading="lazy" alt="Une boutique d'angle aux couleurs vives dans une rue enneigée du centre de Reykjavik">
  <figcaption>BSÍ se trouve juste au sud de tout cela. L'essentiel du vieux centre est à quelques minutes à pied de la gare routière.</figcaption>
</figure>

<h2>L'écart entre l'atterrissage et l'enregistrement</h2>

<p>C'est la partie que personne ne prévoit et contre laquelle tout le monde bute. Votre chambre n'est prête qu'à quatorze heures. Votre vol s'est posé à six heures. Vous êtes au centre à huit heures avec une valise.</p>

<p>Les bagages sont la moitié facile, et le premier réflexe est celui qu'on oublie : demandez à votre hôtel. Une chambre qui n'est pas prête n'est pas un hôtel qui ne peut rien faire, et la plupart gardent les valises jusqu'au check-in sans frais. En prime, votre valise se retrouve là où vous allez dormir, ce qui vaut mieux qu'une consigne.</p>

<p>Si la réponse est non, ou si vous avez réservé un appartement sans réception, il y a des consignes à Keflavík et à BSÍ. Celles de BSÍ sont ouvertes 24 h sur 24, avec 96 casiers de quatre tailles, ce qui est plus que ce que proposent la plupart des gares de cette taille.</p>

<p>Les heures sont la meilleure moitié, car le vieux centre fait une vingtaine de minutes de part en part et n'a pas besoin d'une chambre d'hôtel pour être apprécié. Un creux de quatre à cinq heures absorbe la balade de 2 h à 2 h 30 autour de laquelle ce site est construit, et laisse encore la place d'un petit-déjeuner et d'un café qui s'étire. Les cafés ouvrent bien avant les comptoirs de réception.</p>

<h2>Trois cas de figure</h2>

<h3>Si vous atterrissez tôt</h3>
<p>Le Flybus, parce que ses départs suivent les arrivées. Bagages casés, petit-déjeuner au centre, et vous commencez à marcher au lever du jour — autour du solstice d'hiver, pas avant onze heures environ, prévoyez donc d'abord une heure au chaud à l'intérieur.</p>

<h3>Si vous atterrissez tard</h3>
<p>Le Flybus encore : son horaire court jusqu'en fin de soirée et les derniers départs sont calés sur les arrivées tardives, ce que ne fait pas le bus public. Vérifiez tout de même le dernier départ de votre date. Si vous posez après l'arrêt des autocars, le taxi n'est pas un luxe, c'est ce qui reste.</p>

<h3>Si vous repartez tôt</h3>
<p>Comptez à rebours depuis le comptoir d'enregistrement, pas depuis la porte d'embarquement, et ajoutez les 45 minutes plus ce que vous coûtera la prise en charge à l'hôtel. Les départs matinaux impliquent des autocars quittant la ville au milieu de la nuit : l'horaire du Flybus les couvre, le bus municipal non.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>L'audioguide</h2>
    <p class="lead" style="max-width:720px">Vous aurez des heures au centre avant qu'on vous remette une clé. Les marcher est évident. Savoir pourquoi la ville est là et pourquoi la balade commence sur cette colline précise, c'est ce qu'il faut apporter avec soi.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="L'application TouringBee affichant le parcours de Reykjavik, devant Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">Audioguide TouringBee de Reykjavik</h3>
        <p class="meta" style="margin:0 0 10px">27 étapes · 2 h à 2 h 30 · paiement unique, un an d'accès</p>
        <div class="price">9,99 €<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Pile dans les heures mortes.</strong> Deux heures à deux heures et demie, à peu près ce dont vous disposez avant l'enregistrement</li>
          <li><strong>Fonctionne entièrement hors ligne</strong> une fois téléchargé — pratique avant d'avoir réglé la question des données dans un nouveau pays</li>
          <li><strong>À votre rythme.</strong> Coupez pour le petit-déjeuner et reprenez où vous en étiez</li>
          <li><strong>Un seul paiement.</strong> Pas de groupe, pas d'horaire, pas de guide qui vous attend</li>
        </ul>
        <a {BUY} style="width:100%">Parcourir Reykjavik avec l'audioguide</a>
        <p class="meta" style="margin:12px 0 0;text-align:center">{CHECKOUTNOTE} <a href="{TBPRODUCT}" rel="noopener" data-no-widget>{OPENSHOP}</a>.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap prose">

<h2>Les prix : transfert, bagages et balade</h2>
<table class="tbl">
  <tr><th>Poste</th><th>Coût</th></tr>
  <tr><td>Strætó 55, adulte</td><td>2 400 ISK</td></tr>
  <tr><td>Strætó 55, 12-17 ans, 67+, personnes handicapées</td><td>1 200 ISK</td></tr>
  <tr><td>Strætó 55, moins de 12 ans</td><td>Gratuit</td></tr>
  <tr><td>Flybus vers BSÍ, aller simple</td><td>à partir de 3 999 ISK</td></tr>
  <tr><td>Airport Direct</td><td>Vérifiez le tarif auprès de l'opérateur</td></tr>
  <tr><td>Flybus+ avec dépose à l'hôtel</td><td>Supplément ; voir l'opérateur</td></tr>
  <tr><td>Taxi</td><td>Au compteur, aucun forfait aéroport publié</td></tr>
  <tr><td>Consigne à bagages</td><td>À l'aéroport et à BSÍ, 24 h sur 24</td></tr>
  <tr><td>Audioguide pour le creux</td><td>9,99 €, paiement unique, un an d'accès</td></tr>
</table>

<h2>Cinq erreurs</h2>
<ol>
  <li><strong>Choisir sur le seul tarif.</strong> Vérifiez d'abord votre heure d'atterrissage et l'horaire : l'option économique peut ajouter une longue attente.</li>
  <li><strong>Croire que le bus public dessert votre vol.</strong> Il suit un horaire ; le Flybus suit les arrivées.</li>
  <li><strong>Monter dans un 55 sans vérifier la destination.</strong> Certains trajets finissent à Fjörður, pas à BSÍ.</li>
  <li><strong>Payer Flybus+ par réflexe.</strong> Si votre hôtel est près de BSÍ et vos bagages légers, comparez d'abord la marche et la tournée du minibus.</li>
  <li><strong>Louer une voiture pour le transfert.</strong> Louez-la le jour où vous quittez la ville, pas le jour où vous atterrissez.</li>
</ol>

<h2>Questions fréquentes</h2>
<div class="faq">{FAQHTML}</div>

<h2>Pour aller plus loin</h2>
<ul>
  <li><a href="{ONEDAY}">Reykjavik en un jour</a> — quoi faire des heures que vous venez de libérer</li>
  <li><a href="{TOWER}">Hallgrímskirkja et sa tour</a> — billets, horaires et la limite de 16 h 45</li>
  <li><a href="{HOME}">Le guide complet de Reykjavik</a> — le parcours, les excursions et les saisons</li>
  <li><a href="{GUIDES}">Tous les guides de Reykjavik</a></li>
</ul>

<h2>En résumé</h2>
<p>Prenez le Flybus sauf raison contraire : ses départs suivent les vols, votre place passe au bus suivant en cas de retard, et il vous dépose en bordure du centre pour 3 999 ISK. Prenez le 55 si l'horaire tombe bien et que vous comptez chaque couronne. Prenez une voiture seulement si vous quittez la ville.</p>
<p>Ensuite, casez les bagages et utilisez les heures. Si vous préférez comprendre la ville plutôt que d'y attendre, emportez <a href="#audio">l'audioguide TouringBee</a> : 27 étapes, 2 h à 2 h 30, entièrement hors ligne.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">Votre chambre ne sera prête qu'à quatorze heures</h2>
  <p>La balade dure deux heures et demie. Le calcul se fait tout seul.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Commencer la balade — 9,99 €</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Trouver un hôtel dans le centre</a>
  </div>
</div>

<p class="disc">Certains liens de cette page sont des liens d'affiliation : si vous réservez via ces liens, nous pouvons percevoir une commission, sans surcoût pour vous. Tarifs et horaires vérifiés sur les sites des opérateurs en octobre 2026 ; ils changent sans préavis, vérifiez avant de partir. Flybus : flybus.is. Bus public : straeto.is.</p>

  </div>
</section>
"""
