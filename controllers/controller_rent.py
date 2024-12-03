from models.model_rent import rent
from bd import database
class controller_rent:
    @staticmethod
    def create_rent(isbn,email):
        rent_to_create = rent(isbn,email)
        data_base = database()
        data_base.execute_command(rent_to_create.create())


controller_rent.__name__ = "controller_rent"