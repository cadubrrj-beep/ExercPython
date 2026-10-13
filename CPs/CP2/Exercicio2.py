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

numero = int(input("Digite um número [1 até 10]:"))

for multiplo in range(1, 11):
    tab = multiplo

    if numero <= 0 and numero >=11:
        print("Valor fora do intervalo. É apenas aceito de 1 até 10")
    else:
        print(f"{numero} x {multiplo} = ", multiplo * numero)