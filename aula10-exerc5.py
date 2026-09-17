idade - int(input("Digite a sua idade: "))

'''
X é o valor que vem da variável idade foi definido uma variável genérica para informar um valor possível
'''

match idade:
    case x if x >= 18:
        print("Maior de idade")
    case x if x <18:
        print("Menor de idade")
    case _:
        print("Valor inválido")
