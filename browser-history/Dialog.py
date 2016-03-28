from PyQt4 import QtCore, QtGui


class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)

        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.clicked.connect(self.on_pushButton_clicked)

        self.textBrowser = QtGui.QLabel(self)
        self.textBrowser.setText("KAYIT BAŞARILI")

        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout.addWidget(self.buttonBox)

    def on_pushButton_clicked(self):
        self.close()
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = MyDialog()
    MainWindow.show()
    sys.exit(app.exec_())