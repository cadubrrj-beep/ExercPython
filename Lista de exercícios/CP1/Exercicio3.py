'''
Problema

Desenvolva um algoritmo que solicite ao usuário o valor total de uma compra. O sistema deve aplicar um percentual
de desconto com base na faixa de valor informada:
a. Compras acima de R$ 100,00: Aplicar 10% de desconto e exibir
a mensagem: "Você ganhou 10% de desconto!".
b. Compras de até R$ 100,00: Aplicar 5% de desconto e exibir a mensagem: "Você ganhou 5% de desconto!".
O algoritmo deve garantir que valores iguais a R$ 100,00 recebam o desconto de 5%, conforme a regra de "até". (1 ponto)

Output esperado
Digite o valor da compra: R$ 100.00
Você ganhou 5% de desconto!

Digite o valor da compra: R$ 300.00
Você ganhou 10% de desconto!
'''










'''
# Código entregue
compra = float(input("Digite o valor da compra: R$ "))

if compra > 100:
    desconto = compra * 0.10
    print("Você ganhou 10% de desconto!")
elif compra <= 100:
    desconto = compra * 0.05
    print("Você aganhou 5% de desconto!")
'''