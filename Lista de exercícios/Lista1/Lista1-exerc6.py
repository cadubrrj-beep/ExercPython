# Lista de exercícios de Python

#Exercício 6

'''
Escreva um programa que receba dois números inteiros e troque seus
valores utilizando uma terceira variável auxiliar. Exiba os valores antes e
depois da troca.
'''

numeroInteiro1 = input("Informe o primeiro número inteiro: ") #8
numeroInteiro2 = input("Informe o segundo número inteiro: ") #2

print(f"O valor do inteiro1 é {numeroInteiro1} e o valor do inteiro2 é {numeroInteiro2}.")

variavelAux = numeroInteiro1
numeroInteiro1 = numeroInteiro2
numeroInteiro2 = variavelAux

print(f"Depois da inversão o inteiro1 é {numeroInteiro1} e o inteiro2 é {numeroInteiro2}.")
