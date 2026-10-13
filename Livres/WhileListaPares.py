numeros = []
n = int(input('Número positivo: '))

while n <= 0:
    n = int(input('Tente novamente: '))

numeros.append(n)
print(numeros)