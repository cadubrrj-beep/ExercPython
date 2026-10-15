# Crie um algoritmo que solicite ao usuário a quantidade N de valores a
# serem lidos. Em seguida, calcule e exiba separadamente a média
# aritmética dos números pares e a média dos números ímpares
# informados.

# Usando While

'''
listaPar = []
listaImpar = []

x = int(input("Digite um número (0 para sair): "))

while x != 0:
    if x % 2 == 0:
        listaPar.append(x)
    else:
        listaImpar.append(x)

    x = int(input("Digite outro número (0 para sair): "))

if len(listaPar) > 0:
    mediaPar = sum(listaPar) / len(listaPar)
    print(f"A média dos pares é {mediaPar}")
else:
    print("Nenhum número par informado.")

if len(listaImpar) > 0:
    mediaImpar = sum(listaImpar) / len(listaImpar)
    print(f"A média dos ímpares é {mediaImpar}")
else:
    print("Nenhum número ímpar informado.")
'''



# Usando For

listaPar = []
listaImpar = []

n = int(input("Quantos números deseja informar? "))

for i in range(n):
    x = int(input("Digite um número: "))

    if x % 2 == 0:
        listaPar.append(x)
    else:
        listaImpar.append(x)

if len(listaPar) > 0:
    mediaPar = sum(listaPar) / len(listaPar)
    print(f"Média dos pares: {mediaPar:.2f}")
else:
    print("Nenhum número par informado.")

if len(listaImpar) > 0:
    mediaImpar = sum(listaImpar) / len(listaImpar)
    print(f"Média dos ímpares: {mediaImpar:.2f}")
else:
    print("Nenhum número ímpar informado.")

