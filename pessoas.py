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

    def informacoes_pessoa(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'CPF: {self.cpf}')


class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade, cpf)
        # Criação da lista para receber as contas dos clientes
        self.contas = []

    @property
    def contas(self):
        return self.__contas

    @contas.setter
    def contas(self, recebe_contas):
        self.__contas = recebe_contas

    # Fazer a agregação da conta com o cliente em uma lista
    def nova_conta(self, conta):
        if conta in self.__contas:
            raise Exception('Conta já cadastrada!')
        self.__contas.append(conta)

    def pessoa_consulta_contas(self):
        print(f'{self.nome} possui {len(self.contas)} conta(s)')
        print('')
        for indice, conta in enumerate(self.contas):
            print(f'índice para acessar: {indice}')
            conta.detalhes()
            print(30 * '-')
