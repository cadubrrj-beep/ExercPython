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

soma = 0
qtd = 0

while True:
    numero = int(input("Digite um numero: "))

    if numero == 0:
        break
    elif numero>0:
        soma = soma + numero
        # soma += numero (resumido)
        qtd = qtd + 1
    else:
        print("Numero inválido")

print(f"Somatória: {soma}")

media = soma / qtd
print(f"Média: {media:.2f}")