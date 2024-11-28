class user:
    def __init__(self, nome, cpf, telefone, email, senha) -> None:
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.senha = senha

    def create(self):
        return f"insert into usuario(nome, cpf, telefone, email, senha) value {self.nome, self.cpf, self.telefone, self.email, self.senha};"
    
    def update(self, id_usuario):
        return f"update usuario set nome = '{self.nome}', cpf = '{self.cpf}', telefone = '{self.telefone}', email = '{self.email}', senha = '{self.senha}' where id_usuario = {id_usuario};"
    def delete(self, id_usuario):
        return f"delete from usuario where id_usuario = {id_usuario};"


    

user.__name__ = "user"