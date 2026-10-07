#Imprima a tabuada do 7 (de 1 a 10), no formato 7 x 3 = 21.

tabuada = 7
numero = 0
for multiplo in range(1, 11):
    numero = multiplo
    print(f"{tabuada} x {numero} = ", numero * tabuada)


