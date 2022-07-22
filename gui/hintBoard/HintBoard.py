from PyQt5 import QtCore, QtGui, QtWidgets
from controller.system.DBMainLinkController import DBMainLinkController
from PyQt5.QtWidgets import QMessageBox
from gui.dbTableWidget.DbTableWidget import DbTableWidget
import utils.Glo as Glo


class HintBoard():
  # 线程
  thread = None
  frame = None
  dbTableFrame = None
  # 信号收发
  # signal = QtCore.pyqtSignal(str)

  def closeEvent(self, event):
    print('检测到关闭')
    pass

  def setupUi(self, Frame, linkFrame):
    self.frame = Frame
    self.linkFrame = linkFrame
    Frame.setObjectName("Frame")
    Frame.resize(373, 190)

    self.label = QtWidgets.QLabel(Frame)
    self.label.setGeometry(QtCore.QRect(0, 30, 371, 51))
    font = QtGui.QFont()
    font.setFamily("AcadEref")
    font.setPointSize(20)
    self.label.setFont(font)
    self.label.setText("正在连接.")
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

    # self.signal.connect(self.closeThread)

    # DBTable
    self.dbForm = QtWidgets.QWidget()
    self.dbTable = DbTableWidget(self.dbForm)

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

  def closeThread(self, e):
    result = QMessageBox.critical(
        None, '提示: 连接错误', str(e))

  def setLoopText(self, dbConfig):
    self.label.setText("正在连接。。。。。")
    try:
      linkOut = DBMainLinkController().dbMainLink(dbConfig)
      if linkOut:
        self.closeFrame(self.frame)
        QMessageBox.information(None, ' 提示 ', '  连接成功！  ')
        self.linkFrame.close()
        self.dbForm.show()
        # 设置config
        Glo.set_value('dbConfig', dbConfig)
        self.dbTable.loadDBListData()
    except Exception as e:
      print(e)
      self.closeThread(e)
      self.closeFrame(self.frame)

      # slot = MessageBox()
      # self.linkThread = MainDbLinkThread(
      #     'linkMainDb', 1, self, dbConfig)
      # self.thread.signal.connect(slot.getMessage)
      # self.thread = QtCore.QThread()
      # self.thread.started.connect(self.linkThread)
      # self.thread.start()
      # pass

  def closeFrame(self, Frame):
    Frame.close()
    # self.thread.exitFlag = True
    # self.thread.join()


# class MessageBox(QtCore.QObject):
#   def getMessage(self, e):
#     self.closeThread(e)
