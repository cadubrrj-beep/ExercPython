# Crie um Algoritmo para um restaurante realizar o fechamento de
# comandas
#
# a. Deve solicitar o código do prato.
# ---CÓDIGO PRATO VALOR---
# 1 Hamburguer R$ 40,00
# 2 Lasanha R$ 60,00
# 3 Bife acebolado R$ 30,00
# 4 Strogonoff R$ 35,00
# 5 Picanha R$ 60,00
# 6 Churrasco R$ 60,00
#
# b. Em seguida, deve perguntar se o cliente deseja incluir a taxa de
# serviço de 10% (Sim ou Não).
# c. Calcule o valor final:
# i. Se aceitar a taxa: Total} = Preço* 1.10$
# ii. Se não aceitar: Total=Preço
# d. Exiba o nome do prato escolhido e o valor total a pagar. Caso o
# código seja inexistente, informe "Prato não encontrado".

print("Sistema de comandas")

mesa = int(input("Digite o código da mesa: "))

contaParcial = 0

while True:
    print(f"\n--- CARDÁPIO MESA {mesa} ---")
    print("1 Hamburguer R$ 40,00")
    print("2 Lasanha R$ 60,00")
    print("3 Bife acebolado R$ 30,00")
    print("4 Strogonoff R$ 35,00")
    print("5 Picanha R$ 60,00")
    print("6 Churrasco R$ 60,00")
    print("7 Fechar conta")

    codigo = int(input("Digite o código: "))

    match codigo:
        case 1:
            print("Hamburguer adicionado!")
            contaParcial += 40

        case 2:
            print("Lasanha adicionada!")
            contaParcial += 60

        case 3:
            print("Bife acebolado adicionado!")
            contaParcial += 30

        case 4:
            print("Strogonoff adicionado!")
            contaParcial += 35

        case 5:
            print("Picanha adicionada!")
            contaParcial += 60

        case 6:
            print("Churrasco adicionado!")
            contaParcial += 60

        case 7:
            print("Fechando a conta...")
            break

        case _:
            print("Código não reconhecido. Tente novamente.")

print(f"\nSubtotal: R$ {contaParcial:.2f}")

gorjeta = input("Incluir taxa de serviço de 10%? Sim/Não: ")

if gorjeta == "sim":
    contaTotal = contaParcial * 1.10
else:
    contaTotal = contaParcial

print(f"Conta da mesa {mesa}: R$ {contaTotal:.2f}")