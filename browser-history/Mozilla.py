from PyQt4 import QtGui
from PyQt4.QtCore import QTimer
import Mysql
import MozillaDatabaseController
class MozillaTaramayaBasla(QtGui.QWidget):
	def __init__(self, parent=None):
		super(MozillaTaramayaBasla, self).__init__(parent)

	def tara(self, mozillaMaxHistoryId):
		self.newMaxId=int(MozillaDatabaseController.mozillaMaxIdGetir())
		if(mozillaMaxHistoryId<self.newMaxId):
			while(mozillaMaxHistoryId<self.newMaxId):
				kayıt=MozillaDatabaseController.mozillaGetirById(mozillaMaxHistoryId + 1)
				Mysql.kayıtEkle(kayıt[0],1,kayıt[1])
				mozillaMaxHistoryId= mozillaMaxHistoryId + 1
		return mozillaMaxHistoryId




