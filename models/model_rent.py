class rent:
    def __init__(self, cod_livro, email) -> None:
        self.cod_livro = cod_livro
        self.email = email    
    
    def create(self):
        return f"insert into emprestimo(cod_livro, email) value {self.cod_livro, self.email};"

rent.__name__ = "rent"