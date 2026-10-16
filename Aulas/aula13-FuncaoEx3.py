def alterar(n1):
    n1 = n1 + 1 # variável local via redeclaração
    print("Dentro da função: ", n1)

    n1 = 10 # variável global

    alterar(n1)

    print("Fora da função: ", n1)
