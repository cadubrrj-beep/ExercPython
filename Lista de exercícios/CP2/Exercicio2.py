
numero = int(input("Digite um número [1 até 10]:"))

for multiplo in range(1, 11):
    tab = multiplo

    if numero <= 0 and numero >=11:
        print("Valor fora do intervalo. É apenas aceito de 1 até 10")
    else:
        print(f"{numero} x {multiplo} = ", multiplo * numero)