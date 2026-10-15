# Elabore um algoritmo que leia 10 números inteiros e identifique o menor
# valor entre eles, exibindo-o ao final da execução.

'''
menor = 0

for i in range(10):
  num = int(input(f"Digite o {i+1} número inteiro: "))

  if menor == 0 or num < menor:
    menor = num

print(f"O menor valor digitado foi: {menor}")
'''

menor = int(input("Digite o 1º número: "))

for i in range(9):
    num = int(input("Digite outro número: "))

    if num < menor:
        menor = num

print(f"O menor valor digitado foi: {menor}")

