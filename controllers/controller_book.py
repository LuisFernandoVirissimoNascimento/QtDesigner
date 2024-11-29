from models.model_book import book
from bd import database
class controller_book:
    @staticmethod
    def create_book(titulo, autor, genero, isbn):
        book_to_create = book(titulo, autor, genero, isbn)
        data_base = database()
        data_base.execute_command(book_to_create.create())


controller_book.__name__ = "controller_book"