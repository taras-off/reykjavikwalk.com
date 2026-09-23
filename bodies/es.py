# -*- coding: utf-8 -*-
"""ES — escrito en español, no traducido. Registro: tú. Las historias se quedan en la audioguía."""

HEADLINE = "Reikiavik en un día: qué ver y en qué orden"
TITLE = "Reikiavik en un día: qué ver y ruta a pie"
DESC = ("Qué ver en Reikiavik en un día: una ruta a pie montada sobre los dos límites que deciden la "
        "jornada, las horas de luz y la última subida a la torre a las 16:45.")

FAQ = [
 ("¿Un día es suficiente para Reikiavik?",
  "Para la ciudad en sí, sí. El casco antiguo se cruza en veinte minutos y la ruta a pie clásica son unos "
  "5 km, así que un día la cubre de sobra con paradas. Un día no da para añadir el Círculo Dorado ni la "
  "costa sur: son jornadas aparte, y la mayor parte de cada una se pasa en carretera."),
 ("¿A qué hora conviene empezar en invierno?",
  "En diciembre intenta estar en la calle a las 10:30 y trata las 16:45 como un límite firme: es la última "
  "subida a la torre de Hallgrímskirkja de septiembre a mayo. Todo lo que viene después del anochecer sigue "
  "funcionando — el puerto, la piscina, la cena. El mirador y las fotos, no."),
 ("¿Necesito la audioguía si ya tengo esta ruta?",
  "Esta página responde al dónde y al cuándo: horarios, reservas y un plan alternativo si el tiempo se "
  "estropea. La audioguía responde a qué estás mirando exactamente y por qué tiene interés: 27 historias "
  "sobre la misma línea. Así que la ruta te sirve de plan del día y TouringBee de relato por el camino."),
 ("¿Hace falta coche para un día en Reikiavik?",
  "No. El día urbano se hace a pie y es llano salvo por una subida. Los autobuses Strætó cubren lo que "
  "queda más lejos por 690 ISK el trayecto. El coche empieza a compensar cuando sales de la ciudad."),
 ("¿Cuánto cuesta un día en Reikiavik?",
  "Caminar no cuesta nada. Los gastos fijos son pequeños: 1.500 ISK la torre y 690 ISK el autobús. Lo que "
  "mueve el total son la laguna y la cena — entre las dos pueden superar todo lo demás junto."),
 ("¿Qué conviene reservar antes de llegar?",
  "Para un día urbano normal, sobre todo la laguna: Sky Lagoon y Blue Lagoon funcionan por franjas horarias "
  "y las de la tarde, que son las más buscadas, pueden agotarse con antelación. En verano, añade la salida "
  "para ver ballenas con un día de margen. El resto se decide por la mañana."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/hero-1536.webp" width="1536" height="864" alt="El paseo marítimo de Reikiavik bajo un cielo islandés enorme" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reikiavik</a> › Un día en Reikiavik</p>
    <h1>Reikiavik en un día: qué ver, y una ruta que aguanta las horas de luz</h1>
    <p class="sub">Dos límites deciden este día: cuántas horas de luz te tocan y las 16:45. Todo lo demás se negocia.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, autor de las audioguías de TouringBee">
      <span>Por Eugene · Actualizado el 23 de septiembre de 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#plan">Ir al plan</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Excursiones de un día</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">A finales de diciembre el sol asoma por encima de los tejados hacia las 11:20 y a las tres y media ya se ha ido. La última subida a la torre de Hallgrímskirkja sale a las 16:45. Tu día entero en Reikiavik cabe entre esas dos horas.</p>

<p>Por eso lo que viene no es una lista de monumentos, sino un horario. El casco antiguo se cruza en veinte minutos y la ruta completa son unos 5 km. Aquí las piernas no son el problema. Lo son la luz y los horarios de cierre.</p>

<p>Puedes hacer el día entero solo con esta página. Y si además quieres saber qué hay detrás de los sitios por los que pasas, <a href="#audio">el paseo con audio de TouringBee</a> sigue la misma línea. ¿Estás montando el viaje completo? Empieza por <a href="{HOME}">nuestra guía completa de Reikiavik</a>.</p>

<div class="glance">
  <h2>En resumen</h2>
  <dl>
    <dt>A pie</dt><dd>Unos 5 km, llano salvo la subida por Skólavörðustígur</dd>
    <dt>Forma del día</dt><dd>Casco antiguo → la iglesia y su torre → el paseo marítimo → agua caliente</dd>
    <dt>Hora límite</dt><dd>16:45 — última subida a la torre, del 1 de septiembre al 31 de mayo</dd>
    <dt>Entrada a la torre</dt><dd>1.500 ISK adultos · 200 ISK niños de 7 a 16 · solo en taquilla</dd>
    <dt>Autobús</dt><dd>690 ISK el trayecto en Strætó</dd>
    <dt>Reservar antes</dt><dd>La laguna — la reserva que sí conviene dejar hecha antes de viajar</dd>
    <dt>Peor mes para improvisar</dt><dd>Diciembre: unas cuatro horas de luz aprovechables</dd>
  </dl>
</div>

<div class="minicta">
  <h2>Haz esta ruta con la audioguía</h2>
  <p>La misma línea por el centro, contada: <strong>27 paradas, 2–2,5 horas</strong>, mapa y audio sin conexión. Párate para la torre, para comer o para un museo y retómala donde la dejaste.</p>
  <a {BUY}>Audioguía de Reikiavik — 9,99 €</a>
</div>

<h2 id="plan">Comprueba primero dos cosas: la puesta de sol y la torre</h2>

<p>El primer límite es el sol, y no perdona. Reikiavik está justo por debajo del Círculo Polar Ártico, así que la diferencia entre pleno verano y pleno invierno es mayor que en casi cualquier sitio al que hayas viajado antes.</p>

<table class="tbl">
  <tr><th>Mes</th><th>Luz aprovechable</th><th>Qué significa para un solo día</th></tr>
  <tr><td>Diciembre – enero</td><td>4–5 horas</td><td>Un bloque al aire libre, no dos. El resto pasa de noche, y no pasa nada.</td></tr>
  <tr><td>Febrero – abril</td><td>Sube rápido</td><td>La ruta entera con luz, y noches todavía bastante oscuras para buscar auroras.</td></tr>
  <tr><td>Mayo – julio</td><td>Prácticamente todo el día</td><td>Puedes salir a mediodía o a las nueve de la noche. El límite de luz desaparece; también es temporada alta.</td></tr>
  <tr><td>Agosto – noviembre</td><td>Baja rápido</td><td>Septiembre y octubre son un buen equilibrio entre horas de luz y noches lo bastante oscuras para la aurora.</td></tr>
</table>

<p>El segundo límite es la torre. Hallgrímskirkja sigue siendo el único mirador alto del centro y, del 1 de septiembre al 31 de mayo, la iglesia cierra a las 17:00, con la última subida a las 16:45. En verano abre hasta las 20:00 y la torre hasta las 19:45. Las entradas no se reservan y valen una sola vez el día de la compra, así que no es algo que puedas encajar cuando te venga bien.</p>

<table class="tbl">
  <tr><th>Entrada a la torre</th><th>Precio</th></tr>
  <tr><td>Adultos</td><td>1.500 ISK</td></tr>
  <tr><td>Niños de 7 a 16 años</td><td>200 ISK</td></tr>
  <tr><td>Estudiantes, mayores de 67, personas con discapacidad</td><td>1.300 ISK</td></tr>
</table>

<p>Los oficios y los conciertos cierran la iglesia al público sin mucho aviso, así que echa un vistazo al programa del día antes de montar la tarde alrededor de la torre.</p>

<figure>
  <img src="{P}img/tile-hallgrimskirkja.webp" width="800" height="600" loading="lazy" alt="Hallgrímskirkja vista desde abajo, con la bandera islandesa ondeando junto a la torre">
  <figcaption>La única parada del día con hora de cierre — y la única por la que merece la pena reorganizarlo todo.</figcaption>
</figure>

<h2>Mañana: el casco antiguo</h2>

<p>Empieza en Arnarhóll, la loma verde sobre la carretera del puerto, donde la estatua del fundador de la ciudad mira hacia la bahía. El sitio no lo eligió él. Dejó que lo eligiera otra cosa, y esa es una historia que la audioguía se toma con calma.</p>

<p>Desde ahí el casco antiguo se despliega cuesta abajo en unas tres calles. La plaza de Austurvöllur tiene el parlamento a un lado. Tjörnin, el estanque, tiene el ayuntamiento metido dentro sobre pilotes. Entre medias quedan los museos pequeños, incluido el que está construido alrededor de un muro de casa vikinga excavado bajo la acera. Nada de esto lleva mucho tiempo. Todo esto se recorre gratis.</p>

<p>Dos apuntes prácticos. Islandia funciona con tarjeta hasta un punto extremo: puedes pasar una semana sin tocar efectivo, y hay sitios que ya no lo aceptan. Y el agua del grifo es excelente y gratis en todas partes, así que una botella reutilizable ahorra más de lo que parece.</p>

<h2>Mediodía: la calle del arcoíris y luego la torre</h2>

<p>Skólavörðustígur sube desde la calle comercial hasta la puerta de la iglesia, y su último tramo está pintado con franjas de arcoíris permanentes. Es uno de los sitios más fotografiados de Reikiavik. A primera o a última hora la tienes casi vacía; entre las once y las tres en verano, no.</p>

<p>Sube a la torre ahora, no la dejes para el final del día. En invierno, comprimir la mañana es justo lo que te compra esta subida. En verano tienes más margen, aunque suele estar más tranquilo temprano o cerca de la última subida.</p>

<h2>La comida y la reserva de la que hay que ocuparse</h2>

<p>Se come en Laugavegur y en las calles de al lado. El clásico barato es la <em>pylsa</em> islandesa: un perrito caliente hecho con una mezcla de cordero, cerdo y ternera. Pídelo <em>eina með öllu</em>, «uno con todo». En invierno, un plato de sopa de cordero cumple la misma función. Los restaurantes con mesa son caros de verdad: ahí es donde un día en Reikiavik deja de ser barato.</p>

<div class="ticketbox">
  <h3>Reserva la laguna antes de volar</h3>
  <p>Sky Lagoon y Blue Lagoon funcionan por franjas horarias, y las de la tarde, que son las más buscadas, pueden agotarse con antelación. Para un día urbano normal, esta es la reserva principal que conviene dejar hecha antes de llegar.</p>
  <a class="btn sm" href="{TIQETS}" {OTA}>Ver entradas para la laguna</a>
  <a class="btn sm outline" href="{GYG}" {OTA}>Comparar excursiones y traslados</a>
</div>

<h2>Tarde: el paseo marítimo</h2>

<p>La segunda mitad del día va pegada al mar. Harpa, el auditorio de cristal al borde del puerto, se puede entrar libremente y en un día claro merece cinco minutos de quedarte quieto dentro. Más adelante, en el camino de Sæbraut, está el Sun Voyager, la escultura de acero que todo el mundo fotografía como si fuera un drakkar. No lo es, y el motivo real es mejor que el mito.</p>

<figure>
  <img src="{P}img/sec-sun-voyager.webp" width="1024" height="683" loading="lazy" alt="Una visitante pasa junto a la escultura Sun Voyager en el paseo de Sæbraut en invierno">
  <figcaption>Fotografiada sin parar y casi siempre mal identificada.</figcaption>
</figure>

<p>Luego el puerto viejo: los barcos de avistamiento de ballenas, los restaurantes de pescado y un buque gris de la guardia costera atracado, con un historial de combate frente a una armada mucho mayor. Si sigues hasta el final, llegas al montículo de hierba donde termina la ruta de audio.</p>

<p>Aquí está la única decisión de verdad de la tarde. Una salida a ver ballenas desde el puerto viejo son unas tres horas y se come toda la luz que te queda. Merece la pena en verano si has venido por la fauna; es un mal cambio en diciembre, cuando esas tres horas son toda tu luz.</p>

<h2>Noche: primero agua caliente, después cenar</h2>

<p>Los islandeses terminan el día en el agua y no en el bar, y tienes dos niveles para elegir.</p>

<p>Sky Lagoon es la versión cuidada: frente al océano, a quince minutos del centro y con un ritual de siete pasos incluido en la entrada. El pase Saman arranca sobre los 113 € por adulto (57 € para jóvenes); el Sér, con vestuarios privados, sobre los 136 €.</p>

<p>La opción local es una piscina municipal geotérmica: Sundhöllin en el centro, Laugardalslaug para el complejo entero. Calentadas desde el subsuelo, abiertas hasta tarde y a una fracción del precio de la laguna; la tarifa de adulto vigente está en reykjavik.is. Una norma importa más que ninguna otra: antes de entrar al agua hay que ducharse a fondo y sin bañador. Está puesto en todos los vestuarios y se cumple.</p>

<h2>Tres variantes</h2>

<h3>Una escala, no un día</h3>
<p>Si estás entre vuelos con seis o siete horas en la ciudad, quítale la mitad del paseo marítimo. Autobús desde Keflavík, casco antiguo y torre, comida en Laugavegur y autobús de vuelta. Eso cabe en una escala corta con el traslado por los dos lados y aun así te da las mejores vistas de la ciudad.</p>

<h3>Un día de diciembre</h3>
<p>Comprime todo lo de exterior entre las 11:00 y las 15:30 y asume que el puerto, la cena y la piscina van a ser de noche. No es una rebaja: las luces del puerto sobre el agua superan a la versión diurna. Y la mitad oscura del día es tu oportunidad de ver una aurora, si coinciden la nubosidad y la actividad solar. El tramo oscuro del paseo de Sæbraut es lo más sencillo desde la ciudad. El faro de Grótta, un autobús hacia el oeste, es más oscuro todavía. Pero ninguno sustituye a salir de verdad de las luces urbanas.</p>

<h3>Un día mojado y con viento de lado</h3>
<p>El tiempo cambia cada hora y el daño lo hace el viento. En un día malo, dale la vuelta al plan: museos y piscina en el centro del día y el paseo en la ventana que se abra. El paraguas aquí sirve de poco: una racha fuerte lo vuelve del revés. Un chubasquero con capucha y un gorro son más fiables, en cualquier mes.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>La audioguía</h2>
    <p class="lead" style="max-width:720px">Ver la ruta es una cosa. Entender por qué Reikiavik acabó justo aquí, qué representa en realidad el Sun Voyager y cómo un país tan pequeño se las arregló para plantarle cara a otros mucho mayores es otra distinta.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="La app de TouringBee mostrando la ruta de Reikiavik, delante de Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">Audioguía de TouringBee para Reikiavik</h3>
        <p class="meta" style="margin:0 0 10px">27 paradas · 2–2,5 horas · un año de acceso</p>
        <div class="rate">{STARS}<b>4,7</b> {RATELABEL}</div>
        <div class="price">9,99 €<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Funciona del todo sin conexión</strong> una vez descargada — mapa e ilustraciones incluidos, no gastas datos por el camino</li>
          <li><strong>A tu ritmo.</strong> Párate a comer o a ver un museo y sigue dos horas después en el mismo punto</li>
          <li><strong>Narrada en primera persona</strong> por un pescador de Reikiavik que tiene tiempo antes de volver a salir al mar</li>
          <li><strong>Un solo pago.</strong> Sin grupo, sin horario y sin un guía esperándote</li>
        </ul>
        <a {BUY} style="width:100%">Recorrer Reikiavik con la audioguía</a>
        <p class="meta" style="margin:12px 0 0;text-align:center">{CHECKOUTNOTE} <a href="{TBPRODUCT}" rel="noopener" data-no-widget>{OPENSHOP}</a>.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap prose">

<h2>Lo que cuesta el día</h2>
<table class="tbl">
  <tr><th>Concepto</th><th>Coste</th></tr>
  <tr><td>Recorrer la ciudad a pie</td><td>Gratis</td></tr>
  <tr><td>Audioguía, pago único</td><td>9,99 €</td></tr>
  <tr><td>Torre de Hallgrímskirkja, adulto</td><td>1.500 ISK</td></tr>
  <tr><td>Billete sencillo de Strætó</td><td>690 ISK</td></tr>
  <tr><td>Piscina municipal</td><td>Una fracción de lo que cuesta la laguna</td></tr>
  <tr><td>Sky Lagoon, pase Saman</td><td>desde unos 113 €</td></tr>
  <tr><td>Ballenas, unas 3 horas</td><td>Precio según el operador; el coste real es la luz</td></tr>
</table>

<p>La ciudad en sí no es cara. El presupuesto se dispara en cuanto añades laguna, excursiones fuera y cenas de restaurante.</p>

<h2>Cinco errores que te cuestan el día</h2>
<ol>
  <li><strong>Dejar la torre para el final en invierno.</strong> Última subida a las 16:45, de septiembre a mayo, y las entradas solo se venden en taquilla.</li>
  <li><strong>Meter el Círculo Dorado en un día urbano.</strong> Son ocho horas de carretera. Necesita su propio día.</li>
  <li><strong>Darle a un barco casi toda la luz de diciembre.</strong> Tres horas en el mar cuando tienes cuatro de luz.</li>
  <li><strong>Contar con un paraguas.</strong> El viento lo vuelve del revés. Mejor capas, capucha y gorro.</li>
  <li><strong>Tratar la laguna como un sitio al que se entra sin más.</strong> Va por franjas, y las de la tarde son las primeras en irse.</li>
</ol>

<h2>Preguntas frecuentes</h2>
<div class="faq">{FAQHTML}</div>

<h2>Seguir leyendo</h2>
<ul>
  <li><a href="{HOME}">La guía completa de Reikiavik</a> — la ruta, las excursiones y las estaciones</li>
  <li><a href="{GUIDES}">Todas las guías de Reikiavik</a> — lo publicado y lo que viene</li>
</ul>

<h2>La versión corta</h2>
<p>Reikiavik entrega casi todo lo que tiene en un día a pie. Las distancias nunca van a ser el problema. La luz sí.</p>
<p>Así que mira la hora de la puesta de sol, no dejes la torre para la noche y haz el resto a tu ritmo. Y si quieres entender la ciudad por el camino en vez de solo mirarla, llévate <a href="#audio">la audioguía de TouringBee para Reikiavik</a>: 27 paradas, 2–2,5 horas y todo sin conexión.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">Veintisiete paradas sobre la misma línea</h2>
  <p>Esta página te lleva al sitio correcto a la hora correcta. La audioguía te cuenta qué tienes delante.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Empezar el paseo — 9,99 €</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Buscar hotel en el centro</a>
  </div>
</div>

<p class="disc">Algunos enlaces de esta página son de afiliación: si reservas a través de ellos podemos llevarnos una comisión, sin coste extra para ti. Precios y horarios comprobados en las webs de los operadores en septiembre de 2026; cambian sin avisar, confírmalos antes de viajar. Torre: hallgrimskirkja.is. Autobuses: straeto.is. Laguna: skylagoon.com.</p>

  </div>
</section>
"""
