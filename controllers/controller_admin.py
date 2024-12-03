from models.model_admin import admin
from controllers.controller_user import controller_user
from bd import database
class controller_admin(controller_user):
    @staticmethod
    def create_user(nome, cpf, telefone, email, senha):
        user_to_register = admin(nome, cpf, telefone, email, senha)
        data_base = database()
        data_base.execute_command(user_to_register.create())

    @staticmethod
    def delete_user(id_usuario):
        user_to_delete = admin("0","0","0","0","0")
        data_base = database()
        data_base.execute_command(user_to_delete.delete(id_usuario))

    @staticmethod
    def read_user():
        user_to_read = admin("0","0","0","0","0")
        data_base = database()
        return data_base.read_command(user_to_read.read())


controller_admin.__name__ = "controller_admin"