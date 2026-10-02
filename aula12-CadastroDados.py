#Gerenciar aluno
# 1 - Cadastrar
# 2 - Consultar
# 3 - Atualizar
# 4 - Remover
# 5 - Listar alunos
# 6 - Sair do programa

while True:
    print("Gerenciar aluno")
    print("1 - Cadastrar")
    print("2 - Atualizar")
    print("3 - Atualizar")
    print("4 - Remover")
    print("5 - Listar")
    print("6 - Sair")
    opcao = input("Digite uma opção: ")

    if opcao.isdigit(): #funcao do python para validar se é número
        opcao = int(opcao)
        match opcao:
            case 1:
                print("Cadastrando aluno")
            case 2:
                print("Consultar o aluno")
            case 3:
                print("Atualizar o aluno")
            case 4:
                print("Remover o aluno")
            case 5:
                print("Lista os aluno")
            case 6:
                print("Saindo do programa")
                break
            case _:
                print("Você digitou uma opção inválida! Tente novamente")

    else:
        print("Digite apenas números. De 0 até 6")