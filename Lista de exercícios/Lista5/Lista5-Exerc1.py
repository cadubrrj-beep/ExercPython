# Crie um Algoritmo que o nome de um dia da semana (ex: "Sábado",
# "Segunda"). Usando match-case, o programa deve informar se é um
# "Dia útil" ou "Final de semana".

diaSemana = input("Digite uma dia da semana: ")

match diaSemana:
    case "sábado" | "domingo":
        print("Final de semana")
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("Dia útil")
    case _:
        print("Dia digitado errado")


