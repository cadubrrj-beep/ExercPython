num = 0
som = 0
med = 0
while True:
    num = int(input("Digite um número: "))
    if num ==0:
        print(f"Somatoria: {som}")
        print(f"Media: {som / med}")
        break
    elif num <0:
        print("Valor invalido, digie um número e digite 0 para calcular")
    else:
        med += 1
        som = som + num


