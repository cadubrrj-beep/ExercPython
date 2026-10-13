# Crie um Algoritmo que solicita a entrada de um valor inteiro e exiba uma
# mensagem: “é número par” OU “é número ímpar”.

numero = int(input("Digite um número par e inteiro: "))

if numero % 2 == 0:
    print("Numero é par")
else:
    print("Numero é impar")