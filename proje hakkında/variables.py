# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'değikenler.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_degiskenler(object):
    def setupppUi(self, degiskenler):
        degiskenler.setObjectName("degiskenler")
        degiskenler.resize(1103, 862)
        degiskenler.setAcceptDrops(True)
        degiskenler.setStyleSheet("background:rgb(50, 156, 146);")
        self.baslik = QtWidgets.QLabel(degiskenler)
        self.baslik.setGeometry(QtCore.QRect(200, 80, 651, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.baslik.setFont(font)
        self.baslik.setStyleSheet("")
        self.baslik.setObjectName("baslik")
        self.basinc = QtWidgets.QPushButton(degiskenler)
        self.basinc.setGeometry(QtCore.QRect(400, 240, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.basinc.setFont(font)
        self.basinc.setStyleSheet("background:rgb(150, 27, 70);\n"
"border:none;\n"
"border-radius:30px;\n"
"color:white;")
        self.basinc.setObjectName("basinc")
        self.gaz = QtWidgets.QPushButton(degiskenler)
        self.gaz.setGeometry(QtCore.QRect(400, 330, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gaz.setFont(font)
        self.gaz.setStyleSheet("background:rgb(150, 27, 70);\n"
"border:none;\n"
"border-radius:30px;\n"
"color:white;")
        self.gaz.setObjectName("gaz")
        self.sicaklik = QtWidgets.QPushButton(degiskenler)
        self.sicaklik.setGeometry(QtCore.QRect(400, 410, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sicaklik.setFont(font)
        self.sicaklik.setStyleSheet("background:rgb(150, 27, 70);\n"
"border:none;\n"
"border-radius:30px;\n"
"color:white;")
        self.sicaklik.setObjectName("sicaklik")
        self.nem = QtWidgets.QPushButton(degiskenler)
        self.nem.setGeometry(QtCore.QRect(400, 500, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.nem.setFont(font)
        self.nem.setStyleSheet("background:rgb(150, 27, 70);\n"
"border:none;\n"
"border-radius:30px;\n"
"color:white;")
        self.nem.setObjectName("nem")
        self.iscianaliz = QtWidgets.QPushButton(degiskenler)
        self.iscianaliz.setGeometry(QtCore.QRect(400, 580, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.iscianaliz.setFont(font)
        self.iscianaliz.setStyleSheet("background:rgb(150, 27, 70);\n"
"border:none;\n"
"border-radius:30px;\n"
"color:white;")
        self.iscianaliz.setObjectName("iscianaliz")

        self.retranslateUi(degiskenler)
        QtCore.QMetaObject.connectSlotsByName(degiskenler)

    def retranslateUi(self, degiskenler):
        _translate = QtCore.QCoreApplication.translate
        degiskenler.setWindowTitle(_translate("degiskenler", "Form"))
        self.baslik.setText(_translate("degiskenler", "Görmek istediğiniz işlem hangisi?"))
        self.basinc.setText(_translate("degiskenler", "BASINÇ"))
        self.gaz.setText(_translate("degiskenler", "GAZ"))
        self.sicaklik.setText(_translate("degiskenler", "SICAKLIK"))
        self.nem.setText(_translate("degiskenler", "NEM"))
        self.iscianaliz.setText(_translate("degiskenler", "İŞÇİLERİ GÖRÜNTÜLE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    degiskenler = QtWidgets.QWidget()
    ui = Ui_degiskenler()
    ui.setupppUi(degiskenler)
    degiskenler.show()
    sys.exit(app.exec_())
