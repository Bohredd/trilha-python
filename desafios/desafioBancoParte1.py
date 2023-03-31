opcoesMenu = """
[D] Depositar
[S] Sacar
[E] Extrato
[N] Sair
"""

funcionalidadeBanco = ""

saldoUsuario = 0
limite = 500
extrato = ""
numeroSaques = 0 
saquesMaximos = 5 

while funcionalidadeBanco != "N":
    print("Digite sua opcao de funcionalidade! ")
    funcionalidadeBanco = str(input(opcoesMenu))
    
    if funcionalidadeBanco == "D":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldoUsuario += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
        
    elif funcionalidadeBanco == "S":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldoUsuario

        excedeu_limite = valor > limite

        excedeu_saques = numeroSaques >= saquesMaximos

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldoUsuario -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeroSaques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
        
    elif funcionalidadeBanco == "E":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldoUsuario:.2f}")
        print("==========================================")
        
    elif funcionalidadeBanco == "N":
        break
        
    else:
        print("Erro! Digite novamente: ")