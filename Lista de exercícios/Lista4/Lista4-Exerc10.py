# Crie um algoritmo que receba um número inteiro qualquer e exiba a sua
# tabuada de multiplicação do 1 ao 10, apresentando os resultados no
# formato: N x i = Resultado.

n = int(input("Digite o número da tabuada: "))

for i in range(11):
    print(f"{n} x {i} = ", n * i)