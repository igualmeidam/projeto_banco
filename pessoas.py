from abc import abstractmethod, ABC
from validador_cpf import remover_caracteres, valida_cpf


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter  # Recebe o nome, e verifica se não é um número
    def nome(self, recebe_nome):
        if not isinstance(recebe_nome, str):
            raise Exception('Seu nome não pode ser um número!')
        self.__nome = recebe_nome

    @property
    def idade(self):
        return self.__idade

    # Recebe a idade, verifica se é um numero inteiro e se está no limite
    @idade.setter
    def idade(self, recebe_idade):
        if not isinstance(recebe_idade, int):
            raise ValueError('Idade precisa ser um número inteiro')
        if recebe_idade >= 150:
            raise Exception('Idade limite atingida!')
        self.__idade = recebe_idade

    @property
    def cpf(self):
        return self.__cpf

    # Recebe o cpf, trata os caracteres, e faz a validação do cpf recebido
    @cpf.setter
    def cpf(self, recebe_cpf):
        recebe_cpf = str(recebe_cpf)
        recebe_cpf = remover_caracteres(recebe_cpf)
        if valida_cpf(recebe_cpf):
            self.__cpf = recebe_cpf
        else:
            raise Exception('Seu CPF é invalido!')


class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade, cpf)
        # Criação da lista para receber as contas dos clientes
        self.__contas = []

    # Fazer a agregação da conta com o cliente em uma lista
    def nova_conta(self, conta):
        self.__contas.append(conta)

    # Faz a consulta das contas agregadas pelo cliente
    def consultar_contas(self):
        if not len(self.__contas) >= 2:
            print(f'Possui apenas {len(self.__contas)} conta')
        else:
            print(f'Possui {len(self.__contas)} contas')
        for conta in self.__contas:
            print(f'{self.__nome} possui uma {conta.__class__.__name__}')
            print(f'Número da agência: {conta.agencia}')
            print('fNumero da conta: {conta.conta}')
            print(f'Saldo Atual: {conta.saldo}')

    def informacoes_cliente(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'CPF: {self.cpf}')
