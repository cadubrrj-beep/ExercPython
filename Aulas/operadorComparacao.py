

'''
num = int(input("Digite um número: "))

if num == 5:
    print("5 é a quantidade de títulos que o Brasil tem")
else:
    print("Digite outro número")
'''

'''
senha = input("Digite a senha: ")

if senha != "Fiap":
    print("Senha incorreta")
else:
    print("Acesso permitido")
'''

#Operadores de comparação
# > Maior que
# < Menor que
# >= Maior ou igual
# <= Menor ou igual
# == Igualdade
# != Diferente

'''
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if senha != "Fiap" or usuario !="Admin":
    print("Nome de usuário ou senha estão incorretos")
else:
    print("Acesso permitido")
'''

'''
if senha == "Fiap" and usuario =="Admin":
    print("Acesso permitido")
else:
    print("Nome de usuário ou senha estão incorretos")
'''


'''
# Jeito 1

idade = int(input("Digite a sua idade: "))
cnh = input("Tem CNH? (Sim ou Não): ")

if idade>=18 and cnh=="sim":
    print("Você é permitido a dirigir")
elif idade>=18 and cnh=="não":
    print("Você tem o direito em solicitar a CNH, mas não pode dirigir")
else:
    print("Você não tem idade para dirigir")
'''

'''
#Jeito 2

idade = int(input("Digite a sua idade: "))
cnh = input("Tem CNH? (Sim ou Não): ")

if idade>=18:
    if cnh=="sim":
        print("Você é permitido a dirigir")
    else:
        print("Você tem o direito em solicitar a CNH, mas não pode dirigir")
else:
    print("Você não tem idade para dirigir")
'''


dia = int(input("Digite o dia da semana: "))

if dia==7 or dia==1:
    print("Final de semana")
elif dia==2 or dia==3 or dia==4 or dia==5 or dia==6:
    print("Dia útil")
'''
if dia==7 or dia==1:
    print("Final de semana")
elif dia>=2 and dia<=6:
    print("Dia útil")
'''









