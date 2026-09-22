'''
Crie um Algoritmo que solicita a entrada de um valor inteiro e exiba uma
mensagem: “é número par” OU “é número ímpar”
'''

numInteiro = int(input("Digite um número inteiro: "))
if numInteiro % 2 == 0:
    resultado = "Número é par"
else:
    resultado = "Número é ímpar"

print(f"O número digitado é {numInteiro} é {resultado}")
