from os import O_TRUNC

from tomlkit import item
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView, QMessageBox
from controller.system.DBListController import DBListController
import utils.Glo as Glo
import utils.enum.Enum as ENUM
import sys


class DbOtherTableWidget:
  selfForm = None

  def __init__(self, Form, mainDBFrame) -> None:
    self.selfForm = Form
    self.mainDBFrame = mainDBFrame
    Form.setObjectName("Form")
    Form.resize(570, 430)
    self.tableWidget = QtWidgets.QTableWidget(Form)
    self.tableWidget.setGeometry(QtCore.QRect(160, 90, 256, 192))
    self.tableWidget.setObjectName("tableOtherWidget")
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
    # 关闭窗口
    self.pushButton_2.clicked.connect(self.exitDbFrame)

  def retranslateUi(self, Form):
    _translate = QtCore.QCoreApplication.translate
    Form.setWindowTitle(_translate("Form", "登陆向导(数据库)"))
    item = self.tableWidget.horizontalHeaderItem(0)
    item.setText(_translate("Form", "ID"))
    item = self.tableWidget.horizontalHeaderItem(1)
    item.setText(_translate("Form", "账套名称"))
    item = self.tableWidget.horizontalHeaderItem(2)
    item.setText(_translate("Form", "数据库名"))

    self.label.setText(_translate("Form", "请选择其他数据库"))
    self.pushButton.setText(_translate("Form", "确定"))
    self.pushButton_2.setText(_translate("Form", "返回"))
    self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
    # self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
    # 设置第三列隐藏列
    self.tableWidget.setColumnHidden(0, True)
    # 固定行高
    self.tableWidget.horizontalHeader().setSectionResizeMode(
        0, QHeaderView.ResizeToContents)
    # self.tableWidget.horizontalHeader().setSectionResizeMode(0,
    #                                                          QHeaderView.Interactive)
    # self.tableWidget.setColumnWidth(0, 100)
    # self.tableWidget.horizontalHeader().setSectionResizeMode(1,
    #                                                          QHeaderView.Interactive)
    # self.tableWidget.setColumnWidth(1, 120)

  def filterOtherDB(self, list):
    for n in range(len(list)):
      if list[n].db_name == Glo.get_value(ENUM.DBKey.MASTER.value).db_name:
        return n
        # pass
    return None

  def loadDBListData(self):
    _translate = QtCore.QCoreApplication.translate
    dbController = DBListController()
    # print(Glo.get_value(Enum.getCode(Enum.DBKey, 'MASTER')).db_name)
    # 去掉主数据库
    self.dataResult = dbController.findDBList()
    exceptNum = self.filterOtherDB(self.dataResult)
    print(exceptNum)
    if exceptNum is None:
      return
    self.dataResult.pop(exceptNum)
    # print(self.dataResult.pop(exceptNum))
    # print(self.dataResult)
    self.tableWidget.setRowCount(len(self.dataResult))
    for i in range(len(self.dataResult)):
      item = QtWidgets.QTableWidgetItem()
      self.tableWidget.setItem(i, 0, item)
      item = self.tableWidget.item(i, 0)
      item.setText(_translate("MainWindow", str(self.dataResult[i].id)))
      # 不可编辑
      item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
      item = QtWidgets.QTableWidgetItem()
      self.tableWidget.setItem(i, 1, item)
      item = self.tableWidget.item(i, 1)
      item.setText(_translate("MainWindow", self.dataResult[i].db_remark))
      # 不可编辑
      item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
      # ID
      item = QtWidgets.QTableWidgetItem()
      self.tableWidget.setItem(i, 2, item)
      item = self.tableWidget.item(i, 2)
      item.setText(_translate("MainWindow", self.dataResult[i].db_name))
      # 不可编辑
      item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
    # 选择行
    self.tableWidget.selectRow(0)

  def onMainDbSelectConfirm(self):
    # 确定选择
    # print(self.dataResult[self.tableWidget.currentRow()].db_name)
    # Glo.set_value(ENUM.getCode(ENUM.DBKey, 'MASTER'),
    #               self.dataResult[self.tableWidget.currentRow()])
    selectedRows = self.getSelectRowsItem(self.getSelectedRows(
        self.tableWidget.selectedItems()), self.dataResult)
    Glo.set_value(ENUM.DBKey.OTHER.value, selectedRows)
    QMessageBox.information(None, ' 提示 ', '  选择成功！  ')
    self.selfForm.close()
    # print(Glo.get_value(ENUM.getCode(ENUM.DBKey, 'MASTER')))
    # Glo.set_value(ENUM.DBKey['MASTER']['code'],
    #               self.dataResult[self.tableWidget.currentRow()])
    # Glo.get_value(Enum.DBKey['M'])

  def exitDbFrame(self):
    self.selfForm.close()
    self.mainDBFrame.show()
    pass

  def getSelectedRows(self, selectedItem):
    rows = []
    for selectedRow in selectedItem:
      r_index = selectedRow.row()
      if r_index not in rows:
        rows.append(r_index)
    return rows

  def getSelectRowsItem(self, rows, dataResult):
    items = []
    for index in rows:
      items.append(dataResult[index])
    return items
