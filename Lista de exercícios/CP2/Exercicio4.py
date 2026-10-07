

c1 = int(input("Digite a idade do Cliente [1] :"))
c2 = int(input("Digite a idade do Cliente [2] :"))
c3 = int(input("Digite a idade do Cliente [3] :"))
c4 = int(input("Digite a idade do Cliente [4] :"))
c5 = int(input("Digite a idade do Cliente [5] :"))

#Idade superior a 18
maior = 0

if c1 >= 18:
    maior += 1
if c2 >= 18:
    maior += 1
if c3 >= 18:
    maior += 1
if c4 >= 18:
    maior += 1
if c5 >= 18:
    maior += 1

print("Clientes com idade superior a 18 anos: ", maior)


#Idade menor que 18
menor = 0

if c1 <= 18:
    menor += 1
if c2 <= 18:
    menor += 1
if c3 <= 18:
    menor += 1
if c4 <= 18:
    menor += 1
if c5 <= 18:
    menor += 1

print("Clientes com idade inferior a 18 anos: ", menor)


#C - mais velho
if c1 >= c2 and c3 and c4 and c5:
    print(f"Cliente mais velho: Cliente [1] com", c1)
elif c2 >= c1 and c3 and c4 and c5:
    print(f"Cliente mais velho: Cliente [2] com", c2)
elif c3 >= c1 and c2 and c4 and c5:
    print(f"Cliente mais velho: Cliente [3] com", c3)
elif c4 >= c1 and c2 and c3 and c5:
    print(f"Cliente mais velho: Cliente [4] com", c4)
else:
    print(f"Cliente mais velho: Cliente [5] com", c5)