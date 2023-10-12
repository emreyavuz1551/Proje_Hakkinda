
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import *
import sys
from login_ekrani import Ui_Form
from createaccount import Ui_Formm

class main(QWidget):
    def __init__(self) :
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.sayfayiac = Ui_Formm()
        self.ui.kullanicikekle.clicked.connect(self.girisyap)

    def girisyap(self):
        isim = self.ui.kullaniciadi.text()
        sifre = self.ui.sifrekutusu.text()
        if isim == "admin" and sifre == "123":
            self.sayfayiac.show()
            
            
            
            




app =QApplication([])
pencere = main()
pencere.show()
app.exec_()