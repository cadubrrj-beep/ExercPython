opcao = int(input("Digite uma opcao (0 até 3): "))

'''A estrutura match case por padrão compara valores por igualdade. Em outras linguagens é conhecida como Switch-Case.
No Match, informamos a variável que será verificada, no nosso caso é "Opção". No Match não há limitação para cases,
podemos ter N. Porém, de maneira mínima há 1 CASE e 1 CASE Default (case -:)'''

match opcao:
    case 0: #opcao == 0
        print("Opção 0")
    case 1: #opcao == 1
        print("Opção 1")
    case 2: #opcao == 2
        print("Opção 2")
    case 3: #opcao == 3
        print("Opção 3")
    case _: #else
        print("Valor incorreto. Digite de 0 até 3")

#OU

if opcao == 0:
    print("Opção 0")
elif opcao == 1:
    print("Opcao 1")
elif opcao == 2:
    print("Opcao 2")
elif opcao == 3:
    print("Opcao 3")
else:
    print("Valor incorreto. Digite de 0 a 3")

