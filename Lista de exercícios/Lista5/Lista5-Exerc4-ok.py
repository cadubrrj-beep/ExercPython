# Crie um Algoritmo que recebe um número inteiro e mostre o menu para
# selecionar o tipo de cálculo que deve ser realizado. Exiba o resultado do
# cálculo efetuado.
# 1 - O dobro
# 2 - A metade
# 3 - 10% do número

valor = int(input("Insira um número inteiro: "))
operacao = int(input("Selecione a operação da calculadora. Digite (1) para dobrar o valor, (2) dividir pela metade, (3) informar 10% do valor informado"))

match operacao:
    case 1:
        print("O valor dobrado fica em: ", (valor * 2))
    case 2:
        print("O valor pela metade fica em: ", (valor / 2))
    case 3:
        print("10% do valor fica em: ", (valor * 0.1))