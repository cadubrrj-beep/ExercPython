# Crie um Algoritmo que solicita a entrada de dois valores inteiros e exiba
# apenas o maior entre eles. Caso sejam iguais, exiba a mensagem
# “Números iguais”

# Sem while
'''
i = 0
lista = []

lista.append(input("Digite o primeiro número inteiro: ")) # Inclui números na lista. Não precisa especificar o número
lista.append(input("Digite o segundo número inteiro: ")) # Ao incluir ele já organiza na ordem

if lista[0] > lista[1]:
    print(f"O número 1 {lista[0]} é maior que o número 2 {lista[1]}")
elif lista[0] < lista[1]:
    print(f"O número 2 {lista[1]} é maior que o número 1 {lista[0]}")
else:
    print("Números iguais")
'''

# Com while

lista = []

while len(lista) < 2:
    numero = int(input("Digite um número inteiro: "))
    lista.append(numero)

if lista[0] > lista[1]:
    print(f"O maior número é {lista[0]}")

elif lista[0] < lista[1]:
    print(f"O maior número é {lista[1]}")

else:
    print("Números iguais")
