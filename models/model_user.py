class user:
    def __init__(self, nome, cpf, telefone, email) -> None:
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    def create(self):
        return f"insert into usuario(nome, cpf, telefone, email) value {self.nome, self.cpf, self.telefone, self.email};"
    

user.__name__ = "user"