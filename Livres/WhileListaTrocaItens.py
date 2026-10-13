originais = [4, 15, 8, 22, 10]
resultado = []
i = 0

while i < len(originais):
    if originais[i] > 10:
        resultado.append(originais[i])
    i += 1

print(resultado)