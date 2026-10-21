# Crie a função calcular_area_retangulo(base, altura), que devolva a área
# de um retângulo. Solicite base e altura ao usuário, chame a função e
# mostre o resultado fora dela. Teste com base 5 e altura 3, cujo resultado
# esperado é 15.

base = int(input("Digite a base: "))
altura = int(input("Digite a altura: "))

def calcular_area_retangulo(base, altura):
    area = base * altura
    return area

area = calcular_area_retangulo(base, altura)
print(area)
