'''
def valida_senha (senha):
    if len(senha) >= 8:
        return True
    else:
        return Fal
'''




def valida_senha (senha):
    return len (senha)>=8

def main():
    while True:
        senha = input("Digite uma senha: ")

        if valida_senha (senha) :
            print("Senha válida")
            break

        print("Senha inválida")