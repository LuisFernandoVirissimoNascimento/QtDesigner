from models.model_user import user

class admin(user):

    def create(self):
        return f"insert into usuario(nome, cpf, telefone, email, senha) value {self.nome, self.cpf, self.telefone, self.email, self.senha};"


    

admin.__name__ = "admin"