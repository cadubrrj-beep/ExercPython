'''
Uma loja deseja analisar o perfil de 5 clientes. Crie um algoritmo que
solicite a idade de cada um desses 5 clientes e, ao final, informe:
a. b. Quantas pessoas têm 18 anos ou mais.
Quantas pessoas têm menos de 18 anos.
c. A idade da pessoa mais velha.

Output esperado:
Digite a idade do Cliente [1] : 20
Digite a idade do Cliente [2] : 17
Digite a idade do Cliente [3] : 25
Digite a idade do Cliente [4] : 35
Digite a idade do Cliente [5] : 55
Clientes com idade superior a 18 anos: 1
Clientes com idade inferior a 18 anos: 4
Cliente mais velho: Cliente [5] com 55
'''

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

