
total_economizado = 0
mes = 1

while mes<=3:
    valor = float(input(f"Digite o valor a ser economizado no mês {mes} R$: "))
    total_economizado = valor + total_economizado
    mes +=1 #contador

print("Parabéns! você economizou", total_economizado)

#contador normalmente é utilizado na condição do loop
#acumulador pode ser utilizado na condição do loop

#Acumulador pode ser utilizado na condição do loop, não soma valores padronziados.