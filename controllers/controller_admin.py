from models.model_user import user
class controller_admin:
    @staticmethod
    def register_user(nome, cpf, telefone, email):
        user_to_register = user(nome, cpf, telefone, email)
        return user_to_register.create()


controller_admin.__name__ = "controller_admin"