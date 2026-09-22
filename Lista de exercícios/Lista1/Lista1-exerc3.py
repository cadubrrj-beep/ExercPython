# Lista de exercícios de Python

#Exercício 3

''''
Crie um programa que solicite o peso e altura de uma determinada
pessoa e calcule o seu IMC (Índice de Massa Corpórea). A fórmula:
IMC = peso / altura²
'''


peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura "))
imc = peso / (altura * altura)
print(f"O seu IMC é: {imc}")


