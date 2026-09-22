'''
Crie um Algoritmo que solicita a entrada de um valor inteiro e exiba uma
mensagem: “é positivo”, “é negativo” ou “é zero”.
'''

valorInteiro = int(input("Digite o número: "))
if valorInteiro == 0:
    print("O número digitado é zero")
elif valorInteiro > 0:
    print("O número digitado é positivo")
else:
    print("O número digitado é negativo")