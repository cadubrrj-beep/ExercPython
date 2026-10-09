# Projeto: NextLevel - Challenge Turma do Bem
# Programa com menu para orientar quem quer ajudar a Turma do Bem

while True:
    # ---------- MENU PRINCIPAL ----------
    print("\n===== TURMA DO BEM =====")
    print("\nDigite uma opção de contato:")
    print("1 - Quero ajudar")
    print("2 - Preciso de ajuda")
    print("3 - Contato")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao.isdigit():
        opcao = int(opcao)

        match opcao:
            # ---------- OPÇÃO 1: Quero ajudar ----------
            case 1:
                print("\nComo você pode ajudar?")
                print("1 - Doar via Pix e outras formas")
                print("2 - Doar pela Nota Fiscal Paulista")
                print("3 - Quero ser um dentista voluntário ou voluntário de outra especialidade")
                print("0 - Voltar ao menu principal")

                escolha_ajuda = input("Escolha: ")

                match escolha_ajuda:
                    # ----- Simular doação -----
                    case "1":
                        print("\n--- Simular doação ---")

                        # Regra de negócio: valor mínimo de doação é R$ 1
                        while True:
                            valor = input("Qual o valor da doação em R$ (apenas números)? ")
                            if not valor.isdigit():
                                print("Valor inválido! Digite apenas números.")
                            else:
                                valor = int(valor)
                                if valor < 1:
                                    print("O valor mínimo para doação é R$ 1.")
                                else:
                                    break

                        # Escolha da forma de pagamento
                        while True:
                            print("\nForma de pagamento:")
                            print("1 - Pix")
                            print("2 - Cartão de crédito")
                            print("3 - Boleto")
                            pagamento = input("Escolha: ")

                            match pagamento:
                                case "1":
                                    forma = "Pix"
                                    break
                                case "2":
                                    forma = "Cartão de crédito"
                                    break
                                case "3":
                                    forma = "Boleto"
                                    break
                                case _:
                                    print("Opção inválida. Escolha de 1 a 3.")

                        # Saída do resultado com f-string
                        print(f"\nObrigado pela sua doação de R$ {valor} via {forma}! Simulação concluída com sucesso.")

                    # ----- Nota Fiscal Paulista -----
                    case "2":
                        print("Cadastre a Turma do Bem na Nota Fiscal Paulista.")
                        print("Entenda os passos em: https://bit.ly/3VxBvzK")

                    # ----- Voluntário -----
                    case "3":
                        print("\nComo você pode se voluntariar?")
                        print("1 - Sou dentista e quero fazer parte da Turma do Bem")
                        print("2 - Sou profissional de outra área e quero fazer parte da Turma do Bem")
                        print("0 - Voltar ao menu principal")

                        voluntario = input("Escolha: ")

                        match voluntario:
                            case "1":
                                print("\n--- Cadastro de dentista voluntário ---")

                                # Regra de negócio: só continua o cadastro se houver disponibilidade
                                while True:
                                    print("Você tem disponibilidade para atender como voluntário na sua clínica?")
                                    print("1 - Sim")
                                    print("2 - Não")
                                    disponibilidade = input("Escolha: ")
                                    if disponibilidade == "1" or disponibilidade == "2":
                                        break
                                    else:
                                        print("Opção inválida. Escolha 1 ou 2.")

                                if disponibilidade == "2":
                                    print("Infelizmente só aceitamos dentistas que possam atender em pelo menos um horário livre na própria clínica.")
                                    print("Quando tiver disponibilidade, faça seu cadastro novamente. Voltando ao menu principal...")
                                else:
                                    # Entrada com validação do nome do dentista
                                    while True:
                                        nome = input("Qual o seu nome? ")
                                        if nome == "":
                                            print("Nome inválido! O nome não pode ficar vazio.")
                                        elif nome.isdigit():
                                            print("Nome inválido! Não digite apenas números.")
                                        else:
                                            break

                                    # Entrada com validação do CRO (apenas números)
                                    while True:
                                        cro = input("Qual o seu número do CRO (apenas números)? ")
                                        if not cro.isdigit():
                                            print("CRO inválido! Digite apenas números.")
                                        else:
                                            break

                                    # Entrada com validação da cidade
                                    while True:
                                        cidade = input("Em qual cidade você atua? ")
                                        if cidade == "":
                                            print("Cidade inválida! Não pode ficar vazia.")
                                        elif cidade.isdigit():
                                            print("Cidade inválida! Não digite apenas números.")
                                        else:
                                            break

                                    print(f"\nObrigado, {nome}! Cadastro do CRO {cro} ({cidade}) recebido com sucesso. Entraremos em contato em breve")
                                    print("Para mais informações sobre o programa visite: https://bit.ly/4hKyrb0")

                            case "2":
                                print("Para outras especialidades entre em contato pelo e-mail faleconosco@tdb.org.br")

                            case "0":
                                print("Voltando ao menu principal...")

                            case _:
                                print("Opção inválida. Escolha uma das opções listadas.")

                    case "0":
                        print("Voltando ao menu principal...")

                    case _:
                        print("Opção inválida. Escolha uma das opções listadas.")

            # ---------- OPÇÃO 2: Preciso de ajuda ----------
            case 2:
                # Validação do nome: repete até digitar algo válido
                while True:
                    nome = input("\nQual o seu nome? ")
                    if nome == "":
                        print("Nome inválido! O nome não pode ficar vazio.")
                    elif nome.isdigit():
                        print("Nome inválido! Não digite apenas números.")
                    else:
                        break

                idade = input("\nQual a sua idade? ")

                if idade.isdigit():
                    idade = int(idade)
                    # Regra de negócio: a ONG atende pessoas em vulnerabilidade socioeconômica entre 11 e 17 anos
                    if 11 <= idade <= 17:
                        print(f"Olá, {nome} com {idade} anos, você pode receber tratamentos pela ONG. Entre em contato pelo site https://turmadobem.org.br/contato/")
                    else:
                        print(f"Infelizmente {nome} com {idade} anos, não é possível se cadastrar no programa. Atendemos apenas na faixa de 11 a 17 anos")
                else:
                    print("Idade inválida! Digite apenas números.")

            # ---------- OPÇÃO 3: Contato ----------
            case 3:
                # Validação do nome
                while True:
                    nome = input("\nQual é o seu nome? ")
                    if nome == "":
                        print("Nome inválido! O nome não pode ficar vazio.")
                    elif nome.isdigit():
                        print("Nome inválido! Não digite apenas números.")
                    else:
                        break

                # Validação do telefone (apenas números, com DDD)
                while True:
                    telefone = input("\nQual é o seu telefone com DDD (apenas números)? ")
                    if not telefone.isdigit():
                        print("Telefone inválido! Digite apenas números.")
                    else:
                        break

                # Validação da mensagem
                while True:
                    mensagem = input("\nEscreva sua mensagem: ")
                    if mensagem == "":
                        print("A mensagem não pode ficar vazia.")
                    else:
                        break

                print(f"\nObrigado, {nome}! Recebemos sua mensagem \"{mensagem}\". Caso necessite de uma resposta, entraremos em contato pelo telefone {telefone}.")

            # ---------- OPÇÃO 4: Sair ----------
            case 4:
                print("Obrigado por visitar a Turma do Bem. Até logo!")
                break

            # Qualquer outro número
            case _:
                print("Opção inválida! Escolha de 1 a 4.")

    else:
        # Não digitou número: programa volta ao menu
        print("Opção inválida! Digite apenas números.")