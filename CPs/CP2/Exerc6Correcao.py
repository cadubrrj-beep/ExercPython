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

faturamento = 0
while True:
    print("----Menu----")
    print("1 - Registrar nova venda")
    print("2 - Fechar o caixa")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        print("-- Registrar nova venda --")
        qtd = int(input("Digite a quantidade de itens diferentes: "))
        preco = float(input("Digite o preço do item R$: "))

        subtotal = qtd * preco

        if subtotal>500:
            desconto = subtotal * 0.15
        else:
            desconto = subtotal * 0.05

        total_venda = subtotal - desconto
        faturamento += total_venda

        print(f"Subtotal da venda R$ {subtotal:.2f}")
        print(f"Desconto R$: {desconto:.2f}")
        print(f"Total da venda R$: {total_venda:.2f}")
    elif opcao == "2":
        print(f"Faturamento total R$ {faturamento:.2f}")
        break
    else:
        print("Opção inválida. Digite 1 ou 2")