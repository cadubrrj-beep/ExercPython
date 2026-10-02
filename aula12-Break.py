
contador =1

while contador <=10:
    print(contador)

    #contador += 1 Antes do break não exibe o 5

    if contador == 5:
        print("Achei o 5!")
        break #Break pertence ao while, mas está dentro do if. Força a parada no loop

    contador+=1

    print("Fora de laçø!")

