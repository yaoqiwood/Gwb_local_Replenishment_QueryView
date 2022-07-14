from PyQt5 import QtCore, QtGui, QtWidgets
from thread.MainDbLinkThread import MainDbLinkThread
import time


class HintBoard(object):
  # 线程
  thread = None
  frame = None

  def closeEvent(self, event):
    print('检测到关闭')
    pass

  def setupUi(self, Frame):
    self.frame = Frame
    Frame.setObjectName("Frame")
    Frame.resize(373, 190)

    self.label = QtWidgets.QLabel(Frame)
    self.label.setGeometry(QtCore.QRect(0, 30, 371, 51))
    font = QtGui.QFont()
    font.setFamily("AcadEref")
    font.setPointSize(20)
    self.label.setFont(font)
    # self.label.setText("正在连接.")
    self.label.setAlignment(QtCore.Qt.AlignCenter)
    self.label.setObjectName("label")
    # self.pushButton = QtWidgets.QPushButton(Frame)
    # self.pushButton.setGeometry(QtCore.QRect(130, 130, 101, 31))
    # self.pushButton.setObjectName("pushButton")
    # self.pushButton.clicked.connect(lambda: self.closeFrame(Frame))

    # 禁用最大化
    Frame.setWindowFlags(
        QtCore.Qt.FramelessWindowHint)
    # 禁止拉伸窗口
    Frame.setFixedSize(Frame.width(), Frame.height())

    self.retranslateUi(Frame)
    QtCore.QMetaObject.connectSlotsByName(Frame)

  def retranslateUi(self, Frame):
    _translate = QtCore.QCoreApplication.translate
    Frame.setWindowTitle(_translate("Frame", "Frame"))
    # self.pushButton.setText(_translate("Frame", "取消"))

  def onMainDbLink(self):
    self.loopHintText()

  def loopHintText(self):
    # self.label.setText("正在连接")
    # self.threadBlocker = False
    self.label.setText("正在连接。")

  def setLoopText(self, dbConfig):
    self.thread = MainDbLinkThread('linkMainDb', 1, self, dbConfig)
    self.thread.start()

  def closeFrame(self, Frame):
    Frame.close()
    self.thread.exitFlag = True
    # self.thread.join()
