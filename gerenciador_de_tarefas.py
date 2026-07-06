"""
Gerenciador de Tarefas (to-do list) - versão terminal
Agora usando Programação Orientada a Objetos (POO), do Mundo 4.
Cada tarefa virou um OBJETO da classe Tarefa, em vez de uma lista.
"""


class Tarefa:
    def __init__(self, descricao):
        # roda quando uma tarefa nova é criada
        self.descricao = descricao   # atributo: o texto da tarefa
        self.concluida = False       # tarefa nova sempre começa não concluída

    def concluir(self):
        # método: marca esta tarefa como concluída
        self.concluida = True


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
    """Pede uma descrição e adiciona uma nova tarefa (objeto) na lista."""
    descricao = input("Digite a nova tarefa: ")
    tarefas.append(Tarefa(descricao))   # cria um objeto Tarefa e guarda
    print("Tarefa adicionada!")


def listar_tarefas(tarefas):
    """Mostra todas as tarefas com um número e o status."""
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada ainda.")
        return

    print("\n--- Suas tarefas ---")
    for i in range(len(tarefas)):
        tarefa = tarefas[i]
        status = "[X]" if tarefa.concluida else "[ ]"
        print(f"{i + 1}. {status} {tarefa.descricao}")


def concluir_tarefa(tarefas):
    """Marca uma tarefa da lista como concluída."""
    if len(tarefas) == 0:
        print("Não há tarefas para concluir.")
        return

    listar_tarefas(tarefas)
    entrada = input("Digite o número da tarefa concluída: ")

    if not entrada.isdigit():
        print("Digite um número válido.")
        return

    numero = int(entrada)
    indice = numero - 1

    if indice < 0 or indice >= len(tarefas):
        print("Essa tarefa não existe.")
        return

    tarefas[indice].concluir()   # chama o método do objeto
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
    print(f'Tarefa "{removida.descricao}" removida!')


def salvar_tarefas(tarefas):
    """Salva todas as tarefas num arquivo de texto."""
    with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
        for tarefa in tarefas:
            arquivo.write(f"{tarefa.descricao};{tarefa.concluida}\n")


def carregar_tarefas():
    """Lê as tarefas do arquivo. Se não existir, começa com lista vazia."""
    tarefas = []
    try:
        with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha == "":
                    continue
                partes = linha.split(";")
                descricao = partes[0]
                tarefa = Tarefa(descricao)          # cria o objeto
                tarefa.concluida = partes[1] == "True"  # ajusta o status lido
                tarefas.append(tarefa)
    except FileNotFoundError:
        pass
    return tarefas


# ===== Programa principal =====
def main():
    tarefas = carregar_tarefas()

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            adicionar_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif opcao == "5":
            print("Até logo! 👋")
            break
        else:
            print("Opção inválida, tente de novo.")


if __name__ == "__main__":
    main()