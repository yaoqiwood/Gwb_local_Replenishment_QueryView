import sys
import gui.Gui as GUI
from PyQt5 import QtCore, QtGui, QtWidgets

# SHOW GUI
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = GUI.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
