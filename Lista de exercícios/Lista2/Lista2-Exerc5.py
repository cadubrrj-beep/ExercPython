'''
Crie um algoritmo que solicita a entrada de três valores inteiros e exiba
apenas o menor entre eles. Caso sejam iguais, exiba a mensagem
“Números iguais”
'''

valor1 = int(input("Digite o primeiro valor inteiro: "))
valor2 = int(input("Digite o segundo valor inteiro: "))
valor3 = int(input("Digite o terceiro valor inteiro: "))

if valor1 == valor2 == valor3:
    print("Os números são iguais")
elif valor1 < valor2 and valor1 < valor3:
    print("Número 1 é menor que os números 2 e 3")
elif valor2 < valor1 and valor2 < valor3:
    print("Número 2 é menor que os números 1 e 3")
else:
    print("Número 3 é menor que os números 1 e 2")