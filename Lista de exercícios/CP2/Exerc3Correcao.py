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