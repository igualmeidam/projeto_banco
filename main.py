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
    conta3 = ContaCorrente(9999, 1234567491)

    # Criação do Banco recebendo nome como atributo
    banco1 = Banco('Antonio')

    # Objeto cliente agrega as contas
    pessoa1.nova_conta(conta1)
    pessoa1.nova_conta(conta2)
    pessoa2.nova_conta(conta3)

    # Cadastra os clientes e contas no sistema banco
    banco1.banco_cadastra_cliente_conta(pessoa1, conta1)
    banco1.banco_cadastra_cliente_conta(pessoa2, conta3)

    # instancia o banco realizando a consulta de cls e contas agregadas
    banco1.consulta_cliente_contas()

    # Realiza o saque recebendo:
    # O cliente, indice do cl, índice da conta, e o valor p/ a operação
    banco1.banco_sac(pessoa1, 0, 0, 10)
    banco1.banco_sac(pessoa2, 1, 0, 30)
