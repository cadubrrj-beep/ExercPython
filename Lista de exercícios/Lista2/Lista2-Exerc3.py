'''
Crie um Algoritmo que solicita a entrada de dois valores inteiros. O
primeiro valor é das “horas” e o segundo dos “minutos”. Valide se a hora
e minutos estão dentro do valor permitido, sendo de 0 até 23 para horas
e 0 até 59 para minutos.
'''

valorInteiro1 = int(input("Digite as horas: "))
valorInteiro2 = int(input("Digite os minutos: "))
if valorInteiro1 and valorInteiro2 >= 0 and valorInteiro1 <= 23 and valorInteiro2 <= 59:
    print(f"São {valorInteiro1} horas e {valorInteiro2} minutos")
else:
    print("Um ou mais valores não estão corretos")

'''
Usando While

while True:
    valorInteiro1 = int(input("Informe as horas (0 a 23): "))
    if valorInteiro1 < 0:
        print("Valor precisa ser igual ou maior que 0")
    elif valorInteiro1 > 23:
        print("Valor precisa ser menor que 23")
    else:
        break

while True:
    valorInteiro2 = int(input("Informe os minutos: "))
    if valorInteiro2 < 0:
        print("Valor precisa ser igual ou maior que 0")
    elif valorInteiro2 > 59:
        print("Valor precisa ser menor que 59")
    else:
        break

print(f"São {valorInteiro1} horas e {valorInteiro2} minutos")

'''
