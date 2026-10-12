'''
Desenvolva um algoritmo que simule o fechamento de caixa de uma
loja. O programa deve operar em um loop principal que permite
processar várias vendas até que o usuário decida encerrar o expediente.
Se o subtotal for superior a R$ 500,00, aplique um desconto de 15%.
Caso contrário, aplique apenas 5% de desconto

Output esperado:
------ MENU ---------
1 – Registrar nova venda
2 – Fechar o Caixa
Digite uma opção: 1
-- Registrar nova venda --
Digite a quantidade de itens diferentes: 2
Digite o preço do item R$: 50.00
Subtotal da Venda R$ 100.00
Desconto aplicado R$ 5.00
Total da Venda R$: 95.00
------ MENU ---------
1 – Registrar nova venda
2 – Fechar o Caixa
Digite uma opção: 2
Faturamento Total Acumulado: R$95.00
'''

precoTotalFinal = 0

while True:
    print("------ MENU ------")
    print("1 - Registrar nova venda")
    print("2 - Fechar o Caixa")

    quant = 0
    preco = 0.0

    precoTotal = 0

    opcao = input("Digite uma opção: ")
    if opcao.isdigit():  # funcao do python para validar se é número
        opcao = int(opcao)
        match opcao:
            case 1:
                quant = int(input("Digite a quantidade de itens diferentes: "))
                preco = float(input("Digite o preço do item R$: "))
                subTotal = quant * preco
                if subTotal >= 500:
                    precoTotal = subTotal - (subTotal * 0.15)
                else:
                    precoTotal = subTotal * (subTotal * 0.05)
                print("Subtotal da Venda R$:", subTotal)
                print("Desconto aplicado R$:", (subTotal - precoTotal))
                print("Total da Venda R$:", precoTotal)
                precoTotalFinal = precoTotalFinal + precoTotal
            case 2:
                print("Fechar o caixa")
                print("Total do dia: ", precoTotalFinal)
                break
            case _:
                print("Você digitou uma opção inválida! Tente novamente")
    else:
        print("Digite apenas números. De 0 até 6")


