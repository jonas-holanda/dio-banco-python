# Anotações para a segunda versão
# função saque keyword only - saldo, valor, extrato, limite, numero_saques, limite_saques. Retorno: saldo e extrato

# função depósito positional only - saldo, valor, extrato. Retorno: saldo e extrato.

# função extrato positional e keyword - args posicionais(saldo), args nomeados(extrato).

# novas funções (criar usuario, criar conta corrente, *opcional=listar contas)

# criar usuario: Usarios em uma lista. Usuário: nome, data_nascimento, cpf(números e somente um cpf),
# endereço(logradouro, nro - bairro - cidade/sigla estado)

# criar conta corrente: Contas em uma lista. Conta: agência, número conta, usuário. Número inicia em 1
# agência é fixo 0001. Usuário pode ter mais de uma conta, mas a conta pertence a um só usuário.

def sacar(*,saldo, extrato, limite, LIMITE_SAQUES, numero_saques, contas_corrente):
    conta = conta_usuario_existente(contas_corrente)
    if conta:
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Digite o valor a ser sacado:".rjust(36)))

            if valor > limite:
                print("O valor a ser sacado não pode ser maior que R$500.".center(50))
                return saldo, extrato, numero_saques
            else:
                if valor > saldo:
                    print("Valor do saque maior que o saldo na conta.".center(50))
                    return saldo, extrato, numero_saques
                else:
                    saldo -=valor
                    numero_saques +=1

                    extrato += f"- Valor sacado: -R$ {valor:.2f}  \n"
                    extrato += "".center(36, "-")
                    extrato += "\n" 
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso!".center(50))
                    print()

                    return saldo, extrato, numero_saques
        else:
            print("Você atingiu o limite de saques por hoje. Tente novamente amanhã.".center(50))
    else:
        print("Usuário ou Conta não existe!")
        return saldo, extrato, numero_saques

def depositar(saldo, extrato, contas_corrente, /):
    conta = conta_usuario_existente(contas_corrente)
    if conta:
        valor = float(input("Digite o valor a ser depositado:".rjust(36)))
        saldo +=valor
        extrato += f"- Valor depositado: R$ {valor:.2f}\n"
        extrato += "".center(36, "-")
        extrato += "\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        print()
        return saldo, extrato
    else:
        print("Usuário ou Conta não existe!")
        return saldo, extrato
    
def exibir_extrato(contas_corrente, saldo, /, *, extrato):
    conta = conta_usuario_existente(contas_corrente)
    if conta:
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            print(f"Saldo atual: R$ {saldo:.2f}")
    else:
        print("Usuário ou Conta não existe!")
    
def cadastro_usuario(usuarios):
    dados = {}
    dados["cpf"] = input("Informe o CPF (Somente Números): ")
    usuario = usuario_existente(dados["cpf"], usuarios)
    if usuario:
        print("Usuário já existe!")
        return usuarios
    else:
        dados["nome"] = input("Informe seu Nome: ")
        dados["data_nascimento"] = input("Informe sua data de nascimento: ")
        dados["endereco"] = input("Informe seu Endereço: ")
        usuarios.append(dados)
        print()
        print("Usuário cadastrado com sucesso.")

        return usuarios
           

def usuario_existente(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    return usuarios_filtrados[0] if usuarios_filtrados else None
    

def exibir_usuario(usuarios):
    cpf = input("Informe seu CPF: ")
    usuario = usuario_existente(cpf, usuarios)
    if usuario:
        print(f"Nome: {usuario['nome']}")
        print(f"CPF: {usuario['cpf']}")    
        print(f"Data de Nascimento: {usuario['data_nascimento']}")    
        print(f"Endereço: {usuario['endereco']}")
    else:
        print("Usuário não existe!")

def cadastro_conta_corrente(contas_corrente, AGENCIA, numero_conta, usuarios):
   
    cpf = input("Informe o CPF (Somente Números): ")
    usuario = usuario_existente(cpf, usuarios)
    if usuario:
        dados = {}
        dados["agencia"] = AGENCIA
        dados["numero_conta"] = numero_conta
        dados["cpf_usuario"] = cpf
        contas_corrente.append(dados)
        numero_conta +=1
        print()
        print("Conta corrente cadastrada com sucesso.")
        print(f"O número da sua conta é: {dados['numero_conta']}. Anote.")
        return contas_corrente, numero_conta
    else:
        print("Usuário não existe!")
        return contas_corrente, numero_conta

def exibir_contas(contas_corrente):
    conta = conta_usuario_existente(contas_corrente)
    if conta:
       
        print(f"Agência = {conta['agencia']} ")  
        print(f"Numero conta = {conta['numero_conta']} ")  
 
    else:
      print("Usuário ou Conta não existe!")  
     

def conta_usuario_existente(contas_corrente):
    cpf = input("Informe o CPF (Somente Números): ")
    num_conta = int(input("Informe o Número da Conta: "))
    indice = num_conta-1
    if indice < len(contas_corrente):

        contas_filtradas_cpf = [conta for conta in contas_corrente if contas_corrente[indice]["cpf_usuario"] == cpf]
        contas_filtradas_numero = [conta for conta in contas_corrente if contas_corrente[indice]["numero_conta"] == num_conta]
        return contas_corrente[indice] if contas_filtradas_numero and contas_filtradas_cpf else None
    else:
        print("Conta não existe!")


def main():

    menu = """
    ========= MENU - SYS BANCO =========

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar Usuário
    [5] Cadastrar Conta Corrente
    [6] Exibir dados do Usuário
    [7] Exibir dados da Conta
    [0] Sair

    ==================================== 
    """
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    numero_conta = 1
    usuarios = []
    contas_corrente = []


    while True:
        opcao = int(input(menu))
        print()

        if opcao == 1:
            saldo, extrato = depositar(saldo, extrato, contas_corrente)    

        elif opcao == 2:   
            saldo, extrato, numero_saques = sacar(saldo=saldo, extrato=extrato, limite=limite, LIMITE_SAQUES=LIMITE_SAQUES, numero_saques=numero_saques, contas_corrente=contas_corrente)
       
        elif opcao == 3:
            exibir_extrato(contas_corrente, saldo, extrato=extrato)

        elif opcao == 4:
            usuarios = cadastro_usuario(usuarios)
        
        elif opcao == 5:
            contas_corrente, numero_conta = cadastro_conta_corrente(contas_corrente, AGENCIA, numero_conta, usuarios)
        
        elif opcao == 6:
            exibir_usuario(usuarios)
        
        elif opcao == 7:
            exibir_contas(contas_corrente)

        elif opcao == 0:
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.".center(50))

main()