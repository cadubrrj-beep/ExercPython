# Crie um algoritmo que solicita a entrada de três valores inteiros e exiba
# apenas o menor entre eles. Caso sejam iguais, exiba a mensagem
# “Números iguais”

lista = []
x = 0

while x <= 2:
    lista.append (input("Digite um valor inteiro: "))
    x += 1

if lista[0] < lista[1] and lista[0] < lista[2]:
    # índice 0 da lista é o menor.
    print("O primeiro número é o menor")
elif lista[1] < lista[0] and lista[1] < lista[2]:
    # índice 1 da lista é o menor.
    print("O segundo número é o menor")
elif lista[2] < lista[0] and lista[2] < lista[1]:
    # índice 2 da lista é o menor.
    print("O segundo número é o menor")
else:
    # todos são iguais
    print("Todos são iguais")
