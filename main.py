import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
main_file = "main_screen.ui"
rent_file = "register_rent.ui"
user_file = "register_user.ui"
book_file = "register_book.ui"



class MainWindow(QMainWindow):
    def __init__(self, batata):
        super().__init__()
        self.batata = batata
        uic.load_ui.loadUi(main_file,self)
        self.setWindowIcon(QIcon("bg.ico"))
        self.b_wolf.clicked.connect(self.load_book)

    def load_user(self):
        uic.load_ui.loadUi(user_file,self)
        self.batata += 1;
        print(self.batata)
        self.b_wolf.clicked.connect(self.load_main)
    def load_rent(self):
        uic.load_ui.loadUi(rent_file,self)
        self.batata += 1;
        print(self.batata)
        self.b_wolf.clicked.connect(self.load_user)
    def load_book(self):
        uic.load_ui.loadUi(book_file,self)
        self.batata += 1;
        print(self.batata)
        self.b_wolf.clicked.connect(self.load_rent)
    def load_main(self):
        uic.load_ui.loadUi(main_file,self)
        self.batata += 1;
        print(self.batata)
        self.b_wolf.clicked.connect(self.load_book)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("bg.ico"))
    window = MainWindow(0)
    window.show()
    sys.exit(app.exec())