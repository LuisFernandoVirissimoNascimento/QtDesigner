class user:
    def __init__(self,id_usuario, nome, cpf, telefone) -> None:
        self.id_usuario = id_usuario
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def create(self):
        return f"insert into usuario(id_usuario, nome, cpf, telefone) value {self.id_usuario, self.nome, self.cpf, self.telefone};"
    

user.__name__ = "user"