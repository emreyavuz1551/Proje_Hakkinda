# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ilk.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_arayz(object):
    def setupUi(self, arayz):
        arayz.setObjectName("arayz")
        arayz.resize(905, 654)
        arayz.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.lineEdit = QtWidgets.QLineEdit(arayz)
        self.lineEdit.setGeometry(QtCore.QRect(270, 110, 321, 91))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(arayz)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 240, 321, 91))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(arayz)
        self.pushButton.setGeometry(QtCore.QRect(290, 380, 291, 61))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(arayz)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 470, 291, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(arayz)
        QtCore.QMetaObject.connectSlotsByName(arayz)

    def retranslateUi(self, arayz):
        _translate = QtCore.QCoreApplication.translate
        arayz.setWindowTitle(_translate("arayz", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    arayz = QtWidgets.QWidget()
    ui = Ui_arayz()
    ui.setupUi(arayz)
    arayz.show()
    sys.exit(app.exec_())
