from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView, QAbstractItemView


class Table:
  tableConfig = {
      'rowWidth': 20
  }
  tableWidget = None
  centralwidget = None
  _translate = None

  def __init__(self, _translate, centralwidget):
    self.centralwidget = centralwidget
    self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
    # self.tableWidget.setEditTriggers(
    #     QtWidgets.QAbstractItemView.NoEditTriggers)
    self._translate = _translate
    self.tableWidget.setGeometry(QtCore.QRect(270, 20, 991, 661))
    self.tableWidget.setObjectName("tableWidget")
    self.tableWidget.setColumnCount(7)
    self.tableWidget.setRowCount(2)
    # 这里的代码指定为列的行号是否显示
    # item = QtWidgets.QTableWidgetItem()
    # self.tableWidget.setVerticalHeaderItem(0, item)
    # item = QtWidgets.QTableWidgetItem()
    # self.tableWidget.setVerticalHeaderItem(1, item)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setHorizontalHeaderItem(1, item)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setHorizontalHeaderItem(2, item)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setHorizontalHeaderItem(3, item)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setHorizontalHeaderItem(4, item)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setHorizontalHeaderItem(5, item)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setHorizontalHeaderItem(6, item)

    # header  TODO 这部分业务代码后续抽离
    headerJSON = ['基本条码（货柜号）', '商品全名', '草稿数量',
                  '销售数量', '库存数量', '成本单价', '是否建议补货']
    self.setTableHeader(headerJSON)
    self.setData()

  def setTableHeader(self, header):
    for i in range(len(header)):
      item = self.tableWidget.horizontalHeaderItem(i)
      # item.setFlags(QtCore.Qt.ItemIsEditable)
      item.setText(self._translate("MainWindow", header[i]))
      # item.setEditTriggers(QAbstractItemView.NoEditTriggers)
    self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                             QHeaderView.Interactive)
    self.tableWidget.setColumnWidth(0, 150)
    self.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                             QHeaderView.Interactive)
    self.tableWidget.setColumnWidth(1, 200)

  def setData(self):
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setItem(0, 0, item)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setItem(0, 1, item)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setItem(0, 2, item)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setItem(0, 3, item)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setItem(0, 4, item)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setItem(0, 5, item)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setItem(0, 6, item)

    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setItem(1, 0, item)
    # item = QtWidgets.QTableWidgetItem()
    # self.tableWidget.setItem(1, 1, item)
    # item = QtWidgets.QTableWidgetItem()
    # self.tableWidget.setItem(1, 2, item)
    # item = QtWidgets.QTableWidgetItem()
    # self.tableWidget.setItem(1, 3, item)
    # item = QtWidgets.QTableWidgetItem()
    # self.tableWidget.setItem(1, 4, item)
    # item = QtWidgets.QTableWidgetItem()
    # self.tableWidget.setItem(1, 5, item)
    # item = QtWidgets.QTableWidgetItem()
    # self.tableWidget.setItem(1, 6, item)
    # item = self.tableWidget.verticalHeaderItem(0)
    # item.setText(self._translate("MainWindow", "1"))
    # item = self.tableWidget.horizontalHeaderItem(0)
    # item.setText(self._translate("MainWindow", "基本条码（货柜号）"))
    # item = self.tableWidget.horizontalHeaderItem(1)
    # item.setText(self._translate("MainWindow", "商品全名"))
    # item = self.tableWidget.horizontalHeaderItem(2)
    # item.setText(self._translate("MainWindow", "草稿数量"))
    # item = self.tableWidget.horizontalHeaderItem(3)
    # item.setText(self._translate("MainWindow", "销售数量"))
    # item = self.tableWidget.horizontalHeaderItem(4)
    # item.setText(self._translate("MainWindow", "库存数量"))
    # item = self.tableWidget.horizontalHeaderItem(5)
    # item.setText(self._translate("MainWindow", "成本单价"))
    # item = self.tableWidget.horizontalHeaderItem(6)
    # item.setText(self._translate("MainWindow", "是否建议补货"))
    __sortingEnabled = self.tableWidget.isSortingEnabled()
    self.tableWidget.setSortingEnabled(False)
    item = self.tableWidget.item(0, 0)
    item.setText(self._translate("MainWindow", "A-D12-1106007"))
    item = self.tableWidget.item(0, 1)
    item.setText(self._translate("MainWindow", "水泵皮带轮 21号 6BD1(双槽6孔)"))
    # 不可编辑
    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
    item = self.tableWidget.item(0, 2)
    item.setText(self._translate("MainWindow", "1"))
    item = self.tableWidget.item(0, 3)
    item.setText(self._translate("MainWindow", "2"))
    item = self.tableWidget.item(0, 4)
    item.setText(self._translate("MainWindow", "2个"))
    item = self.tableWidget.item(0, 5)
    item.setText(self._translate("MainWindow", "54"))
    item = self.tableWidget.item(0, 6)
    item.setText(self._translate("MainWindow", "否"))
    item = self.tableWidget.item(1, 0)
    item.setText(self._translate("MainWindow", "A-D12-1106007"))
    # item = self.tableWidget.item(1, 1)
    # item.setText(self._translate("MainWindow", "水泵皮带轮 21号 6BD1(双槽6孔)"))
    # item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
    # item = self.tableWidget.item(1, 2)
    # item.setText(self._translate("MainWindow", "1"))
    # item = self.tableWidget.item(1, 3)
    # item.setText(self._translate("MainWindow", "2"))
    # item = self.tableWidget.item(1, 4)
    # item.setText(self._translate("MainWindow", "2个"))
    # item = self.tableWidget.item(1, 5)
    # item.setText(self._translate("MainWindow", "54"))
    # item = self.tableWidget.item(1, 6)
    # item.setText(self._translate("MainWindow", "否"))
    self.tableWidget.setSortingEnabled(__sortingEnabled)
    # self.treeWidget.headerItem().setText(0, _translate("MainWindow", "仓库分类树"))
    # __sortingEnabled = self.treeWidget.isSortingEnabled()
    # self.treeWidget.setSortingEnabled(False)
    # self.treeWidget.topLevelItem(0).setText(
    #     0, self._translate("MainWindow", "五金/易损件"))
    # self.treeWidget.topLevelItem(0).child(0).setText(
    #     0, self._translate("MainWindow", "水泵皮带轮"))
    # self.treeWidget.setSortingEnabled(__sortingEnabled)
