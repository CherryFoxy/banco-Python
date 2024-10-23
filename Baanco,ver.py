import textwrap

def menu(): #Função MENU

    menu = """\n
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Novo Usuário
    [6] Sair

    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato): #Função Depositar recebe três valores (positian only)
    if valor > 0:
        saldo += valor #Somando o valor ao saldo
        extrato += f"Depósito:\tR$ {valor:2f}\n"
        print("\n*** Depósito realizado com sucesso! ***")
    else:
        print("*** Número de depósito inválido! Por favor, inserir valor válido ***")

    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques): #Função SACAR
    if valor > saldo:
        print("\n *** SALDO INSULFICIENTE! ***")

    elif valor > limite:
        print("\n *** NÃO FOI POSSÍVEL REALIZAR ESSA OPERAÇÃO! SAQUE EXCEDE O LIMITE. ***")

    elif numero_saques >= limite_saques:
        print("\n *** NUMERO DE SAQUES EXCEDIDOS, NÃO FOI POSSÍVEL CONCLUIR A OPERAÇÃO ***")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("=== SAQUE REALIZADO COM SUCESSO! RETIRE O DINHEIRO ===")

    else:
        print("*** VALOR INFORMADO É INVÁLIDO ***")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):  #Função extrato (positional only e keyword only)
    print("\n=== EXTRATO === ")
    print("NENHUMA MOVIMENTAÇÃO REGISTRADA POR AQUI." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("============================")

def criar_usuario(usuarios):
    cpf = input("INFORME O CPF (Somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuarios: #Se usuário não for None, ou seja, já existe um usuario com o mesmo cpf
        print("Já existe um usuário com esse CPF!")
        return
    
    #Crianção do Usuário
    nome = input("Nome completo: ")
    data_nascimento = input("Data de Nascimento: ")
    endereco = input("Endereço (Logradouro, N° - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(" === USUÁRIO CRIADO! === ")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados= [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n*** Usuário não encontrado\nEncerrando Processo! ***")

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas =[]

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("VALOR A SER SACADO: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            break

        else:
            print("*** OPÇÃO INVÁLIDA ***")


main()