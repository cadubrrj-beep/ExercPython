# Elabore um algoritmo que receba 15 números inteiros e, ao final, informe
# quantos desses valores estão compreendidos no intervalo entre 10 e 50
# (inclusive).

inteiros = 0
dentro = 0
fora = 0

while inteiros < 15:
    numero = int(input("Digite um número inteiro: "))

    if numero >= 10 and numero <= 50:
        inteiros += 1
        dentro += 1
    else:
        inteiros += 1
        fora += 1

print(f"Os números dentro do intervalo são {dentro} e os fora {fora}")