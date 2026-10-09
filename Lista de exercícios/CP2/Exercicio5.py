inv = float(input("Digite o valor inicial para investimento R$:"))
jur = float(input("Digite o valor da taxa de Juros (%): "))
taxa = float((inv * jur) / 100)
mesAtual = 0
mesFinal = int(input("Digite a quantidade de meses: "))

while True:
    if mesAtual < mesFinal:

        mesAtual += 1
        inv = inv + taxa
        print(f"Mês {mesAtual}: {inv}")
    else:
        print(inv)
        break