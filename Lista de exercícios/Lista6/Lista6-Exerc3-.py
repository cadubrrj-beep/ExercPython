# Crie a função eh_par(numero), que devolve True se o número recebido
# for par e False caso contrário. Solicite cinco números ao usuário. Para
# cada um, chame a função e informe se é par ou ímpar. A função não
# deve solicitar dados nem imprimir mensagens.


def eh_par(numero):
    return numero % 2 == 0

for i in range(5):
    numero = int(input("Digite um número: "))

    if eh_par(numero):
        print("É par")
    else:
        print("É ímpar")