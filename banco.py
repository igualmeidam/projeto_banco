class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.__cpf_clientes = []
        self.__contas = []
        self.__numero_contas = []

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
        for conta_cadastrada in self.__numero_contas:
            if recebe_conta.conta == conta_cadastrada:
                raise Exception('Numero da conta já cadastrado no sistema!')
        self.__numero_contas.append(recebe_conta.conta)

    def banco_cadastra_cliente_conta(self, recebe_cliente, recebe_conta):
        self.banco_novo_cliente(recebe_cliente)
        self.banco_novo_cpf_cliente(recebe_cliente)
        self.banco_nova_conta(recebe_conta)
        self.banco_novo_numero_conta(recebe_conta)

    def consulta_cliente_contas(self):
        indice = 0
        for cliente in self.__clientes:
            print(f'indice para acessar: {indice}')
            cliente.informacoes_pessoa()
            cliente.pessoa_consulta_contas()
            indice += 1
