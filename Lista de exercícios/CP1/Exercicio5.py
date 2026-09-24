'''
Problema

Considere a tabela para o cálculo do Imposto de Renda (IR-2025) sobre
o salário:

De          Até
0,00      | 2.428,80 | 0,00%  | 0,00
2.428,81  | 2.826,65 | 7,50%  | 182,16
2.826,66  | 3.751,05 | 15,00% | 394,16
3.751,05  | 4.664,68 | 22,50% | 675,49
4.664,69  |    ---   | 27,50% | 908,73

Formula: (Salário * Alíquota) – Dedução = IR

Desenvolva um algoritmo que solicite o Salário de um CLT e calcule
quanto ele pagará de IR (2 pontos)

Output esperado:
Salário: R$ 4000
IR R$ 205,8

'''










'''
# Código entregue
salario = float(input("Salário: R$ "))

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


#salario <= 8475.55 and salario > 4354.27:
'''



