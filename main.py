from pessoas import Cliente
from contas import ContaCorrente
from banco import Banco
from contas import ContaPoupanca


if __name__ == "__main__":
    pessoa1 = Cliente('Igor', 69, '13879486875')
    conta1 = ContaCorrente(467, 103232)
    conta2 = ContaPoupanca(467, 103232)
    banco1 = Banco('Tei')
    banco1.nova_conta(conta1)
    banco1.novo_cliente(pessoa1)
    pessoa1.consultar_contas()
   