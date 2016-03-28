from PyQt4 import QtGui
from PyQt4.QtCore import QTimer
import Mysql
import MozillaDatabaseController
import GoogleDatabaseController
from Google import GoogleTaramayaBasla
from Mozilla import MozillaTaramayaBasla


class TarayiciTaramaBaslat(QtGui.QWidget):
	def __init__(self, parent=None):
		super(TarayiciTaramaBaslat, self).__init__(parent)
		timer = QTimer(self)
		timer.timeout.connect(self.time)
		timer.setInterval(1000)
		timer.start()
		print("timer başladı")
		self.mozillaMaxHistoryId=int(MozillaDatabaseController.mozillaMaxIdGetir())
		self.googleMaxHistoryId=GoogleDatabaseController.googleMaxIdGetir()


	def time(self):

		mozilla=MozillaTaramayaBasla(parent=self)
		self.mozillaMaxHistoryId=mozilla.tara(mozillaMaxHistoryId=self.mozillaMaxHistoryId)

		google=GoogleTaramayaBasla(parent=self)
		self.googleMaxHistoryId=google.tara(googleMaxHistoryId=self.googleMaxHistoryId)

