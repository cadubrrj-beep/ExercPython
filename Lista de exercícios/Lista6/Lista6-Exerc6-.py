# Crie a função maior_numero(a, b), que devolva o maior dos dois valores.
# Se forem iguais, a função deve devolver esse valor. Faça três chamadas
# com pares de números diferentes.

def maior_numero(a, b):
    if a > b:
        #return print(f"{a} maior que {b}")
        return a
    elif a < b:
        #return print(f"{b} maior que {a}")
        return b
    else:
        #return print("Ambos são iguais")
        return a

for i in range(3):
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    resultado = maior_numero(a, b)

    print(f"O maior número é {resultado}")





