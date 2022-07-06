class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.__clientes = []
        self.__cpf_clientes = []
        self.__contas = []
        self.__numero_contas = []
        self.__agencias = []

    @property
    def nome(self):
        return self.__nome

    # Recebe o nome do banco permitindo apenas uma string com letras
    @nome.setter
    def nome(self, recebe_nome_banco):
        if not recebe_nome_banco.isalpha():
            raise Exception('Nome do banco inválido!')
        self.__nome = recebe_nome_banco

    #  Adiciona o OBJETO cliente em uma lista e checa por repetições
    def banco_novo_cliente(self, recebe_cliente):
        for cliente_cadastrado in self.__clientes:
            if recebe_cliente == cliente_cadastrado:
                raise Exception('Cliente já cadastrado!')
        self.self.__clientes.append(recebe_cliente)

    # Adiciona o CPF do cliente em uma lista e checa por duplicatas
    def banco_novo_cpf_cliente(self, recebe_cliente):
        for cpf_cadastrado in self.__cpf_clientes:
            if cpf_cadastrado == recebe_cliente.cpf:
                raise Exception('CPF já cadastrado no sistema!')
        self.__cpf_clientes.append(recebe_cliente.cpf)

    #  Adiciona o OBJETO conta em uma lista e checa por repetições
    def banco_nova_conta(self, recebe_conta):
        for conta_cadastrada in self.__contas:
            if recebe_conta == conta_cadastrada:
                raise Exception('Conta já cadastrada!')
        self.__contas.append(recebe_conta)

    # Adiciona o numero da conta do cliente em uma lista e checa por duplicatas
    def banco_novo_numero_conta(self, recebe_conta):
        for conta_cadastrada in self.__numero_contas:
            if conta_cadastrada == recebe_conta.conta:
                raise Exception('Numero da conta já cadastrado no sistema!')
        self.__numero_contas.append(recebe_conta.conta)
        print(self.__numero_contas)

    def autoriza_saque(self, cliente):
        pass
