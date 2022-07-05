from PyQt5 import QtCore, QtGui, QtWidgets


class Tree:
  centralwidget = 0

  def __init__(self, centralwidget):
    self.centralwidget = centralwidget
    self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
    self.treeWidget.setGeometry(QtCore.QRect(10, 20, 241, 661))
    self.treeWidget.setObjectName("treeWidget")

    item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
    item_1 = QtWidgets.QTreeWidgetItem(item_0)
