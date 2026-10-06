# -*- coding: utf-8 -*-
"""PT-PT — registo: 3.ª pessoa (Comece / Pergunte / ao seu ritmo). Nenhuma forma de «tu»."""

HEADLINE = "Do aeroporto de Keflavík a Reykjavik: que transfer encaixa na hora de aterragem"
TITLE = "Keflavík a Reykjavik: autocarro, táxi ou carro"
DESC = ("De Keflavík a Reykjavik: os preços reais do Flybus, do autocarro público e do carro, e o "
        "que fazer das horas entre a aterragem e o check-in no hotel.")

FAQ = [
 ("Qual é a forma mais barata de ir do aeroporto de Keflavík a Reykjavik?",
  "O autocarro público, a carreira Strætó 55, a 2.400 ISK por adulto. Jovens dos 12 aos 17, pessoas com "
  "mais de 67 anos e passageiros com deficiência pagam 1.200 ISK, e as crianças até aos 12 viajam de "
  "graça. Circula todos os dias mas não a cada chegada, e nem todas as viagens acabam no BSÍ: algumas "
  "terminam em Fjörður, em Hafnarfjörður, que não é o centro da cidade."),
 ("Quanto tempo demora de Keflavík a Reykjavik?",
  "Cerca de 45 minutos de autocarro para uns 50 km, e praticamente o mesmo de carro. O tempo não se "
  "perde no percurso. Perde-se à espera do autocarro, que sai 35 a 45 minutos depois da aterragem, e "
  "depois outra vez, porque o quarto só fica pronto à tarde."),
 ("É preciso reservar o autocarro com antecedência?",
  "Habitualmente não. O Flybus vende bilhetes no aeroporto e também online, e as partidas acompanham os "
  "voos que chegam. O bilhete online poupa alguma coisa, evita a fila depois de um voo longo e compensa "
  "em datas cheias. Se o voo atrasar, o operador passa o seu lugar para a partida seguinte em vez de "
  "segurar o autocarro."),
 ("O Flybus leva até ao meu hotel?",
  "A tarifa normal leva-o ao terminal BSÍ. O Flybus+ continua de miniautocarro até aos hotéis aderentes, "
  "mediante suplemento. Se o alojamento for no centro antigo, o bilhete normal mais uma caminhada curta "
  "costuma ser mais rápido do que esperar pela volta do miniautocarro."),
 ("Compensa alugar carro só para o transfer?",
  "Por si só não. Uma estrada, 45 minutos e, no fim, um carro para estacionar numa cidade que se "
  "atravessa a pé. O aluguer começa a fazer sentido quando o aeroporto é o início de uma viagem por "
  "estrada: o Círculo Dourado, a costa sul, tudo o que fica fora da capital. A pergunta verdadeira é se "
  "vai sair da cidade."),
 ("Onde deixar a bagagem antes do check-in?",
  "Comece por perguntar no hotel: um quarto que não está pronto não é o mesmo que um hotel que não pode "
  "ajudar, e a maioria guarda as malas até ao check-in sem cobrar. Caso contrário, há cacifos em "
  "Keflavík e no BSÍ, os do BSÍ abertos 24 horas, com 96 cacifos de quatro tamanhos."),
]

