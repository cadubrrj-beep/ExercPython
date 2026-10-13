'''
Desenvolva um algoritmo que peça um número inteiro ao usuário e
exiba a tabuada desse número de 1 a 10 no formato: X * 1 = X.

Digite um número [1 até 10]: 1
1x1=1 1x2 1x3=3 1x4=4 1x5=5 1x6=6 1x7=7 1x8=8 1x9=9
1x10=10

Digite um número [1 até 10]: 11
Valor fora do intervalo. É apenas aceito de 1 até 10
Digite um número [1 até 10]:
'''

while True:
    numero = int(input("Digite um número [1 até 10]: "))

    if numero>=1 and numero<=10:
        break
    else:
        print("Valor fora do intervalo.")

# I: incremento (é o contador)
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

