maior_idade = 0
maiores = 0
menores = 0
cliente = 0
for i in range(1,6):
    while True:
        idade = int(input(f"Digite a idade do Cliente [{i}]: "))
        if idade>=0:
            break
        else:
            print("A idade não pode ser negativa")

    if idade >= 18:
        maiores +=1
    else:
        menores +=1

    if idade> maior_idade:
        maior_idade = idade
        cliente = i

print(f"Clientes com 18 anos ou mais: {maiores}")
print(f"Clientes com menos de 18 anos: {menores}")
print(f"Cliente mais velho: Cliente [{cliente}] com {maior_idade} anos")

