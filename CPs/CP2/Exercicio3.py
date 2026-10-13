'''
Escreva um programa que receba números inteiros positivos do usuário.
O programa deve parar quando o usuário digitar 0. Ao final, o sistema
deve exibir a soma total dos números digitados e a média aritmética
(excluindo o zero da média)

Digite um número: 5
Digite um número: 6
Digite um número: 10
Digite um número: 0
Somatória: 21
Média: 7
'''

num = 0
som = 0
med = 0
while True:
    num = int(input("Digite um número: "))
    if num ==0:
        print(f"Somatoria: {som}")
        print(f"Media: {som / med}")
        break
    elif num <0:
        print("Valor invalido, digie um número e digite 0 para calcular")
    else:
        med += 1
        som = som + num


