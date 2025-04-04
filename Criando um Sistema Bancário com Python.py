menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[l] Limite Diário
[q] Sair

=> """

saldo = 0
limite = 500
limite_diario = 1500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def verificar_limite_diario(limite_diario):
    print(f"\nSeu limite diário restante para saques é de R$ {limite_diario:.2f}.")

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        excedeu_limite_diario = valor > limite_diario  # Verifica se ainda há limite diário disponível

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif excedeu_limite_diario:
            print(f"Operação falhou! Seu limite diário restante é de R$ {limite_diario:.2f}.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            limite_diario -= valor

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "l":
            print(f"\nSeu limite diário restante para saques é de R$ {limite_diario:.2f}.")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")