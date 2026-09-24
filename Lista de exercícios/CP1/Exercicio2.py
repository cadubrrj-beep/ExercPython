'''
Problema

Escreva um programa que receba duas notas informadas pelo usuário e calcule a sua média aritmética simples.
O sistema deve exibir a mensagem "Média [valor] - Reprovado" se o resultado for inferior a 5,0, ou "Média
[valor] - Aprovado" caso seja igual ou superior a esse valor. (1 ponto)

Output esperado
Nota 1: 6.0
Nota 2: 6.0

Média 6 - Aprovado

Nota 1: 3.0
Nota 2: 4.0

Média 3.5 - Reprovado
'''










'''
# Código entregue
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

media = (n1 + n2) / 2

if media <= 5:
    print(f"Média {media} - Reprovado")
else:
    print(f"Média {media} - Aprovado")
'''