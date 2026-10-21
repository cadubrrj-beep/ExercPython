'''
emprestimo = int

jurosM = int
valorEmprestimo = int
mesesPag = int
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
