import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kullanıcı Girişi")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.username_label = QLabel("Kullanıcı Adı:")
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.password_label = QLabel("Şifre:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Giriş Yap")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.db_connection = sqlite3.connect("users.db")
        self.create_table()

    def create_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """)
        self.db_connection.commit()

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        if user:
            QMessageBox.information(self, "Giriş Başarılı", "Hoş geldiniz, {}".format(username))
        else:
            QMessageBox.warning(self, "Giriş Başarısız", "Kullanıcı adı veya şifre hatalı")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
