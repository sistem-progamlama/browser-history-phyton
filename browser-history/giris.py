# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giriş.ui'
#
# Created: Sun Mar 20 02:31:08 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
from mailcap import show

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication

import User
import Mysql
from Tarayıcı import TarayiciTaramaBaslat

from kayitOl import Ui_MainWindow

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(QtGui. QMainWindow):
    def __init__(self, parent=None):
        super(Ui_Dialog, self).__init__(parent)
        self.setObjectName(_fromUtf8("Dialog"))
        parent.resize(320, 240)
        self.setMinimumSize(QtCore.QSize(550, 500))
        self.setMaximumSize(QtCore.QSize(550, 500))
        self.pushButton = QtGui.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(160, 100, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(140, 20, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(40, 20, 91, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_2 = QtGui.QLineEdit(MainWindow)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 50, 113, 27))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_2 = QtGui.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(90, 60, 41, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 100, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.retranslateUi(MainWindow)

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.uyeOl)
        self.yeniform = None

    def uyeOl(self):
        self.yeniform=Ui_MainWindow()
        self.yeniform.show()


    def click(self):
        ad = self.lineEdit.text()
        sifre = self.lineEdit_2.text()
        u=User.User(ad,sifre,"")
        print("user oluşturuldu")

        if Mysql.getir(u):
            """from anasayfa import AnaSayfa
            self.anasayfa=AnaSayfa()
            self.anasayfa.show()"""
            basla=TarayiciTaramaBaslat(self)

        else:
            print ("basarisiz")

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "GİRİŞ YAP", None))
        self.label.setText(_translate("Dialog", "Kullanıcı Adi:", None))
        self.label_2.setText(_translate("Dialog", "Şifre:", None))
        self.pushButton_2.setText(_translate("Dialog", "ÜYE OL", None))
import sys
app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = Ui_Dialog(MainWindow)
MainWindow.show()
app.exec_()

