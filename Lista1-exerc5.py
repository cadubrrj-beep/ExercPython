# Lista de exercícios de Python

#Exercício 5

nomeVendedor = input("Informe o nome do vendedor: ")
qtdProdutos = int(input("Informe a quantidade de produtos vendidos: "))
valorTotal = int(input("Informe o valor total de vendas: R$ "))

comissaoVariavel = valorTotal * 3 / 100
comissaoFixa = 150 * qtdProdutos
valorSalario = 1800

salarioTotal = valorSalario + comissaoVariavel + comissaoFixa

print(f"O total do {nomeVendedor} foi de: R$ {salarioTotal}")
