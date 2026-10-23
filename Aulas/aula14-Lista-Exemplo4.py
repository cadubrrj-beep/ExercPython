pokemons = ["Pikachu", "Mew", "Abra", "Charmander", "Rayquaza", "Dragonite", "Lucario"]

print(pokemons, len(pokemons))

pokemons.append("Mewtwo")
pokemons.append("Articuno")
pokemons.append("Zapdos")
pokemons.append("Moltres")

print(pokemons, len(pokemons))

#insert(indice, valor): adicionar um item atraves de uma posicão
pokemons.insert(1, "Gengar")

#extend([valor, valor, valor]): adicionar multiplos itens
pokemons.extend(["Eevee"])

#pop(index): remover item da lista por base do index
pokemons. pop (3)
print(pokemons)

#reverse: inverte a ordem original da lista
pokemons.reverse()
print(pokemons)

#sort: Ordenar valores de uma listano modo crescente(A-Z, 0-n, etc)
pokemons.sort()
print(pokemons)

#remove(valor): remover um item da lista por base do valor
pokemons. remove("Zapdos")
print(pokemons)

#del(index)
del pokemons [17]
print(pokemons)

del pokemons[1:3] #Remove o 1 e o 2 (intervalo)
print(pokemons)

#clear(): Limpar a lista
pokemons.clear()
print(pokemons)

