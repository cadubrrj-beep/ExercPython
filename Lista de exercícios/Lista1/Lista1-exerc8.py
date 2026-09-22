# Lista de exercícios de Python

#Exercício 8

'''
Escreva um programa que receba:
- Distância percorrida (km)
- Quantidade de combustível gasto (litros)
Calcule e exiba o consumo médio do veículo (km/l).
'''

distPercorrida = float(input("Informe a distância percorrida: "))
combGasto = float(input("Informe o combustível gasto: "))

gastoTotal = (distPercorrida / combGasto)

print(f"O gasto médio ficou em: {gastoTotal} litros por quilômetro rodado.")
