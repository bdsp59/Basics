# Basics
Repositório com o objetivo de armazenar códigos iniciais a cada linguagem de programação.

O objetivo desse repositório é ter uma lista de programas do básico a intermediário para começar a estudar qualquer linguagem de programação. Aqui ficaram os códigos de diversas linguagens, indicando que são as que comecei a estudar.

## Lista de Programas a serem implementados
 ### Calculadora
 Criar uma calculadora com as funções de soma, subtração, multiplicação, divisão, raiz, potência e limpar conta.
 Criar uma interface gráfica para gerir a calculadora.
 
 ### Jogo de Xadrez
 Criar um jogo de xadrez com peças, possibilidades de movimento, regras para impedir movimentos, contagem de pontos e identificar xeques.
 Criar uma interface gráfica para jogar.
 ***Depois de pronto a jogabilidade para o usuário, criar um IA para jogar contra***
 
 ### Cadastro de Usuário
 Criar um formulário para pegar dados do usuário (nome, email, telefone, cpf, login e senha) e depois gerar um arquivo de texto organizado com esses dados.
 Criar uma interface gráfica.
 
 ### Lista de Compras
 Criar um arquivo para o cliente inserir um nome para a lista de compras, o que deseja comprar e a quantidade. E depois gerar um arquivo com a seguinte visualização:
 
 """
 Nome da Lista
 
 Produto...........Quantidade - Comprou?[]
 """
 
 Criar uma interface gráfica para inserir os dados.
 
 ### Conversor de Medidas
 Criar uma interface gráfica que vai receber o valor, qual unidade de medida original, qual unidade de medida desejada e vai exibir o resultado da conversão.
 
 ### Jogo Forca que salva pontuação
 Criar um jogo de forca que vai ter um menu inicial com um botão iniciar, outro com registro das 5 maiores pontuações e outro com opção de crédito, indicando nome de quem fez o jogo e tecnologias utilizadas.
 A palavra da forca deve vir de um banco de dados e selecionada aleatoriamente pelo sistema. O registro das pontuações devem ser salvo no banco também, com a  identificação do jogador, inserida ao final da partida.
 O jogo deve funcionar da seguinte maneira:
  - Cada letra correta adiciona 5 pontos a pontuação e cada letra errada diminui 5 pontos.
  - Cada palavra correta adiciona 50 pontos a pontuação.
  - Se acertar a palavra, a outra deve ser escolhida aleatoriamente automaticamente.
  - Existem 6 tentativas para a forca (Cabeça, Corpo, Braços e Pernas).
  - Se ocorrer a forca, encerra o jogo, pede o nome do jogador e salva a pontuação.
  - Jogador pode encerrar a partida quando quiser, salvando a pontuação e nome nesse momento.
 Criar uma interface gráfica para exibir o jogo e a forca.
 
 ### Programa para Jogar com 5 Jogos
 Criar um programa com 5 jogos diferentes (Forca, Xadrez, Jogo da Velha, Paciência e Damas), onde o usuário pode escolher qual deseja jogar dentro de um menu de opções.
 Quando selecionar uma opção deve-se abrir um menu do jogo contendo o botão iniciar, crédito e detalhes do como é o jogo. Só tem necessidade de fazer a parte de pontuação se fizer sentido ao jogo.
 E os jogos, que fizerem sentido, devem ter uma IA oponente para o usuário.
 O menu seleção terá uma interface gráfica comum a todos os jogos e depois cada jogo deve ter a sua própria.
 
 ### Mercadinho
 Pensando em uma estrutura de um mercadinho, onde deve é possível que clientes realizem compras, utilizando dinheiro ou cartão, que tem um estoque dos produtos comercializados e no fechamento do caixa o funcionário escreve um relatório das transações realizadas no dia. 
 Imaginando o mercadinho acima, deve-se criar um programa que atendam todas as necessidades do estabelecimento, sendo elas:
   - Aviso para renovar o estoque -> Sempre que um produto chegar a 20% da capacidade máxima.
   - Agrupar as compras realizadas por clientes por tipo de pagamento, pagamentos a fornecedores e sangrias para gerar o relatório no fim do dia.
   - Ter controle sobre o dinheiro em caixa -> Funcionário deve informar quanto dinheiro tinha quando o caixa abriu e com quanto dinheiro estava ao fechar, e sistema deve verificar se a quantidade está de acordo com as transações feitas em dinheiro. Se estiver correto, sistema já deve armazenar dinheiro do fim do dia para o valor de abertura do dia seguinte.
   - Permitir entrada de descontos nos produtos (percentual ou valor) e sangrias no caixa.
   - Ao final do mês gerar um relatório mensal -> Neste relatório deve constar apenas os valores totais das vendas realizadas, não precisa especificar venda a venda, de cada meio de pagamento, valores gastos com compras de produtos e frequência de reposição dos produtos, nessa caso especificar por produto em ordem alfabética, e trazer o lucro, considerando apenas despesas de compra.
 Criar uma interface gráfica.
 
 ### Jogo Plataforma
 Desenvolver um jogo de plataforma 2D (Ninja's Mask da faculdade). 
 Características do jogo:
  - Personagem pode se mover para esquerda e direita, pular e atacar com espada os inimigos.
  - Ao final de um cenário (qualquer lado) deve-se entrar em um novo cenário, exceto começo e fim da fase.
  - Ter inimigos com IA de movimentação e ataque.
  - Ter pelo menos 5 fases, com aumento de dificuldade em cada nova fase e chefe ao final de cada uma.
  - Ataque a distância e poder limitados a certa quantidade ou condição.
  - Jogo volta a menu inicial quando personagem morrer, quando o jogo acabar ou quando o jogador sair.
  - Se o jogador sair ele deve ter a opção de recomeçar no começo da fase, mas com pontuação e atributos do personagem iguais a quando saiu.
  - Menu inicial com as opções continuar (se houver um jogo incompleto registrado), novo jogo, score e créditos.
