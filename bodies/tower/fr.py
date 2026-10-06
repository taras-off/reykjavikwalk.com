# -*- coding: utf-8 -*-
"""FR — écrit en français. Registre : vous. Les histoires restent à l'audioguide."""

HEADLINE = "Tour de Hallgrímskirkja : billets, horaires et quand monter"
TITLE = "Hallgrímskirkja : billets, horaires et quand monter"
DESC = ("Billets et horaires de la tour de Hallgrímskirkja, la limite de 16 h 45 en hiver, ce que "
        "la vue montre vraiment et quand l'église est fermée aux visiteurs.")

FAQ = [
 ("Combien coûte la montée à Hallgrímskirkja ?",
  "1 500 ISK pour un adulte et 200 ISK pour un enfant de 7 à 16 ans. Les étudiants et les personnes "
  "handicapées paient 1 300 ISK ; les plus de 67 ans ont un tarif réduit, mais l'église n'en publie pas "
  "le montant. Remise de 10 % à partir de dix personnes, gratuité pour les groupes scolaires de moins de "
  "16 ans. Entrer dans l'église ne coûte rien : seule la tour est payante."),
 ("Peut-on réserver les billets de la tour en ligne ?",
  "Non. L'église indique clairement qu'il n'est pas possible de réserver la tour à l'avance. Les billets "
  "se vendent à la boutique de l'église, à gauche en entrant dans le hall, et ne valent que pour le jour "
  "de l'achat. Ce qui se vend en ligne sous le nom de Hallgrímskirkja est une visite guidée autour de "
  "l'église, pas l'accès à la tour."),
 ("À quelle heure ferme la tour de Hallgrímskirkja ?",
  "Du 1er septembre au 31 mai, l'église ferme à 17 h et la dernière montée part à 16 h 45. Du 1er juin au "
  "31 août, ouverture jusqu'à 20 h et tour jusqu'à 19 h 45. Offices, cérémonies et concerts ferment aussi "
  "l'église aux visiteurs : regardez le programme du jour avant de bâtir votre après-midi autour."),
 ("La tour vaut-elle le détour ?",
  "Pour la vue, oui : c'est le seul point haut du vieux centre, et le seul d'où l'on voit les toits "
  "colorés à la verticale. Vingt minutes et 1 500 ISK, c'est un bon échange. Pour un panorama plus large "
  "sur toute la baie et les montagnes, Perlan fait mieux, mais coûte plus cher et prend une demi-journée."),
 ("Monte-t-on en ascenseur jusqu'en haut ?",
  "Presque. Un ascenseur couvre l'essentiel de la hauteur, puis il reste une courte volée de marches "
  "jusqu'à la plateforme. Celle-ci est fermée, avec des ouvertures sur les quatre côtés plutôt qu'à l'air "
  "libre : elle fonctionne donc par tous les temps. Elle est petite, et l'église la ferme quand il y a "
  "trop de monde."),
 ("Peut-on visiter l'église gratuitement ?",
  "Oui. Hallgrímskirkja est une paroisse en activité : entrer voir la nef et l'orgue ne coûte rien "
  "pendant les heures d'ouverture. Vous ne payez que pour monter. Les offices sont ouverts à tous, mais "
  "pendant ceux-ci le bâtiment n'est pas une étape touristique."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/tile-hallgrimskirkja.webp" width="800" height="600" alt="Hallgrímskirkja vue d'en bas, le drapeau islandais flottant à côté du clocher" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reykjavik</a> › Hallgrímskirkja</p>
    <h1>Hallgrímskirkja : billets, horaires et le bon moment pour monter</h1>
    <p class="sub">L'église est gratuite. La tour ne l'est pas, elle ne se réserve pas, et en hiver elle cesse de laisser monter à 16 h 45.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, auteur des audioguides TouringBee">
      <span>Par Eugene · Mis à jour le 29 septembre 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#hours">Horaires et tarifs</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Visites à Reykjavik</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">Deux choses prennent les visiteurs de court à Hallgrímskirkja. Le billet de la tour ne s'achète pas à l'avance, nulle part, à aucun prix. Et de septembre à mai, la dernière montée part à 16 h 45 — en décembre, bien avant que la plupart des gens aient fini de déjeuner.</p>

<p>Le reste est simple. L'église est gratuite, elle se trouve en haut de la rue que vous alliez monter de toute façon, et l'arrêt complet prend une demi-heure, file d'attente comprise.</p>

<p>Cette page traite de la tour : le tarif, les horaires, les fermetures pour offices, et si la vue vaut son prix face aux alternatives. Elle complète <a href="{ONEDAY}">notre itinéraire d'un jour à Reykjavik</a>, où cette tour est le point fixe autour duquel tout le reste s'organise. Pour l'histoire du bâtiment plutôt que la logistique, c'est <a href="#audio">la balade audio TouringBee</a> qui s'en charge.</p>

<div class="glance">
  <h2>L'essentiel</h2>
  <dl>
    <dt>Entrée de l'église</dt><dd>Gratuite</dd>
    <dt>Billet de la tour</dt><dd>1 500 ISK adulte · 200 ISK enfant 7–16 ans · 1 300 ISK étudiant ou personne handicapée</dd>
    <dt>Réservation</dt><dd>Impossible. Vente à la boutique de l'église, pour le jour même</dd>
    <dt>Horaires d'hiver</dt><dd>1er sept. – 31 mai : église 10 h–17 h, dernière montée 16 h 45</dd>
    <dt>Horaires d'été</dt><dd>1er juin – 31 août : église 9 h–20 h, tour jusqu'à 19 h 45</dd>
    <dt>Durée</dt><dd>Environ 30 minutes, attente comprise</dd>
    <dt>Accès</dt><dd>Ascenseur presque jusqu'en haut, puis une courte volée de marches</dd>
    <dt>Hauteur</dt><dd>73 m selon l'église — le plus haut bâtiment de la ville</dd>
  </dl>
</div>

<div class="minicta">
  <h2>L'église n'est qu'une étape d'une balade plus longue</h2>
  <p>La balade audio TouringBee passe par Hallgrímskirkja et <strong>26 autres étapes</strong> du vieux centre — <strong>2 h à 2 h 30</strong>, carte et audio hors ligne, à votre rythme.</p>
  <a {BUY}>Audioguide de Reykjavik — 9,99 €</a>
</div>

<h2 id="hours">Ce qui est payant et ce qui ne l'est pas</h2>

<p>Hallgrímskirkja est une paroisse luthérienne en activité, pas un musée, et l'entrée est libre pendant les heures d'ouverture. Vous pouvez vous asseoir dans la nef, regarder l'orgue et repartir sans rien payer. Le billet ne concerne que la tour.</p>

<table class="tbl">
  <tr><th>Billet de la tour</th><th>Tarif</th></tr>
  <tr><td>Adultes</td><td>1 500 ISK</td></tr>
  <tr><td>Enfants 7–16 ans</td><td>200 ISK</td></tr>
  <tr><td>Étudiants, personnes handicapées (sur justificatif)</td><td>1 300 ISK</td></tr>
  <tr><td>Plus de 67 ans</td><td>Tarif réduit ; le montant n'est pas publié par l'église</td></tr>
  <tr><td>Groupes de 10 personnes et plus</td><td>−10 %</td></tr>
  <tr><td>Groupes scolaires, élèves de 16 ans et moins</td><td>Gratuit</td></tr>
</table>

<p>Vous trouverez d'autres chiffres en ligne. L'office de tourisme de Reykjavik affichait encore 1 400 ISK et une dernière entrée à 16 h 30 lors de notre vérification en septembre 2026. Beaucoup de guides recopient aussi une ancienne grille tarifaire que l'église a laissée sur son propre site, au-dessus de la grille en vigueur. Les tarifs ci-dessus sont ceux pratiqués aujourd'hui.</p>

<h2>Les horaires, et la limite</h2>

<table class="tbl">
  <tr><th>Saison</th><th>Église</th><th>Dernière montée</th></tr>
  <tr><td>1er septembre – 31 mai</td><td>10 h – 17 h</td><td>16 h 45</td></tr>
  <tr><td>1er juin – 31 août</td><td>9 h – 20 h</td><td>19 h 45</td></tr>
</table>

<p>C'est autour de ce 16 h 45 qu'il faut organiser la journée, car il ne suit pas la lumière. Fin décembre, le soleil a de toute façon disparu à 15 h 30 : la tour et le jour s'arrêtent ensemble. En février, il fait encore clair à 16 h 45, et les gens ratent la montée parce que le ciel n'a pas l'air d'une fin de journée.</p>

<p>Les autres fermetures sont moins prévisibles. L'église ferme aux visiteurs pendant les offices, les mariages, les enterrements et les concerts, et elle le dit sans détour : les horaires sont susceptibles de changer. Elle ferme aussi la plateforme lors de certains événements, et plus tôt que prévu quand il y a foule. Le dimanche matin est le moyen le plus sûr d'arriver devant une porte close.</p>

<h2>Acheter le billet</h2>

<p>La boutique se trouve à gauche en entrant dans le hall. C'est le seul endroit où le billet existe. L'église le formule ainsi : il n'est pas possible de réserver la tour à l'avance. Pas de vente en ligne, pas de créneaux, pas de coupe-file.</p>

<p>Ce que vous voyez annoncé en ligne comme un billet pour Hallgrímskirkja est autre chose : une visite guidée qui s'arrête devant, ou un pass urbain qui vous remboursera peut-être. Le billet vaut une fois, le jour de l'achat : impossible de l'acheter le matin pour l'utiliser au crépuscule.</p>

<h2>La montée</h2>

<p>Un ascenseur couvre l'essentiel de la hauteur, une courte volée de marches fait le reste. La plateforme est fermée, avec des ouvertures en arc sur les quatre côtés plutôt qu'à l'air libre — c'est pourquoi elle reste agréable un jour où le vent démonte les parapluies en bas.</p>

<p>Elle est petite. En juillet, c'est la file au rez-de-chaussée qui prend du temps, pas la montée, et l'église fait patienter plutôt que d'entasser les gens là-haut. Quinze minutes suffisent largement.</p>

<figure>
  <img src="{P}img/tile-rainbow-street.webp" width="800" height="600" loading="lazy" alt="Skólavörðustígur peinte en bandes arc-en-ciel, montant vers Hallgrímskirkja">
  <figcaption>La rue que vous montez pour arriver ici. Depuis la plateforme, vous la redescendez du regard.</figcaption>
</figure>

<h2>Ce que l'on voit vraiment</h2>

<p>Regardez vers l'ouest et vous avez l'image pour laquelle tout le monde vient. Skólavörðustígur descend en bandes arc-en-ciel, puis les toits de tôle colorés du vieux centre s'empilent jusqu'au port, avec la baie et le mont Esja derrière. C'est cette vue qui justifie le billet. C'est aussi la seule chose que Perlan ne peut pas offrir : il est trop loin pour surplomber les toits.</p>

<p>Au sud et à l'est, Reykjavik résidentielle et, par temps clair, la péninsule de Reykjanes. Au nord, le port et l'eau. Aucun côté n'est raté, mais si vous n'avez qu'un instant de ciel dégagé et un appareil photo, prenez l'ouest.</p>

<p>La lumière compte plus que l'heure. En été, le soleil rasant de fin de journée rend mieux que midi. En hiver, la fenêtre est étroite de toute façon, et un ciel couvert aplatit les toits en gris — bon à savoir avant de dépenser 1 500 ISK le mauvais après-midi.</p>

<h2>À l'intérieur, sans payer</h2>

<p>La nef accueille 1 200 personnes et reste volontairement nue : blanche, haute, presque sans décor. Au fond se dresse l'orgue Klais, construit à Bonn et achevé en 1992 — 5 275 tuyaux, 15 mètres de haut, environ 25 tonnes. Il existe un second orgue, plus petit, signé Frobenius au Danemark, reconstruit et reconsacré en 2024. Des organistes viennent du monde entier enregistrer sur le grand ; si une répétition tourne quand vous entrez, restez.</p>

<p>Le chantier fut long. Guðjón Samúelsson, architecte d'État, a remporté la commande dans les années trente et n'a pas vu l'achèvement. Les travaux ont couru de 1945 à la consécration de 1986, et la paroisse a utilisé la crypte pendant 26 ans entre-temps. On décrit en général la façade comme des orgues basaltiques ; l'église, elle, la compare aux roches en colonnes, aux montagnes et aux glaciers islandais.</p>

<p>Cette comparaison est la version que donnent tous les guides. Pourquoi un architecte d'État a passé sa carrière à chercher un style proprement islandais est une histoire plus longue, et l'audioguide prend le temps de la raconter.</p>

<p>Une dernière chose, dehors. La statue sur le parvis était là avant l'église, et ce n'est pas l'Islande qui a eu l'idée de l'y mettre.</p>

<h2>La tour ou Perlan ?</h2>

<table class="tbl">
  <tr><th></th><th>Hallgrímskirkja</th><th>Perlan</th></tr>
  <tr><td>Où</td><td>En haut du vieux centre, à pied</td><td>Sur une colline hors du centre, bus ou taxi</td></tr>
  <tr><td>La vue</td><td>À la verticale sur les toits colorés et la rue arc-en-ciel</td><td>Panorama large : baie, ville, montagnes</td></tr>
  <tr><td>Plateforme</td><td>Fermée, petite</td><td>Terrasse ouverte, plus des expositions</td></tr>
  <tr><td>Billet</td><td>1 500 ISK, sur place uniquement</td><td>Plus cher ; vérifiez le tarif, il change</td></tr>
  <tr><td>Temps</td><td>30 minutes</td><td>Une demi-journée avec le trajet</td></tr>
</table>

<p>Sur une seule journée en ville, la tour gagne rien que sur le temps. Avec deux jours dont un pluvieux, Perlan est le meilleur bâtiment de mauvais temps, parce qu'il y a de quoi s'occuper à l'intérieur.</p>

<div class="ticketbox">
  <h3>La tour ne se réserve pas — le reste, si</h3>
  <p>Rien ne se réserve pour Hallgrímskirkja même. Tout autour, si : Perlan, les lagons et les visites guidées qui passent devant l'église vendent leurs créneaux à l'avance.</p>
  <a class="btn sm" href="{TIQETS}" {OTA}>Billets pour Reykjavik</a>
  <a class="btn sm outline" href="{GYG}" {OTA}>Comparer les visites</a>
</div>

<h2>Trois situations</h2>

<h3>Vous avez quelques heures entre deux vols</h3>
<p>La tour est le meilleur usage d'une escale courte : vingt minutes à pied depuis l'arrêt de bus du centre, et toute la ville d'un coup. Montez-y d'abord, puis redescendez vers le vieux centre plutôt que l'inverse.</p>

<h3>C'est un dimanche</h3>
<p>Les offices du matin ferment l'église aux visiteurs. Venez après le déjeuner : en hiver, cela laisse encore de la marge avant 16 h 45.</p>

<h3>Le temps a tourné</h3>
<p>Ne renoncez pas pour autant. La plateforme est fermée et le vent qui gâche la rue ne vous gêne pas là-haut. Le vrai problème, c'est le plafond bas : si vous ne voyez pas l'Esja depuis le trottoir, vous ne verrez pas grand-chose depuis 73 mètres.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>L'audioguide</h2>
    <p class="lead" style="max-width:720px">Depuis la plateforme, vous voyez à quoi ressemble Reykjavik. Pourquoi la ville a poussé exactement là, ce que fait cette statue sur le parvis et ce que l'architecte construisait vraiment sont d'autres questions.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="L'application TouringBee affichant le parcours de Reykjavik, devant Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">Audioguide TouringBee de Reykjavik</h3>
        <p class="meta" style="margin:0 0 10px">27 étapes · 2 h à 2 h 30 · un an d'accès</p>
        <div class="rate">{STARS}<b>4,7</b> {RATELABEL}</div>
        <div class="price">9,99 €<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Hallgrímskirkja est l'une des 27 étapes</strong> — le parcours va de la colline du fondateur au vieux port</li>
          <li><strong>Fonctionne entièrement hors ligne</strong> une fois téléchargé, carte et illustrations comprises</li>
          <li><strong>À votre rythme.</strong> Coupez pour monter à la tour et reprenez où vous en étiez</li>
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

<h2>Cinq erreurs</h2>
<ol>
  <li><strong>Chercher des billets en ligne.</strong> Ils n'existent pas. La boutique de l'église est le seul point de vente.</li>
  <li><strong>Garder la tour pour la fin d'après-midi entre septembre et mai.</strong> 16 h 45, quoi qu'en dise le ciel.</li>
  <li><strong>Arriver un dimanche matin.</strong> Les offices ferment l'église aux visiteurs.</li>
  <li><strong>Faire confiance à un tarif lu sur un annuaire.</strong> Plusieurs affichent encore 1 400 ISK et 16 h 30.</li>
  <li><strong>Monter sous un plafond bas.</strong> Si l'Esja est invisible depuis la rue, gardez le billet pour demain.</li>
</ol>

<h2>Questions fréquentes</h2>
<div class="faq">{FAQHTML}</div>

<h2>Pour aller plus loin</h2>
<ul>
  <li><a href="{ONEDAY}">Reykjavik en un jour</a> — l'itinéraire dont cette tour est le pivot</li>
  <li><a href="{KEF}">De l'aéroport de Keflavík au centre</a> — comment arriver avant tout le reste</li>
  <li><a href="{HOME}">Le guide complet de Reykjavik</a> — le parcours, les excursions et les saisons</li>
  <li><a href="{GUIDES}">Tous les guides de Reykjavik</a> — ce qui est publié et ce qui arrive</li>
</ul>

<h2>En résumé</h2>
<p>Entrez gratuitement, payez 1 500 ISK à la boutique si vous voulez la vue, et faites-le avant 16 h 45 en hiver. Regardez vers l'ouest pour les toits. Une demi-heure, et c'est la meilleure demi-heure que vende le vieux centre.</p>
<p>Et si vous préférez comprendre ce que vous surplombez plutôt que seulement le regarder, emportez <a href="#audio">l'audioguide TouringBee</a> : 27 étapes à travers le centre, celle-ci comprise, entièrement hors ligne.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">L'église est la première de vingt-sept étapes</h2>
  <p>Cette page vous fait monter à la bonne heure. L'audioguide vous dit ce qu'est la ville en dessous.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Commencer la balade — 9,99 €</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Trouver un hôtel dans le centre</a>
  </div>
</div>

<p class="disc">Certains liens de cette page sont des liens d'affiliation : si vous réservez via ces liens, nous pouvons percevoir une commission, sans surcoût pour vous. Tarifs et horaires vérifiés sur hallgrimskirkja.is en septembre 2026 ; ils changent sans préavis, vérifiez avant de partir.</p>

  </div>
</section>
"""
