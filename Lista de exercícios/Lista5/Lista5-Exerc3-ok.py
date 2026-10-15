# Crie um Algoritmo que solicita a entrada do nome de um mês (ex:
# "Janeiro", "Julho"). O mesmo deve informar em que estação do ano esse
# mês se encontra (considerando o Hemisfério Sul):
# • Verão: Dezembro, Janeiro, Fevereiro.
# • Outono: Março, Abril, Maio.
# • Inverno: Junho, Julho, Agosto.
# • Primavera: Setembro, Outubro, Novembro.

estacoes = str(input("Digite o mês para consultar a estação: "))


match estacoes:
    case "janeiro" | "fevereiro" | "dezembro":
        print("O mês consultado pertence ao Verão")
    case "março" | "abril" | "maio":
        print("O mês consultado pertence ao Outono")
    case "junho" | "julho" | "agosto":
        print("O mês consultado pertence ao Inverno")
    case "setembro" | "outubro" | "novembro":
        print("O mês consultado pertence a Primavera")
    case _:
        print("Mês digitado incorretamente. Digite todas minúsculas")