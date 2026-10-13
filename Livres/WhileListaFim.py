

nomes = []
nome = 0

while True:
    nome = input("Digite um novo nome: ")
    if nome != "fim":
        nomes.append(nome)
        print(nomes)
    else:
        print(nomes)
        break