from controllers.controller_admin import controller_admin


class biblioteca:
    @staticmethod
    def cadastrar_usuario():
        controller_admin.cadastrar_usuario()


biblioteca.__name__ = "blibioteca"