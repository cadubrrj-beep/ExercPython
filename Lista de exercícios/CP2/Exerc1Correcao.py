while True:
    nota = float(input("Digite uma nota [0 até 10]: "))

    if nota>=0 and nota<=10:
        print(f"Nota {nota} registrada com sucesso")
        break
    else:
        print("Nota inválida. É apenas aceito de 0 até 10.")

