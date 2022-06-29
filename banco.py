class Banco:
    def __init__(self, nome):
        self._nome = nome
        self._clientes = []
        self._contas = []
        self._clienteconta = []

    def novo_clienteconta(self, cliente, conta):
        self._clienteconta.append((cliente, conta))
        for cliente, conta in self._clienteconta:
            print(cliente, conta)
            print(type(cliente, conta))

    def novo_cliente(self, cliente):
        self._clientes.append(cliente)
        for cliente in self._clientes:
            print(cliente.informacoes_cliente())
            print(type(cliente))

    def nova_conta(self, conta):
        self._contas.append(conta)
        for conta in self._contas:
            print(conta)
            print(type(conta))

    def ver_clientes(self):
        for clientes in self._clientes:
            print(f'Banco {self._nome}')
            clientes.informacoes_cliente()
            clientes.consultar_contas()
            print('')

    def ver_contas(self):
        print(f'Banco {self._nome}')
        for contas in self._contas:
            contas.detalhes()
