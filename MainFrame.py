import sys
from gui.dbLoginWidget.DBLoginWidget import DBLoginWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import utils.SystemConfig as SystemConfig

# SHOW GUI
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = DBLoginWidget(SystemConfig.mainDBConfig)
ui.setupUi(Form)
Form.show()
sys.exit(app.exec_())
