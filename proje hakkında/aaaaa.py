from PyQt5.QtWidgets import QApplication, QWidget
from login_ekrani import Ui_Form
from createaccount import Ui_Formm
from variables import Ui_degiskenler

class CreateAccountWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Formm()
        self.ui.setuppUi(self)
        self.ui.kullanicikekle_2.clicked.connect(self.anageri)   #kullanıcı eklendikten sonra giriş ekranına
    def anageri(self):
        self.sayfayiac = AnaPencere()
        self.close()
        self.sayfayiac.show()

class Degiskenler(QWidget):
    def __init__(self):
        super().__init__()
        self.ui2 = Ui_degiskenler()
        self.ui2.setupppUi(self)

class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.girisyap)           
        self.ui.kullanicikekle.clicked.connect(self.newaccount)
    def newaccount(self):
        isim = self.ui.kullaniciadi.text()
        sifre = self.ui.sifrekutusu.text()
        if isim == "" and sifre == "":           #Databasede olmayan bilgide uyarı verilecek
            self.sayfayiac = CreateAccountWindow()
            self.close()
            self.sayfayiac.show()

    def girisyap(self):
        isim = self.ui.kullaniciadi.text()
        sifre = self.ui.sifrekutusu.text()         
        if isim == "admin" and sifre == "123":          #Databasede olan kullanıcıların girebileceği şekilde olacak
            self.sayfayiac = Degiskenler()           #Değişkenlerin olduğu sayfaya yönlendirir
            self.close()
            self.sayfayiac.show()
            

app = QApplication([])
pencere = AnaPencere()
pencere.show()
app.exec_()
