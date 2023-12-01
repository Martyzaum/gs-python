import datetime

def agendar_exame():
    # Bem-vindo ao sistema de agendamento de exames!
    print("Bem-vindo ao sistema de agendamento de exames!")

    # Solicita informações do usuário
    nome = input("Por favor, digite seu nome: ")
    idade = input("Por favor, digite sua idade: ")
    cidade = input("Por favor, digite sua cidade: ")

    # Apresenta informações do usuário
    print(f"\nOlá {nome}, de {cidade}. Você tem {idade} anos.")

    # Apresenta opções de exames
    print("\nAqui estão as opções de exames que você pode agendar:")
    print("1. Exame de sangue")
    print("2. Raio-X")
    print("3. Ultrassom")

    # Configuração de tentativas para a escolha do exame
    tentativas = 0
    escolha = None

    # Loop enquanto a escolha não for válida e o número de tentativas for menor que 5
    while escolha not in ['1', '2', '3'] and tentativas < 5:
        escolha = input("\nPor favor, digite o número do exame que você gostaria de agendar: ")

        # Se a escolha não for válida, exibe mensagem e incrementa o contador de tentativas
        if escolha not in ['1', '2', '3']:
            print("\nDesculpe, opção inválida. Por favor, tente novamente.")
            tentativas += 1

    # Se atingir o número máximo de tentativas, encerra o programa
    if tentativas == 5:
        print("\nNúmero máximo de tentativas atingido. Encerrando o programa.")
        return

    # Exibe a escolha do exame
    if escolha == '1':
        print("\nVocê escolheu o exame de sangue.")
    elif escolha == '2':
        print("\nVocê escolheu o raio-X.")
    elif escolha == '3':
        print("\nVocê escolheu o ultrassom.")

    # Apresenta opções de data para o exame
    print("\nAqui estão as opções de data para o seu exame:")
    hoje = datetime.date.today()
    
    for i in range(1, 4):
        data = hoje + datetime.timedelta(days=i)
        print(f"{i}. {data.strftime('%d/%m/%Y')}")

    # Configuração de tentativas para a escolha da data
    tentativas = 0
    data_escolhida = None

    # Loop enquanto a data escolhida não for válida e o número de tentativas for menor que 5
    while data_escolhida not in ['1', '2', '3'] and tentativas < 5:
        data_escolhida = input("\nPor favor, digite o número da data que você gostaria de agendar: ")

        # Se a data escolhida não for válida, exibe mensagem e incrementa o contador de tentativas
        if data_escolhida not in ['1', '2', '3']:
            print("\nDesculpe, opção inválida. Por favor, tente novamente.")
            tentativas += 1

    # Se atingir o número máximo de tentativas, encerra o programa
    if tentativas == 5:
        print("\nNúmero máximo de tentativas atingido. Encerrando o programa.")
        return

    # Calcula a data agendada e exibe mensagem de confirmação
    data = hoje + datetime.timedelta(days=int(data_escolhida))
    print(f"\nObrigado {nome}, seu exame foi agendado para {data.strftime('%d/%m/%Y')}.")

# Chama a função principal
agendar_exame()
