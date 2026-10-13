# Crie um Algoritmo que solicita a entrada de um valor inteiro e exiba uma
# mensagem: “é positivo”, “é negativo” ou “é zero”.

numero = int(input("Digite uma número inteiro: "))

if numero > 0:
    print("é positivo")
elif numero < 0:
    print("é negativo")
else:
    print("é zero")