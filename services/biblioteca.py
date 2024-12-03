from controllers.controller_admin import controller_admin
from controllers.controller_rent import controller_rent
from controllers.controller_book import controller_book

class biblioteca:
    ########## User
    @staticmethod
    def create_user(nome, cpf, telefone, email, senha, senha_confirmar):
        if senha != senha_confirmar:
            print("This password is not the same.")
            return
        controller_admin.create_user(nome, cpf, telefone, email, senha)
    @staticmethod
    # Controller_admin.read_user retorna uma tuple dupla a partir do id do usuário, logo separamos em dois for loops que nos da uma index de ambos o usuário e os items do usuário.
    # A Primeira index (i) sempre é o usuário listado.
    # A Segunda index (j) sempre é o item do usuário, seja nome, cpf, telefone, email ou senha.
    # Indexes dos items significam:
    # 0 - ID
    # 1 - Nome
    # 2 - CPF
    # 3 - Telefone
    # 4 - Email
    # 5 - Senha
    def read_user(this, id_usuario):
        data = controller_admin.read_user(id_usuario)
        amount_rows = len(data)
        this.l_user.setRowCount(amount_rows)
        for i in range(len(data)):
            for j in range(len(data[i])):
                this.l_user.setItem(i, j, j)
                print(f"Index [{i}][{j}]: {data[i][j]}")
    @staticmethod
    def update_user(id_usuario, nome, cpf, telefone, email, senha):
        controller_admin.update_user(id_usuario, nome, cpf, telefone, email, senha)
    @staticmethod
    def delete_user(id_usuario):
        controller_admin.delete_user(id_usuario)
    ########## Rent
    @staticmethod
    def create_rent(cod_livro, email):

        controller_rent.create_rent(cod_livro, email)
    ########## Book
    @staticmethod
    def create_book(titulo, autor, genero, isbn):
        controller_book.create_book(titulo, autor, genero, isbn)
    @staticmethod
    def update_book(titulo, autor, genero, isbn):
        controller_book.update_book(titulo, autor, genero, isbn)
    @staticmethod
    def delete_book(isbn):
        controller_book.delete_book(isbn)

biblioteca.__name__ = "blibioteca"