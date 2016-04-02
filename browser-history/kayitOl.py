# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayitOlArayüz.ui'
#
# Created: Mon Mar 21 21:12:18 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from uno import _uno_extract_printable_stacktrace

import Mysql
from Dialog import MyDialog
from User import User

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


class Ui_MainWindow(QtGui.QWidget):
	def __init__(self, parent=None):
		super(Ui_MainWindow, self).__init__(parent)
		self.setObjectName(_fromUtf8("self"))
		self.setWindowModality(QtCore.Qt.NonModal)
		self.resize(550, 500)
		self.setMinimumSize(QtCore.QSize(550, 500))
		self.setMaximumSize(QtCore.QSize(550, 500))
		self.setBaseSize(QtCore.QSize(550, 500))
		self.setStyleSheet(_fromUtf8("background-color : lightgrey"))
		self.centralwidget = QtGui.QWidget(self)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.label = QtGui.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(160, 40, 169, 64))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Exo"))
		font.setPointSize(36)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setObjectName(_fromUtf8("label"))
		self.layoutWidget = QtGui.QWidget(self.centralwidget)
		self.layoutWidget.setGeometry(QtCore.QRect(60, 140, 297, 26))
		self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.label_2 = QtGui.QLabel(self.layoutWidget)
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Exo"))
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.label_2.setFont(font)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.horizontalLayout.addWidget(self.label_2)
		self.txt_kayitAdi = QtGui.QLineEdit(self.layoutWidget)
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Verdana"))
		font.setPointSize(11)
		self.txt_kayitAdi.setFont(font)
		self.txt_kayitAdi.setText(_fromUtf8(""))
		self.txt_kayitAdi.setObjectName(_fromUtf8("txt_kayitAdi"))
		self.horizontalLayout.addWidget(self.txt_kayitAdi)
		self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
		self.layoutWidget1.setGeometry(QtCore.QRect(60, 200, 295, 26))
		self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
		self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
		self.horizontalLayout_2.setMargin(0)
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.label_3 = QtGui.QLabel(self.layoutWidget1)
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Exo"))
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.label_3.setFont(font)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.horizontalLayout_2.addWidget(self.label_3)
		self.txt_kayitEmail = QtGui.QLineEdit(self.layoutWidget1)
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Verdana"))
		font.setPointSize(11)
		self.txt_kayitEmail.setFont(font)
		self.txt_kayitEmail.setObjectName(_fromUtf8("txt_kayitEmail"))
		self.horizontalLayout_2.addWidget(self.txt_kayitEmail)
		self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
		self.layoutWidget2.setGeometry(QtCore.QRect(60, 260, 296, 26))
		self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
		self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
		self.horizontalLayout_3.setMargin(0)
		self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
		self.label_4 = QtGui.QLabel(self.layoutWidget2)
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Exo"))
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.label_4.setFont(font)
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.horizontalLayout_3.addWidget(self.label_4)
		self.txt_kayitSifre = QtGui.QLineEdit(self.layoutWidget2)
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Verdana"))
		font.setPointSize(11)
		self.txt_kayitSifre.setFont(font)
		self.txt_kayitSifre.setEchoMode(QtGui.QLineEdit.Password)
		self.txt_kayitSifre.setObjectName(_fromUtf8("txt_kayitSifre"))
		self.horizontalLayout_3.addWidget(self.txt_kayitSifre)
		self.layoutWidget3 = QtGui.QWidget(self.centralwidget)
		self.layoutWidget3.setGeometry(QtCore.QRect(60, 320, 295, 26))
		self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
		self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget3)
		self.horizontalLayout_4.setMargin(0)
		self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
		self.label_5 = QtGui.QLabel(self.layoutWidget3)
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Exo"))
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.label_5.setFont(font)
		self.label_5.setObjectName(_fromUtf8("label_5"))
		self.horizontalLayout_4.addWidget(self.label_5)
		self.txt_kayitSifreTekrar = QtGui.QLineEdit(self.layoutWidget3)
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Verdana"))
		font.setPointSize(11)
		self.txt_kayitSifreTekrar.setFont(font)
		self.txt_kayitSifreTekrar.setEchoMode(QtGui.QLineEdit.Password)
		self.txt_kayitSifreTekrar.setObjectName(_fromUtf8("txt_kayitSifreTekrar"))
		self.horizontalLayout_4.addWidget(self.txt_kayitSifreTekrar)
		self.layoutWidget4 = QtGui.QWidget(self.centralwidget)
		self.layoutWidget4.setGeometry(QtCore.QRect(40, 380, 356, 38))
		self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
		self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget4)
		self.horizontalLayout_6.setMargin(0)
		self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
		self.btn_kayitIptal = QtGui.QPushButton(self.layoutWidget4)
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Exo"))
		font.setPointSize(16)
		font.setBold(True)
		font.setWeight(75)
		self.btn_kayitIptal.setFont(font)
		self.btn_kayitIptal.setObjectName(_fromUtf8("btn_kayitIptal"))
		self.horizontalLayout_6.addWidget(self.btn_kayitIptal)
		self.btn_kayitTamam = QtGui.QPushButton(self.layoutWidget4)
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Exo"))
		font.setPointSize(16)
		font.setBold(True)
		font.setWeight(75)
		self.btn_kayitTamam.setFont(font)
		self.btn_kayitTamam.setAutoDefault(False)
		self.btn_kayitTamam.setDefault(False)
		self.btn_kayitTamam.setFlat(False)
		self.btn_kayitTamam.setObjectName(_fromUtf8("btn_kayitTamam"))
		self.horizontalLayout_6.addWidget(self.btn_kayitTamam)
		self.lbl_kayitSifreHata = QtGui.QLabel(self.centralwidget)
		self.lbl_kayitSifreHata.setGeometry(QtCore.QRect(360, 320, 201, 21))
		self.lbl_kayitSifreHata.setVisible(False)
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Verdana"))
		font.setPointSize(10)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		font.setStyleStrategy(QtGui.QFont.PreferDefault)
		self.lbl_kayitSifreHata.setFont(font)
		self.lbl_kayitSifreHata.setWordWrap(False)
		self.lbl_kayitSifreHata.setMargin(2)
		self.lbl_kayitSifreHata.setObjectName(_fromUtf8("lbl_kayitSifreHata"))
		self.label_6 = QtGui.QLabel(self.centralwidget)
		self.label_6.setGeometry(QtCore.QRect(70, 20, 81, 101))
		self.label_6.setText(_fromUtf8(""))
		self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("uye-ol.png")))
		self.label_6.setObjectName(_fromUtf8("label_6"))
		#        self.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(self)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		#        self.setMenuBar(self.menubar)
		QtCore.QObject.connect(self.btn_kayitTamam, QtCore.SIGNAL(_fromUtf8("clicked()")), self.closeEven)
		self.dialogTextBrowser = MyDialog()
		self.retranslateUi(self)
		QtCore.QMetaObject.connectSlotsByName(self)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		self.label.setText(_translate("MainWindow", "Kayıt Ol", None))
		self.label_2.setText(_translate("MainWindow", "Kullanıcı Adı     :", None))
		self.label_3.setText(_translate("MainWindow", "E-mail              :", None))
		self.label_4.setText(_translate("MainWindow", "Sifre                 :", None))
		self.label_5.setText(_translate("MainWindow", "Sifre (Tekrar)  :", None))
		self.btn_kayitIptal.setText(_translate("MainWindow", "Iptal", None))
		self.btn_kayitTamam.setText(_translate("MainWindow", "Tamamla", None))
		self.lbl_kayitSifreHata.setText(_translate("MainWindow",
		                                           "<html><head/><body><p><span style=\" color:#ff0000;\">Şifreleriniz uyuşmamaktadır!</span></p></body></html>",
		                                           None))

	def closeEven(self):
		adi = self.txt_kayitAdi.text()
		email = self.txt_kayitEmail.text()
		sifre = self.txt_kayitSifre.text()
		sifreTekrar = self.txt_kayitSifreTekrar.text()
		u = User(adi, sifre, email,"")
		if sifreTekrar == sifre:
			try:
				Mysql.üyeOl(u)
				self.dialogTextBrowser.show()
				self.close()
			except Exception:
				print(_uno_extract_printable_stacktrace())

		else:
			self.lbl_kayitSifreHata.setVisible(True)


if __name__ == "__main__":
	import sys

	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
