# Desenvolva um algoritmo que solicite o salário atual de um funcionário e
# o percentual de reajuste. O programa deve calcular o valor do aumento
# e exibir o novo salário atualizado.

salario = int(input("Digite o salário: "))
reajuste = int(input("Digite o reajuste: "))

ajustado = (reajuste / 100)

print("O salário ajustado ficou em: ",salario + (salario * ajustado))