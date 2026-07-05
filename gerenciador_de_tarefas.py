"""
Gerenciador de Tarefas (to-do list) - versão terminal
Projeto de estudo usando o que foi aprendido no Python Mundo 2:
listas, laços de repetição e funções.

Como funciona: cada tarefa é uma lista [descricao, concluida]
Exemplo: ["Estudar Python", False]
E guardamos todas as tarefas dentro de outra lista: tarefas = []
"""


def mostrar_menu():
    """Mostra o menu e devolve a opção escolhida pelo usuário."""
    print("\n===== GERENCIADOR DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ")
    return opcao


def adicionar_tarefa(tarefas):
    """Pede uma descrição e adiciona uma nova tarefa na lista."""
    descricao = input("Digite a nova tarefa: ")
    tarefas.append([descricao, False])   # False = ainda não concluída
    print("Tarefa adicionada!")


def listar_tarefas(tarefas):
    """Mostra todas as tarefas com um número e o status."""
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada ainda.")
        return

    print("\n--- Suas tarefas ---")
    for i in range(len(tarefas)):
        descricao = tarefas[i][0]
        concluida = tarefas[i][1]
        status = "[X]" if concluida else "[ ]"
        # i + 1 para mostrar começando em 1 (mais amigável que 0)
        print(f"{i + 1}. {status} {descricao}")


def concluir_tarefa(tarefas):
    """Marca uma tarefa da lista como concluída."""
    if len(tarefas) == 0:
        print("Não há tarefas para concluir.")
        return

    listar_tarefas(tarefas)
    entrada = input("Digite o número da tarefa concluída: ")

    # isdigit() confirma que o usuário digitou só números
    if not entrada.isdigit():
        print("Digite um número válido.")
        return

    numero = int(entrada)
    # o usuário vê começando em 1, mas a lista começa em 0
    indice = numero - 1

    if indice < 0 or indice >= len(tarefas):
        print("Essa tarefa não existe.")
        return

    tarefas[indice][1] = True
    print("Tarefa marcada como concluída!")


def remover_tarefa(tarefas):
    """Remove uma tarefa da lista."""
    if len(tarefas) == 0:
        print("Não há tarefas para remover.")
        return

    listar_tarefas(tarefas)
    entrada = input("Digite o número da tarefa que quer remover: ")

    if not entrada.isdigit():
        print("Digite um número válido.")
        return

    numero = int(entrada)
    indice = numero - 1

    if indice < 0 or indice >= len(tarefas):
        print("Essa tarefa não existe.")
        return

    removida = tarefas.pop(indice)
    print(f'Tarefa "{removida[0]}" removida!')


# ===== Programa principal =====
def main():
    tarefas = []   # começa vazio

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("Até logo! 👋")
            break
        else:
            print("Opção inválida, tente de novo.")


# Isso faz o programa rodar quando você executa o arquivo
if __name__ == "__main__":
    main()
