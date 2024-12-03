import mysql.connector
#        bd = Database("10.28.2.69","suporte","suporte","blibioteca")
class database:
    def __init__(self):
        self.host = "10.28.2.69"
        self.user = "suporte"
        self.password = "suporte"
        self.database = "biblioteca"

    def connect(self):
        self.conexao = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
        self.cursor = self.conexao.cursor()

    def desconnect(self):
        self.conexao.close()

    def execute_command(self, command):
        self.connect()
        self.cursor.execute(command)
        self.conexao.commit()
        self.desconnect()

    def read_command(self, command):
        self.connect()
        self.cursor.execute(command)
        result = self.cursor.fetchall()
        self.desconnect()
        return result
    