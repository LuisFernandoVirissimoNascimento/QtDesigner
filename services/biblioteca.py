from controllers.controller_admin import controller_admin

class biblioteca:
    @staticmethod
    def register_user(nome, cpf, telefone, email, senha, senha_confirmar):
        if senha != senha_confirmar:
            print("nu uh")
            return
        controller_admin.register_user(nome, cpf, telefone, email, senha)
    @staticmethod
    def update_user(id_usuario, nome, cpf, telefone, email, senha):
        controller_admin.update_user(id_usuario, nome, cpf, telefone, email, senha)

biblioteca.__name__ = "blibioteca"