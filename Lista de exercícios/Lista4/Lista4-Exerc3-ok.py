# Escreva um algoritmo que leia números indeterminados até que o valor
# zero seja inserido. Ao encerrar, apresente a soma de todos os valores
# digitados.

lista = []
contador = 0

while True:
    numeros = int(input("Digite um número: "))
    lista.append(numeros)
    contador += 1

    if numeros == 0:
        total = sum(lista)
        print(f"A soma dos {contador} números digitados foi: {total}")
        break