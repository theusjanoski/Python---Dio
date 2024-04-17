def menu():
    menu = """
    ========= Banco Central =========

        [d]  Depositar
        [s]  Sacar
        [e]  Extrato
        [nu] Novo usuário
        [nc] Nova conta
        [lc] Listar contas
        [q]  Sair

    =================================
    => """
    return input(menu)


def depositar(saldo, valor, depositos, /):
    if valor > 0:
        saldo += valor
        depositos.append(valor)
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, depositos


def sacar(*, saldo, valor, saques, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        saques.append(valor)
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, saques


def exibir_extrato(saldo, /, *, saques, depositos):
        print("=============== EXTRATO ===============")
        print("Depósitos:")
        for i, valor in enumerate(depositos, 1):
            print(f"[{i}] {valor:.2f}")
        print(f"Total de depósitos: {sum(depositos):.2f}")
        print(" ")

        print("Saques:")
        for i, valor in enumerate(saques, 1):
            print(f"[{i}] {valor:.2f}")
        print(f"Total de saques: {sum(saques):.2f}")
        print(" ")

        print(f"O valor atual na conta é de {saldo:.2f}")
        print("=======================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: {conta['agencia']}
            C/C:     {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    numero_saques = 0
    depositos = []
    saques = []
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, depositos = depositar(saldo, valor, depositos)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, saques = sacar(
                saldo=saldo,
                valor=valor,
                saques=saques,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, saques=saques, depositos=depositos)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
