# Desenvolva um algoritmo que receba dois números distintos. Utilize uma
# estrutura de repetição para garantir que os valores sejam diferentes e,
# após a validação, exiba a soma entre eles.

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

while True:
    if x != y:
        soma = x + y
        print("Os números são diferentes e a soma deles é: ", soma)
        break
    else:
        print("Os números são iguais")
        break






