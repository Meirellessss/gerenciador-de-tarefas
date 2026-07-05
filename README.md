# Gerenciador de Tarefas

Esse é um projetinho que eu fiz pra praticar o que aprendi no Python, mais especificamente no Mundo 2 do Curso em Vídeo. É um gerenciador de tarefas bem simples que roda direto no terminal.

A ideia era treinar de verdade em vez de só assistir aula, então resolvi montar algo que juntasse listas, laço de repetição e funções, que foi o que eu tinha acabado de estudar.

## O que ele faz

- Adicionar uma tarefa
- Listar todas as tarefas (mostra se já foi concluída ou não)
- Marcar uma tarefa como concluída
- Remover uma tarefa
- Sair do programa

## Como rodar

Precisa ter o Python instalado no computador. Aí é só abrir o terminal na pasta onde está o arquivo e rodar:
python gerenciador_de_tarefas.py

Depois é só ir digitando o número das opções do menu.

## Como eu organizei

Cada tarefa é uma lista com duas informações: a descrição e se ela já foi concluída (True ou False). Por exemplo: `["Estudar Python", False]`. Todas as tarefas ficam guardadas dentro de outra lista.

Separei cada parte em uma função (adicionar, listar, concluir, remover) pra não deixar tudo jogado num monte de código só. O menu fica dentro de um `while` que repete até eu escolher sair.

## O que eu aprendi fazendo

A parte de adicionar e listar foi tranquila. O que me deu mais trabalho foi a hora de concluir e remover, porque o usuário vê a lista começando no número 1, mas na lista do Python o primeiro item é o índice 0. Aí eu tive que ajustar isso (número - 1) e ainda checar se o número que a pessoa digitou existe mesmo, senão o programa quebra.

## Próximos passos

Por enquanto as tarefas somem quando eu fecho o programa, porque fica tudo na memória. Quando eu terminar o Mundo 3 (a parte de arquivos) eu quero fazer ele salvar as tarefas num arquivo pra não perder tudo. Depois disso pretendo tentar uma versão web.