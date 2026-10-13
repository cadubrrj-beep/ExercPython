# Você está recebendo uma lista de valores representando os produtos de sua loja virtual e gostaria de calcular a soma
# total desses produtos para entender o desempenho financeiro semanal.

#valores = [10, 20, 30, 40, 50]
#Crie um programa para implementar a soma.
#Saída esperada:
# A soma total das receitas é: 150


valores = [10, 20, 30, 40, 50]
somaTotal = 0

for i in valores:
    somaTotal += i
    print(f"A soma total das receitas é: {somaTotal}")

