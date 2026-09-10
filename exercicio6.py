# Lista de exercícios de Python

#Exercício 6

numeroInteiro1 = input("Informe o primeiro número inteiro: ")
numeroInteiro2 = input("Informe o segundo número inteiro: ")

print(f"O valor do inteiro1 é {numeroInteiro1} e o valor do inteiro2 é {numeroInteiro2}.")

variavelAux = numeroInteiro1
numeroInteiro1 = numeroInteiro2
numeroInteiro2 = variavelAux

print(f"Depois da inversão o inteiro1 é {numeroInteiro1} e o inteiro2 é {numeroInteiro2}.")