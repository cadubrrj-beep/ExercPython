# Crie um Algoritmo para um recepcionista realizar operações rápidas no
# sistema de reservas, com as seguintes opções:
# 1. Check-in
# 2. Check-out
# 3. Consultar Quarto
# 4. Sair

operacao = int(input("Sistema de reservas de hotel. Digite a operação desejada: (1) Check-in, (2) Check-out, (3) Consultar Quarto, (4) Sair do sistema. "))

match operacao:
    case 1:
        print("Check-in selecionado, entrando no cadastro")
    case 2:
        print("Check-out selecionado, entrando no protocolo de saída de hóspede")
    case 3:
        print("COnsultar disponibilidade do quarto selecionado, verificando sistema e controle de limpeza")
    case 4:
        print("Saindo do sistema")
    case _:
        print("Opção não identificada. Tente novamente")