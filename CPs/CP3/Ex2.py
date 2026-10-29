"""
Crie uma procedure chamada mostrar_tabuada (numero) que exiba a
tabuada de um número de 1 até 10. O programa deve: validar a entrada
e chamar a procedure.
"""


'''
numero = int(input("Digite um número [1 até 10]: "))

def mostrar_tabuada(numero):
    if numero >=11 or numero <=0:
        print("Valor fora do intervalo. É apenas aceito de 1 até 10")
    else:
        for i in range(10):
            tabuada = numero * i
            print(f"{numero}x{i}={(i * numero)} ")

mostrar_tabuada(numero)
'''



def mostrar_tabuada(numero):
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")


def valida_numero():
    while True:
        numero = int(input("Digite um número [1 até 10]: "))

        if numero >= 1 and numero <= 10:
            return numero

        print("Valor fora do intervalo. São aceitos apenas números de 1 até 10.")


def main():
    numero = valida_numero()
    mostrar_tabuada(numero)


main()
