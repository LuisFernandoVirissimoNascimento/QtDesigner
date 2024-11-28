class user:
    def __init__(self, nome, cpf, telefone, email, senha) -> None:
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.senha = senha

    def create(self):
        return f"insert into usuario(nome, cpf, telefone, email, senha) value {self.nome, self.cpf, self.telefone, self.email, self.senha};"
    

user.__name__ = "user"