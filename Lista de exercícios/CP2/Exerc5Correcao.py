valor_invest = float(input("Digite o valor inicial para investimento R$: "))
taxa = float(input("Digite o valor da taxa de juros (%): "))
meses = int(input("Digite a quantidade de meses: "))

for i in range (1, meses+1):
    valor_invest += valor_invest * (taxa/100)
    print(f"Mês {i}: R$ {valor_invest:.2f}")