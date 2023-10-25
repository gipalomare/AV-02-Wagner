class Cliente:
    def __init__(self, nome, idade, email, senha):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.senha = senha


class CadastroClientes:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, nome, idade, email, senha):
        cliente = Cliente(nome, idade, email, senha)
        self.clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")

    def fazer_login(self, email, senha):
        for cliente in self.clientes:
            if cliente.email == email and cliente.senha == senha:
                print("Login bem-sucedido. Bem-vindo,", cliente.nome)
                return
        print("Login falhou. Verifique suas credenciais.")