'''

Um investidor aplica um valor inicial (ex: R$ 1000.00) com uma taxa de
juros mensal (ex: 1%). Desenvolva um programa que solicite o valor
inicial, a taxa e a quantidade de meses. O programa deve usar um laço
de repetição para calcular e exibir o saldo mês a mês.

Output esperado:

Digite o valor inicial para investimento R$: 1000
Digite o valor da taxa de Juros (%) : 1
Digite a quantidade de meses: 3
Mês 1: R$1010.00
Mês 2: R$1020.10
Mês 3: R$1030.30

'''


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