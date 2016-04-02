import webbrowser

from PyQt4 import QtGui
from PyQt4.QtCore import QTimer, Qt
from PyQt4.QtGui import QTableWidgetItem, QAbstractItemView
from PyQt4.QtSql import QSqlQuery


import Mysql
from User import User as u
class AnaSayfa(QtGui.QWidget):
	def __init__(self, parent=None):
		super(AnaSayfa, self).__init__(parent)
		self.setWindowTitle("%s adlı kullanıcının geçmişi" %(u.adi))
		self.resize(1100, 600)
		self.layout = QtGui.QGridLayout()
		self.setLayout(self.layout)
		self.table = QtGui.QTableWidget()
		self.btn_eliminar = QtGui.QPushButton("Seçili satırı sil")
		self.chck=QtGui.QCheckBox("otomotik güncelleme yapılsın mı ")
		self.layout.addWidget(self.btn_eliminar)
		self.layout.addWidget(self.chck)
		self.layout.addWidget(self.table)
		self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.show()
		self.Seleccionar()
		self.btn_eliminar.clicked.connect(self.Eliminar)
		self.table.doubleClicked.connect(self.doubleClick)
		timer = QTimer(self)
		timer.timeout.connect(self.otoRefresh)
		timer.setInterval(5000)
		timer.start()

	def doubleClick(self):
		row = self.table.selectionModel().selectedRows()
		index=[]
		for i in row:
			index.append(i.row())
		url=self.table.item(index[0],0).text()
		tarayıcı=self.table.item(index[0],2).text()

		if tarayıcı == "mozilla-fireofox":
			webbrowser.get("firefox").open_new_tab(url)

		elif tarayıcı == "google-chrome":
			webbrowser.get('google-chrome').open_new_tab(url)


	def otoRefresh(self):
		if(self.chck.isChecked()):
			self.Seleccionar()

	def Seleccionar(self):
			self.table.setRowCount(0)
			self.table.setColumnCount(0)
			self.table.setColumnCount(3)
			self.table.setColumnWidth(0,700)
			self.table.setColumnWidth(1,200)
			self.table.setColumnWidth(2,200)
			self.table.setHorizontalHeaderLabels(["girilen siteler","tarih","browser"])
			row = 0
			query = Mysql.gecmisGetir()
			for q in query:
				self.table.insertRow(row)

				url = QTableWidgetItem(str(q[0]))
				ad=QTableWidgetItem(str(q[2]))
				tarih=QTableWidgetItem(str(q[1]))

				self.table.setItem(row, 0, url)
				self.table.setItem(row, 1, tarih)
				self.table.setItem(row, 2, ad)
				row = row + 1



	def Eliminar(self):
			rows = self.table.selectionModel().selectedRows()
			index = []
			for i in rows:
				index.append(i.row())
			index.sort(reverse=True)
			for i in index:
				url = self.table.item(i, 0).text()
				zaman = self.table.item(i, 1).text()
				self.table.removeRow(i)
				Mysql.historySil(url,zaman)






