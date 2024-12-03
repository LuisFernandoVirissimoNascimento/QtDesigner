class rent:
    def __init__(self, isbn, email) -> None:
        self.cod_livro = isbn # Se chama ISBN oficialmente, mas o banco de dados fica Cod_livro.
        self.email = email    
    
    def create(self):
        return f"insert into emprestimo(cod_livro, email) value {self.cod_livro, self.email};"

rent.__name__ = "rent"