##########Global Variables########
title = None
message = None

##############Lists################
info_users = []
category = []
menu_tui = ["1-Adicionar", "2-Remover", "3-Analisar", "4-Atualizar", "5-Sair"]


##########Interfaces##########
while True:
    ############MENU###############
    print("\n" * 100)
    print("======MENU======")
    if message != None:
        print(f"[Aviso]: {message}")
    print()
    print("1-Atualizar carteira")
    print("2-Modificar categorias")
    print("3-Analisar economia mensal")
    print("4-Modificar perfis")
    print("5-Sair")
    input_system = int(input("Digite uma opção em números:"))

    #########Conditions Menu########
    if input_system == 1:
        title = "Carteira"
        message = None

        while True:
            print("\n" * 100)

            ############TUI##############
            print(f"======{title}======")

            for item in menu_tui:
                print(item)
            input_action = int(input("Digite uma opção em números:"))

            ###########Conditions TUI###########
            match input_action:
                case 1:
                    income = float(input("Digite sua renda mensal: "))
                    expenses = float(input("Digite suas despesas mensais: "))
                    economy_month = income - expenses
                    info_users.append([income, expenses, economy_month])
                    print("Dados adicionados com sucesso!")
                case 2:
                    if info_users == []:
                        print("Nenhum registro para remover")
                    else:
                        for index in range(len(info_users)):
                            print(index, info_users[index])

                        input_remove = int(
                            input("Digite o número do registro que deseja remover: "))

                        if input_remove >= 0 and input_remove < len(info_users):
                            info_users.pop(input_remove)
                            print("Registro removido com sucesso!")
                        else:
                            print("Número inválido")
                case 3:
                    pass
                case 4:
                     if info_users == []:
                        print("Nenhum registro para atualizar")
                    else:
                        for index in range(len(info_users)):
                            print(index, info_users[index])
                        input_update = int(
                            input("Digite o número do registro que deseja atualizar: "))
                        if input_update >= 0 and input_update < len(info_users):
                            income = float(input("Digite a nova renda mensal: "))
                            expenses = float(input("Digite as novas despesas mensais: "))

                            economy_month = income - expenses

                            info_users[input_update] = [ income, expenses, economy_month ]
                            print("Registro atualizado com sucesso!")
                        else:
                            print("Número inválido")
                case 5:
                    break
                case _:
                    print("Número inválido")
    elif input_system == 2:
        title = "Categoria"
        message = "Funcionalidade em desenvolvimento."
    elif input_system == 3:
        title = "Economia Mensal"
        message = "Funcionalidade em desenvolvimento."
    elif input_system == 4:
        title = "Perfis"
        message = "Funcionalidade em desenvolvimento."
    elif input_system == 5:
        print("Programa encerrando!")
        break
    else:
        message = "Número inválido."
