# Lista que armazenará as tarefas
tarefas = []

def exibir_menu():
    """
    Mostra as opções disponíveis para o usuário.
    """
    print("\n===== Menu de Tarefas =====")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

def adicionar_tarefa():
    """
    Solicita ao usuário uma nova tarefa e adiciona à lista.
    """
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append({"descricao": tarefa, "concluida": False})
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    """
    Exibe todas as tarefas com status (concluída ou pendente).
    """
    if not tarefas:
        print("Nenhuma tarefa registrada.")
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            status = "✔️" if tarefa["concluida"] else "❌"
            print(f"{i}. {tarefa['descricao']} [{status}]")

def concluir_tarefa():
    """
    Permite marcar uma tarefa como concluída com base no índice.
    """
    listar_tarefas()
    try:
        indice = int(input("Número da tarefa a concluir: ")) - 1
        tarefas[indice]["concluida"] = True
        print("Tarefa marcada como concluída.")
    except:
        print("Índice inválido.")

def remover_tarefa():
    """
    Remove uma tarefa com base no índice.
    """
    listar_tarefas()
    try:
        indice = int(input("Número da tarefa a remover: ")) - 1
        tarefas.pop(indice)
        print("Tarefa removida.")
    except:
        print("Índice inválido.")

def main():
    """
    Função principal que mantém o app em execução até o usuário sair.
    """
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            print("Encerrando o app de tarefas.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
