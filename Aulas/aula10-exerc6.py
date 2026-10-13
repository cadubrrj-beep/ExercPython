idade = int(input("Digite a sua idade: "))
cnh = input("Tem CNH? (sim ou não)? ").lower()

'''
match idade,cnh:
    case i,c if i>=18 and c=="sim":
        print("Permitido a dirigir")
    case i,c if i<18 and c=="não":
        print("Não é permitido a dirigir")
    case i,c if i>18 and c=="não":
        print("Tem idade para tirar a CNH, mas não pode dirigir")
    case _:
        print("Valores inválidos")
'''

#ou de uma maneira mais direta

'''
match idade,cnh:
    case i, _ if i < 0:
        print("Idade inválida")
    case i, "sim" if i>=18 :
        print("Permitido a dirigir")
    case i, "não" if i<18 :
        print("Não é permitido a dirigir")
    case i, "não" if i>18 :
        print("Tem idade para tirar a CNH, mas não pode dirigir")
    case i, "sim" if i<18:
        print("Você não tem idade suficiente para ter uma CNH definitiva")
    case _:
        print("Valores inválidos")
  '''

#Usando If-ElIf

if idade<0:
    print("Idade invalida")
elif idade>=18 and cnh=="sim":
    print("Permitido a dirigir")
elif idade>=18 and cnh=="não":
    print("Tem idade para tirar CNH, mas não pode dirigir")
elif idade<18 and cnh=="não":
    print("Não é permitido a dirigir")
elif idade<18 and cnh=="sim":
    print("Você não tem idade suficiente para ter uma CNH definitiva")
else:
    print("Valores invalidos")