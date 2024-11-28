from controllers.controller_admin import controller_admin


class biblioteca:
    @staticmethod
    def cadastrar_usuario(nome, cpf, telefone, email):
        controller_admin.cadastrar_usuario(nome, cpf, telefone, email)


biblioteca.__name__ = "blibioteca"