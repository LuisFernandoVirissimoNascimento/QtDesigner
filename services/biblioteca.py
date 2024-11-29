from controllers.controller_admin import controller_admin
from controllers.controller_rent import controller_rent
from controllers.controller_book import controller_book

class biblioteca:
    @staticmethod
    def register_user(nome, cpf, telefone, email, senha, senha_confirmar):
        if senha != senha_confirmar:
            print("This password is not the same.")
            return
        controller_admin.register_user(nome, cpf, telefone, email, senha)
    @staticmethod
    def update_user(id_usuario, nome, cpf, telefone, email, senha):
        controller_admin.update_user(id_usuario, nome, cpf, telefone, email, senha)
    @staticmethod
    def delete_user(id_usuario):
        controller_admin.delete_user(id_usuario)
    @staticmethod
    def create_rent(cod_livro, email):
        controller_rent.create_rent(cod_livro, email)
    @staticmethod
    def create_book(titulo, autor, genero, isbn):
        controller_book.create_book(titulo, autor, genero, isbn)

biblioteca.__name__ = "blibioteca"