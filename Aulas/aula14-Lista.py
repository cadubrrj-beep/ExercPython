veiculos = ["Gol", "Kwid", "HB20", "UP", "Mobi"]


#Acessar os elementos
#Acesso rápido: Lista e seu índice
#Toda índice de lista começa com 0

#Recuperar e alterar valores

print("veiculos[2]")

veiculo = veiculos[3]
print(veiculo)

#alterando um elemento da lista
veiculos[1] = "BYD"
print(veiculos[1])

#Trocando itens na lista
veiculo1 = veiculos[1]
veiculo2 = veiculos[2]
veiculos[1] = veiculo2
veiculos[2] = veiculo1

print(veiculos)

#Acesso posicional
#For-each
#For item in nome_lista
print("Percorrendo uma lista com for-each")
i=0

#Item é uma variável local, craida para receber 1 valor da lista a cada loop
for item in veiculos:
    print(f"{i} : {item}")
    i+=1

#Obter o tamanho da lista
print("Tamanho da lista é: ", len(veiculos))


# Ou
# For
# For i in range(len(lista))
print("Percorrendo uma lista com for")
#for necessita da variavel i para percorrer na lista
for i in range(len(veiculos)):
    print(f"{i} : {veiculos}")
    #i: index

# Ou
# While i < len(lista):

ii = 0
print("Percorrendo uma lista com While")
while ii< len(veiculos):
    print(f"{ii} : {veiculos[ii]}")
    ii+=1