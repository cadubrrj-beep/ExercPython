# Lista de exercícios de Python

#Exercício 5

'''
Uma loja paga aos seus vendedores:
a. Salário base de R$ 1.800,00
b. Comissão fixa de R$ 150,00 por produto vendido
c. 3% sobre o valor total das vendas
Escreva um programa que solicite:
- Nome do vendedor
- Quantidade de produtos vendidos
- Valor total das vendas
O programa deve calcular e exibir o salário final.
'''

nomeVendedor = input("Informe o nome do vendedor: ")
qtdProdutos = int(input("Informe a quantidade de produtos vendidos: "))
valorTotal = int(input("Informe o valor total de vendas: R$ "))

comissaoVariavel = valorTotal * 3 / 100
comissaoFixa = 150 * qtdProdutos
valorSalario = 1800

salarioTotal = valorSalario + comissaoVariavel + comissaoFixa

print(f"O total do {nomeVendedor} foi de: R$ {salarioTotal}")
