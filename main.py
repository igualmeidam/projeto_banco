from pessoas import Cliente
from contas import ContaCorrente
from banco import Banco
from contas import ContaPoupanca


if __name__ == "__main__":
    # Criação da Pessoa
    pessoa1 = Cliente('Igor', 69, '38051234855')
    pessoa2 = Cliente('Rosana', 69, '13879486875')

    # Criação das Contas com agência e conta
    conta1 = ContaCorrente(467, 103232)  # Pode definir saldo e limite
    conta2 = ContaPoupanca(467, 103232)  # Só pode definir saldo

    # Criação do Banco recebendo nome como atributo
    banco1 = Banco('Antonio')

    pessoa1.nova_conta(conta1)

    # banco1.banco_novo_cliente_conta(pessoa1, conta1)
    # banco1.autoriza_saque(pessoa1)

    pessoa1.contas.sacar(30)
 
    # Agregação dos clientes as contas
    # pessoa1.nova_conta(conta1)
    # pessoa1.nova_conta(conta2)
    # pessoa2.nova_conta(conta1)

