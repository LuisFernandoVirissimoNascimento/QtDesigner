class user:
    def __init__(self, nome) -> None:
        self.nome = nome

    def create(self):
        return f"insert into usuario(nome) value {self.nome};"
    

user.__name__ = "user"