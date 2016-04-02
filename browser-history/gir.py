# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gir.ui'
#
# Created: Fri Apr  1 22:23:31 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import Mysql
from Tarayıcı import TarayiciTaramaBaslat
from User import User
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

class Ui_Dialog:
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(350, 205)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 201))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setEnabled(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.checkBox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.click)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.uyeOl)
        self.yeniform = None

    def uyeOl(self):
        self.yeniform=Ui_MainWindow()
        self.yeniform.show()

    def click(self):
        if "GİRİS" in self.pushButton.text():
            if self.girisYap():
                self.gorunmezYap()
                self.pushButton.setText(_translate("Dialog", "ÇIKIŞ", None))
        else:
            self.gorunurYap()
            self.pushButton.setText(_translate("Dialog", "GİRİS", None))
            User.uid=""
            User.adi=""
            User.mail=""
            User.sifre=""

    def girisYap(self):
        ad = self.lineEdit.text()
        sifre = self.lineEdit_2.text()
        u=User(ad,sifre,"","")
        print("user oluşturuldu")

        if Mysql.getir(u):
            if self.checkBox.isChecked():
                from anasayfa import AnaSayfa
                self.anasayfa=AnaSayfa()
                self.anasayfa.show()
            basla=TarayiciTaramaBaslat(Dialog)
            return  True

        else:
            print ("basarisiz")
            return  False
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Tarayıcıyı kullanabilmek için giriş yapınız", None))
        self.label.setText(_translate("Dialog", "          Kullanici adi:", None))
        self.label_2.setText(_translate("Dialog", "                        Sİfre:", None))
        self.pushButton_2.setText(_translate("Dialog", "UYE OL", None))
        self.pushButton.setText(_translate("Dialog", "GİRİS", None))
        self.label_3.setText(_translate("Dialog", " ", None))
        self.checkBox.setText(_translate("Dialog", "Geçmiş Açılsın mı?", None))

    def gorunmezYap(self):
        self.label.setVisible(False)
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.lineEdit.setVisible(False)
        self.lineEdit_2.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.checkBox.setVisible(False)

    def gorunurYap(self):
        self.label.setVisible(True)
        self.label_2.setVisible(True)
        self.label_3.setVisible(True)
        self.lineEdit.setVisible(True)
        self.lineEdit_2.setVisible(True)
        self.pushButton_2.setVisible(True)
        self.checkBox.setVisible(True)


import sys
app = QtGui.QApplication(sys.argv)
Dialog = QtGui.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


