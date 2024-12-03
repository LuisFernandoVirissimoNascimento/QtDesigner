import sys
from services.biblioteca import biblioteca
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
login_file = "views/login_screen.ui"
main_file = "views/main_screen.ui"
rent_file = "views/register_rent.ui"
user_file = "views/register_user.ui"
update_user_file = "views/update_user.ui"
read_user_file = "views/read_user.ui"
book_file = "views/register_book.ui"



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.load_ui.loadUi(login_file,self)
        self.setWindowIcon(QIcon("bg.ico"))
        self.load_login()

    # This bit is the function to load and apply actions to a page. This will load the main page with uic.load and then take each button ( That you have to get manually btw ) to connect their clicked action to a function. The function can exist after this.
    def load_main(self):
        uic.load_ui.loadUi(main_file,self)
        self.b_quit.clicked.connect(self.load_login)
        self.b_wolf.clicked.connect(self.load_book)
        self.b_load_update_user.clicked.connect(self.load_update_user)
        self.b_load_rent.clicked.connect(self.load_rent)
        self.b_load_register_user.clicked.connect(self.load_user)
        self.b_load_register_book.clicked.connect(self.load_book)
        self.b_load_read_user.clicked.connect(self.load_read_user)

    def load_login(self):
        uic.load_ui.loadUi(login_file,self)
        self.b_login.clicked.connect(self.load_main)
    def load_user(self):
        uic.load_ui.loadUi(user_file,self)
        self.b_wolf.clicked.connect(self.load_main)
        self.b_load_main.clicked.connect(self.load_main)

        #self.b_register.clicked.connect(lambda : biblioteca.read_user(self, self.i_user_name.text())) # This takes the input for user name and gives it's text, neat!

        self.b_register.clicked.connect(lambda : biblioteca.create_user(self.i_user_name.text(), self.i_user_cpf.text(), self.i_user_telefone.text(),self.i_user_email.text(),self.i_user_password.text(),self.i_user_confirm_password.text())) # This takes the input for user name and gives it's text, neat!

    def load_read_user(self):
        uic.load_ui.loadUi(read_user_file,self)
        self.b_wolf.clicked.connect(self.load_main)
        self.b_load_main.clicked.connect(self.load_main)

        self.b_register.clicked.connect(lambda : biblioteca.read_user(self)) # This takes the input for user name and gives it's text, neat!

    def load_update_user(self):
        uic.load_ui.loadUi(update_user_file,self)
        self.b_wolf.clicked.connect(self.load_main)
        self.b_load_main.clicked.connect(self.load_main)        

        self.b_update.clicked.connect(lambda : biblioteca.update_user(self.i_user_id.text(),self.i_user_name.text(), self.i_user_cpf.text(), self.i_user_telefone.text(),self.i_user_email.text(),self.i_user_password.text()))

        self.b_delete.clicked.connect(lambda : biblioteca.delete_user(self.i_user_id.text()))

    def load_rent(self):
        uic.load_ui.loadUi(rent_file,self)
        self.b_wolf.clicked.connect(self.load_user)
        self.b_load_main.clicked.connect(self.load_main)
    def load_book(self):
        uic.load_ui.loadUi(book_file,self)
        self.b_wolf.clicked.connect(self.load_rent)
        self.b_load_main.clicked.connect(self.load_main)

        self.b_register.clicked.connect(lambda : biblioteca.create_book(self.i_titulo.text(),self.i_autor.text(),self.i_genero.text(),self.i_isbn.text()))
        self.b_update.clicked.connect(lambda : biblioteca.update_book(self.i_titulo.text(),self.i_autor.text(),self.i_genero.text(),self.i_isbn.text()))
        self.b_delete.clicked.connect(lambda : biblioteca.delete_book(self.i_isbn.text()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("bg.ico"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())