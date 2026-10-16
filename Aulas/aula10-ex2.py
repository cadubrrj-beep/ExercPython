dia = int(input("Digite um dia da Semana (1 a 7):"))

match dia:
    case1:
        print("Domingo")
    case2:
        print("Segunda")
    case3:
        print("Terça")
    case4:
        print("Quarta")
    case5:
        print("Quinta")
    case6:
        print("Sexta")
    case7:
        print("Sábado")
    case _:
        print("Dia inválido!")