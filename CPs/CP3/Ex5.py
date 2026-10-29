'''
contratos = int(0)

while True:
    print("---MENU---")
    print("1 - Realizar nova simulação")
    print("2 – Consultar contratos realizados")
    print("3 – Encerrar sistema")

    simulacao = int(input("Digite uma opção: "))

    match simulacao:
        case 1:
            valorEmprestimo = int(input("Digite o valor do emprestimo: "))
            juros = int(input("Digite a taxa de juros (%): "))
            mesesPag = int(input("Digite a quantidade de meses: "))

            jurosM = juros / 100
            valorTotal = int(0)

            for i in range(mesesPag):
                # print(i)
                valorTotal = (valorEmprestimo * jurosM)
                print(f"Mês: R$ {valorTotal}")
                contratos += 1

        case 2:
            valorTotal = int(0)
            print(f"Quantidade de contratos simulados: {contratos}")
            print(f"Valor total financiado acumulado: R$ {valorTotal}")

        case 3:
            break
'''

def calcular_financiamento(valor, taxa_mensal, meses):
    saldo = valor
    taxa = taxa_mensal / 100

    print("\n--- Evolução do saldo devedor ---")

    for mes in range(1, meses + 1):
        saldo = saldo * (1 + taxa)
        print(f"Mês {mes}: R$ {saldo:.2f}")

    parcela = saldo / meses
    return saldo, parcela


def nova_simulacao():
    try:
        valor = float(input("Valor do empréstimo: "))
        taxa = float(input("Taxa de juros mensal (%): "))
        meses = int(input("Quantidade de meses: "))
    except ValueError:
        print("Dados inválidos.")
        return 0

    if valor <= 0 or taxa < 0 or meses <= 0:
        print("Valores inválidos.")
        return 0

    total, parcela = calcular_financiamento(
        valor, taxa, meses
    )

    print(f"\nValor total financiado: R$ {total:.2f}")
    print(f"Valor de cada parcela: R$ {parcela:.2f}")

    return total


def main():
    quantidade = 0
    total_acumulado = 0

    while True:
        print("\n----- MENU -----")
        print("1 - Nova simulação")
        print("2 - Consultar contratos simulados")
        print("3 - Encerrar")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            total = nova_simulacao()

            if total > 0:
                quantidade += 1
                total_acumulado += total

        elif opcao == "2":
            print(f"Contratos simulados: {quantidade}")
            print(f"Total acumulado: R$ {total_acumulado:.2f}")

        elif opcao == "3":
            print(f"Contratos simulados: {quantidade}")
            print(f"Total acumulado: R$ {total_acumulado:.2f}")
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


main()