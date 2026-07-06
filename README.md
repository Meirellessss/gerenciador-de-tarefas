# Gerenciador de Tarefas

Esse é um projeto que eu comecei pra praticar o que aprendi no Python, no Curso em Vídeo. Ele é um gerenciador de tarefas que roda direto no terminal.

Comecei com o básico do Mundo 2 (listas, laços e funções), e fui evoluindo o projeto conforme avançava nos estudos: adicionei salvamento em arquivo e tratamento de erros (Mundo 3) e depois refatorei tudo usando Programação Orientada a Objetos (Mundo 4). Foi uma forma de aplicar cada coisa nova que eu aprendia num projeto de verdade.



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

Cada tarefa é um objeto da classe Tarefa, com a descrição e o status (concluída ou não) como atributos, e um método para marcar como concluída. Refatorei o projeto para usar Programação Orientada a Objetos depois de aprender POO no Mundo 4.

## O que eu aprendi fazendo

A parte de adicionar e listar foi tranquila. O que me deu mais trabalho foi a hora de concluir e remover, porque o usuário vê a lista começando no número 1, mas na lista do Python o primeiro item é o índice 0. Aí eu tive que ajustar isso (número - 1) e ainda checar se o número que a pessoa digitou existe mesmo, senão o programa quebra.

## Próximos passos

Agora o programa salva as tarefas num arquivo de texto, então elas não somem mais quando eu fecho e abro de novo. Pra fazer isso usei manipulação de arquivos e try/except, que aprendi no Mundo 3 do Curso em Vídeo.

O próximo passo que eu quero tentar é uma versão web desse projeto mais pra frente.
