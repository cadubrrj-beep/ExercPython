while True:
    nota = float(input("Digite sua Nota (0 até 10): "))
    if nota >10 or nota <0:
        print("Nota inválida, é apenas aceito de 0 até 10")
    else:
        print(f'Nota "{nota}" registrada com sucesso')
        break

