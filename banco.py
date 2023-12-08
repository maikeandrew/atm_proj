"""Codigo do ATM"""
from typing import List
from time import sleep


from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []


def main() -> None:
    """Main"""
    menu()


def menu() -> None:
    """Menu inicial"""
    print("====================================")
    print("=============== ATM ================")
    print("=========== Bank Project ===========")
    print("=========== Menu Inicial ===========")
    print("====================================")

    print("Selecione uma opcao no menu: ")
    print("1 - Criar Conta")
    print("2 - Efetuar Saque")
    print("3 - Efetuar Deposito")
    print("4 - Efetuar Transferencia")
    print("5 - Listar Contas")
    print("6 - Sair do Sistema")

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print("Volte Sempre")
        sleep(2)
        exit(0)
    else:
        print("Opcao invalida")
        sleep(2)
        menu()


def criar_conta() -> None:
    """Cadastro de conta"""
    print("Informe os dados do cliente: ")

    nome: str = input("Nome do cliente: ")
    email: str = input("E-Mail do cliente: ")
    cpf: str = input("CPF do cliente: ")
    data_nascimento: str = input("Data de Nascimento do Cliente: ")

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print("Conta criada com sucesso!")
    print("Dados da conta: ")
    print("-----------------")
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    """Efetuar saque"""
    if len(contas) > 0:
        numero: int = int(input("Informe o numero da sua conta: "))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input("Informe o valor do saque: "))

            conta.sacar(valor)

            print('Saque efetuado com sucesso')
        else:
            print(f"Nao foi encontrado a conta com numero {numero}")
    else:
        print("Ainda nao existem contas cadastradas.")
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    """Depositar"""
    if len(contas) > 0:
        numero: int = int(input("Informe o numero da conta pra deposito: "))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input("Informe o valor do deposito: "))

            conta.depositar(valor)
        else:
            print(f"Conta com o numero {numero} nao encontrada.")
    else:
        print("Ainda nao existem contas cadastradas.")
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    """Transferencias"""
    if len(contas) > 0:
        numero_o: int = int(input("Informe o numero da conta: "))

        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input("Informe o numero da conta destino: "))

            conta_d: Conta = buscar_conta_por_numero(numero_d)
            if conta_d:
                valor: float = float(input("Informe o valor da transferencia: "))

                conta_o.transferir(conta_d, valor)
            else:
                print(f"O numero {conta_d} nao foi encontrado.")
        else:
            print(f"A sua conta com nuemro {numero_o} nao foi encontrada.")
    else:
        print("Ainda nao existem contas cadastradas.")
    sleep(2)
    menu()


def listar_contas() -> None:
    """Listagem de contas"""
    if len(contas) > 0:
        print("Listagem de contas")

        for conta in contas:
            print(conta)
            print("--------------------")
            sleep(1)
    else:
        print("Nao existem contas cadastradas.")
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    """Buscas"""
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == "__main__":
    main()
