from models.model_user import user
from bd import database
class controller_admin:
    @staticmethod
    def register_user(nome, cpf, telefone, email, senha):
        user_to_register = user(nome, cpf, telefone, email, senha)
        data_base = database()
        data_base.execute_command(user_to_register.create())


controller_admin.__name__ = "controller_admin"