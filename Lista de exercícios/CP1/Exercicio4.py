'''
Problema

Considere a tabela para o cálculo de INSS sobre o salário:

De       | Até      | Aliquota | Dedução
0,00     | 1.621,00 | 7,50%    | 0,00
1.621,01 | 2.902,84 | 9,00%    | 24,32
2.902,85 | 4.354,27 | 12,00%   | 111,40
4.354,28 | 8.475,55 | 14,00%   | 198,49

Atenção!
• Há um TETO máximo que pode ser descontado de um
assalariado, sendo 14% de 8475.55, acima desse valor é fixo.
• Formula: (Salário * Alíquota) – Dedução = INSS
Desenvolva um algoritmo que leia o Salário de um CLT e calcule quanto ele
pagará de INSS (2 pontos)

Output esperado
Salário: R$ 4.000
INSS: R$ 368,60

Salário: R$ 1.621
INSS: R$121.57
'''










'''
# Código entregue
salario = float(input("Salário: R$ "))

if salario <= 1621:
    inss = (salario * 0.075)
    print(f"INSS = {inss:.2f}")
elif salario <= 2902.84 and salario > 1621:
    inss = (salario * 0.09) - 24.32
    print(f"INSS = {inss:.2f}")
elif salario <= 4354.27 and salario > 2902.85:
    inss = (salario * 0.12) - 111.40
    print(f"INSS = {inss:.2f}")
else:
    print("INSS = ", ((salario * 0.14) - 198.49))
'''

'''
Correção
salario = float(input(Salário: R$"))

if salario<=1621:
    inss = salario*0.075
elif salario<=

CONTINUAR PREENCHIMENTO DO PRINT





'''


