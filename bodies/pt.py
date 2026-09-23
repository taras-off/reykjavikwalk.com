# -*- coding: utf-8 -*-
"""PT-PT — escrito em português europeu, não traduzido.

Registo: 3.ª pessoa (Comece / Suba / ao seu ritmo). Nenhuma forma de «tu» no texto.
As histórias ficam para o audioguia.
"""

HEADLINE = "Reykjavik num dia: o que ver e por que ordem"
TITLE = "Reykjavik num dia: o que ver e percurso a pé"
DESC = ("O que ver em Reykjavik num dia: um percurso a pé montado sobre os dois limites que decidem o "
        "dia, as horas de luz e a última subida à torre às 16:45.")

FAQ = [
 ("Um dia chega para Reykjavik?",
  "Para a cidade em si, chega. O centro antigo atravessa-se em vinte minutos e o percurso a pé clássico "
  "tem cerca de 5 km, pelo que um dia o cobre com folga para paragens. Um dia não chega para acrescentar o "
  "Círculo Dourado ou a costa sul: são dias à parte, e grande parte de cada um passa-se dentro de um "
  "veículo."),
 ("A que horas convém começar no inverno?",
  "Em dezembro, procure estar na rua pelas 10:30 e trate as 16:45 como um limite rígido: é a última subida "
  "à torre da Hallgrímskirkja de setembro a maio. Tudo o que vem depois de escurecer continua a funcionar — "
  "o porto, a piscina, o jantar. O miradouro e as fotografias, não."),
 ("Preciso do audioguia se já tenho este percurso?",
  "Esta página responde ao onde e ao quando: horários, reservas e um plano alternativo quando o tempo "
  "piora. O audioguia responde ao que está a ver exatamente e porque é que tem interesse: 27 histórias ao "
  "longo da mesma linha. O percurso serve-lhe de plano do dia e o TouringBee de narração pelo caminho."),
 ("É preciso carro para um dia em Reykjavik?",
  "Não. O dia na cidade faz-se a pé e é plano, tirando uma subida. Os autocarros Strætó cobrem tudo o que "
  "fica mais longe por 690 ISK por viagem. O carro só começa a compensar quando se sai da cidade."),
 ("Quanto custa um dia em Reykjavik?",
  "Andar a pé não custa nada. As despesas fixas são pequenas: 1.500 ISK pela torre e 690 ISK pelo "
  "autocarro. O que mexe com o total é a lagoa e o jantar — juntos podem pesar mais do que tudo o resto."),
 ("O que convém reservar antes de chegar?",
  "Para um dia normal na cidade, sobretudo a lagoa: a Sky Lagoon e a Blue Lagoon funcionam por horários "
  "marcados e os do fim da tarde, que são os mais procurados, podem esgotar com antecedência. No verão, "
  "acrescente a saída para ver baleias com um dia de margem. O resto decide-se na própria manhã."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/hero-1536.webp" width="1536" height="864" alt="A marginal de Reykjavik sob um céu islandês enorme" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reykjavik</a> › Um dia em Reykjavik</p>
    <h1>Reykjavik num dia: o que ver, e um percurso que aguenta as horas de luz</h1>
    <p class="sub">Dois limites decidem este dia: quantas horas de luz lhe calham, e as 16:45. Todo o resto é negociável.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, autor dos audioguias TouringBee">
      <span>Por Eugene · Atualizado a 23 de setembro de 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#plan">Ir para o plano</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Excursões de um dia</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">No final de dezembro o sol passa por cima dos telhados por volta das 11:20 e às três e meia já desapareceu. A última subida à torre da Hallgrímskirkja sai às 16:45. O seu dia inteiro em Reykjavik cabe entre estas duas horas.</p>

<p>O que se segue não é, por isso, uma lista de monumentos, mas um horário. O centro antigo atravessa-se em vinte minutos e o percurso completo tem cerca de 5 km. Aqui o problema não são as pernas. São a luz e as horas de fecho.</p>

<p>O dia inteiro pode ser feito só com esta página. Se também quiser saber o que está por trás dos sítios por onde passa, <a href="#audio">o percurso com áudio da TouringBee</a> segue a mesma linha. Ainda está a montar a viagem toda? Comece pelo <a href="{HOME}">nosso guia completo de Reykjavik</a>.</p>

<div class="glance">
  <h2>Em resumo</h2>
  <dl>
    <dt>A pé</dt><dd>Cerca de 5 km, plano tirando a subida da Skólavörðustígur</dd>
    <dt>Forma do dia</dt><dd>Centro antigo → a igreja e a sua torre → a marginal → água quente</dd>
    <dt>Hora limite</dt><dd>16:45 — última subida à torre, de 1 de setembro a 31 de maio</dd>
    <dt>Bilhete da torre</dt><dd>1.500 ISK adultos · 200 ISK crianças dos 7 aos 16 · só na bilheteira</dd>
    <dt>Autocarro</dt><dd>690 ISK por viagem na rede Strætó</dd>
    <dt>Reservar antes</dt><dd>A lagoa — a reserva principal a tratar antes de chegar</dd>
    <dt>Pior mês para improvisar</dt><dd>Dezembro: cerca de quatro horas de luz aproveitáveis</dd>
  </dl>
</div>

<div class="minicta">
  <h2>Faça este percurso com o audioguia</h2>
  <p>A mesma linha pelo centro, contada: <strong>27 paragens, 2 a 2,5 horas</strong>, mapa e áudio offline. Pare para a torre, para almoçar ou para um museu e retome onde ficou.</p>
  <a {BUY}>Audioguia de Reykjavik — 9,99 €</a>
</div>

<h2 id="plan">Verifique primeiro duas coisas: o pôr do sol e a torre</h2>

<p>O primeiro limite é o sol, e não facilita. Reykjavik fica mesmo abaixo do Círculo Polar Árctico, pelo que a diferença entre pleno verão e pleno inverno é maior do que em quase todos os destinos habituais.</p>

<table class="tbl">
  <tr><th>Mês</th><th>Luz aproveitável</th><th>O que muda para um só dia</th></tr>
  <tr><td>Dezembro – janeiro</td><td>4 a 5 horas</td><td>Um bloco na rua, não dois. O resto acontece às escuras, e não faz mal nenhum.</td></tr>
  <tr><td>Fevereiro – abril</td><td>Aumenta depressa</td><td>O percurso todo com luz, e noites ainda escuras o suficiente para procurar a aurora.</td></tr>
  <tr><td>Maio – julho</td><td>Praticamente o dia inteiro</td><td>Pode arrancar ao meio-dia ou às nove da noite. O limite da luz desaparece; é também época alta.</td></tr>
  <tr><td>Agosto – novembro</td><td>Diminui depressa</td><td>Setembro e outubro são um bom compromisso entre horas de luz e noites escuras o suficiente para a aurora.</td></tr>
</table>

<p>O segundo limite é a torre. A Hallgrímskirkja continua a ser o único ponto alto do centro e, de 1 de setembro a 31 de maio, a igreja fecha às 17:00, com a última subida às 16:45. No verão fica aberta até às 20:00 e a torre até às 19:45. Os bilhetes não se reservam e valem uma vez no dia da compra, pelo que não é uma coisa que se encaixe quando der mais jeito.</p>

<table class="tbl">
  <tr><th>Bilhete da torre</th><th>Preço</th></tr>
  <tr><td>Adultos</td><td>1.500 ISK</td></tr>
  <tr><td>Crianças dos 7 aos 16 anos</td><td>200 ISK</td></tr>
  <tr><td>Estudantes, maiores de 67, pessoas com deficiência</td><td>1.300 ISK</td></tr>
</table>

<p>Celebrações e concertos fecham a igreja aos visitantes com pouco aviso, por isso vale a pena espreitar o programa do dia antes de construir a tarde à volta da torre.</p>

<figure>
  <img src="{P}img/tile-hallgrimskirkja.webp" width="800" height="600" loading="lazy" alt="A Hallgrímskirkja vista de baixo, com a bandeira islandesa ao lado da torre">
  <figcaption>A única paragem do dia com hora de fecho — e a única por que vale a pena reorganizar tudo.</figcaption>
</figure>

<h2>Manhã: o centro antigo</h2>

<p>Comece em Arnarhóll, a colina verde por cima da estrada do porto, onde a estátua do fundador da cidade olha para a baía. O sítio não foi ele que o escolheu. Deixou que outra coisa escolhesse por ele, e essa é uma história com que o audioguia se demora.</p>

<p>Dali o centro antigo abre-se em descida ao longo de três ruas. A praça Austurvöllur tem o parlamento de um dos lados. Tjörnin, o lago, tem a câmara municipal assente lá dentro sobre estacas. Pelo meio ficam os museus pequenos, incluindo o que foi construído à volta de uma parede de casa comprida escavada debaixo do passeio. Nada disto demora muito. Tudo isto se atravessa de graça.</p>

<p>Duas notas práticas. A Islândia funciona a cartão de forma extrema: dá para passar cá uma semana sem tocar em dinheiro vivo, e vários sítios já não o aceitam. E a água da torneira é excelente e gratuita em todo o lado, por isso uma garrafa reutilizável poupa mais do que parece.</p>

<h2>Meio-dia: a rua do arco-íris e depois a torre</h2>

<p>A Skólavörðustígur sobe da rua comercial até à porta da igreja, e o seu último troço está pintado com faixas de arco-íris permanentes. É um dos sítios mais fotografados de Reykjavik. Cedo ou ao fim da tarde, está quase vazia; entre as onze e as três no verão, não.</p>

<p>Suba à torre agora, não a deixe para o fim do dia. No inverno, é precisamente para isto que a manhã foi comprimida. No verão há mais folga, embora costume estar mais calmo logo cedo ou perto da última subida.</p>

<h2>Almoço, e a reserva a tratar</h2>

<p>Come-se na Laugavegur e nas ruas ao lado. O clássico barato é a <em>pylsa</em> islandesa: um cachorro feito com uma mistura de borrego, porco e vaca. Peça <em>eina með öllu</em>, «um com tudo». No inverno, uma sopa de borrego faz o mesmo trabalho. Os restaurantes com serviço à mesa são caros a sério: é aí que um dia em Reykjavik deixa de ser barato.</p>

<div class="ticketbox">
  <h3>Reserve a lagoa antes de voar</h3>
  <p>A Sky Lagoon e a Blue Lagoon funcionam por horários marcados, e os do fim da tarde, que são os mais procurados, podem esgotar com antecedência. Para um dia normal na cidade, esta é a reserva principal a tratar antes de chegar.</p>
  <a class="btn sm" href="{TIQETS}" {OTA}>Ver bilhetes para a lagoa</a>
  <a class="btn sm outline" href="{GYG}" {OTA}>Comparar excursões e transferes</a>
</div>

<h2>Tarde: a marginal</h2>

<p>A segunda metade do dia corre junto ao mar. A Harpa, a sala de concertos de vidro na beira do porto, entra-se livremente e num dia limpo merece cinco minutos parado lá dentro. Mais à frente, no caminho da Sæbraut, está o Sun Voyager, a escultura de aço que toda a gente fotografa como se fosse um barco viking. Não é, e a razão verdadeira é melhor do que o mito.</p>

<figure>
  <img src="{P}img/sec-sun-voyager.webp" width="1024" height="683" loading="lazy" alt="Uma visitante passa junto à escultura Sun Voyager na marginal da Sæbraut no inverno">
  <figcaption>Fotografada sem parar e quase sempre identificada de forma errada.</figcaption>
</figure>

<p>Depois o porto velho: os barcos para ver baleias, os restaurantes de peixe e um navio cinzento da guarda costeira atracado, com um historial de combate contra uma marinha muito maior. Quem seguir até ao fim chega ao montículo de relva onde o percurso em áudio termina.</p>

<p>É aqui que está a única decisão a sério da tarde. Uma saída para ver baleias a partir do porto velho leva cerca de três horas e come toda a luz que resta. No verão compensa, se foi pelos animais que veio; em dezembro é uma má troca, porque essas três horas são toda a luz que há.</p>

<h2>Noite: primeiro água quente, depois jantar</h2>

<p>Os islandeses acabam o dia na água e não no bar, e há dois níveis à escolha.</p>

<p>A Sky Lagoon é a versão polida: à beira do oceano, a quinze minutos do centro, com um ritual de sete passos já incluído no bilhete. O passe Saman começa por volta dos 113 € por adulto (57 € para jovens); o Sér, com balneários privados, por volta dos 136 €.</p>

<p>A opção local é uma piscina municipal geotérmica: a Sundhöllin no centro, a Laugardalslaug para o complexo completo. Aquecidas a partir do subsolo, abertas até tarde e por uma fração do preço da lagoa; o preço de adulto em vigor está em reykjavik.is. Uma regra conta mais do que todas as outras: antes de entrar na água toma-se um duche completo, sem fato de banho. Está afixado em todos os balneários e é cumprido.</p>

<h2>Três variantes</h2>

<h3>Uma escala, não um dia</h3>
<p>Para quem está entre voos com seis ou sete horas na cidade, corte a metade da marginal. Autocarro desde Keflavík, centro antigo e torre, almoço na Laugavegur, autocarro de volta. Isto cabe numa escala curta com o transfer dos dois lados e ainda assim dá a melhor vista da cidade.</p>

<h3>Um dia de dezembro</h3>
<p>Comprima tudo o que é na rua entre as 11:00 e as 15:30 e aceite que o porto, o jantar e a piscina acontecem às escuras. Não é uma versão menor: as luzes do porto na água ganham à versão diurna. E a longa metade escura do dia é a sua hipótese de ver a aurora, se a nebulosidade e a atividade solar ajudarem. O troço escuro da marginal da Sæbraut é o mais fácil a partir da cidade. O farol de Grótta, um autocarro para oeste, é mais escuro ainda. Mas nenhum deles substitui uma saída a sério para longe das luzes da cidade.</p>

<h3>Um dia molhado e com vento de lado</h3>
<p>O tempo muda de hora a hora e o estrago é feito pelo vento. Num dia mau, inverta o plano: museus e piscina a meio do dia, a caminhada na janela que abrir. O chapéu de chuva aqui serve de pouco: uma rajada forte vira-o do avesso. Um casaco impermeável com capuz e um gorro são mais fiáveis, em qualquer mês.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>O audioguia</h2>
    <p class="lead" style="max-width:720px">Ver o percurso é uma coisa. Perceber porque é que Reykjavik acabou por nascer precisamente aqui, o que representa na verdade o Sun Voyager e como é que um país tão pequeno conseguiu discutir com outros bem maiores é outra.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="A aplicação TouringBee com o percurso de Reykjavik, à frente da Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">Audioguia TouringBee de Reykjavik</h3>
        <p class="meta" style="margin:0 0 10px">27 paragens · 2 a 2,5 horas · um ano de acesso</p>
        <div class="rate">{STARS}<b>4,7</b> {RATELABEL}</div>
        <div class="price">9,99 €<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Funciona totalmente offline</strong> depois de descarregado — mapa e ilustrações incluídos, sem gastar dados pelo caminho</li>
          <li><strong>Ao seu ritmo.</strong> Pare para almoçar ou para um museu e retome duas horas depois no mesmo ponto</li>
          <li><strong>Narrado na pele</strong> de um pescador de Reykjavik que tem tempo até voltar ao mar</li>
          <li><strong>Um único pagamento.</strong> Sem grupo, sem horário e sem um guia à sua espera</li>
        </ul>
        <a {BUY} style="width:100%">Percorrer Reykjavik com o audioguia</a>
        <p class="meta" style="margin:12px 0 0;text-align:center">{CHECKOUTNOTE} <a href="{TBPRODUCT}" rel="noopener">{OPENSHOP}</a>.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap prose">

<h2>Quanto custa o dia</h2>
<table class="tbl">
  <tr><th>Item</th><th>Custo</th></tr>
  <tr><td>Percorrer a cidade a pé</td><td>Grátis</td></tr>
  <tr><td>Audioguia, pagamento único</td><td>9,99 €</td></tr>
  <tr><td>Torre da Hallgrímskirkja, adulto</td><td>1.500 ISK</td></tr>
  <tr><td>Viagem simples de Strætó</td><td>690 ISK</td></tr>
  <tr><td>Piscina municipal</td><td>Uma fração do preço da lagoa</td></tr>
  <tr><td>Sky Lagoon, passe Saman</td><td>a partir de cerca de 113 €</td></tr>
  <tr><td>Baleias, cerca de 3 horas</td><td>Preço do operador; o custo verdadeiro é a luz</td></tr>
</table>

<p>A cidade em si não é cara. O orçamento sobe de repente quando se acrescentam a lagoa, as excursões fora da cidade e os jantares de restaurante.</p>

<h2>Cinco erros que custam o dia</h2>
<ol>
  <li><strong>Deixar a torre para o fim no inverno.</strong> Última subida às 16:45, de setembro a maio, e os bilhetes vendem-se apenas na bilheteira.</li>
  <li><strong>Encaixar o Círculo Dourado num dia de cidade.</strong> São oito horas dentro de um veículo. Merece um dia só para ele.</li>
  <li><strong>Dar quase toda a luz de dezembro a um barco.</strong> Três horas no mar quando há quatro horas de luz.</li>
  <li><strong>Contar com o chapéu de chuva.</strong> O vento vira-o do avesso. Camadas, capuz e gorro em vez dele.</li>
  <li><strong>Tratar a lagoa como um sítio onde se entra sem mais.</strong> Funciona por horários marcados, e os do fim da tarde são os primeiros a ir.</li>
</ol>

<h2>Perguntas frequentes</h2>
<div class="faq">{FAQHTML}</div>

<h2>Continuar a ler</h2>
<ul>
  <li><a href="{HOME}">O guia completo de Reykjavik</a> — o percurso, as excursões e as estações</li>
  <li><a href="{GUIDES}">Todos os guias de Reykjavik</a> — o que está publicado e o que vem a caminho</li>
</ul>

<h2>Em duas linhas</h2>
<p>Reykjavik entrega quase tudo o que tem num dia a pé. As distâncias nunca vão ser o problema. A luz vai.</p>
<p>Por isso confirme o pôr do sol, não deixe a torre para a noite e faça o resto ao seu ritmo. E se quiser perceber a cidade pelo caminho em vez de apenas olhar para ela, leve <a href="#audio">o audioguia TouringBee de Reykjavik</a>: 27 paragens, 2 a 2,5 horas, totalmente offline.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">Vinte e sete paragens na mesma linha</h2>
  <p>Esta página leva-o ao sítio certo à hora certa. O audioguia diz-lhe o que tem à frente.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Começar o percurso — 9,99 €</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Encontrar hotel no centro</a>
  </div>
</div>

<p class="disc">Alguns links desta página são de afiliação: se reservar através deles podemos receber uma comissão, sem custo adicional para si. Preços e horários verificados nos sites dos operadores em setembro de 2026; mudam sem aviso, confirme antes de viajar. Torre: hallgrimskirkja.is. Autocarros: straeto.is. Lagoa: skylagoon.com.</p>

  </div>
</section>
"""
