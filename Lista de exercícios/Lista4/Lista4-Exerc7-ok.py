# Escreva um algoritmo que receba um número inteiro positivo N e calcule
# o seu fatorial. Lembre-se que o fatorial é o produto de todos os inteiros
# positivos menores ou iguais a N.

numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("Número inválido.")

else:
    fatorial = 1
    contador = numero

    while contador > 1:
        fatorial *= contador
        contador -= 1

    print(f"O fatorial de {numero} é {fatorial}")
