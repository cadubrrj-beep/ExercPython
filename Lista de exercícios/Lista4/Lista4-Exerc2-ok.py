# Elabore um algoritmo que receba a idade de 10 pessoas e, ao final,
# exiba o total de pessoas menores de 18 anos.

maior = []
menor = []

for i in range(10):
    idade = int(input("Digite as idades: "))
    if idade > 17:
        maior.append(idade)
    else:
        menor.append(idade)

print(len(menor), "Foram as idades menores de 18")