'''
Crie um algoritmo que calcula o salário de um determinado vendedor. É
necessário solicitar a entrada:
a. Salário Fixo
b. Valor de Vendas
Sabendo-se que ele recebe uma comissão de 5% sobre o total das
vendas em até R$5.000,00 e 7% sobre o que ultrapassar. Exiba o salário
total do vendedor e a comissão que ele irá receber.
'''

salFixo = int(input("Informe o salário fixo do vendedor. R$: "))
valVendas = int(input("Informe o valor de vendas. R$: "))
valorCorte = int(5000)
comissaoBase = int()
comissaoExtra = int()

if valVendas <= valorCorte:
    comissaoBase = valorCorte * 0.05
else:
    comissaoExtra = (valVendas - valorCorte) * 0.07
    comissaoBase = valorCorte * 0.05

somaComissao = comissaoBase + comissaoExtra
salFinal = (salFixo + somaComissao)

print(f"Com um total de comissões de {somaComissao} nesse mês, o salário do vendedor ficou em R$ {salFinal}")