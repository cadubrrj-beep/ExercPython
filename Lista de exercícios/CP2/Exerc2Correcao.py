while True:
    numero = int(input("Digite um número [1 até 10]: "))

    if numero>=1 and numero<=10:
        break
    else:
        print("Valor fora do intervalo.")

# I: incremento (é o contador)
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

