# Lista de exercícios de Python

#Exercício 7

'''
Escreva um programa que receba um número inteiro com quatro dígitos
e mostre o número invertido.

Entrada: 1234
Saída: 4321
'''

entrada = input("Informe um número com 4 dígitos: ")

saida = int(str(entrada)[::-1])

print(f"A inversão fica {saida}.")
