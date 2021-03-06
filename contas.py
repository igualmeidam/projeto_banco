""" Módulo de criação das contas, corrente e poupança.

Esse módulo é responsável pela criação e especificação das classes de contas,
seja ela uma conta corrente ou poupança, através da herança da super
classe Conta.
"""
from abc import abstractmethod, ABC


class Conta(ABC):  # Criação da super classe abstrata
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, recebe_agencia):
        if not isinstance(recebe_agencia, (int)):
            raise ValueError('Valor tem de ser numérico!')
        if recebe_agencia >= 10000:
            raise Exception('Número da agência inválida!')
        self.__agencia = recebe_agencia

    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self, recebe_conta):
        if not isinstance(recebe_conta, (int)):
            raise ValueError('Valor tem de ser numérico!')
        recebe_conta = str(recebe_conta)
        if len(recebe_conta) != 10:
            raise Exception('Número da conta inválido!')
        recebe_conta = int(recebe_conta)
        self.__conta = recebe_conta

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (float, int)):
            raise ValueError('Saldo precisa ser numérico')
        self.__saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (float, int)):
            raise ValueError('O valor para depósito precisa ser numérico')
        self.saldo += valor
        print(f'Você depositou {valor}R$')
        print(f'Saldo:{self.saldo}')

    def detalhes(self):
        print(f'Tipo da conta: {__class__.__name__}')
        print(f'Agência:{self.agencia}', end=' ')
        print(f' Conta:{self.conta}', end=' ')
        print(f' Saldo:{self.saldo}', end=' ')

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, recebe_limite):
        self.__limite = recebe_limite

    def detalhes(self):
        print(f'Tipo da conta: {__class__.__name__}')
        print(f'Agência:{self.agencia}', end=' ')
        print(f' Conta:{self.conta}', end=' ')
        print(f' Saldo:{self.saldo}', end=' ')
        print(f' Limite:{self.limite}')

    def sacar(self, valor):
        if not isinstance(valor, (float, int)):
            raise ValueError('O valor para depósito precisa ser numérico')
        if (self.saldo + self.limite) < valor:
            raise Exception('Seu saldo é insuficiente!')
        self.saldo -= valor
        print(f'Você sacou {valor}R$')
        print(f'Saldo:{self.saldo}')
        print(f'Limite:{self.limite}')

    def depositar(self, valor):
        if not isinstance(valor, (float, int)):
            raise ValueError('O valor para depósito precisa ser numérico')
        self.saldo += valor
        print(f'Você depositou {valor}R$')
        print(f'Saldo:{self.saldo}')
        print(f'Limite:{self.limite}')


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if not isinstance(valor, (float, int)):
            raise ValueError('O valor para depósito precisa ser numérico')
        if self.saldo < valor:
            raise Exception('Seu saldo é insuficiente!')
        self.saldo -= valor
        print(f'Você sacou {valor}R$')
        print(f'Saldo:{self.saldo}')

    def detalhes(self):
        print(f'Tipo da conta: {__class__.__name__}')
        print(f'Agência:{self.agencia}', end=' ')
        print(f' Conta:{self.conta}', end=' ')
        print(f' Saldo:{self.saldo}', end=' ')
