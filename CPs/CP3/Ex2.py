"""
Crie uma procedure chamada mostrar_tabuada (numero) que exiba a
tabuada de um número de 1 até 10. O programa deve: validar a entrada
e chamar a procedure.
"""

numero = int(input("Digite um número [1 até 10]: "))

def mostrar_tabuada(numero):
    if numero >=11 or numero <=0:
        print("Valor fora do intervalo. É apenas aceito de 1 até 10")
    else:
        for i in range(10):
            tabuada = numero * i
            print(f"{numero}x{i}={(i * numero)} ")

mostrar_tabuada(numero)