numeros = []
n = int(input('Número (0 encerra): '))

while len(numeros) < 5 and n != 0:
    numeros.append(n)
    print(numeros)
    n = int(input('Próximo: '))
