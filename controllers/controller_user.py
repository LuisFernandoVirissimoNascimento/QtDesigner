from models.model_user import user
from bd import database
class controller_user:
    @staticmethod
    def update_user(id_usuario, nome, cpf, telefone, email, senha):
        user_to_update = user(nome, cpf, telefone, email, senha)
        data_base = database()
        data_base.execute_command(user_to_update.update(id_usuario))    


controller_user.__name__ = "controller_user"