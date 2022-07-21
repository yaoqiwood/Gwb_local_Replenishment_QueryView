from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView
from controller.system.DBListController import DBListController


class DbTableWidget:
  def __init__(self, Form) -> None:
    Form.setObjectName("Form")
    Form.resize(570, 430)
    self.tableWidget = QtWidgets.QTableWidget(Form)
    self.tableWidget.setGeometry(QtCore.QRect(160, 90, 256, 192))
    self.tableWidget.setObjectName("tableWidget")
    self.tableWidget.setColumnCount(3)
    self.tableWidget.setRowCount(0)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setHorizontalHeaderItem(1, item)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setHorizontalHeaderItem(2, item)
    self.label = QtWidgets.QLabel(Form)
    self.label.setGeometry(QtCore.QRect(10, 20, 551, 51))
    font = QtGui.QFont()
    font.setFamily("Comic Sans MS")
    font.setPointSize(20)
    self.label.setFont(font)
    self.label.setAlignment(QtCore.Qt.AlignCenter)
    self.label.setObjectName("label")
    self.pushButton = QtWidgets.QPushButton(Form)
    self.pushButton.setGeometry(QtCore.QRect(120, 320, 111, 41))
    font = QtGui.QFont()
    font.setFamily("AcadEref")
    font.setPointSize(12)
    self.pushButton.setFont(font)
    self.pushButton.setObjectName("pushButton")
    self.pushButton_2 = QtWidgets.QPushButton(Form)
    self.pushButton_2.setGeometry(QtCore.QRect(340, 320, 111, 41))
    font = QtGui.QFont()
    font.setFamily("AcadEref")
    font.setPointSize(12)
    self.pushButton_2.setFont(font)
    self.pushButton_2.setObjectName("pushButton_2")

    self.retranslateUi(Form)
    QtCore.QMetaObject.connectSlotsByName(Form)

    # 按钮函数调用
    self.pushButton.clicked.connect(self.onMainDbSelectConfirm)

  def retranslateUi(self, Form):
    _translate = QtCore.QCoreApplication.translate
    Form.setWindowTitle(_translate("Form", "登陆向导(数据库)"))
    item = self.tableWidget.horizontalHeaderItem(0)
    item.setText(_translate("Form", "ID"))
    item = self.tableWidget.horizontalHeaderItem(1)
    item.setText(_translate("Form", "账套名称"))
    item = self.tableWidget.horizontalHeaderItem(2)
    item.setText(_translate("Form", "数据库名"))

    self.label.setText(_translate("Form", "请选择主数据库"))
    self.pushButton.setText(_translate("Form", "确定"))
    self.pushButton_2.setText(_translate("Form", "返回"))
    self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
    self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
    # 设置第三列隐藏列
    self.tableWidget.setColumnHidden(0, True)
    # self.tableWidget.horizontalHeader().setSectionResizeMode(0,
    #                                                          QHeaderView.Interactive)
    # self.tableWidget.setColumnWidth(0, 100)
    # self.tableWidget.horizontalHeader().setSectionResizeMode(1,
    #                                                          QHeaderView.Interactive)
    # self.tableWidget.setColumnWidth(1, 120)

  def loadDBListData(self):
    _translate = QtCore.QCoreApplication.translate
    dbController = DBListController()
    dataResult = dbController.findDBList()
    self.tableWidget.setRowCount(len(dataResult))
    for i in range(len(dataResult)):
      item = QtWidgets.QTableWidgetItem()
      self.tableWidget.setItem(i, 0, item)
      item = self.tableWidget.item(i, 0)
      item.setText(_translate("MainWindow", str(dataResult[i].id)))
      # 不可编辑
      item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
      item = QtWidgets.QTableWidgetItem()
      self.tableWidget.setItem(i, 1, item)
      item = self.tableWidget.item(i, 1)
      item.setText(_translate("MainWindow", dataResult[i].db_remark))
      # 不可编辑
      item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
      # ID
      item = QtWidgets.QTableWidgetItem()
      self.tableWidget.setItem(i, 2, item)
      item = self.tableWidget.item(i, 2)
      item.setText(_translate("MainWindow", dataResult[i].db_name))
      # 不可编辑
      item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
    # 选择行
    self.tableWidget.selectRow(0)

  def onMainDbSelectConfirm(self):
    # 确定选择
    print(self.tableWidget.currentRow())
