precoTotalFinal = 0

while True:
    print("------ MENU ------")
    print("1 - Registrar nova venda")
    print("2 - Fechar o Caixa")

    quant = 0
    preco = 0

    precoTotal = 0

    opcao = input("Digite uma opção: ")
    if opcao.isdigit(): #funcao do python para validar se é número
        opcao = int(opcao)
        match opcao:
            case 1:
                quant = input("Digite a quantidade de itens diferentes: ")
                preco = input("Digite o preço do item R$: ")
                subTotal = (quant * preco)
                if subTotal >= 500:
                    precoTotal = subTotal * 0.15
                else:
                    precoTotal = subTotal * 0.05
                print("Subtotal da Venda R$:", subTotal)
                print("Desconto aplicado R$:", (precoTotal - subTotal))
                print("Total da Venda R$:", precoTotal)
            case 2:
                print("Fechar o caixa")
                break
            case _:
                print("Você digitou uma opção inválida! Tente novamente")

    else:
        print("Digite apenas números. De 1 até 2")