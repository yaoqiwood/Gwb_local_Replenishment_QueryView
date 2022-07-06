from PyQt5 import QtCore, QtGui, QtWidgets
from .tableWidget.ReplenishTable import Table


class Ui_MainWindow():
  def setupUi(self, MainWindow):
    # 界面初始化
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(1280, 720)
    _translate = QtCore.QCoreApplication.translate

    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    Table(_translate, self.centralwidget)

    MainWindow.setCentralWidget(self.centralwidget)
    self.statusbar = QtWidgets.QStatusBar(MainWindow)
    self.statusbar.setObjectName("statusbar")
    MainWindow.setStatusBar(self.statusbar)

    self.retranslateUi(MainWindow, _translate)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow, _translate):
    MainWindow.setWindowTitle(_translate("MainWindow", "三驰工具宝本地数据查询PY端"))
