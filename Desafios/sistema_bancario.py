menu = """
========= Banco Central =========

    [d] Depósitar
    [s] Sacar
    [e] Extrato
    [q] Sair

=================================
=> """

saldo = 0
limite = 500
numeros_saque = 0
saques = []
depositos = []
LIMITE_SAQUE = 3


while True:

    opcao = input(menu).strip().lower()

    if opcao == "d":
        deposito = float(input("Digite o valor: "))

        if deposito > 0:
            saldo += deposito
            depositos.append(deposito)
            print(f"Depósito de {deposito:.2f} feito com sucesso!")
        else:
            print("Operação falhou! O valor de depósito deve ser maior que R$0,00")
    
    elif opcao == "s":
        if numeros_saque < LIMITE_SAQUE:
            saque = float(input("Digite o valor de saque: "))
            
            if saque > limite:
                print("Valor não autorizado, máximo de R$500,00")
            elif saque > saldo:
                print("Não será possível sacar por falta de saldo.")
            else:
                saldo -= saque
                saques.append(saque)
                numeros_saque += 1
                print(f"Saque de {saque:.2f} feito com sucesso!")
        else:
            print("Limite de saque diário atingido!")
    
    elif opcao == "e":
        print(" ")
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
    
    elif opcao == "q":
        print("Obrigado pela preferência, volte sempre!")
        break

    else:
        print("Operação inválida, por favor seleciona a opção desejada.")

    print(" ")