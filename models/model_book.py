class book:
    def __init__(self, titulo, autor, genero, isbn) -> None:
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.isbn = isbn # Primary key
    
    def create(self):
        return f"insert into livro(titulo, autor, genero, isbn) value {self.titulo, self.autor, self.genero, self.isbn};"

book.__name__ = "book"