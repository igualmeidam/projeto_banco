class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.__cpf_clientes = []
        self.__agencias = [1111, 2222, 3333]
        self.__contas = []
        self.__clienteconta = {}

    @property
    def nome(self):
        return self.__nome

    # Recebe o nome do banco permitindo apenas uma string com letras
    @nome.setter
    def nome(self, recebe_nome_banco):
        if not recebe_nome_banco.isalpha():
            raise Exception('Nome do banco inválido!')
        self.__nome = recebe_nome_banco

    # Adiciona o CPF do cliente em uma lista e checa casos de repetição
    def banco_novo_cpf_cliente(self, cliente):
        for cpf in self.__cpf_clientes:
            if cliente.cpf == cpf:
                raise Exception('Cliente já cadastrado!')
        self.__cpf_clientes.append(cliente.cpf)
         
    #  Adiciona o numero da conta em uma lista e checa casos de repetição
    def banco_nova_conta_cliente(self, conta):
        for conta_cadastrada in self.__contas:
            if conta.conta == conta_cadastrada:
                raise Exception('Conta já cadastrada!')
        self.__contas.append(conta.conta)

    # Adiciona o cliente e a conta respectiva em um dicionário
    def banco_novo_cliente_conta(self, cliente, conta):
        for clientes in self.__clienteconta.keys():
            if clientes == cliente:
                raise Exception('Cliente ja cadastrado!')
        self.__clienteconta[cliente] = conta

    def autoriza_saque(self, cliente):
        if cliente not in self.__clienteconta.keys():
            raise Exception('Cliente não cadastrado!')
        return True
