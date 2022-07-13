from PyQt5 import QtCore, QtGui, QtWidgets
import time
import _thread


class HintBoard(object):
  # 线程关闭器
  threadBlocker = False

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
    self.pushButton.clicked.connect(lambda: self.closeFrame(Frame))

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
    self.threadBlocker = False
    self.label.setText("正在连接。。。")
    _thread.start_new_thread(self.setLoopText, ())

  def setLoopText(self):
    i = 1
    while True:
      if (self.threadBlocker):
        break
      text = ''
      for j in range(i):
        i += 1
        if (i == 5):
          i = 0
          text = ''
        text += '。'
        # print(text)
      self.label.setText("正在连接" + text)
      time.sleep(1)

  def closeFrame(self, Frame):
    Frame.close()
    self.threadBlocker = True
