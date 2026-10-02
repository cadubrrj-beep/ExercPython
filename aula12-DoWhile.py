#Do-While
while True:
    n = int(input("Digite 0 para sair "))

    if n == 0 or n == 1:
        print(f"Você digitou {0}. Saindo do laço")
        break

    print("Você digitou", n, "Tente novamente!")

print("Fora do laço!")