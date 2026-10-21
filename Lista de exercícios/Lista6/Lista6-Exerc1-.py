# Crie uma função chamada exibir_saudacao() que mostre a mensagem
# “Bem-vindo à aula de funções!”. Chame a função duas vezes no
# programa principal. Explique em um comentário por que a mensagem só
# aparece quando a função é chamada.

'''
msg = str("Bem vindo a aula de funções!")

def exibir_saudacao():
    print(msg)

exibir_saudacao()
exibir_saudacao()
'''


def exibir_saudacao(msg =("Digite a mensagem que vc deseja")):
    print(msg)

exibir_saudacao("Bem vindo a aula de funções!")
exibir_saudacao("Bem vindo a aula de funções!")

# A mensagem só aparece quando a função é chamada duas vezes. Nesse caso eu defini a mensagem já no chamado da função e não como o exemplo anterior eu já vinha carregada de antes.