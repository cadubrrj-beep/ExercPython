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