'''
Problema




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



