import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
login_file = "login_screen.ui"
main_file = "main_screen.ui"
rent_file = "register_rent.ui"
user_file = "register_user.ui"
book_file = "register_book.ui"



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.load_ui.loadUi(login_file,self)
        self.setWindowIcon(QIcon("bg.ico"))
        self.load_login()

    # This bit is the function to load and apply actions to a page. This will load the main page with uic.load and then take each button ( That you have to get manually btw ) to connect their clicked action to a function. The function can exist after this.
    def load_main(self):
        uic.load_ui.loadUi(main_file,self)
        self.b_wolf.clicked.connect(self.load_book)
        self.b_load_rent.clicked.connect(self.load_rent)
        self.b_load_register_user.clicked.connect(self.load_user)
        self.b_load_register_book.clicked.connect(self.load_book)

    def load_login(self):
        uic.load_ui.loadUi(login_file,self)
        self.b_login.clicked.connect(self.load_main)
    def load_user(self):
        uic.load_ui.loadUi(user_file,self)
        self.b_wolf.clicked.connect(self.load_main)
        self.b_load_main.clicked.connect(self.load_main)
    def load_rent(self):
        uic.load_ui.loadUi(rent_file,self)
        self.b_wolf.clicked.connect(self.load_user)
        self.b_load_main.clicked.connect(self.load_main)
    def load_book(self):
        uic.load_ui.loadUi(book_file,self)
        self.b_wolf.clicked.connect(self.load_rent)
        self.b_load_main.clicked.connect(self.load_main)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("bg.ico"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())