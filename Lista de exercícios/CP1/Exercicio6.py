'''
Problema

Considerando os cálculos (INSS e IR) dos últimos dois exercícios, faça
um programa que leia um salário bruto, calcule e exiba os dois impostos
e calcule e exiba o salário líquido do CLT (1 ponto)

Output esperado
Salário: R$ 4000
INSS R$ 368,60
IR R$ 205,8
Salário Líquido R$ 3.425,6

'''










'''
# Código entregue
salario = float(input("Salário: R$ "))

# INSS

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

# IR

if salario <= 2428.80:
    ir = (salario * 0)
    print(f"IR R$ {ir:.2f}")
elif salario <= 2826.65 and salario > 2428.81:
    ir = (salario * 0.075) - 182.16
    print(f"IR R$ {ir:.2f}")
elif salario <= 3751.05 and salario > 2826.65:
    ir = (salario * 0.15) - 394.16
    print(f"IR R$ {ir:.2f}")
elif salario <= 4664.68 and salario > 3751.05:
    ir = (salario * 0.225) - 675.49
    print(f"IR R$ {ir:.2f}")
else:
    print("IR R$", ((salario * 0.275) - 908.73))

slrLiquido = (salario - inss) - ir
print(f"Salário Líquido R$ {slrLiquido:.2f}")
'''