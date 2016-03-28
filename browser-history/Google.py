import os
from sqlite3 import OperationalError

import shutil
from PyQt4 import QtGui

import Mysql
import GoogleDatabaseController
class GoogleTaramayaBasla(QtGui.QWidget):
	def __init__(self, parent=None):
		super(GoogleTaramayaBasla, self).__init__(parent)
		os.remove('/home/celal/.config/google-chrome/Default/History-yedek')
		shutil.copyfile('/home/celal/.config/google-chrome/Default/History', '/home/celal/.config/google-chrome/Default/History-yedek')
	def tara(self, googleMaxHistoryId=None):
			googleMaxHistoryId=int(googleMaxHistoryId)
			self.newMaxId=int(GoogleDatabaseController.googleMaxIdGetir())
			print(self.newMaxId)
			if(googleMaxHistoryId<self.newMaxId):
				while(googleMaxHistoryId<self.newMaxId):
					kayıt=GoogleDatabaseController.googleGetirById(googleMaxHistoryId + 1)
					Mysql.kayıtEkle(kayıt[0],2,kayıt[1])
					googleMaxHistoryId= googleMaxHistoryId + 1
			return googleMaxHistoryId



