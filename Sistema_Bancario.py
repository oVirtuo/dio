#Projeto v1.0 Sistema Bancario: implementar funcao de deposito, saque e extrato

#Variaveis da conta
valor_na_conta = 1000
valor_deposito = 0
valor_saque = 0
limite_de_saque_diario = 3
hist_deposito = []
hist_saque = []

def deposito(valor_na_conta, hist_deposito):
    global valor_deposito

    valor_deposito = float((input("\nInsira o valor do deposito: ")))
    while valor_deposito != None:
        if valor_deposito > 0:
            valor_na_conta += valor_deposito
            hist_deposito.append(("R$ "+ str(valor_deposito)))
            print(f"\nAgora voce tem R$ {valor_na_conta} na sua conta.")
            break
        else:
            print("\nValor de deposito invalido ou muito baixo. Tente nvamente.")
            deposito(valor_na_conta, hist_deposito)
    menu(valor_na_conta, valor_deposito, valor_saque)

def saque(valor_na_conta, hist_saque):
    global valor_saque
    global limite_de_saque_diario

    while valor_saque != None:
        if limite_de_saque_diario <= 0:
            print("\nVoce excedeu o limite de saques por hoje. Encerrando funcao.")
            break
        else:
            valor_saque = float((input("Insira o valor do saque: ")))
            while valor_saque != None:
                if valor_na_conta <= 0:
                    print("\nSaldo insuficiente para saque.")
                    break
                elif valor_saque > 500:
                    print("\nVoce nao pode sacar um valor maior que R$500,00. Tente novamente.")
                    saque(valor_na_conta, hist_saque)
                elif valor_saque <= 0:
                    print("\nValor de saque invalido. Tente novamente.")
                    saque(valor_na_conta)
                else:
                    limite_de_saque_diario -=1
                    valor_na_conta -= valor_saque
                    hist_saque.append(("R$ "+ str(valor_saque)))
                    print(f"\nAgora voce tem R$ {valor_na_conta} na sua conta.")
                    break
        break
    menu(valor_na_conta, valor_deposito, valor_saque)

def extrato(valor_na_conta, valor_ultimo_deposito, valor_ultimo_saque):
    ext = "Extrato"
    print()
    print(ext.center(25, "#"))
    print(f"Valor na conta: R$ {valor_na_conta:.2f}")
    if hist_deposito:
        print(f"Historico de depositos:")
        for depositos in hist_deposito:
            print(depositos)
    else:
        print("\nNão foram realizados depositos.")
    if hist_saque:
        print(f"Historico de saques:")
        for saques in hist_saque:
            print(saques)
    else:
        print("Não foram realizados saques.")
    menu(valor_na_conta, valor_ultimo_deposito, valor_ultimo_saque)


def menu(valor_na_conta, valor_deposito, valor_saque):

    print(f'''
    ############### MENU ###############
        Bem vindo. Selecione a ação:

        1 - Depósito
        2 - Saque
        3 - Extrato
        
        0 - Sair

    ####################################
    ''')

    opcao = int(input())

    while opcao != 0 and opcao != None:
        if opcao == 1:
            deposito(valor_na_conta, hist_deposito)
        elif opcao == 2:
            saque(valor_na_conta, hist_saque)
            
        elif opcao == 3:
            extrato(valor_na_conta, hist_deposito, hist_saque)
            
        elif opcao == 0:
            print("Voce escolheu sair. Obrigado pela preferencia")
            break
            
        else:
            print("Opcao invalida. Selecione novamente.")
            menu(valor_na_conta, valor_deposito, valor_saque)


menu(valor_na_conta, valor_deposito, valor_saque)