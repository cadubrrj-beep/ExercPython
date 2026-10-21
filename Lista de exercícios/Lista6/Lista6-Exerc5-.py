# Crie a função calcular_preco_final(preco, percentual), que devolva o
# preço após o desconto. Solicite os dois valores ao usuário e exiba o
# preço original, o valor descontado e o preço final.

preco = int(input("Digite o preço "))
percentual = int(input("Digite o percentual "))

def calcular_preco_final(preco, percentual):
    valorDescontado = (percentual / 100) * preco
    precoFinal = preco - valorDescontado
    return precoFinal

precoFinal = calcular_preco_final(preco, percentual)
valorDescontado = preco - precoFinal


print(f"O preço original é {preco}, o valor descontado é {valorDescontado} e o preço final é {precoFinal}")
