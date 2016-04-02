import subprocess
from PyQt4 import QtGui
from User import User as u
from PyQt4.QtCore import QTimer


class Starter(QtGui.QWidget):
	def __init__(self, parent=None):
		super(Starter, self).__init__(parent)
		timer = QTimer(self)
		timer.timeout.connect(self.time)
		timer.setInterval(1000)
		timer.start()

	def time(self):
		output=subprocess.getoutput("ps aux")
		if u.uid == "":
			if "google" in output:
				subprocess.getoutput("killall -9 chrome")
				from gir import Ui_Dialog
			elif "firefox" in output:
				subprocess.getoutput("killall -9 firefox")
				from gir import Ui_Dialog

import sys
app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = Starter(MainWindow)
app.exec_()