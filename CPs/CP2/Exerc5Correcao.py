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

valor_invest = float(input("Digite o valor inicial para investimento R$: "))
taxa = float(input("Digite o valor da taxa de juros (%): "))
meses = int(input("Digite a quantidade de meses: "))

for i in range (1, meses+1):
    valor_invest += valor_invest * (taxa/100)
    print(f"Mês {i}: R$ {valor_invest:.2f}")