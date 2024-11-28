from controllers.controller_admin import controller_admin
from bd import database

class biblioteca:
    @staticmethod
    def register_user(nome, cpf, telefone, email):
        controller_admin.register_user(nome, cpf, telefone, email)


biblioteca.__name__ = "blibioteca"