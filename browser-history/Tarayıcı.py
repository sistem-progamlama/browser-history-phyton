from PyQt4 import QtGui
from PyQt4.QtCore import QTimer
import Mysql
import MozillaDatabaseController
import GoogleDatabaseController
from Google import GoogleTaramayaBasla
from Mozilla import MozillaTaramayaBasla
from User import User


class TarayiciTaramaBaslat(QtGui.QWidget):
	def __init__(self,parent=None):
		super(TarayiciTaramaBaslat, self).__init__(parent)
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.time)
		self.timer.setInterval(1000)
		self.timer.start()
		print("timer başladı")

		google=GoogleTaramayaBasla(parent=self)
		mozilla=MozillaTaramayaBasla(parent=self)

		self.mozillaMaxHistoryId=int(MozillaDatabaseController.mozillaMaxIdGetir())
		self.googleMaxHistoryId=GoogleDatabaseController.googleMaxIdGetir()

	def time(self):
		if(User.uid == ""):
			print("timer durdu")
			self.timer.deleteLater()
			self.timer.destroyed()
		mozilla=MozillaTaramayaBasla(parent=self)
		self.mozillaMaxHistoryId=mozilla.tara(mozillaMaxHistoryId=self.mozillaMaxHistoryId)

		google=GoogleTaramayaBasla(parent=self)
		self.googleMaxHistoryId=google.tara(googleMaxHistoryId=self.googleMaxHistoryId)

