
""" Módulo de criação da classe Banco.

Módulo de criação da classe banco, que agrega clientes e contas para fazer
a verificação de os mesmos estão cadastrados em seu "sistema", e através
dele realizar o saque caso as verificações retornem válidas.
"""


class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.__cpf_clientes = []
        self.__contas = []
        self.__nm = []

    @property
    def nome(self):
        return self.__nome

    #  Recebe o nome do banco permitindo apenas uma string com letras
    @nome.setter
    def nome(self, recebe_nome_banco):
        if not recebe_nome_banco.isalpha():
            raise Exception('Nome do banco inválido!')
        self.__nome = recebe_nome_banco

    #  Getter e Setter p/ ter acesso a instanciação do cliente
    @property
    def clientes(self):
        return self.__clientes

    @clientes.setter
    def clientes(self, recebe_cliente):
        self.__clientes = recebe_cliente

    #  Adiciona o OBJETO cliente em uma lista e checa por repetições
    def banco_novo_cliente(self, recebe_cliente):
        for cliente_cadastrado in self.__clientes:
            if recebe_cliente == cliente_cadastrado:
                raise Exception('Cliente já cadastrado!')
        self.__clientes.append(recebe_cliente)

    #  Adiciona o CPF do cliente em uma lista e checa por duplicatas
    def banco_novo_cpf_cliente(self, recebe_cliente):
        for cpf_cadastrado in self.__cpf_clientes:
            if recebe_cliente.cpf == cpf_cadastrado:
                raise Exception('CPF já cadastrado no sistema!')
        self.__cpf_clientes.append(recebe_cliente.cpf)

    #  Adiciona o OBJETO conta em uma lista e checa por repetições
    def banco_nova_conta(self, recebe_conta):
        for conta_cadastrada in self.__contas:
            if recebe_conta == conta_cadastrada:
                raise Exception('Conta já cadastrada!')
        self.__contas.append(recebe_conta)

    #  Adiciona o numero da conta do cliente em uma lista e checa por duplicata
    def banco_novo_numero_conta(self, recebe_conta):
        for conta_cadastrada in self.__nm:
            if recebe_conta.conta == conta_cadastrada:
                raise Exception('Numero da conta já cadastrado no sistema!')
        self.__nm.append(recebe_conta.conta)

    # Agrega as funções de inserção do cliente ao banco
    def banco_cadastra_cliente_conta(self, recebe_cliente, recebe_conta):
        self.banco_novo_cliente(recebe_cliente)
        self.banco_novo_cpf_cliente(recebe_cliente)
        self.banco_nova_conta(recebe_conta)
        self.banco_novo_numero_conta(recebe_conta)

    # Fas a consulta dos clientes e das contas com seus índices
    def consulta_cliente_contas(self):
        for indice, cliente in enumerate(self.__clientes):
            print(f'indice para acessar: {indice}')
            cliente.informacoes_pessoa()
            cliente.pessoa_consulta_contas()

    # Faz a verificação e a autorização do saque
    def autoriza_saque_cliente(self, recebe_cliente, indice_co):
        if recebe_cliente not in self.clientes:
            raise Exception('Cliente não cadastrado!')
        if recebe_cliente.cpf not in self.__cpf_clientes:
            raise Exception('CPF do cliente não cadastrado!')
        if recebe_cliente.contas[indice_co] not in self.__contas:
            raise Exception('Conta não cadastrada')
        if recebe_cliente.contas[indice_co].conta not in self.__nm:
            raise Exception('Numero da conta não cadastrado!')
        return True

    # Faz o saque através do banco
    def banco_sac(self, cliente, ind_cl, ind_co, val):
        if not cliente == self.clientes[ind_cl]:
            raise Exception('Verificação para o cliente errado!')
        if self.autoriza_saque_cliente(cliente, ind_co):
            print(f'Acesso ao cliente {cliente.nome}')
            self.clientes[ind_cl].contas[ind_co].sacar(val)

    # Faz o depósito através do banco
    def banco_dep(self, cliente, ind_cl, ind_co, val):
        if not cliente == self.clientes[ind_cl]:
            raise Exception('Verificação para o cliente errado!')
        if self.autoriza_saque_cliente(cliente, ind_co):
            print(f'Acesso ao cliente {cliente.nome}')
            self.clientes[ind_cl].contas[ind_co].depositar(val)
