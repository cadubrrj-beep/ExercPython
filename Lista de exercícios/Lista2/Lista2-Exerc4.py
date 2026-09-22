'''
Crie um Algoritmo que solicita a entrada de dois valores inteiros e exiba
apenas o maior entre eles. Caso sejam iguais, exiba a mensagem
“Números iguais”
'''

valor1 = int(input("Digite o primeiro valor inteiro: "))

valor2 = int(input("Digite o segundo valor inteiro: "))

if valor1 == valor2:
    print("Os números são iguais")
elif valor1 > valor2:
    print("Número 1 maior que o número 2")
else:
    print("Número 2 maior que o número 1")