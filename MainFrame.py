from ast import For
import sys
from gui.dbLoginWidget.DBLoginWidget import DBLoginWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import utils.SystemConfig as SystemConfig
import utils.Glo as Glo

# SHOW GUI
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = DBLoginWidget(SystemConfig.mainDBConfig)
ui.setupUi(Form)
Form.show()
# 初始化
Glo._init()
# DBForm.show()
# Frame.show()

sys.exit(app.exec_())
