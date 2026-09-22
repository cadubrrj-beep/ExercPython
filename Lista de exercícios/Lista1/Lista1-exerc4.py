# Lista de exercícios de Python

#Exercício 4

''''
Crie um programa que receba o salário de um funcionário e calcule o
novo salário com um aumento de 15%. Por Exemplo:
Salário: 2000
Novo salário: 2300
'''


salario = int(input("Informe o seu salário: "))
aumento = int(input("Informe o seu aumento percentual: "))
resultado = (salario * aumento) / 100
print(f"O seu salário atual é de : R${salario + resultado}")
