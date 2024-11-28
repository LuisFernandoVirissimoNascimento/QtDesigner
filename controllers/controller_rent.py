from models.model_rent import rent
from bd import database
class controller_user:
    @staticmethod
    def create_rent(cod_livro,email):
        rent_to_create = rent(cod_livro,email)
        data_base = database()
        data_base.execute_command(rent_to_create.create())


controller_user.__name__ = "controller_user"