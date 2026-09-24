'''
Problema




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


#salario <= 8475.55 and salario > 4354.27:
'''