BODY_TMPL = """
<div class="arthero">
  <img class="bg" src="{P}img/sec-old-town.webp" width="1024" height="683" alt="Uma bicicleta encostada a uma montra no centro antigo de Reykjavik" fetchpriority="high">
  <div class="wrap">
    <p class="crumb"><a href="{HOME}">Reykjavik</a> › Do aeroporto de Keflavík ao centro</p>
    <h1>Do aeroporto de Keflavík a Reykjavik: as opções, e qual encaixa na sua hora de aterragem</h1>
    <p class="sub">Cinquenta quilómetros, uma estrada, quarenta e cinco minutos. O transfer é a parte fácil; o intervalo entre aterrar e entrar no quarto não é.</p>
    <div class="byline"><img src="{P}img/author-eugene.webp" width="36" height="36" loading="lazy" alt="Eugene, autor dos audioguias TouringBee">
      <span>Por Eugene · Atualizado a 5 de outubro de 2026</span></div>
    <div class="btnrow">
      <a {BUY}>{BUYLABEL}</a>
      <a class="btn dark" href="#options">Comparar as opções</a>
      <a class="btn ghost" href="{GYG}" {OTA}>Transferes e excursões</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap prose">

<p class="lead">De Keflavík a Reykjavik há uma única estrada e demora cerca de 45 minutos. O autocarro do aeroporto acerta as partidas pelos voos que chegam: costuma sair 35 a 45 minutos depois de uma aterragem, com um horário que começa por volta das 03:30 e vai até ao fim da noite. Chegar à cidade é um problema resolvido.</p>

<p>Por resolver está a hora a que aterra. Em Reykjavik o check-in nos hotéis é normalmente às 14:00 ou às 15:00. Quem aterra antes chega à cidade com as malas, o quarto fechado e várias horas para encher — e é isso, não os 50 km, que decide o bilhete a comprar.</p>

<p>Por isso esta página faz as duas metades: as opções de transfer com os preços que os operadores cobram mesmo, e depois o que fazer com o intervalo. Se ele o deixar no centro com tempo, <a href="{ONEDAY}">o nosso roteiro de um dia</a> e <a href="#audio">o percurso com áudio da TouringBee</a> foram feitos exatamente para essas horas. A montar a viagem toda? Comece pelo <a href="{HOME}">guia completo de Reykjavik</a>.</p>

<div class="glance">
  <h2>Em resumo</h2>
  <dl>
    <dt>Distância</dt><dd>Cerca de 50 km do aeroporto ao centro de Reykjavik</dd>
    <dt>Viagem</dt><dd>Cerca de 45 minutos de autocarro ou de carro</dd>
    <dt>Flybus</dt><dd>A partir de 3.999 ISK por viagem até ao terminal BSÍ</dd>
    <dt>Autocarro público</dt><dd>Strætó 55 — 2.400 ISK adulto, 1.200 ISK reduzido, grátis até aos 12 anos</dd>
    <dt>Partidas</dt><dd>O Flybus acompanha as chegadas, das 03:30 ao fim da noite; o Strætó cumpre horário fixo</dd>
    <dt>Reserva</dt><dd>Habitualmente não é preciso. Há bilhetes no aeroporto</dd>
    <dt>Bagagem</dt><dd>Pergunte primeiro no hotel; há cacifos no aeroporto e no BSÍ</dd>
    <dt>A verdadeira restrição</dt><dd>O check-in às 14:00–15:00, não o transfer</dd>
  </dl>
</div>

<div class="minicta">
  <h2>Aterra cedo? É essa a janela do percurso</h2>
  <p>O percurso com áudio da TouringBee são <strong>27 paragens e 2 a 2,5 horas</strong> pelo centro antigo, com mapa e áudio offline. Resolvidas as malas, as horas mortas antes do check-in passam a ser a melhor parte do primeiro dia.</p>
  <a {BUY}>Audioguia de Reykjavik — 9,99 €</a>
</div>

<h2 id="options">Comece pela hora de aterragem, não pelo preço</h2>

<p>Todos os guias sobre esta ligação comparam tarifas. Mas o preço é só metade da conta: um bilhete barato deixa de compensar no momento em que o seu horário acrescenta uma hora de espera.</p>

<p>Pergunte antes outra coisa: a que horas tocam as rodas na pista e onde é que vai dormir? Quem aterra ao meio-dia com o quarto pronto às duas pode usar qualquer coisa. Quem aterra às seis da manhã precisa de um plano para a bagagem e de outro para si. O autocarro mais barato não serve todos os voos, por isso pode custar-lhe uma hora que preferia ter gasto noutro sítio.</p>

<table class="tbl">
  <tr><th>Opção</th><th>Preço</th><th>Deixa em</th><th>Quando é a sua</th></tr>
  <tr><td><strong>Flybus</strong></td><td>desde 3.999 ISK por viagem</td><td>Terminal BSÍ</td><td>Por defeito. Partidas ligadas às chegadas; em caso de atraso o lugar passa para o autocarro seguinte</td></tr>
  <tr><td><strong>Flybus+</strong></td><td>suplemento</td><td>Hotéis aderentes</td><td>Muita bagagem, crianças, mau tempo ou alojamento fora do centro</td></tr>
  <tr><td><strong>Airport Direct</strong></td><td>tarifa a confirmar</td><td>Terminal central, premium até ao hotel</td><td>O segundo autocarro regular: vale comparar o preço com o Flybus</td></tr>
  <tr><td><strong>Strætó 55</strong></td><td>2.400 ISK adulto</td><td>BSÍ ou Fjörður</td><td>De dia, com pouca bagagem, se o horário der</td></tr>
  <tr><td><strong>Táxi ou transfer privado</strong></td><td>Ao taxímetro ou por orçamento</td><td>À sua porta</td><td>São três ou quatro, ou a hora é má</td></tr>
  <tr><td><strong>Carro alugado</strong></td><td>Tarifa diária</td><td>Onde quiser</td><td>Só se depois sair da cidade</td></tr>
</table>

<h2>O Flybus, e porque é a opção por defeito</h2>

<p>É o autocarro do aeroporto que a maioria apanha, e o que vende não é velocidade mas certeza. As partidas acompanham os voos que chegam em vez de seguirem um intervalo fixo: normalmente 35 a 45 minutos depois de uma aterragem. O horário publicado começa por volta das 03:30 e vai até ao fim da noite, por isso, num voo muito cedo ou muito tarde, confirme o horário da sua data em vez de confiar na regra geral.</p>

<p>Se o voo atrasar, o operador não segura o autocarro: garante-lhe lugar na partida seguinte, sem custo adicional. É uma diferença relevante e vale a pena saber antes de ficar nervoso na fila do controlo de passaportes. A tarifa inclui duas malas até 23 kg cada.</p>

<p>O bilhete normal termina no BSÍ, a central de camionagem no limite sul do centro. O Flybus+ acrescenta um troço de miniautocarro até aos hotéis aderentes, com suplemento. Compensa com bagagem pesada, com crianças, com mau tempo e quando o alojamento fica na periferia.</p>

<p>Quem viaja leve e fica no centro antigo deve comparar: o miniautocarro percorre uma lista de moradas e a sua pode não ser a primeira. Veja a que distância fica o hotel do BSÍ e decida por aí, e não por hábito.</p>

<h2>Strætó 55, a opção barata e a sua armadilha</h2>

<p>O autocarro público é a carreira 55 e custa 2.400 ISK por adulto: 1.200 ISK dos 12 aos 17, para maiores de 67 e passageiros com deficiência, e grátis até aos 12. Para uma família, essa diferença é dinheiro a sério.</p>

<p>Duas armadilhas. Cumpre horário e não o seu voo, por isso uma aterragem às 05:30 pode significar uma longa espera. E nem todas as viagens acabam no BSÍ: algumas terminam em Fjörður, em Hafnarfjörður, um concelho a sul de Reykjavik que não é de todo o centro. Confirme o destino antes de entrar, e não depois.</p>

<div class="ticketbox">
  <h3>Transferes privados e excursões</h3>
  <p>Sendo três ou quatro, calcule a tarifa do autocarro por pessoa contra um único veículo antes de assumir que o autocarro sai mais barato. Os transferes privados e as excursões que recolhem em Keflavík vendem-se com antecedência.</p>
  <a class="btn sm" href="{GYG}" {OTA}>Comparar transferes</a>
  <a class="btn sm outline" href="{TIQETS}" {OTA}>Bilhetes em Reykjavik</a>
</div>

<h2>O táxi, e quando a distância encurta</h2>

<p>Os táxis islandeses andam ao taxímetro e não há tarifa fixa publicada para o aeroporto, por isso trate o táxi como a opção cara e peça uma estimativa antes de entrar.</p>

<p>Para três ou quatro pessoas, peça uma estimativa atual e compare-a com o total dos bilhetes de autocarro. O táxi cobra-se por veículo e o autocarro por passageiro, por isso a distância encurta à medida que o grupo cresce. Isso não torna o táxi barato, apenas mais próximo do que parece para quem viaja sozinho.</p>

<h2>O carro alugado, com honestidade</h2>

<p>Só para o transfer, não. É uma estrada a direito que fará uma vez e, no fim, um carro para estacionar numa cidade que se atravessa a pé. O aluguer começa a fazer sentido quando o aeroporto é o início de uma viagem por estrada: o Círculo Dourado, a costa sul, tudo o que fica fora da capital. Decida pela viagem, não pelo transfer.</p>

<figure>
  <img src="{P}img/sec-winter-street.webp" width="1024" height="683" loading="lazy" alt="Uma loja de esquina de cores vivas numa rua com neve no centro de Reykjavik">
  <figcaption>O BSÍ fica mesmo a sul de tudo isto. Quase todo o centro antigo está a uma curta caminhada da central.</figcaption>
</figure>

<h2>O intervalo entre aterrar e fazer check-in</h2>

<p>Esta é a parte que ninguém planeia e contra a qual todos esbarram. O quarto só fica pronto às duas da tarde. O voo aterrou às seis da manhã. Às oito está no centro com uma mala.</p>

<p>A bagagem é a metade fácil, e o primeiro passo é aquele de que toda a gente se esquece: pergunte no hotel. Um quarto que não está pronto não é o mesmo que um hotel que não pode ajudar, e a maioria guarda as malas até ao check-in sem cobrar. E assim a mala fica onde vai dormir, o que é melhor do que qualquer cacifo.</p>

<p>Se a resposta for não, ou se reservou um apartamento sem receção, há cacifos em Keflavík e no BSÍ. Os do BSÍ funcionam 24 horas, com 96 cacifos de quatro tamanhos, mais do que a maioria das centrais desta dimensão.</p>

<p>As horas são a metade melhor, porque o centro antigo atravessa-se em cerca de vinte minutos e não precisa de um quarto de hotel para se aproveitar. Um intervalo de quatro ou cinco horas acomoda o percurso de 2 a 2,5 horas à volta do qual este site foi construído e ainda deixa espaço para o pequeno-almoço e um café demorado. Os cafés abrem muito antes dos balcões de receção.</p>

<h2>Três horários</h2>

<h3>Se aterrar cedo</h3>
<p>O Flybus, porque as partidas seguem as chegadas. Bagagem tratada, pequeno-almoço no centro e a caminhar assim que houver luz: por altura do solstício de inverno isso só acontece por volta das onze da manhã, portanto conte antes com uma hora quente dentro de portas.</p>

<h3>Se aterrar tarde</h3>
<p>Outra vez o Flybus: o horário vai até ao fim da noite e as últimas partidas estão ligadas às chegadas tardias, coisa que o autocarro público não faz. Ainda assim, confirme a última partida da sua data. Se aterrar depois de os autocarros terminarem, o táxi não é um luxo: é o que resta.</p>

<h3>Se partir cedo</h3>
<p>Conte para trás a partir do balcão de check-in e não da porta de embarque, e some os 45 minutos mais o que custar a recolha no hotel. As partidas de madrugada implicam autocarros a sair da cidade a meio da noite: o horário do Flybus cobre isso, o autocarro urbano não.</p>

  </div>
</section>

<section class="soft" id="audio">
  <div class="wrap">
    <h2>O audioguia</h2>
    <p class="lead" style="max-width:720px">Vai ter horas no centro antes de alguém lhe dar uma chave. Percorrê-lo é óbvio. Saber porque é que a cidade está ali e porque é que o percurso começa naquela colina em concreto é a parte que tem de trazer consigo.</p>
    <div class="product" style="margin-top:26px">
      <div class="ph"><img src="{P}img/product-reykjavik.webp" width="1200" height="800" loading="lazy" alt="A aplicação TouringBee com o percurso de Reykjavik, à frente da Hallgrímskirkja"></div>
      <div class="bd">
        <h3 style="margin:0 0 6px">Audioguia TouringBee de Reykjavik</h3>
        <p class="meta" style="margin:0 0 10px">27 paragens · 2 a 2,5 horas · pagamento único, um ano de acesso</p>
        <div class="price">9,99 €<small>{PRICESUB}</small></div>
        <ul class="ticks">
          <li><strong>Encaixa nas horas mortas.</strong> Duas a duas horas e meia, mais ou menos o que tem antes do check-in</li>
          <li><strong>Funciona totalmente offline</strong> depois de descarregado — útil antes de resolver os dados num país novo</li>
          <li><strong>Ao seu ritmo.</strong> Pare para o pequeno-almoço e retome onde ficou</li>
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

<h2>Preços: transfer, bagagem e percurso</h2>
<table class="tbl">
  <tr><th>Item</th><th>Custo</th></tr>
  <tr><td>Strætó 55, adulto</td><td>2.400 ISK</td></tr>
  <tr><td>Strætó 55, 12–17, 67+, deficiência</td><td>1.200 ISK</td></tr>
  <tr><td>Strætó 55, até aos 12 anos</td><td>Grátis</td></tr>
  <tr><td>Flybus até ao BSÍ, uma viagem</td><td>desde 3.999 ISK</td></tr>
  <tr><td>Airport Direct</td><td>Confirme a tarifa com o operador</td></tr>
  <tr><td>Flybus+ com entrega no hotel</td><td>Suplemento; confirme com o operador</td></tr>
  <tr><td>Táxi</td><td>Ao taxímetro, sem tarifa fixa publicada para o aeroporto</td></tr>
  <tr><td>Cacifo de bagagem</td><td>No aeroporto e no BSÍ, 24 horas</td></tr>
  <tr><td>Audioguia para o intervalo</td><td>9,99 €, pagamento único, um ano de acesso</td></tr>
</table>

<h2>Cinco erros</h2>
<ol>
  <li><strong>Escolher só pela tarifa.</strong> Veja primeiro a hora de aterragem e o horário: a opção barata pode acrescentar uma longa espera.</li>
  <li><strong>Partir do princípio de que o autocarro público serve o seu voo.</strong> Cumpre horário; o Flybus segue as chegadas.</li>
  <li><strong>Entrar num 55 sem confirmar o destino.</strong> Algumas viagens acabam em Fjörður, não no BSÍ.</li>
  <li><strong>Pagar o Flybus+ por hábito.</strong> Se o hotel fica perto do BSÍ e a bagagem é leve, compare primeiro a caminhada com a volta do miniautocarro.</li>
  <li><strong>Alugar carro para o transfer.</strong> Alugue-o no dia em que sai da cidade, não no dia em que aterra.</li>
</ol>

<h2>Perguntas frequentes</h2>
<div class="faq">{FAQHTML}</div>

<h2>Continuar a ler</h2>
<ul>
  <li><a href="{ONEDAY}">Reykjavik num dia</a> — o que fazer com as horas que acabou de libertar</li>
  <li><a href="{TOWER}">Hallgrímskirkja e a torre</a> — bilhetes, horários e o limite das 16:45</li>
  <li><a href="{HOME}">O guia completo de Reykjavik</a> — o percurso, as excursões e as estações</li>
  <li><a href="{GUIDES}">Todos os guias de Reykjavik</a></li>
</ul>

<h2>Em duas linhas</h2>
<p>Leve o Flybus salvo motivo em contrário: as partidas seguem os voos, em caso de atraso o lugar passa para o seguinte e deixa-o no limite do centro por 3.999 ISK. Leve o 55 se o horário der e se estiver a contar cada coroa. Leve carro só se for sair da cidade.</p>
<p>Depois trate das malas e use as horas. Quem preferir perceber a cidade a esperar nela leve <a href="#audio">o audioguia TouringBee</a>: 27 paragens, 2 a 2,5 horas, totalmente offline.</p>

<div class="final" style="margin-top:28px">
  <h2 style="color:#fff">O quarto só fica pronto às duas</h2>
  <p>O percurso são duas horas e meia. A conta faz-se sozinha.</p>
  <div class="btnrow" style="justify-content:center">
    <a {BUY} style="background:#fff;color:var(--navy);border-color:#fff">Começar o percurso — 9,99 €</a>
    <a class="btn ghost" href="{HOTELS}" {OTA}>Encontrar hotel no centro</a>
  </div>
</div>

<p class="disc">Alguns links desta página são de afiliação: se reservar através deles podemos receber uma comissão, sem custo adicional para si. Tarifas e horários verificados nos sites dos operadores em outubro de 2026; mudam sem aviso, confirme antes de viajar. Flybus: flybus.is. Autocarro público: straeto.is.</p>

  </div>
</section>
"""
