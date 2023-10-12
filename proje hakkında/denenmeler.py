import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kullanıcı Ekle")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.username_label = QLabel("Kullanıcı Adı:")
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.password_label = QLabel("Şifre:")
        self.password_input = QLineEdit()
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.add_button = QPushButton("Ekle")
        self.add_button.clicked.connect(self.add_user)
        layout.addWidget(self.add_button)

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

    def add_user(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username.isalpha() and password.isdigit():
            cursor = self.db_connection.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.db_connection.commit()
            print("Kullanıcı eklendi:", username, password)
        else:
            print("Geçersiz kullanıcı adı veya şifre formatı")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
