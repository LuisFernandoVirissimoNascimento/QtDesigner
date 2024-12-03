from models.model_user import user

class admin(user):

    def create(self):
        return f"insert into usuario(nome, cpf, telefone, email, senha) value {self.nome, self.cpf, self.telefone, self.email, self.senha};"
    def read(self):
        return f"select * from usuario"
    def delete(self, id_usuario):
        return f"delete from usuario where id_usuario = {id_usuario};"


    

admin.__name__ = "admin"