# Crie um algoritmo que calcula o salário de um determinado vendedor. É
# necessário solicitar a entrada:
# a. Salário Fixo
# b. Valor de Vendas
# Sabendo-se que ele recebe uma comissão de 5% sobre o total das
# vendas em até R$5.000,00 e 7% sobre o que ultrapassar. Exiba o salário
# total do vendedor e a comissão que ele irá receber.

salario = int(input("Digite o salário fixo: R$"))
valorVenda = int(input("Digite o valor de vendas: R$"))
comissaoBase = 0
comissaoExtra = 0

if valorVenda <= 5000:
    comissaoBase = valorVenda * 0.05
else:
    comissaoExtra = (valorVenda - comissaoBase) * 0.07

print(f"O salário total foi de R$ {salario + comissaoBase + comissaoExtra:.2f} composto de comissão de R$ {comissaoBase + comissaoExtra:.2f}")