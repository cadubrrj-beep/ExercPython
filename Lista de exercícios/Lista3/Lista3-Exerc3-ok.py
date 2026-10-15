# Crie um Algoritmo que solicita a entrada de dois valores inteiros. O primeiro valor é das “horas”
#  e o segundo dos “minutos”. Valide se a hora e minutos estão dentro do valor permitido,
#  sendo de 0 até 23 para horas 0 até 59 para minutos.

num1 = int(input("Digite o primeiro número: "))

while num1 < 0 or num1 > 23:
    print("Valor inválido, digite novamente")
    num1 = int(input("Digite o primeiro número: "))

num2 = int(input("Digite o segundo número: "))

while num2 < 0 or num2 > 59:
    print("Valor inválido, digite novamente")
    num2 = int(input("Digite o segundo número: "))

print(f"São {num1} horas e {num2} minutos")

'''
num1 = 0
num2 = 0

while num1 >= 0 and num1 <= 23:
    num1 = int(input("Digite o primeiro número: "))
else:
    print("Valor inválido, digite novamente")
    num1 = int(input("Digite o primeiro número: "))


while num2 >= 0 and num2 <= 59:
    num2 = int(input("Digite o segundo número: "))
    break
else:
    print("Valor inválido, digite novamente")
    num2 = int(input("Digite o segundo número: "))

print(f"São {num1} horas e {num2} minutos")
'''
