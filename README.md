# Jogo de Perguntas (Python Quiz)

Um quiz interativo e dinâmico desenvolvido em Python para consolidar conceitos de estruturas de dados e controle de fluxo. O projeto foi evoluído para garantir uma experiência de jogo única a cada execução, aplicando conceitos de aleatoriedade e modularização.

## O que ele faz?

O jogo apresenta um conjunto de perguntas sobre a linguagem Python, onde o objetivo é alcançar a pontuação máxima.
* Duplo Sistema de Aleatoriedade: O jogo embaralha tanto a ordem em que as perguntas aparecem quanto a posição das alternativas na tela.
* Interface Dinâmica: Limpa o terminal automaticamente a cada rodada, melhorando a experiência do usuário.
* Tratamento Avançado de Inputs: Validação de strings flexível, aceitando respostas em maiúsculas ou minúsculas e eliminando espaços em branco acidentais.
* Feedback em Tempo Real: Sistema de pontuação cumulativa com funções dedicadas para respostas corretas e incorretas.

## Como testar

Se você tiver o Python instalado na sua máquina, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/GabrielOliveira8684/jogo-de-perguntas.git
   ```

2. Acesse a pasta do projeto:
   ```bash
   cd jogo-de-perguntas
   ```

3. Rode o script:
   ```bash
   python jogo.py
   ```

## O que eu pratiquei e aprendi nesse projeto

Com a nova atualização, o projeto deixou de ser apenas um script linear e passou a utilizar conceitos mais maduros de desenvolvimento:

* Manipulação de Matrizes (Listas de Listas): Organização das alternativas em uma estrutura bidimensional para controle de índices.
* Modularização com Funções (def): Criação de funções com passagem de parâmetros e escopo de variáveis (como o controle do fluxo do contador e da pontuação).
* Biblioteca random (shuffle): Aplicação de algoritmos de embaralhamento direto na memória para garantir a aleatoriedade das perguntas e respostas.
* Interação com o Sistema Operacional (os e platform): Identificação automática do sistema do usuário (Windows vs. Linux/Mac) para executar comandos de terminal nativos (cls ou clear).
* Lógica de Busca Orientada a Conteúdo: Uso do operador in para rastrear quais dados estavam dentro da linha sorteada da matriz, blindando o código contra erros de referência.

Valeu!