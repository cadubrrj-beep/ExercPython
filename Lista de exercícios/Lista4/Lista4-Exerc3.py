# Escreva um algoritmo que leia números indeterminados até que o valor
# zero seja inserido. Ao encerrar, apresente a soma de todos os valores
# digitados.

lista = []

while True:
    numeros = int(input("Digite um número: "))
    lista.append(numeros)

    if numeros == 0:
        total = sum(lista)
        print(total)
        break