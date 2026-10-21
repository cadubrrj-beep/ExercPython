# Implemente duas versões para calcular a média de duas notas:
# a. exibir_media(nota1, nota2), que mostra o resultado dentro da
# própria função, e
# b. calcular_media(nota1, nota2), que devolve o resultado com
# return.
# c. Chame as duas versões. Use o valor devolvido pela segunda
# para informar “Aprovado” quando a média for maior ou igual a 6 e
# “Reprovado” nos demais casos.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = 0

def exibir_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    print(f"A média é de {media}")

#calcula e mostra a media
exibir_media(nota1, nota2)

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

#calcula e devolve média que por sua vez fica guardada na variável resultado
resultado = calcular_media(nota1, nota2)

if resultado >= 6:
    print("Aprovado")
else:
    print("Reprovado")




