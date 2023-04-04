# Título e Imagem de capa
<h1 align="center"> Contador sequencial de Fibonacci </h1>

![fibo](https://user-images.githubusercontent.com/129625591/229647386-f61c870b-63b6-4cf4-9279-860c332183c2.png)

# Badges
![badge1](https://img.shields.io/badge/python-3.11-blue) ![badge2](https://img.shields.io/badge/status-aguardando%20revis%C3%A3o-yellow) ![badge3](https://img.shields.io/badge/gitstars-4-blue) ![badge4](https://img.shields.io/badge/testado%20por-44Sec-green)


# Índice 

* [Título e Imagem de capa](#título-e-imagem-de-capa)
* [Badges](#badges)
* [Índice](#índice)
* [Descrição do Projeto](#descrição-do-projeto)
* [Status do Projeto](#status-do-projeto)
* [A Sequência Fibonacci](#a-sequência-fibonacci)
* [Forma de contagem](#forma-de-contagem)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Link de vídeo explicativo](#link-de-vídeo-explicativo)
* [Pessoas Desenvolvedoras do Projeto](#pessoas-desenvolvedoras-do-projeto)
* [Licença](#licença)
* [Conclusão](#conclusão)

# Descrição do Projeto

O seguinte projeto tem como objetivo realizar a contagem de acordo com a sequencia de Fibonacci, entregando desta forma ao usuário o valor numérico sequecial até a casa solicitada pelo mesmo.

# Status do Projeto

O projeto foi desenvolvido diante da proposta de trabalho do professor Fábio Cabrini, como primeiro checkoint da disciplina Coding For Security da turma 1TDCG da Faculdade de Adminsitração e Informatica Paulista. Aguardando aprovação do docente responsável.

# A Sequência Fibonacci

A sequência de Fibonacci, ou sucessão de Fibonacci, é uma sequência matemática composta por números inteiros. Normalmente, começando por 0 e 1 e cada termo subsequente é formado pela soma dos dois anteriores.

Essa sequência é uma sucessão infinita de números que seguem o mesmo padrão. A palavra Fibonacci é usada porque o matemático italiano, Leonardo de Pisa, foi quem concebeu uma fórmula para essa sequência. Mas, além de saber o que é Fibonacci, é importante saber que essa sequência é aplicada em análise de mercados financeiros, na ciência da computação e em teoria dos jogos. 

Também aparece, por exemplo, em configurações biológicas, galhos de árvores, folhas em uma haste, no arranjo do cone da alcachofra, no abacaxi e no desenrolar da samambaia.

# Forma de contagem

![contagem](https://static.significados.com.br/foto/fibonacci2_bg.jpg)

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2594...

É possível observar que a composição é formada por números que são o resultado da soma dos
dois anteriores:

![contagem](https://user-images.githubusercontent.com/129625591/229652427-790f7379-9e6b-4bd8-ac15-50e6ee4d61eb.png)

# Funcionalidades e Demonstração da Aplicação

Para executar o programa incie primeiro o interpretador com o comando py ou python, no windows powershell ou no terminal de computador do seu sistema operacional.

* Clone o repositório no diretório desejado

```
$ git clone https://github.com/44SEC/contador-sequencial-fibonacci.git
```

* Execute o script com o seguinte comando

```
$ python3 fibonacci.py
```

O código vai exibir uma menssegem de boas vindas e em seguida irá solicitar que o usuários insira o número de casa que deseja contar. A seguinte mensagem deverá ser exibia: 

"Insira um número para gerar a sequência de Fibonnaci:"

O número minimo aceito pelo script é 2, tendo em vista parâmetros solicitados para o desenvolvimento do trabalho. Caso o usuário insira um número menor, uma mensagem de erro será exibida e o programa voltará ou seu ponto inicial.

A aplicação só aceita números inteiros, caso uma string seja inserida o programa exibirá uma mensagem de erro e retornará ao ponto inicial.

Após a inserção, o programa retornará a contagem em forma de lista sem quebra de linha, o ultimo número indica a casa solicitada pelo usuário, mas o mesmo pode ver toda a contagem até lá. 

AVISO 
-Para fins de segurança e preservação da capacidade de processamento de computadores convencionais limitamos a entrada de contagem em 5000 mil caracteres. Caso um número maior seja inserido, uma mensagem de erro será exibida e o programa retornará ao inicio.

# Tecnologias utilizadas

Para realizar os cálculos e entregar ao usuário a contagem sequêncial, o grupo 44SEC optou por utilizar a liguagem Python, versão 3.11. Para a criação do código, foram utilizadas funções como "input", "list", "for", "while", "try", "except" e "print", dispensando a necessidade do uso de bibliotecas.

# Link de vídeo explicativo

# Pessoas Desenvolvedoras do Projeto

Felipe de Resende Madeira 

João Victor Santos Alves 

Rakel de Macedo Oliveira 

Pedro Henrique Lima Vieira 

Suellen Guedes Rufino 

# Licença

Todos os direitos reservados 44Sec - Fortification for Security

# Conclusão

A sequência de Fibonacci se mostra um efetivo exercício para a pratíca da programação, pois foge do óbvio e propõe aos alunos que busquem encontrar uma forma de tranferir a lógica da contagem para o programa criado no exercício. Isso faz com que os mesmos busquem ferramentas que podem ser utilizadas no código para conseguir automatizar esta contagem.  

