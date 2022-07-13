from PyQt5 import QtCore, QtGui, QtWidgets
import time


class HintBoard(object):
  def setupUi(self, Frame):
    Frame.setObjectName("Frame")
    Frame.resize(373, 184)
    self.label = QtWidgets.QLabel(Frame)
    self.label.setGeometry(QtCore.QRect(0, 30, 371, 51))
    font = QtGui.QFont()
    font.setFamily("AcadEref")
    font.setPointSize(20)
    self.label.setFont(font)
    # self.label.setText("正在连接.")
    self.label.setAlignment(QtCore.Qt.AlignCenter)
    self.label.setObjectName("label")
    self.pushButton = QtWidgets.QPushButton(Frame)
    self.pushButton.setGeometry(QtCore.QRect(130, 130, 101, 31))
    self.pushButton.setObjectName("pushButton")
    self.pushButton.clicked.connect(Frame.close)

    # 禁用最大化
    Frame.setWindowFlags(
        QtCore.Qt.WindowCloseButtonHint)
    # 禁止拉伸窗口
    Frame.setFixedSize(Frame.width(), Frame.height())

    self.retranslateUi(Frame)
    QtCore.QMetaObject.connectSlotsByName(Frame)

  def retranslateUi(self, Frame):
    _translate = QtCore.QCoreApplication.translate
    Frame.setWindowTitle(_translate("Frame", "Frame"))
    self.pushButton.setText(_translate("Frame", "取消"))

  def loopHintText(self):
    # self.label.setText("正在连接")
    self.label.setText("正在连接。。。")
    # while True:
    #   print(11112)
    #   text = '.'
    #   i = 0
    #   for j in range(i):
    #     i += 1
    #     if (i == 5):
    #       i = 0
    #     text += '.'
    #   # self.label.setText("正在连接" + text)
    #   time.sleep(1)
