# -*- coding: utf-8 -*-
"""PT-PT — registo: 3.ª pessoa (Entre / Suba / ao seu ritmo). Nenhuma forma de «tu»."""

HEADLINE = "Torre da Hallgrímskirkja: bilhetes, horários e quando subir"
TITLE = "Hallgrímskirkja: bilhetes, horários e quando subir"
DESC = ("Bilhetes e horários da torre da Hallgrímskirkja, o limite das 16:45 no inverno, o que se vê "
        "realmente lá de cima e quando a igreja está fechada a visitantes.")

FAQ = [
 ("Quanto custa subir à Hallgrímskirkja?",
  "1.500 ISK por adulto e 200 ISK por criança dos 7 aos 16 anos. Estudantes e pessoas com deficiência "
  "pagam 1.300 ISK; a partir dos 67 há tarifa reduzida, embora a igreja não publique o valor. Grupos de "
  "dez ou mais têm 10% de desconto e os grupos escolares até aos 16 anos entram de graça. Entrar na "
  "igreja não custa nada: paga-se apenas a torre."),
 ("É possível reservar bilhetes para a torre online?",
  "Não. A igreja afirma com clareza que não é possível reservar a torre com antecedência. Os bilhetes "
  "vendem-se na loja da igreja, à esquerda de quem entra no átrio, e só são válidos no dia da compra. O "
  "que aparece online como «bilhete para a Hallgrímskirkja» é outra coisa: uma visita guiada que para à "
  "porta, não o acesso à torre."),
 ("A que horas fecha a torre da Hallgrímskirkja?",
  "De 1 de setembro a 31 de maio a igreja fecha às 17:00 e a última subida é às 16:45. De 1 de junho a "
  "31 de agosto está aberta até às 20:00, com a torre até às 19:45. Celebrações, cerimónias e concertos "
  "fecham a igreja a visitantes noutras alturas, por isso convém ver o programa do dia antes de montar a "
  "tarde à volta disto."),
 ("Vale a pena?",
  "Pela vista, vale: é o único ponto alto do centro antigo e o único de onde se veem os telhados "
  "coloridos a pique. Vinte minutos e 1.500 ISK é uma troca justa. Para um panorama mais largo, com toda "
  "a baía e as montanhas, a Perlan faz melhor, mas custa mais e leva meio dia."),
 ("Sobe-se de elevador até cima?",
  "Quase. Um elevador faz a maior parte da altura e depois há um lanço curto de escadas até ao "
  "miradouro. O miradouro é fechado, com aberturas nos quatro lados em vez de ser ao ar livre, pelo que "
  "funciona com qualquer tempo. É pequeno, e a igreja fecha-o quando enche."),
 ("Pode visitar-se a igreja de graça?",
  "Pode. A Hallgrímskirkja é uma paróquia em atividade e entrar para ver a nave e o órgão não custa nada "
  "durante o horário de abertura. Só se paga para subir. As celebrações são abertas a todos, mas "
  "enquanto decorrem o edifício não é uma paragem turística."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/tile-hallgrimskirkja.webp" width="800" height="600" alt="A Hallgrímskirkja vista de baixo, com a bandeira islandesa ao lado da torre" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reykjavik</a> › Hallgrímskirkja</p>
    <h1>Hallgrímskirkja: bilhetes, horários e quando subir à torre</h1>
    <p class="sub">A igreja é grátis. A torre não é, não se reserva, e no inverno deixa de deixar subir às 16:45.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, autor dos audioguias TouringBee">
      <span>Por Eugene · Atualizado a 29 de setembro de 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#hours">Horários e preços</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Visitas em Reykjavik</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">Duas coisas apanham as pessoas desprevenidas na Hallgrímskirkja. O bilhete da torre não se compra com antecedência, em lado nenhum e por preço nenhum. E de setembro a maio a última subida sai às 16:45 — em dezembro, bem antes de a maioria ter acabado de almoçar.</p>

<p>O resto é simples. A igreja visita-se de graça, fica no topo da rua que já ia subir de qualquer maneira, e a paragem inteira leva cerca de meia hora com a fila incluída.</p>

<p>Esta página trata da torre: quanto custa, quando abre, quando fecha por causa das celebrações e se a vista compensa face às alternativas. Faz par com <a href="{ONEDAY}">o nosso roteiro de um dia em Reykjavik</a>, onde esta torre é o ponto fixo à volta do qual o resto se dobra. Para a história do edifício em vez da logística, é <a href="#audio">o percurso com áudio da TouringBee</a> que trata disso.</p>

<div class="glance">
  <h2>Em resumo</h2>
  <dl>
    <dt>Entrada na igreja</dt><dd>Grátis</dd>
    <dt>Bilhete da torre</dt><dd>1.500 ISK adulto · 200 ISK criança 7–16 · 1.300 ISK estudante ou pessoa com deficiência</dd>
    <dt>Reserva</dt><dd>Impossível. Venda na loja da igreja, apenas para o próprio dia</dd>
    <dt>Horário de inverno</dt><dd>1 set – 31 mai: igreja 10:00–17:00, última subida 16:45</dd>
    <dt>Horário de verão</dt><dd>1 jun – 31 ago: igreja 09:00–20:00, torre até às 19:45</dd>
    <dt>Quanto demora</dt><dd>Cerca de 30 minutos com a fila</dd>
    <dt>Como se sobe</dt><dd>Elevador quase até cima e depois um lanço curto de escadas</dd>
    <dt>Altura</dt><dd>73 m segundo a própria igreja: o edifício mais alto da cidade</dd>
  </dl>
</div>

<div class="minicta">
  <h2>A igreja é uma paragem de um percurso mais longo</h2>
  <p>O percurso com áudio da TouringBee inclui a Hallgrímskirkja e <strong>outras 26 paragens</strong> pelo centro antigo: <strong>2 a 2,5 horas</strong>, mapa e áudio offline, ao seu ritmo.</p>
  <a {BUY}>Audioguia de Reykjavik — 9,99 €</a>
</div>

<h2 id="hours">O que se paga e o que não se paga</h2>

<p>A Hallgrímskirkja é uma paróquia luterana em atividade, não um museu, e a entrada é livre durante o horário de abertura. Dá para sentar na nave, olhar para o órgão e sair sem pagar nada. O bilhete diz respeito apenas à torre.</p>

<table class="tbl">
  <tr><th>Bilhete da torre</th><th>Preço</th></tr>
  <tr><td>Adultos</td><td>1.500 ISK</td></tr>
  <tr><td>Crianças dos 7 aos 16 anos</td><td>200 ISK</td></tr>
  <tr><td>Estudantes e pessoas com deficiência (com comprovativo)</td><td>1.300 ISK</td></tr>
  <tr><td>Maiores de 67</td><td>Tarifa reduzida; a igreja não publica o valor</td></tr>
  <tr><td>Grupos de 10 ou mais</td><td>10% de desconto</td></tr>
  <tr><td>Grupos escolares, alunos até aos 16</td><td>Grátis</td></tr>
</table>

<p>Online vão aparecer outros números. O portal turístico da própria Reykjavik ainda indicava 1.400 ISK e última entrada às 16:30 quando verificámos, em setembro de 2026. Muitos guias copiam também uma tabela de preços antiga que a igreja deixou no seu próprio site, por cima da que está em vigor. Os preços acima são os que ela cobra agora.</p>

<h2>Os horários, e o limite</h2>

<table class="tbl">
  <tr><th>Época</th><th>Igreja</th><th>Última subida</th></tr>
  <tr><td>1 de setembro – 31 de maio</td><td>10:00 – 17:00</td><td>16:45</td></tr>
  <tr><td>1 de junho – 31 de agosto</td><td>09:00 – 20:00</td><td>19:45</td></tr>
</table>

<p>É à volta dessas 16:45 que se planeia o dia, porque não acompanham a luz. No final de dezembro o sol já desapareceu às três e meia, por isso a torre e a luz aproveitável acabam ao mesmo tempo. Em fevereiro ainda há claridade às 16:45 e as pessoas perdem a subida exatamente por isso: o céu não parece hora de fecho.</p>

<p>Os outros encerramentos são menos previsíveis. A igreja fecha a visitantes durante celebrações, casamentos, funerais e concertos, e diz isso sem rodeios: os horários estão sujeitos a alteração. Também fecha o miradouro em certos eventos, e mais cedo do que o anunciado quando enche. A manhã de domingo é a forma mais fiável de chegar e encontrar a porta fechada.</p>

<h2>Comprar o bilhete</h2>

<p>A loja fica à esquerda de quem entra no átrio. É o único sítio onde o bilhete da torre existe. A formulação da igreja é esta: não é possível reservar a torre com antecedência. Sem venda online, sem horários marcados, sem acesso prioritário.</p>

<p>O que aparece anunciado online como bilhete para a Hallgrímskirkja é outra coisa: uma visita guiada que para à porta, ou um passe de cidade que talvez reembolse. O bilhete vale uma vez, no dia da compra, por isso não dá para comprar de manhã e usar ao anoitecer.</p>

<h2>A subida</h2>

<p>Um elevador faz quase toda a altura e um lanço curto de escadas faz o resto. O miradouro é fechado, com aberturas em arco nos quatro lados em vez de ser ao ar livre. É por isso que continua a funcionar num dia em que lá em baixo o vento desfaz chapéus de chuva.</p>

<p>O miradouro é pequeno. Em julho a parte lenta é a fila cá em baixo e não a subida, e a igreja prefere fazer esperar a amontoar gente lá em cima. Um quarto de hora chega bem.</p>

<figure>
  <img src="{P}img/tile-rainbow-street.webp" width="800" height="600" loading="lazy" alt="A Skólavörðustígur pintada com faixas de arco-íris, a subir na direção da Hallgrímskirkja">
  <figcaption>A rua que se sobe para chegar aqui. Do miradouro, desce-se outra vez com o olhar.</figcaption>
</figure>

<h2>O que se vê de facto</h2>

<p>Olhe para oeste e tem a imagem por que toda a gente vem. A Skólavörðustígur desce em faixas de arco-íris e atrás os telhados de chapa colorida do centro antigo empilham-se até ao porto, com a baía e o monte Esja ao fundo. É esta vista que justifica o bilhete. É também a única coisa que a Perlan não consegue dar: fica demasiado longe para olhar os telhados de cima.</p>

<p>A sul e a leste fica a Reykjavik residencial e, num dia limpo, a península de Reykjanes. A norte, o porto e a água. Não há um lado mau, mas quem tiver apenas um momento de céu limpo e uma máquina fotográfica deve escolher oeste.</p>

<p>Aqui a luz conta mais do que a hora. No verão o sol baixo do fim do dia resulta melhor do que o meio-dia. No inverno a janela é estreita de qualquer forma, e um céu encoberto achata os telhados num cinzento só — o que vale a pena saber antes de gastar 1.500 ISK na tarde errada.</p>

<h2>Por dentro, que não custa nada</h2>

<p>A nave leva 1.200 pessoas e é propositadamente despojada: branca, altíssima e quase sem decoração. Ao fundo está o órgão Klais, construído em Bona e terminado em 1992: 5.275 tubos, 15 metros de altura, cerca de 25 toneladas. Há ainda um segundo órgão mais pequeno, da dinamarquesa Frobenius, reconstruído e novamente consagrado em 2024. Vêm organistas de todo o mundo gravar no grande; se houver um ensaio a decorrer à entrada, vale a pena ficar.</p>

<p>A obra demorou. Guðjón Samúelsson, arquiteto do Estado, ganhou a encomenda nos anos trinta e não chegou a vê-la acabada. A construção foi de 1945 até à consagração em 1986, e entretanto a paróquia usou a cripta durante 26 anos. A fachada costuma ser descrita como colunas de basalto; a própria igreja compara-a à rocha colunar, às montanhas e aos glaciares islandeses.</p>

<p>Essa comparação é a versão que qualquer guia dá. Porque é que um arquiteto do Estado passou a carreira à procura de um estilo especificamente islandês é uma história mais longa, e o audioguia demora-se nela.</p>

<p>Mais uma coisa, cá fora. A estátua no largo já estava aqui antes da igreja, e não foi ideia da Islândia pô-la ali.</p>

<h2>Torre ou Perlan?</h2>

<table class="tbl">
  <tr><th></th><th>Hallgrímskirkja</th><th>Perlan</th></tr>
  <tr><td>Onde</td><td>No topo do centro antigo, a pé</td><td>Numa colina fora do centro, autocarro ou táxi</td></tr>
  <tr><td>A vista</td><td>A pique sobre os telhados coloridos e a rua do arco-íris</td><td>Panorama largo: baía, cidade, montanhas</td></tr>
  <tr><td>Miradouro</td><td>Fechado e pequeno</td><td>Terraço aberto, mais exposições</td></tr>
  <tr><td>Bilhete</td><td>1.500 ISK, só na bilheteira</td><td>Mais caro; confirme o preço atual, muda</td></tr>
  <tr><td>Tempo</td><td>30 minutos</td><td>Meio dia com a deslocação</td></tr>
</table>

<p>Num único dia na cidade, a torre ganha só pelo tempo. Com dois dias e um deles de chuva, a Perlan é o melhor edifício para dia mau, porque lá dentro há o que fazer.</p>

<div class="ticketbox">
  <h3>A torre não se reserva — o que está à volta, sim</h3>
  <p>Para a Hallgrímskirkja em si não há nada para reservar. Para o que a rodeia há: a Perlan, as lagoas e as visitas guiadas que passam pela igreja vendem horário marcado com antecedência.</p>
  <a class="btn sm" href="{TIQETS}" {OTA}>Bilhetes em Reykjavik</a>
  <a class="btn sm outline" href="{GYG}" {OTA}>Comparar visitas guiadas</a>
</div>

<h2>Três situações</h2>

<h3>Tem algumas horas entre voos</h3>
<p>A torre é o melhor uso de uma escala curta: vinte minutos a pé desde a paragem de autocarro no centro, e a cidade inteira de uma vez. Suba primeiro e só depois desça para o centro antigo, não ao contrário.</p>

<h3>É domingo</h3>
<p>As celebrações da manhã fecham a igreja a visitantes. Vá depois do almoço; no inverno isso ainda deixa folga confortável antes das 16:45.</p>

<h3>O tempo virou</h3>
<p>Não risque a torre. O miradouro é fechado e o vento que estraga a rua lá em cima não incomoda. O verdadeiro estraga-prazeres é a nuvem baixa: se não se vê o Esja do passeio, também não se verá grande coisa a 73 metros.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>O audioguia</h2>
    <p class="lead" style="max-width:720px">Do miradouro vê-se o aspeto de Reykjavik. Porque é que a cidade cresceu exatamente ali, o que faz aquela estátua no largo e o que o arquiteto estava mesmo a construir são perguntas diferentes.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="A aplicação TouringBee com o percurso de Reykjavik, à frente da Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">Audioguia TouringBee de Reykjavik</h3>
        <p class="meta" style="margin:0 0 10px">27 paragens · 2 a 2,5 horas · um ano de acesso</p>
        <div class="rate">{STARS}<b>4,7</b> {RATELABEL}</div>
        <div class="price">9,99 €<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>A Hallgrímskirkja é uma das 27 paragens</strong>: o percurso vai da colina do fundador ao porto velho</li>
          <li><strong>Funciona totalmente offline</strong> depois de descarregado, com mapa e ilustrações</li>
          <li><strong>Ao seu ritmo.</strong> Pare para subir à torre e retome onde ficou</li>
          <li><strong>Um único pagamento.</strong> Sem grupo, sem horário e sem um guia à sua espera</li>
        </ul>
        <a {BUY} style="width:100%">Percorrer Reykjavik com o audioguia</a>
        <p class="meta" style="margin:12px 0 0;text-align:center">{CHECKOUTNOTE} <a href="{TBPRODUCT}" rel="noopener" data-no-widget>{OPENSHOP}</a>.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap prose">

<h2>Cinco erros</h2>
<ol>
  <li><strong>Procurar bilhetes online.</strong> Não existem. A loja dentro da igreja é o único ponto de venda.</li>
  <li><strong>Deixar a torre para o fim da tarde entre setembro e maio.</strong> Última subida às 16:45, faça o céu o que fizer.</li>
  <li><strong>Aparecer num domingo de manhã.</strong> As celebrações fecham a igreja a visitantes.</li>
  <li><strong>Confiar num preço lido num diretório.</strong> Vários continuam a mostrar 1.400 ISK e as 16:30.</li>
  <li><strong>Subir com nuvem baixa.</strong> Se o Esja não se vê da rua, guarde o bilhete para amanhã.</li>
</ol>

<h2>Perguntas frequentes</h2>
<div class="faq">{FAQHTML}</div>

<h2>Continuar a ler</h2>
<ul>
  <li><a href="{ONEDAY}">Reykjavik num dia</a> — o roteiro de que esta torre é o eixo</li>
  <li><a href="{KEF}">Do aeroporto de Keflavík ao centro</a> — como chegar antes de tudo o resto</li>
  <li><a href="{HOME}">O guia completo de Reykjavik</a> — o percurso, as excursões e as estações</li>
  <li><a href="{GUIDES}">Todos os guias de Reykjavik</a> — o que está publicado e o que vem a caminho</li>
</ul>

<h2>Em duas linhas</h2>
<p>Entre de graça, pague 1.500 ISK na loja se quiser a vista, e faça-o antes das 16:45 no inverno. Olhe para oeste por causa dos telhados. Meia hora, e é a melhor meia hora que o centro antigo põe à venda.</p>
<p>E quem preferir perceber o que tem por baixo em vez de apenas olhar, leve <a href="#audio">o audioguia TouringBee</a>: 27 paragens pelo centro, esta incluída, totalmente offline.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">A igreja é a paragem um de vinte e sete</h2>
  <p>Esta página leva-o à torre à hora certa. O audioguia diz-lhe o que é a cidade lá em baixo.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Começar o percurso — 9,99 €</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Encontrar hotel no centro</a>
  </div>
</div>

<p class="disc">Alguns links desta página são de afiliação: se reservar através deles podemos receber uma comissão, sem custo adicional para si. Preços e horários verificados em hallgrimskirkja.is em setembro de 2026; mudam sem aviso, confirme antes de viajar.</p>

  </div>
</section>
"""
