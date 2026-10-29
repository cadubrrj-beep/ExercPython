def calcular_media(lista):
    return sum(lista) / len(lista)


def main():
    notas = []

    while True:
        nota = float(input("Digite uma nota: "))

        if nota == -1:
            break

        if nota >= 0 and nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Digite um valor entre 0 e 10.")

    if len(notas) > 0:
        print(f"\nQuantidade: {len(notas)}")
        print(f"Média: {calcular_media(notas):.2f}")
        print(f"Maior nota: {max(notas):g}")
        print(f"Menor nota: {min(notas):g}")
    else:
        print("Nenhuma nota foi cadastrada.")


main()



