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
        self.__agencia = recebe_agencia

    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self, recebe_conta):
        self.__conta = recebe_conta

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (float, int)):
            raise ValueError('Saldo precisa ser numérico')
        self.__saldo = valor

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def detalhes(self):
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

    def sacar(self, valor):
        if not isinstance(valor, (float, int)):
            raise ValueError('O valor para depósito precisa ser numérico')
        if (self.saldo + self.limite) < valor:
            raise Exception('Seu saldo é insuficiente!')
        self.saldo -= valor
        print(f'Você sacou {valor}R$')
        self.detalhes()

    def depositar(self, valor):
        if not isinstance(valor, (float, int)):
            raise ValueError('O valor para depósito precisa ser numérico')
        self.saldo += valor
        print(f'Você depositou {valor}R$')
        self.detalhes()

    def detalhes(self):
        print(f'Tipo da conta: {__class__.__name__}')
        print(f'Agência:{self.agencia}', end=' ')
        print(f' Conta:{self.conta}', end=' ')
        print(f' Saldo:{self.saldo}', end=' ')
        print(f' Limite:{self.limite}')


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo=0):
        super().__init__(agencia, conta, saldo)

    def sacar(self, valor):
        if not isinstance(valor, (float, int)):
            raise ValueError('O valor para depósito precisa ser numérico')
        if self.saldo < valor:
            raise Exception('Seu saldo é insuficiente!')
        self.saldo -= valor
        print(f'Você sacou {valor}R$')
        self.detalhes()

    def depositar(self, valor):
        if not isinstance(valor, (float, int)):
            raise ValueError('O valor para depósito precisa ser numérico')
        self.saldo += valor
        print(f'Você depositou {valor}R$')
        self.detalhes()

    def detalhes(self):
        print(f'Tipo da conta: {__class__.__name__}')
        print(f'Agência:{self.agencia}', end=' ')
        print(f' Conta:{self.conta}', end=' ')
        print(f' Saldo:{self.saldo}', end=' ')
