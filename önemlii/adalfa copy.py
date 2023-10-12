import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from ilk import Ui_arayz
from graph import Ui_Formmm
from matplotlibwidget import MatplotlibWidget
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_arayz()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.add_user)
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton.clicked.connect(self.graphekrani)
        self.db_connection = sqlite3.connect("deneme.db")
        self.create_table()

    def graphekrani(self):
        self.sayfayiac = graphic()
        self.close()
        self.sayfayiac.show()


    def create_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS deneme (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """)
        self.db_connection.commit()

    def add_user(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if username.isalpha() and password.isdigit():
            cursor = self.db_connection.cursor()
            cursor.execute("INSERT INTO deneme (username, password) VALUES (?, ?)", (username, password))
            self.db_connection.commit()
            QMessageBox.information(self, "Kullanıcı Eklendi", "Kullanıcı bilgileri veritabanına eklendi.")
        else:
            QMessageBox.warning(self, "Geçersiz Bilgi", "Kullanıcı adı harf, şifre sayılardan oluşmalıdır.")

    def login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM deneme WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        if user:
            QMessageBox.information(self, "Giriş Başarılı", "Hoş geldiniz, {}".format(username))
        else:
            QMessageBox.warning(self, "Giriş Başarısız", "Kullanıcı adı veya şifre hatalı")


class graphic(QWidget):
    def __init__(self):
        super().__init__()
        self.ui2 = Ui_Formmm()
        self.ui2.setupUi(self)
        self.matplotlib_widget1 = MatplotlibWidget(self.ui2.widget1)
        self.matplotlib_widget_2 = MatplotlibWidget(self.ui2.widget_2)
        self.ui2.pushButton23.clicked.connect(self.plot_graphs)

    def plot_graphs(self):
        super().__init__()
        self.matplotlib_widget1.plot_sample_graph()
        self.matplotlib_widget_2.plot_sample_graph()


app = QApplication([])
pencere = MainWindow()
pencere.show()
sys.exit(app.exec_())
