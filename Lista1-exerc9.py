# Lista de exercícios de Python

#Exercício 9

inputHora = float(input("Informe a quantidade de horas: "))

conversaoMinutos = (float(inputHora * 60))
conversaoSegundos = (float(conversaoMinutos * 60))
# por segundos para hora seria 3600 a multiplicação

print(f"A hora informada se traduz em {conversaoMinutos} minutos ou {conversaoSegundos} segundos")
