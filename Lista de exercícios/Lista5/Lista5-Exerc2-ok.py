# Crie um Algoritmo que que solicite ao utilizador um valor em Reais (R$)
# e a sigla de uma moeda estrangeira para conversão. Usa match-case
# para definir a taxa de câmbio:
# • USD" (Dólar): Multiplicar por 0.20
# • "EUR" (Euro): Multiplicar por 0.18
# • "GBP" (Libra): Multiplicar por 0.15
# • Caso padrão: Exibir "Moeda não suportada".

valorReal = float(input("Digite um valor em Reais (R$): "))
taxaCambio = int(input("Digite o número da taxa desejada (1) USD, (2) Euro, (3) Libra: "))

match taxaCambio:
    case 1:
        print(f"Conversão para Dólar {valorReal * 0.20}")
    case 2:
        print(f"Conversão para Euro {valorReal * 0.18}")
    case 3:
        print(f"Conversão para Libra {valorReal * 0.15}")
    case _:
        print("Moeda não suportada. Digite apenas o número da moeda correspondente")