# -*- coding: utf-8 -*-
"""ES — escrito en español. Registro: tú. Página logística, solo dos ganchos."""

HEADLINE = "Del aeropuerto de Keflavík a Reikiavik: qué traslado encaja con tu hora de aterrizaje"
TITLE = "Keflavík a Reikiavik: autobús, taxi o coche"
DESC = ("De Keflavík a Reikiavik: los precios reales del Flybus, el autobús público y el coche, y "
        "qué hacer con las horas entre el aterrizaje y la entrada al hotel.")

FAQ = [
 ("¿Cuál es la forma más barata de ir del aeropuerto de Keflavík a Reikiavik?",
  "El autobús público, la línea Strætó 55, a 2.400 ISK por adulto. Los jóvenes de 12 a 17 años, los "
  "mayores de 67 y los pasajeros con discapacidad pagan 1.200 ISK, y los menores de 12 viajan gratis. "
  "Funciona a diario pero no con cada llegada, y no todos los trayectos acaban en BSÍ: algunos terminan "
  "en Fjörður, en Hafnarfjörður, que no es el centro de la ciudad."),
 ("¿Cuánto se tarda de Keflavík a Reikiavik?",
  "Unos 45 minutos en autocar para los aproximadamente 50 km, y casi lo mismo en coche. El tiempo no se "
  "va en el trayecto. Se va esperando un autobús que sale 35 o 45 minutos después de aterrizar, y "
  "después esperando otra vez, porque tu habitación no estará lista hasta por la tarde."),
 ("¿Hay que reservar el autobús con antelación?",
  "Normalmente no. El Flybus vende billetes en el aeropuerto y también por internet, y sus salidas van "
  "acompasadas a los vuelos que llegan. El billete online ahorra algo, te evita la cola después de un "
  "vuelo largo y compensa en fechas cargadas. Si tu vuelo se retrasa, el operador pasa tu plaza a la "
  "siguiente salida en vez de retener el autobús."),
 ("¿El Flybus llega hasta mi hotel?",
  "La tarifa estándar te deja en la terminal BSÍ. Flybus+ continúa en microbús hasta los hoteles "
  "adheridos, con un suplemento. Si tu alojamiento está en el casco antiguo, el billete normal más un "
  "paseo corto suele ser más rápido que esperar al microbús."),
 ("¿Compensa alquilar coche solo para el traslado?",
  "Por sí solo no. Una carretera, 45 minutos y, al final, un coche que hay que aparcar en una ciudad que "
  "se cruza andando. El alquiler empieza a tener sentido cuando el aeropuerto es el principio de una "
  "ruta: el Círculo Dorado, la costa sur, cualquier cosa fuera de la capital. La pregunta de verdad es si "
  "vas a salir de la ciudad."),
 ("¿Dónde dejo el equipaje antes de la entrada?",
  "Empieza preguntando en el hotel: que la habitación no esté lista no significa que el hotel no pueda "
  "ayudar, y la mayoría guardan las maletas hasta la hora de entrada sin cobrar. Si no, hay consignas en "
  "Keflavík y en BSÍ; las de BSÍ abren 24 horas, con 96 taquillas de cuatro tamaños."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/sec-old-town.webp" width="1024" height="683" alt="Una bicicleta aparcada junto a un escaparate en el casco antiguo de Reikiavik" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reikiavik</a> › Del aeropuerto de Keflavík al centro</p>
    <h1>Del aeropuerto de Keflavík a Reikiavik: las opciones, y cuál encaja con tu hora de aterrizaje</h1>
    <p class="sub">Cincuenta kilómetros, una carretera, cuarenta y cinco minutos. El traslado es la parte fácil; el hueco entre aterrizar y entrar en la habitación, no.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, autor de las audioguías de TouringBee">
      <span>Por Eugene · Actualizado el 5 de octubre de 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#options">Comparar opciones</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Traslados y excursiones</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">De Keflavík a Reikiavik hay una sola carretera y se tarda unos 45 minutos. El autocar del aeropuerto acompasa sus salidas a los vuelos que llegan: normalmente sale 35 o 45 minutos después de un aterrizaje, con un horario que arranca sobre las 03:30 y llega hasta bien entrada la noche. Llegar a la ciudad es un problema resuelto.</p>

<p>Lo que no está resuelto es a qué hora tomas tierra. En Reikiavik la entrada al hotel suele ser a las 14:00 o las 15:00. Si aterrizas antes, llegas a la ciudad con las maletas, la habitación cerrada y varias horas que llenar — y es eso, y no los 50 km, lo que decide qué billete te conviene.</p>

<p>Por eso esta página hace las dos mitades: las opciones de traslado con los precios que cobran de verdad los operadores y, después, qué hacer con el hueco. Si el hueco te deja en el centro con tiempo, <a href="{ONEDAY}">nuestro itinerario de un día</a> y <a href="#audio">el paseo con audio de TouringBee</a> están hechos justo para esas horas. ¿Montando el viaje entero? Empieza por la <a href="{HOME}">guía completa de Reikiavik</a>.</p>

<div class="glance">
  <h2>En resumen</h2>
  <dl>
    <dt>Distancia</dt><dd>Unos 50 km del aeropuerto al centro de Reikiavik</dd>
    <dt>Trayecto</dt><dd>Unos 45 minutos en autocar o en coche</dd>
    <dt>Flybus</dt><dd>Desde 3.999 ISK el trayecto a la terminal BSÍ</dd>
    <dt>Autobús público</dt><dd>Strætó 55 — 2.400 ISK adulto, 1.200 ISK reducida, gratis menores de 12</dd>
    <dt>Salidas</dt><dd>El Flybus se acompasa a las llegadas, de 03:30 a bien entrada la noche; el Strætó va por horario fijo</dd>
    <dt>Reserva</dt><dd>Normalmente no hace falta. Hay billetes en el aeropuerto</dd>
    <dt>Equipaje</dt><dd>Pregunta primero en el hotel; hay consignas en el aeropuerto y en BSÍ</dd>
    <dt>El límite de verdad</dt><dd>La entrada a las 14:00–15:00, no el traslado</dd>
  </dl>
</div>

<div class="minicta">
  <h2>¿Aterrizas pronto? Esa es la ventana del paseo</h2>
  <p>El paseo con audio de TouringBee son <strong>27 paradas y 2–2,5 horas</strong> por el casco antiguo, con mapa y audio sin conexión. Con las maletas resueltas, las horas muertas antes de entrar al hotel se convierten en lo mejor del primer día.</p>
  <a {BUY}>Audioguía de Reikiavik — 9,99 €</a>
</div>

<h2 id="options">Empieza por tu hora de aterrizaje, no por el precio</h2>

<p>Todas las guías de esta ruta comparan tarifas. Pero el precio es solo la mitad del cálculo: un billete barato deja de ser buen negocio en cuanto su horario te añade una hora de espera.</p>

<p>Pregúntate otra cosa: ¿a qué hora tocan las ruedas la pista y dónde duermes? Si aterrizas a mediodía con la habitación lista a las dos, vale cualquier cosa. Si aterrizas a las seis de la mañana, necesitas un plan para el equipaje y otro para ti. El autobús más barato no cubre todos los vuelos, así que puede costarte una hora que habrías preferido gastar en otra parte.</p>

<table class="tbl">
  <tr><th>Opción</th><th>Precio</th><th>Te deja en</th><th>Cuándo es tu opción</th></tr>
  <tr><td><strong>Flybus</strong></td><td>desde 3.999 ISK por trayecto</td><td>Terminal BSÍ</td><td>Por defecto. Salidas acompasadas a las llegadas; si te retrasas, tu plaza pasa al siguiente autobús</td></tr>
  <tr><td><strong>Flybus+</strong></td><td>suplemento</td><td>Hoteles adheridos</td><td>Mucho equipaje, niños, mal tiempo o alojamiento a las afueras</td></tr>
  <tr><td><strong>Airport Direct</strong></td><td>consultar tarifa</td><td>Terminal céntrica, premium hasta el hotel</td><td>El segundo autocar regular: conviene comparar precio con el Flybus</td></tr>
  <tr><td><strong>Strætó 55</strong></td><td>2.400 ISK adulto</td><td>BSÍ o Fjörður</td><td>De día, con poco equipaje, si el horario cuadra</td></tr>
  <tr><td><strong>Taxi o traslado privado</strong></td><td>Taxímetro o presupuesto</td><td>Tu puerta</td><td>Sois tres o cuatro, o la hora es mala</td></tr>
  <tr><td><strong>Coche de alquiler</strong></td><td>Tarifa diaria</td><td>Donde quieras</td><td>Solo si después sales de la ciudad</td></tr>
</table>

<h2>El Flybus y por qué es la opción por defecto</h2>

<p>Es el autocar que coge la mayoría, y lo que vende no es velocidad sino certeza. Las salidas se acompasan a los vuelos que llegan en vez de ir a intervalos fijos: normalmente 35 o 45 minutos después de aterrizar. El horario publicado empieza sobre las 03:30 y llega hasta bien entrada la noche, así que para un vuelo muy temprano o muy tardío mira el horario de tu fecha en lugar de fiarte de la regla general.</p>

<p>Si tu vuelo se retrasa, el operador no retiene el autobús: te garantiza plaza en la siguiente salida, sin coste añadido. Es una diferencia importante y conviene saberla antes de ponerte nervioso en la cola del control de pasaportes. La tarifa incluye dos bultos de hasta 23 kg cada uno.</p>

<p>El billete normal termina en BSÍ, la estación de autobuses en el borde sur del centro. Flybus+ añade un tramo en microbús hasta los hoteles adheridos, con suplemento. Compensa con equipaje pesado, con niños, con mal tiempo y cuando el alojamiento está a las afueras.</p>

<p>Si viajas ligero y te alojas en el casco antiguo, merece la pena comparar: el microbús va recorriendo una lista de direcciones y la tuya puede no ser la primera. Mira a qué distancia está tu hotel de BSÍ y decide con eso, no por inercia.</p>

<h2>Strætó 55, la opción barata y su trampa</h2>

<p>El autobús público es la línea 55 y cuesta 2.400 ISK por adulto: 1.200 ISK para jóvenes de 12 a 17, mayores de 67 y pasajeros con discapacidad, y gratis para menores de 12. Para una familia esa diferencia es dinero de verdad.</p>

<p>Dos trampas. Va por horario y no por tu vuelo, así que aterrizar a las 05:30 puede suponer una espera larga. Y no todos los trayectos acaban en BSÍ: algunos terminan en Fjörður, en Hafnarfjörður, un municipio al sur de Reikiavik que desde luego no es el centro. Comprueba el destino antes de subir, no después.</p>

<div class="ticketbox">
  <h3>Traslados privados y excursiones</h3>
  <p>Si sois tres o cuatro, calcula el precio del autobús por persona frente a un solo vehículo antes de dar por hecho que el autocar sale más barato. Los traslados privados y las excursiones que recogen en Keflavík se venden por adelantado.</p>
  <a class="btn sm" href="{GYG}" {OTA}>Comparar traslados</a>
  <a class="btn sm outline" href="{TIQETS}" {OTA}>Entradas en Reikiavik</a>
</div>

<h2>El taxi, y cuándo se acorta la distancia</h2>

<p>Los taxis islandeses van con taxímetro y no hay tarifa plana publicada para el aeropuerto, así que trátalo como la opción cara y pide una estimación antes de subir.</p>

<p>Si sois tres o cuatro, pide una estimación actual y compárala con la suma de vuestros billetes de autobús. El taxi se cobra por vehículo y el autobús por pasajero, de modo que la distancia se acorta según crece el grupo. Eso no convierte el taxi en barato, solo lo deja más cerca de lo que parece para quien viaja solo.</p>

<h2>El coche de alquiler, con honestidad</h2>

<p>Para el traslado por sí solo, no. Es una carretera recta que harás una vez y, al final, un coche que aparcar en una ciudad que se cruza andando. El alquiler empieza a tener sentido cuando el aeropuerto es el principio de una ruta: el Círculo Dorado, la costa sur, cualquier cosa fuera de la capital. Decídelo por el viaje, no por el traslado.</p>

<figure>
  <img src="{P}img/sec-winter-street.webp" width="1024" height="683" loading="lazy" alt="Una tienda de esquina de colores vivos en una calle nevada del centro de Reikiavik">
  <figcaption>BSÍ queda justo al sur de todo esto. Casi todo el casco antiguo está a un paseo corto de la estación.</figcaption>
</figure>

<h2>El hueco entre aterrizar y entrar al hotel</h2>

<p>Esta es la parte que nadie planifica y con la que choca todo el mundo. Tu habitación no está lista hasta las dos de la tarde. Tu vuelo aterrizó a las seis de la mañana. A las ocho estás en el centro con una maleta.</p>

<p>El equipaje es la mitad fácil, y el primer movimiento es el que se olvida: pregunta en tu hotel. Que la habitación no esté lista no es lo mismo que un hotel que no pueda echarte una mano, y la mayoría guardan las maletas hasta la entrada sin cobrar. Además deja tu maleta donde vas a dormir, que es mejor que cualquier taquilla.</p>

<p>Si la respuesta es no, o has reservado un apartamento sin recepción, hay consignas en Keflavík y en BSÍ. Las de BSÍ funcionan 24 horas, con 96 taquillas de cuatro tamaños, más de lo que ofrecen la mayoría de estaciones de ese tamaño.</p>

<p>Las horas son la mitad mejor, porque el casco antiguo se cruza en unos veinte minutos y no necesita una habitación de hotel para disfrutarse. Un hueco de cuatro o cinco horas da de sobra para el paseo de 2 a 2,5 horas sobre el que está construido este sitio, y aún deja sitio para desayunar y un café largo. Las cafeterías abren mucho antes que los mostradores de recepción.</p>

<h2>Tres momentos</h2>

<h3>Si aterrizas pronto</h3>
<p>El Flybus, porque sus salidas siguen a las llegadas. Equipaje resuelto, desayuno en el centro y a caminar cuando amanezca: alrededor del solsticio de invierno eso no pasa hasta cerca de las once de la mañana, así que planifica antes una hora caliente bajo techo.</p>

<h3>Si aterrizas tarde</h3>
<p>El Flybus otra vez: su horario llega hasta bien entrada la noche y las últimas salidas están acompasadas a las llegadas tardías, cosa que el autobús público no hace. Aun así, comprueba la última salida de tu fecha. Si aterrizas cuando los autocares ya han terminado, el taxi no es un lujo: es lo único que queda.</p>

<h3>Si sales temprano</h3>
<p>Cuenta hacia atrás desde el mostrador de facturación, no desde la puerta de embarque, y suma los 45 minutos más lo que te lleve la recogida en el hotel. Los vuelos de madrugada implican autocares saliendo de la ciudad de noche cerrada: el horario del Flybus lo cubre, el autobús urbano no.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>La audioguía</h2>
    <p class="lead" style="max-width:720px">Vas a tener horas en el centro antes de que nadie te dé una llave. Caminarlas es lo obvio. Saber por qué la ciudad está aquí y por qué el paseo arranca en esa loma concreta es lo que tienes que traer puesto.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="La app de TouringBee mostrando la ruta de Reikiavik, delante de Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">Audioguía de TouringBee para Reikiavik</h3>
        <p class="meta" style="margin:0 0 10px">27 paradas · 2–2,5 horas · un solo pago, un año de acceso</p>
        <div class="price">9,99 €<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Encaja en las horas muertas.</strong> Dos o dos horas y media, más o menos lo que tienes antes de entrar</li>
          <li><strong>Funciona del todo sin conexión</strong> una vez descargada, útil antes de resolver los datos en un país nuevo</li>
          <li><strong>A tu ritmo.</strong> Párate a desayunar y sigue donde lo dejaste</li>
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

<h2>Precios: traslado, equipaje y paseo</h2>
<table class="tbl">
  <tr><th>Concepto</th><th>Coste</th></tr>
  <tr><td>Strætó 55, adulto</td><td>2.400 ISK</td></tr>
  <tr><td>Strætó 55, 12–17, 67+, discapacidad</td><td>1.200 ISK</td></tr>
  <tr><td>Strætó 55, menores de 12</td><td>Gratis</td></tr>
  <tr><td>Flybus a BSÍ, un trayecto</td><td>desde 3.999 ISK</td></tr>
  <tr><td>Airport Direct</td><td>Consulta la tarifa con el operador</td></tr>
  <tr><td>Flybus+ con entrega en hotel</td><td>Suplemento; consulta al operador</td></tr>
  <tr><td>Taxi</td><td>Taxímetro, sin tarifa plana publicada para el aeropuerto</td></tr>
  <tr><td>Consigna de equipaje</td><td>En el aeropuerto y en BSÍ, 24 horas</td></tr>
  <tr><td>Audioguía para el hueco</td><td>9,99 €, un solo pago, un año de acceso</td></tr>
</table>

<h2>Cinco errores</h2>
<ol>
  <li><strong>Elegir solo por la tarifa.</strong> Mira antes tu hora de aterrizaje y el horario: la opción barata puede añadir una espera larga.</li>
  <li><strong>Dar por hecho que el autobús público cubre tu vuelo.</strong> Va por horario; el Flybus va por llegadas.</li>
  <li><strong>Subir a un 55 sin mirar el destino.</strong> Algunos trayectos acaban en Fjörður, no en BSÍ.</li>
  <li><strong>Pagar Flybus+ por inercia.</strong> Si tu hotel está cerca de BSÍ y llevas poco equipaje, compara antes el paseo con la ronda del microbús.</li>
  <li><strong>Alquilar coche para el traslado.</strong> Alquílalo el día que sales de la ciudad, no el día que aterrizas.</li>
</ol>

<h2>Preguntas frecuentes</h2>
<div class="faq">{FAQHTML}</div>

<h2>Seguir leyendo</h2>
<ul>
  <li><a href="{ONEDAY}">Reikiavik en un día</a> — qué hacer con las horas que acabas de liberar</li>
  <li><a href="{TOWER}">Hallgrímskirkja y su torre</a> — entradas, horarios y el límite de las 16:45</li>
  <li><a href="{HOME}">La guía completa de Reikiavik</a> — la ruta, las excursiones y las estaciones</li>
  <li><a href="{GUIDES}">Todas las guías de Reikiavik</a></li>
</ul>

<h2>La versión corta</h2>
<p>Coge el Flybus salvo que tengas un motivo para no hacerlo: sus salidas siguen a los vuelos, si te retrasas tu plaza pasa al siguiente y te deja en el borde del centro por 3.999 ISK. Coge el 55 si el horario cuadra y cuentas cada corona. Coge coche solo si vas a salir de la ciudad.</p>
<p>Luego resuelve las maletas y aprovecha las horas. Si prefieres entender la ciudad en vez de esperar en ella, llévate <a href="#audio">la audioguía de TouringBee</a>: 27 paradas, 2–2,5 horas y todo sin conexión.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">Tu habitación no estará lista hasta las dos</h2>
  <p>El paseo dura dos horas y media. La cuenta se hace sola.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Empezar el paseo — 9,99 €</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Buscar hotel en el centro</a>
  </div>
</div>

<p class="disc">Algunos enlaces de esta página son de afiliación: si reservas a través de ellos podemos llevarnos una comisión, sin coste extra para ti. Tarifas y horarios comprobados en las webs de los operadores en octubre de 2026; cambian sin avisar, confírmalos antes de viajar. Flybus: flybus.is. Autobús público: straeto.is.</p>

  </div>
</section>
"""
