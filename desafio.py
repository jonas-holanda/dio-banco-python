menu = """
========= MENU - SYS BANCO =========

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

==================================== 
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Digite o valor a ser depositado: "))
        saldo +=valor
        extrato += f"- Valor depositado: R$ {valor:.2f} \n"
        extrato += "".center(36, "-")
        extrato += "\n"    

    elif opcao == 2:
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Digite o valor a ser sacado: "))

            if valor > 500:
                print("O valor a ser sacado não pode ser maior que R$500.")
            else:
                if valor > saldo:
                    print("Valor do saque maior que o saldo na conta.")
                else:
                    saldo -=valor
                    numero_saques +=1

                    extrato += f"- Valor sacado: -R$ {valor:.2f}  \n"
                    extrato += "".center(36, "-")
                    extrato += "\n"  
        else:
            print("Você atingiu o limite de saques por hoje. Tente novamente amanhã.")    

    elif opcao == 3:
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            print(f"  Saldo atual: R$ {saldo:.2f}")

    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")