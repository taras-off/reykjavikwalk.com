# -*- coding: utf-8 -*-
"""ES — escrito en español. Registro: tú. Las historias se quedan en la audioguía."""

HEADLINE = "Torre de Hallgrímskirkja: entradas, horarios y cuándo subir"
TITLE = "Hallgrímskirkja: entradas, horarios y cuándo subir"
DESC = ("Entradas y horarios de la torre de Hallgrímskirkja, el límite de las 16:45 en invierno, qué "
        "se ve desde arriba y cuándo cierra al público.")

FAQ = [
 ("¿Cuánto cuesta subir a Hallgrímskirkja?",
  "1.500 ISK los adultos y 200 ISK los niños de 7 a 16 años. Estudiantes y personas con discapacidad "
  "pagan 1.300 ISK; los mayores de 67 tienen tarifa reducida, aunque la iglesia no publica el importe. "
  "Grupos de diez o más, un 10 % de descuento, y los grupos escolares de menores de 16 entran gratis. "
  "Entrar en la iglesia no cuesta nada: solo la torre se paga."),
 ("¿Se pueden reservar las entradas de la torre por internet?",
  "No. La iglesia dice con todas las letras que no es posible reservar la torre con antelación. Las "
  "entradas se venden en la tienda de la iglesia, a la izquierda según entras al vestíbulo, y valen solo "
  "para el día de la compra. Lo que se vende online como «entrada a Hallgrímskirkja» es otra cosa: una "
  "visita guiada que para delante, no el acceso a la torre."),
 ("¿A qué hora cierra la torre de Hallgrímskirkja?",
  "Del 1 de septiembre al 31 de mayo la iglesia cierra a las 17:00 y la última subida sale a las 16:45. "
  "Del 1 de junio al 31 de agosto abre hasta las 20:00 y la torre hasta las 19:45. Además, los oficios, "
  "las ceremonias y los conciertos cierran la iglesia al público: mira el programa del día antes de "
  "montar la tarde alrededor."),
 ("¿Merece la pena la torre?",
  "Por las vistas, sí: es el único mirador alto del casco antiguo y el único desde el que ves los tejados "
  "de colores en vertical. Veinte minutos y 1.500 ISK es un buen cambio. Si lo que quieres es un "
  "panorama más amplio con toda la bahía y las montañas, Perlan lo hace mejor, pero cuesta más y se "
  "lleva media jornada."),
 ("¿Se sube en ascensor hasta arriba?",
  "Casi. Un ascensor cubre la mayor parte de la altura y luego queda un tramo corto de escaleras hasta el "
  "mirador. El mirador está cerrado, con aberturas en los cuatro lados en vez de estar al aire libre, así "
  "que funciona con cualquier tiempo. Es pequeño, y la iglesia lo cierra cuando se llena."),
 ("¿Se puede visitar la iglesia gratis?",
  "Sí. Hallgrímskirkja es una parroquia en activo y entrar a ver la nave y el órgano no cuesta nada "
  "durante el horario de apertura. Solo pagas si quieres subir. Los oficios están abiertos a todo el "
  "mundo, pero mientras duran el edificio no es una parada turística."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/tile-hallgrimskirkja.webp" width="800" height="600" alt="Hallgrímskirkja vista desde abajo, con la bandera islandesa ondeando junto a la torre" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reikiavik</a> › Hallgrímskirkja</p>
    <h1>Hallgrímskirkja: entradas, horarios y cuándo subir a la torre</h1>
    <p class="sub">La iglesia es gratis. La torre no, no se reserva, y en invierno deja de subir gente a las 16:45.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, autor de las audioguías de TouringBee">
      <span>Por Eugene · Actualizado el 29 de septiembre de 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#hours">Horarios y precios</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Visitas en Reikiavik</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">Dos cosas pillan desprevenida a la gente en Hallgrímskirkja. La entrada a la torre no se compra con antelación, ni aquí ni en ningún sitio, ni a ningún precio. Y de septiembre a mayo la última subida sale a las 16:45, que en diciembre es bastante antes de que la mayoría haya terminado de comer.</p>

<p>Lo demás es fácil. La iglesia se visita gratis, está al final de la calle que ibas a subir de todas formas, y la parada entera son unos treinta minutos con la cola incluida.</p>

<p>Esta página va de la torre: lo que cuesta, cuándo abre, cuándo cierra por oficios y si las vistas compensan frente a las alternativas. Acompaña a <a href="{ONEDAY}">nuestro itinerario de un día en Reikiavik</a>, donde esta torre es el punto fijo alrededor del cual se dobla el resto. Si lo que quieres es la historia del edificio y no la logística, de eso se encarga <a href="#audio">el paseo con audio de TouringBee</a>.</p>

<div class="glance">
  <h2>En resumen</h2>
  <dl>
    <dt>Entrada a la iglesia</dt><dd>Gratis</dd>
    <dt>Entrada a la torre</dt><dd>1.500 ISK adulto · 200 ISK niño de 7 a 16 · 1.300 ISK estudiante o persona con discapacidad</dd>
    <dt>Reserva</dt><dd>Imposible. Se vende en la tienda de la iglesia, solo para ese día</dd>
    <dt>Horario de invierno</dt><dd>1 sep – 31 may: iglesia 10:00–17:00, última subida 16:45</dd>
    <dt>Horario de verano</dt><dd>1 jun – 31 ago: iglesia 09:00–20:00, torre hasta las 19:45</dd>
    <dt>Cuánto lleva</dt><dd>Unos 30 minutos con la cola</dd>
    <dt>Cómo se sube</dt><dd>Ascensor casi hasta arriba y luego un tramo corto de escaleras</dd>
    <dt>Altura</dt><dd>73 m según la propia iglesia: el edificio más alto de la ciudad</dd>
  </dl>
</div>

<div class="minicta">
  <h2>La iglesia es una parada de un paseo más largo</h2>
  <p>El paseo con audio de TouringBee incluye Hallgrímskirkja y <strong>otras 26 paradas</strong> por el casco antiguo: <strong>2–2,5 horas</strong>, mapa y audio sin conexión, a tu ritmo.</p>
  <a {BUY}>Audioguía de Reikiavik — 9,99 €</a>
</div>

<h2 id="hours">Qué se paga y qué no</h2>

<p>Hallgrímskirkja es una parroquia luterana en activo, no un museo, y entrar es gratis durante el horario de apertura. Puedes sentarte en la nave, mirar el órgano y salir sin pagar nada. La entrada es solo para la torre.</p>

<table class="tbl">
  <tr><th>Entrada a la torre</th><th>Precio</th></tr>
  <tr><td>Adultos</td><td>1.500 ISK</td></tr>
  <tr><td>Niños de 7 a 16 años</td><td>200 ISK</td></tr>
  <tr><td>Estudiantes y personas con discapacidad (con acreditación)</td><td>1.300 ISK</td></tr>
  <tr><td>Mayores de 67</td><td>Tarifa reducida; la iglesia no publica el importe</td></tr>
  <tr><td>Grupos de 10 o más</td><td>10 % de descuento</td></tr>
  <tr><td>Grupos escolares, alumnos de 16 o menos</td><td>Gratis</td></tr>
</table>

<p>Por internet vas a encontrar otras cifras. El portal turístico de la propia Reikiavik seguía publicando 1.400 ISK y última entrada a las 16:30 cuando lo comprobamos en septiembre de 2026. Y muchas guías copian una tabla de precios antigua que la iglesia ha dejado en su propia web, encima de la vigente. Los precios de arriba son los que cobra ahora.</p>

<h2>Los horarios, y la hora límite</h2>

<table class="tbl">
  <tr><th>Temporada</th><th>Iglesia</th><th>Última subida</th></tr>
  <tr><td>1 de septiembre – 31 de mayo</td><td>10:00 – 17:00</td><td>16:45</td></tr>
  <tr><td>1 de junio – 31 de agosto</td><td>09:00 – 20:00</td><td>19:45</td></tr>
</table>

<p>Esas 16:45 son el número alrededor del cual hay que planificar, porque no se mueven con la luz. A finales de diciembre el sol ya se ha ido a las tres y media, así que la torre y la luz aprovechable se acaban a la vez. En febrero todavía hay claridad a las 16:45 y la gente pierde la subida precisamente por eso: el cielo no parece de hora de cierre.</p>

<p>Los demás cierres son menos previsibles. La iglesia cierra al público durante oficios, bodas, funerales y conciertos, y lo dice sin rodeos: el horario puede cambiar. También cierra el mirador en determinados eventos, y antes de lo anunciado cuando se llena. La mañana del domingo es la forma más fiable de llegar y que no te dejen pasar.</p>

<h2>Comprar la entrada</h2>

<p>La tienda está a la izquierda según entras al vestíbulo. Es el único sitio donde existe la entrada a la torre. La iglesia lo formula así: no es posible reservar la torre con antelación. Ni venta online, ni franjas horarias, ni acceso preferente.</p>

<p>Lo que veas anunciado por internet como entrada a Hallgrímskirkja es otra cosa: una visita guiada que para fuera, o una tarjeta turística que quizá te lo reembolse. La entrada vale una vez, el día que la compras, así que no puedes comprarla por la mañana y usarla al anochecer.</p>

<h2>La subida</h2>

<p>Un ascensor cubre casi toda la altura y un tramo corto de escaleras hace el resto. El mirador está cerrado, con aberturas en arco en los cuatro lados en lugar de estar al aire libre, y por eso sigue funcionando un día en que abajo el viento está destrozando paraguas.</p>

<p>El mirador es pequeño. En julio lo lento es la cola de abajo, no la subida, y la iglesia prefiere hacer esperar antes que amontonar gente arriba. Con quince minutos allí vas sobrado.</p>

<figure>
  <img src="{P}img/tile-rainbow-street.webp" width="800" height="600" loading="lazy" alt="Skólavörðustígur pintada con franjas de arcoíris, subiendo hacia Hallgrímskirkja">
  <figcaption>La calle que subes para llegar aquí. Desde el mirador la vuelves a bajar con la vista.</figcaption>
</figure>

<h2>Qué se ve de verdad</h2>

<p>Mira al oeste y tienes la foto por la que viene todo el mundo. Skólavörðustígur baja con sus franjas de arcoíris y detrás se amontonan los tejados de chapa de colores del casco antiguo hasta el puerto, con la bahía y el monte Esja al fondo. Esa vista justifica la entrada. Y es lo único que Perlan no te puede dar: queda demasiado lejos para mirar los tejados desde arriba.</p>

<p>Al sur y al este está la Reikiavik residencial y, en un día claro, la península de Reykjanes. Al norte, el puerto y el agua. No hay un lado malo, pero si solo tienes un momento de cielo despejado y una cámara, quédate con el oeste.</p>

<p>Aquí importa más la luz que la hora. En verano el sol bajo del final del día funciona mejor que el mediodía. En invierno la ventana es estrecha de todas formas, y un cielo cubierto aplasta los tejados en un gris uniforme, cosa que conviene saber antes de gastarte 1.500 ISK la tarde equivocada.</p>

<h2>Dentro, que no cuesta nada</h2>

<p>La nave tiene capacidad para 1.200 personas y es deliberadamente sobria: blanca, altísima y casi sin decoración. Al fondo está el órgano Klais, construido en Bonn y terminado en 1992: 5.275 tubos, 15 metros de alto y unas 25 toneladas. Hay un segundo órgano más pequeño, de la casa danesa Frobenius, reconstruido y vuelto a consagrar en 2024. Vienen organistas de todo el mundo a grabar en el grande; si al entrar hay un ensayo, quédate.</p>

<p>El edificio tardó lo suyo. Guðjón Samúelsson, arquitecto del Estado, ganó el encargo en los años treinta y no llegó a verlo terminado. Las obras fueron de 1945 hasta la consagración en 1986, y la parroquia usó la cripta durante 26 años mientras tanto. La fachada suele describirse como columnas de basalto; la propia iglesia la compara con la roca columnar, las montañas y los glaciares islandeses.</p>

<p>Esa comparación es la versión que da cualquier guía. Por qué un arquitecto del Estado se pasó la carrera buscando un estilo específicamente islandés es una historia más larga, y la audioguía se toma su tiempo con ella.</p>

<p>Una cosa más, fuera. La estatua de la explanada ya estaba aquí antes que la iglesia, y no fue idea de Islandia ponerla ahí.</p>

<h2>¿Torre o Perlan?</h2>

<table class="tbl">
  <tr><th></th><th>Hallgrímskirkja</th><th>Perlan</th></tr>
  <tr><td>Dónde</td><td>Arriba del casco antiguo, andando</td><td>En una colina fuera del centro, autobús o taxi</td></tr>
  <tr><td>La vista</td><td>En vertical sobre los tejados de colores y la calle del arcoíris</td><td>Panorámica amplia: bahía, ciudad, montañas</td></tr>
  <tr><td>Mirador</td><td>Cerrado y pequeño</td><td>Terraza abierta, además de exposiciones</td></tr>
  <tr><td>Entrada</td><td>1.500 ISK, solo en taquilla</td><td>Más; comprueba el precio actual, cambia</td></tr>
  <tr><td>Tiempo</td><td>30 minutos</td><td>Media jornada con el desplazamiento</td></tr>
</table>

<p>En un solo día en la ciudad, la torre gana solo por el tiempo. Si tienes dos días y uno sale lluvioso, Perlan es mejor edificio para día de lluvia, porque dentro hay algo que hacer.</p>

<div class="ticketbox">
  <h3>La torre no se reserva; lo de alrededor, sí</h3>
  <p>Para Hallgrímskirkja en sí no se reserva nada. Para lo que la rodea, sí: Perlan, las lagunas y las visitas guiadas que pasan por la iglesia venden su franja con antelación.</p>
  <a class="btn sm" href="{TIQETS}" {OTA}>Entradas en Reikiavik</a>
  <a class="btn sm outline" href="{GYG}" {OTA}>Comparar visitas guiadas</a>
</div>

<h2>Tres situaciones</h2>

<h3>Tienes unas horas entre vuelos</h3>
<p>La torre es el mejor uso de una escala corta: veinte minutos a pie desde la parada de autobús del centro y toda la ciudad de golpe. Sube primero y luego baja hacia el casco antiguo, no al revés.</p>

<h3>Es domingo</h3>
<p>Los oficios de la mañana cierran la iglesia al público. Ve después de comer: en invierno eso todavía te deja margen de sobra antes de las 16:45.</p>

<h3>Ha cambiado el tiempo</h3>
<p>No descartes la torre. El mirador está cerrado y el viento que arruina la calle ahí arriba no molesta. El verdadero aguafiestas es la nube baja: si no ves el Esja desde la acera, tampoco vas a ver gran cosa desde 73 metros.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>La audioguía</h2>
    <p class="lead" style="max-width:720px">Desde el mirador ves qué aspecto tiene Reikiavik. Por qué la ciudad creció exactamente ahí, qué hace esa estatua en la explanada y qué estaba construyendo el arquitecto en realidad son preguntas distintas.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="La app de TouringBee mostrando la ruta de Reikiavik, delante de Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">Audioguía de TouringBee para Reikiavik</h3>
        <p class="meta" style="margin:0 0 10px">27 paradas · 2–2,5 horas · un año de acceso</p>
        <div class="rate">{STARS}<b>4,7</b> {RATELABEL}</div>
        <div class="price">9,99 €<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Hallgrímskirkja es una de las 27 paradas</strong>: la ruta va de la loma del fundador al puerto viejo</li>
          <li><strong>Funciona del todo sin conexión</strong> una vez descargada, con mapa e ilustraciones</li>
          <li><strong>A tu ritmo.</strong> Párate para subir a la torre y sigue donde lo dejaste</li>
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

<h2>Cinco errores</h2>
<ol>
  <li><strong>Buscar entradas por internet.</strong> No existen. La tienda de la iglesia es el único punto de venta.</li>
  <li><strong>Dejar la torre para media tarde entre septiembre y mayo.</strong> Última subida a las 16:45, haga el cielo lo que haga.</li>
  <li><strong>Presentarte un domingo por la mañana.</strong> Los oficios cierran la iglesia al público.</li>
  <li><strong>Fiarte de un precio leído en un directorio.</strong> Varios siguen mostrando 1.400 ISK y las 16:30.</li>
  <li><strong>Subir con nube baja.</strong> Si el Esja no se ve desde la calle, guarda la entrada para mañana.</li>
</ol>

<h2>Preguntas frecuentes</h2>
<div class="faq">{FAQHTML}</div>

<h2>Seguir leyendo</h2>
<ul>
  <li><a href="{ONEDAY}">Reikiavik en un día</a> — el itinerario del que esta torre es el eje</li>
  <li><a href="{HOME}">La guía completa de Reikiavik</a> — la ruta, las excursiones y las estaciones</li>
  <li><a href="{GUIDES}">Todas las guías de Reikiavik</a> — lo publicado y lo que viene</li>
</ul>

<h2>La versión corta</h2>
<p>Entra gratis, paga 1.500 ISK en la tienda si quieres las vistas y hazlo antes de las 16:45 en invierno. Mira al oeste por los tejados. Media hora, y es la mejor media hora que vende el casco antiguo.</p>
<p>Y si prefieres entender lo que tienes debajo en vez de solo mirarlo, llévate <a href="#audio">la audioguía de TouringBee</a>: 27 paradas por el centro, esta incluida, y todo sin conexión.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">La iglesia es la parada uno de veintisiete</h2>
  <p>Esta página te sube a la torre a la hora correcta. La audioguía te cuenta qué es la ciudad que tienes debajo.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Empezar el paseo — 9,99 €</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Buscar hotel en el centro</a>
  </div>
</div>

<p class="disc">Algunos enlaces de esta página son de afiliación: si reservas a través de ellos podemos llevarnos una comisión, sin coste extra para ti. Precios y horarios comprobados en hallgrimskirkja.is en septiembre de 2026; cambian sin avisar, confírmalos antes de viajar.</p>

  </div>
</section>
"""
