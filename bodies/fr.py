# -*- coding: utf-8 -*-
"""FR — écrit en français, pas traduit. Registre : vous. Les histoires restent à l'audioguide."""

HEADLINE = "Reykjavik en un jour : que voir et dans quel ordre"
TITLE = "Reykjavik en un jour : que voir et itinéraire à pied"
DESC = ("Que voir à Reykjavik en un jour : un itinéraire à pied calé sur les deux contraintes "
        "de la journée, la lumière et la montée au clocher de 16 h 45.")

FAQ = [
 ("Une journée suffit-elle pour Reykjavik ?",
  "Pour la ville elle-même, oui. Le vieux centre se traverse en vingt minutes et le parcours à pied "
  "classique fait environ 5 km : une journée le couvre largement, pauses comprises. Une journée ne suffit "
  "pas pour y ajouter le Cercle d'Or ou la côte sud, qui demandent chacun une journée entière, passée en "
  "grande partie en voiture."),
 ("À quelle heure commencer en hiver ?",
  "En décembre, visez 10 h 30 pour être dehors, et tenez 16 h 45 comme limite absolue : c'est la dernière "
  "montée au clocher de Hallgrímskirkja de septembre à mai. Tout ce qui vient après la nuit tombée reste "
  "faisable — le port, la piscine, le dîner. Le panorama et les photos, non."),
 ("L'audioguide sert à quoi si j'ai déjà cet itinéraire ?",
  "Cette page répond à la question où et quand : les horaires, les réservations, le plan de repli quand il "
  "pleut. L'audioguide répond à la question de ce que vous avez sous les yeux et pourquoi c'est intéressant "
  "— 27 histoires sur la même ligne. L'itinéraire sert donc de plan de journée, et TouringBee de récit en "
  "chemin."),
 ("Faut-il une voiture pour une journée à Reykjavik ?",
  "Non. La journée en ville se fait à pied, sur du plat, sauf une montée. Les bus Strætó couvrent le reste "
  "pour 690 ISK le trajet. La voiture ne devient rentable qu'une fois sorti de la ville."),
 ("Combien coûte une journée à Reykjavik ?",
  "Marcher ne coûte rien. Les frais fixes sont modestes : 1 500 ISK pour le clocher et 690 ISK le trajet en "
  "bus. Ce qui fait grimper le total, c'est le lagon et le dîner — à eux deux, ils peuvent dépasser tout le "
  "reste."),
 ("Que faut-il réserver avant de partir ?",
  "Pour une journée en ville, surtout le lagon : le Sky Lagoon comme le Blue Lagoon fonctionnent par "
  "créneaux, et les créneaux du soir, très demandés, peuvent partir longtemps à l'avance. En été, ajoutez "
  "la sortie d'observation des baleines la veille. Le reste se décide le matin même."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/hero-1536.webp" width="1536" height="864" alt="Le front de mer de Reykjavik sous un grand ciel islandais" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reykjavik</a> › Un jour à Reykjavik</p>
    <h1>Reykjavik en un jour : que voir, et un itinéraire qui tient malgré la lumière</h1>
    <p class="sub">Deux contraintes décident de cette journée : les heures de jour dont vous disposez, et 16 h 45. Tout le reste se négocie.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, auteur des audioguides TouringBee">
      <span>Par Eugene · Mis à jour le 23 septembre 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#plan">Aller au plan</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Excursions à la journée</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">Fin décembre, le soleil passe au-dessus des toits vers 11 h 20 et a déjà disparu à 15 h 30. La dernière montée au clocher de Hallgrímskirkja part à 16 h 45. Votre journée à Reykjavik tient tout entière entre ces deux horaires.</p>

<p>Ce qui suit n'est donc pas une liste de sites, mais un horaire. Le vieux centre se traverse en vingt minutes et le parcours complet fait environ 5 km. Ici, ce ne sont pas les jambes qui lâchent. C'est la lumière, ou une porte fermée depuis un quart d'heure.</p>

<p>Vous pouvez faire toute la journée avec cette seule page. Si vous voulez aussi savoir ce qui se cache derrière les lieux traversés, <a href="#audio">la balade audio TouringBee</a> suit la même ligne. Vous préparez le reste du séjour ? Commencez par <a href="{HOME}">notre guide complet de Reykjavik</a>.</p>

<div class="glance">
  <h2>L'essentiel</h2>
  <dl>
    <dt>À pied</dt><dd>Environ 5 km, plat sauf la montée de Skólavörðustígur</dd>
    <dt>Déroulé</dt><dd>Vieux centre → l'église et son clocher → le front de mer → l'eau chaude</dd>
    <dt>Horaire à ne pas rater</dt><dd>16 h 45 — dernière montée au clocher, du 1er septembre au 31 mai</dd>
    <dt>Billet du clocher</dt><dd>1 500 ISK adulte · 200 ISK enfant 7–16 ans · vendu sur place uniquement</dd>
    <dt>Bus</dt><dd>690 ISK le trajet sur le réseau Strætó</dd>
    <dt>À réserver</dt><dd>Le lagon — la seule réservation vraiment à prendre avant de partir</dd>
    <dt>Le mois le plus difficile à improviser</dt><dd>Décembre : environ quatre heures de jour exploitables</dd>
  </dl>
</div>

<div class="minicta">
  <h2>Faites ce parcours avec l'audioguide</h2>
  <p>La même ligne à travers le centre, racontée : <strong>27 étapes, 2 h à 2 h 30</strong>, carte et audio hors ligne. Vous coupez pour le clocher, le déjeuner ou un musée, et vous reprenez là où vous en étiez.</p>
  <a {BUY}>Audioguide de Reykjavik — 9,99 €</a>
</div>

<h2 id="plan">Vérifiez d'abord deux choses : le coucher du soleil et le clocher</h2>

<p>La première contrainte, c'est le soleil, et il ne fait pas de cadeau. Reykjavik se trouve juste sous le cercle polaire : l'écart entre le plein été et le plein hiver dépasse tout ce que la plupart des voyageurs ont connu ailleurs.</p>

<table class="tbl">
  <tr><th>Mois</th><th>Jour exploitable</th><th>Ce que ça change pour une journée</th></tr>
  <tr><td>Décembre – janvier</td><td>4 à 5 heures</td><td>Un seul bloc en extérieur, pas deux. Le reste se passe de nuit, et ce n'est pas un problème.</td></tr>
  <tr><td>Février – avril</td><td>La lumière revient vite</td><td>Tout le parcours de jour, et des nuits encore assez noires pour guetter les aurores.</td></tr>
  <tr><td>Mai – juillet</td><td>Quasiment 24 h sur 24</td><td>Départ à midi ou à neuf heures du soir. La contrainte disparaît ; c'est aussi la haute saison.</td></tr>
  <tr><td>Août – novembre</td><td>La lumière repart vite</td><td>Septembre et octobre offrent un bon compromis entre longueur des journées et nuits assez noires pour les aurores.</td></tr>
</table>

<p>La seconde contrainte, c'est le clocher. Hallgrímskirkja reste le seul point haut du centre, et du 1er septembre au 31 mai l'église ferme à 17 h, dernière montée à 16 h 45. En été, ouverture jusqu'à 20 h et clocher jusqu'à 19 h 45. Les billets ne se réservent pas et ne valent que pour le jour de l'achat : impossible donc de caler la visite quand ça vous arrange.</p>

<table class="tbl">
  <tr><th>Billet du clocher</th><th>Tarif</th></tr>
  <tr><td>Adulte</td><td>1 500 ISK</td></tr>
  <tr><td>Enfant 7–16 ans</td><td>200 ISK</td></tr>
  <tr><td>Étudiants, seniors 67+, personnes handicapées</td><td>1 300 ISK</td></tr>
</table>

<p>Offices et concerts ferment l'église aux visiteurs sans grand préavis : jetez un œil au programme du jour avant de bâtir votre après-midi autour du clocher.</p>

<figure>
  <img src="{P}img/tile-hallgrimskirkja.webp" width="800" height="600" loading="lazy" alt="Hallgrímskirkja vue d'en bas, le drapeau islandais flottant à côté du clocher">
  <figcaption>La seule étape de la journée avec une heure de fermeture — et celle autour de laquelle il vaut la peine de tout réorganiser.</figcaption>
</figure>

<h2>Matin : le vieux centre</h2>

<p>Commencez par Arnarhóll, la petite colline verte au-dessus de la route du port, où la statue du fondateur de la ville regarde la baie. Il n'a pas choisi l'endroit lui-même. Il a laissé quelque chose d'autre choisir à sa place, et c'est une histoire que l'audioguide prend le temps de raconter.</p>

<p>De là, le vieux centre se déroule vers le bas en trois rues à peine. La place Austurvöllur a le parlement d'un côté. Tjörnin, l'étang, porte l'hôtel de ville sur pilotis. Entre les deux se glissent de petits musées, dont celui construit autour d'un mur de maison longue mis au jour sous le trottoir. Rien de tout cela ne prend longtemps. Tout cela se traverse gratuitement.</p>

<p>Deux remarques pratiques. L'Islande fonctionne à la carte bancaire jusqu'à l'excès : on peut y passer une semaine sans toucher un billet, et plusieurs endroits n'acceptent plus les espèces. Et l'eau du robinet est excellente et gratuite partout, donc une gourde vous fait économiser plus que vous ne le croyez.</p>

<h2>Midi : la rue arc-en-ciel, puis le clocher</h2>

<p>Skólavörðustígur monte de la rue commerçante jusqu'à la porte de l'église, et son dernier pâté de maisons est peint en bandes arc-en-ciel permanentes. C'est l'un des endroits les plus photographiés de Reykjavik. Tôt le matin ou en fin de journée, vous l'avez presque pour vous ; entre onze heures et trois heures en été, non.</p>

<p>Montez au clocher maintenant, ne le gardez pas pour la fin de journée. En hiver, c'est précisément pour cela que la matinée a été resserrée. En été vous avez plus de marge, même si c'est en général plus calme tôt ou près de la dernière montée.</p>

<h2>Déjeuner, et la réservation à ne pas oublier</h2>

<p>On mange sur Laugavegur et dans les rues qui la bordent. Le classique bon marché, c'est la <em>pylsa</em> islandaise : un hot-dog préparé à partir d'un mélange d'agneau, de porc et de bœuf. Demandez <em>eina með öllu</em>, « avec tout ». En hiver, une soupe d'agneau fait le même office. Les restaurants avec service sont réellement chers : c'est là qu'une journée à Reykjavik cesse d'être bon marché.</p>

<div class="ticketbox">
  <h3>Réservez le lagon avant de décoller</h3>
  <p>Le Sky Lagoon comme le Blue Lagoon fonctionnent par créneaux, et les créneaux du soir, très demandés, peuvent partir longtemps à l'avance. Pour une journée en ville classique, c'est la réservation principale à prendre avant d'arriver.</p>
  <a class="btn sm" href="{TIQETS}" {OTA}>Voir les billets pour le lagon</a>
  <a class="btn sm outline" href="{GYG}" {OTA}>Comparer excursions et transferts</a>
</div>

<h2>Après-midi : le front de mer</h2>

<p>La seconde moitié de la journée longe la mer. Harpa, la salle de concert de verre au bord du port, est libre d'accès et mérite cinq minutes d'arrêt à l'intérieur par temps clair. Plus loin sur le chemin de Sæbraut se dresse le Sun Voyager, la sculpture d'acier que tout le monde photographie comme un drakkar. Ce n'en est pas un, et la vraie raison vaut mieux que le mythe.</p>

<figure>
  <img src="{P}img/sec-sun-voyager.webp" width="1024" height="683" loading="lazy" alt="Un visiteur passe devant la sculpture Sun Voyager sur le front de mer de Sæbraut en hiver">
  <figcaption>Photographiée sans arrêt, et presque toujours mal identifiée.</figcaption>
</figure>

<p>Puis le vieux port : les bateaux d'observation des baleines, les restaurants de poisson et un navire gris des garde-côtes à quai, avec un passé militaire face à une marine bien plus grande. Allez jusqu'au bout et vous tombez sur le tertre herbeux où se termine le parcours audio.</p>

<p>C'est ici que se joue la seule vraie décision de l'après-midi. Une sortie d'observation des baleines depuis le vieux port prend environ trois heures et avale tout ce qui reste de jour. Cela vaut le coup en été si vous êtes venu pour la faune ; c'est un mauvais calcul en décembre, quand ces trois heures représentent toute votre lumière.</p>

<h2>Soirée : d'abord l'eau chaude, ensuite le dîner</h2>

<p>Les Islandais finissent la journée dans l'eau plutôt qu'au bar, et vous avez le choix entre deux gammes.</p>

<p>Le Sky Lagoon, c'est la version soignée : au bord de l'océan, à quinze minutes du centre, avec un rituel en sept étapes compris dans le billet. Le forfait Saman démarre autour de 113 € par adulte (57 € pour les jeunes), le forfait Sér, avec vestiaires privés, autour de 136 €.</p>

<p>L'option locale, c'est la piscine municipale géothermale : Sundhöllin en centre-ville, Laugardalslaug pour le complexe complet. Chauffées par le sol, ouvertes tard, à une fraction du prix d'un lagon ; le tarif adulte en vigueur figure sur reykjavik.is. Une règle compte plus que les autres : on se douche soigneusement, sans maillot, avant d'entrer dans l'eau. C'est affiché dans chaque vestiaire, et c'est appliqué.</p>

<h2>Trois variantes</h2>

<h3>Une escale, pas une journée</h3>
<p>Si vous avez six ou sept heures entre deux vols, laissez tomber la partie front de mer. Bus depuis Keflavík, vieux centre et clocher, déjeuner sur Laugavegur, bus retour. Cela tient dans une escale courte, transferts compris, et vous offre quand même la meilleure vue de la ville.</p>

<h3>Une journée de décembre</h3>
<p>Comprimez tout l'extérieur entre 11 h et 15 h 30 et acceptez que le port, le dîner et la piscine se passent de nuit. Ce n'est pas une dégradation : les lumières du port sur l'eau valent mieux que la version diurne. Et la longue moitié sombre de la journée est votre chance de voir une aurore, si la couverture nuageuse et l'activité solaire s'y prêtent. Le tronçon sombre du front de mer de Sæbraut est le plus simple depuis la ville. Le phare de Grótta, à un trajet de bus vers l'ouest, est plus noir encore. Mais ni l'un ni l'autre ne remplace une vraie sortie loin des lumières urbaines.</p>

<h3>Un jour de pluie et de vent de travers</h3>
<p>Le temps change d'heure en heure et c'est le vent qui fait les dégâts. Un mauvais jour, inversez le plan : musées et piscine au milieu de la journée, la marche dans la fenêtre qui s'ouvre. Le parapluie ne sert pas à grand-chose ici : une bonne rafale le retourne. Une veste imperméable à capuche et un bonnet sont plus fiables, quel que soit le mois.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>L'audioguide</h2>
    <p class="lead" style="max-width:720px">Voir le parcours est une chose. Comprendre pourquoi Reykjavik s'est installée précisément là, ce que représente vraiment le Sun Voyager et comment un pays aussi petit a pu tenir tête à bien plus fort que lui, c'en est une autre.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="L'application TouringBee affichant le parcours de Reykjavik, devant Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">Audioguide TouringBee de Reykjavik</h3>
        <p class="meta" style="margin:0 0 10px">27 étapes · 2 h à 2 h 30 · un an d'accès</p>
        <div class="rate">{STARS}<b>4,7</b> {RATELABEL}</div>
        <div class="price">9,99 €<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Fonctionne entièrement hors ligne</strong> une fois téléchargé — carte et illustrations comprises, aucune donnée nécessaire en chemin</li>
          <li><strong>À votre rythme.</strong> Coupez pour déjeuner ou visiter un musée et reprenez au même endroit deux heures plus tard</li>
          <li><strong>Raconté par un personnage</strong> — un pêcheur de Reykjavik qui a du temps avant de reprendre la mer</li>
          <li><strong>Un seul paiement.</strong> Pas de groupe, pas d'horaire, pas de guide qui vous attend</li>
        </ul>
        <a {BUY} style="width:100%">Parcourir Reykjavik avec l'audioguide</a>
        <p class="meta" style="margin:12px 0 0;text-align:center">{CHECKOUTNOTE} <a href="{TBPRODUCT}" rel="noopener">{OPENSHOP}</a>.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap prose">

<h2>Ce que coûte la journée</h2>
<table class="tbl">
  <tr><th>Poste</th><th>Coût</th></tr>
  <tr><td>Parcourir la ville à pied</td><td>Gratuit</td></tr>
  <tr><td>Audioguide, paiement unique</td><td>9,99 €</td></tr>
  <tr><td>Clocher de Hallgrímskirkja, adulte</td><td>1 500 ISK</td></tr>
  <tr><td>Trajet simple Strætó</td><td>690 ISK</td></tr>
  <tr><td>Piscine municipale</td><td>Une fraction du prix d'un lagon</td></tr>
  <tr><td>Sky Lagoon, forfait Saman</td><td>à partir d'environ 113 €</td></tr>
  <tr><td>Observation des baleines, ~3 h</td><td>Tarif selon l'opérateur ; le vrai coût, c'est la lumière</td></tr>
</table>

<p>La ville en elle-même n'est pas chère. Le budget grimpe nettement dès qu'on ajoute un lagon, des excursions hors de la ville et des dîners au restaurant.</p>

<h2>Cinq erreurs qui coûtent la journée</h2>
<ol>
  <li><strong>Garder le clocher pour la fin en hiver.</strong> Dernière montée à 16 h 45, de septembre à mai, et billets vendus sur place uniquement.</li>
  <li><strong>Ajouter le Cercle d'Or à une journée en ville.</strong> C'est huit heures de route. Il lui faut sa propre journée.</li>
  <li><strong>Consacrer l'essentiel du jour de décembre à un bateau.</strong> Trois heures en mer quand vous avez quatre heures de lumière.</li>
  <li><strong>Compter sur un parapluie.</strong> Le vent le retourne. Des couches, une capuche et un bonnet à la place.</li>
  <li><strong>Prendre le lagon pour un endroit où l'on entre librement.</strong> Ce sont des créneaux, et ceux du soir partent en premier.</li>
</ol>

<h2>Questions fréquentes</h2>
<div class="faq">{FAQHTML}</div>

<h2>Pour aller plus loin</h2>
<ul>
  <li><a href="{HOME}">Le guide complet de Reykjavik</a> — le parcours, les excursions et les saisons</li>
  <li><a href="{GUIDES}">Tous les guides de Reykjavik</a> — ce qui est publié et ce qui arrive</li>
</ul>

<h2>En résumé</h2>
<p>Reykjavik donne presque tout ce qu'elle a en une journée de marche. Les distances ne seront jamais le problème. La lumière, si.</p>
<p>Vérifiez donc l'heure du coucher du soleil, ne gardez pas le clocher pour le soir, et faites le reste à votre rythme. Et si vous voulez comprendre la ville en chemin plutôt que simplement la regarder, emportez <a href="#audio">l'audioguide TouringBee de Reykjavik</a> : 27 étapes, 2 h à 2 h 30, entièrement hors ligne.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">Vingt-sept étapes sur la même ligne</h2>
  <p>Cette page vous amène au bon endroit à la bonne heure. L'audioguide vous dit ce que vous avez devant vous.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Commencer la balade — 9,99 €</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Trouver un hôtel dans le centre</a>
  </div>
</div>

<p class="disc">Certains liens de cette page sont des liens d'affiliation : si vous réservez via ces liens, nous pouvons percevoir une commission, sans surcoût pour vous. Tarifs et horaires vérifiés sur les sites des opérateurs en septembre 2026 ; ils changent sans préavis, vérifiez avant de partir. Clocher : hallgrimskirkja.is. Bus : straeto.is. Lagon : skylagoon.com.</p>

  </div>
</section>
"""
