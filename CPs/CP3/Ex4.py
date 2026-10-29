PRECOS = {
    "1": 8.00,   # Carro
    "2": 5.00,   # Moto
    "3": 12.00   # Caminhonete
}

def registrar_entrada(veiculos):
    placa = input("Digite a placa: ").upper()

    if placa in veiculos:
        print("Veículo já cadastrado.")
        return

    print("1 - Carro | 2 - Moto | 3 - Caminhonete")
    tipo = input("Digite o tipo do veículo: ")

    if tipo in PRECOS:
        veiculos[placa] = tipo
        print("Entrada registrada com sucesso.")
    else:
        print("Tipo inválido.")


def registrar_saida(veiculos):
    placa = input("Digite a placa: ").upper()

    if placa not in veiculos:
        print("Veículo não encontrado.")
        return 0

    horas = float(input("Digite a quantidade de horas: "))

    if horas <= 0:
        print("Quantidade de horas inválida.")
        return 0

    tipo = veiculos[placa]
    subtotal = horas * PRECOS[tipo]

    if horas <= 2:
        desconto = 0
    elif horas <= 5:
        desconto = 0.05
    else:
        desconto = 0.10

    valor_desconto = subtotal * desconto
    total = subtotal - valor_desconto

    print(f"Subtotal da estadia R$ {subtotal:.2f}")
    print(f"Desconto aplicado R$ {valor_desconto:.2f}")
    print(f"Total a pagar R$ {total:.2f}")

    del veiculos[placa]

    return total


def main():
    veiculos = {}
    faturamento = 0

    while True:
        print("\n----- MENU -----")
        print("1 - Registrar entrada")
        print("2 - Registrar saída")
        print("3 - Ver faturamento")
        print("4 - Encerrar")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            registrar_entrada(veiculos)

        elif opcao == "2":
            faturamento += registrar_saida(veiculos)

        elif opcao == "3":
            print(f"Faturamento: R$ {faturamento:.2f}")

        elif opcao == "4":
            print(f"Faturamento total: R$ {faturamento:.2f}")
            break

        else:
            print("Opção inválida.")


main()