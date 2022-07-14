from pessoas import Cliente
from contas import ContaCorrente
from banco import Banco
from contas import ContaPoupanca


if __name__ == "__main__":
    # Criação da Pessoa
    pessoa1 = Cliente('Igor', 69, '38051234855')
    pessoa2 = Cliente('Rosana', 69, '13879486875')

    # Criação das Contas com agência e conta
    conta1 = ContaCorrente(9999, 1234567891)  # Pode definir saldo e limite
    conta2 = ContaPoupanca(9999, 1234567893)  # Só pode definir saldo
    conta3 = ContaCorrente(6899, 1257557878)

    # Criação do Banco recebendo nome como atributo
    banco1 = Banco('Antonio')

    # Objeto cliente agrega as contas
    pessoa1.nova_conta(conta1)
    pessoa1.nova_conta(conta2)
    pessoa2.nova_conta(conta3)

    # Cadastra os clientes e contas no sistema banco
    banco1.banco_cadastra_cliente_conta(pessoa1, conta1)
    banco1.banco_cadastra_cliente_conta(pessoa2, conta3)

    # Acesso através da agregação
    banco1.consulta_cliente_contas()

    if banco1.autoriza_saque_cliente(pessoa2, 0):
        banco1.clientes[0].contas[0].depositar(30)
    else:
        raise Exception('Cliente/Conta não cadastrados!')
