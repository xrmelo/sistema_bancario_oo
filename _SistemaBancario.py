import textwrap
#from abc import ABC , abstractclassmethod, abstractproperty
# from datetime import datetime

import PessoaFisica , ContaCorrente,  Deposito ,Saque
from F_function  import f_menu, f_encontrar_cliente
from F_function  import recuperar_conta_cliente


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = f_encontrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = f_encontrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = f_encontrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

#--------------------------------------------------------------------------------------------------------------
def f_criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = f_encontrar_cliente(cpf, clientes)

    if not cliente:     
       nome = input("Informe o nome completo: ")
       data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
       endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

       # cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
       retorno = clientes.append(cliente)
       print("\n=== xxxxx Cliente criado com sucesso! ===")       
    else:    
        retorno = None
        print("\n@@@ Já existe cliente com esse CPF! @@@")
    return retorno

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = f_encontrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = f_menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":         
            cliente = f_criar_cliente(clientes)
            if cliente:
                print("\n=== xxxxx Cliente criado com sucesso! ===")   
            else:
                print("\n@@@ Já existe cliente com esse CPF! @@@")

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


main()