# Lista de exercícios de Python

#Exercício 5

nomeVendedor = input("Informe o nome do vendedor: ");
numeroVendas = int(input("Informe a quantidade de produtos vendidos: "));
valorTotalVendas = int(input("Informe o total de vendas: "));
comissaoFixa = numeroVendas * 150;
comissaoVariavel = (comissaoFixa * 3) / 100;

salarioTotal = (1800 + comissaoFixa + comissaoVariavel);

print(f"O total do {nomeVendedor} foi de : R$ {salarioTotal}");