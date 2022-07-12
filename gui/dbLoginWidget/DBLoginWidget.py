from PyQt5 import QtCore, QtGui, QtWidgets
from controller.system.DBMainLinkController import DBMainLinkController
import sys
mainDbConfig = {}


class DBLoginWidget:
  isCheckBoxChecked = False

  def __init__(self, dbConfig) -> None:
    self.mainDbConfig = dbConfig
    # print(self.mainDbConfig)
    pass

  def setupUi(self, Form):
    Form.setObjectName("Form")
    Form.resize(447, 407)
    self.label = QtWidgets.QLabel(Form)
    self.label.setGeometry(QtCore.QRect(0, 20, 451, 51))
    font = QtGui.QFont()
    font.setFamily("AcadEref")
    font.setPointSize(20)
    self.label.setFont(font)
    self.label.setAlignment(QtCore.Qt.AlignCenter)
    self.label.setObjectName("label")
    self.label_2 = QtWidgets.QLabel(Form)
    self.label_2.setGeometry(QtCore.QRect(20, 110, 121, 31))
    font = QtGui.QFont()
    font.setFamily("AcadEref")
    font.setPointSize(10)
    self.label_2.setFont(font)
    self.label_2.setObjectName("label_2")
    self.label_3 = QtWidgets.QLabel(Form)
    self.label_3.setGeometry(QtCore.QRect(20, 210, 121, 31))
    font = QtGui.QFont()
    font.setFamily("AcadEref")
    font.setPointSize(10)
    self.label_3.setFont(font)
    self.label_3.setObjectName("label_3")
    self.label_4 = QtWidgets.QLabel(Form)
    self.label_4.setGeometry(QtCore.QRect(20, 270, 121, 31))
    font = QtGui.QFont()
    font.setFamily("AcadEref")
    font.setPointSize(10)
    self.label_4.setFont(font)
    self.label_4.setObjectName("label_4")
    self.checkBox = QtWidgets.QCheckBox(Form)
    self.checkBox.setGeometry(QtCore.QRect(20, 320, 171, 16))
    self.checkBox.setObjectName("checkBox")
    # self.
    # 连接按钮
    self.pushButton = QtWidgets.QPushButton(Form)
    self.pushButton.setGeometry(QtCore.QRect(60, 350, 101, 31))
    self.pushButton.setObjectName("pushButton")
    self.pushButton.clicked.connect(self.onConfirmLinkClick)
    # 关闭按钮
    self.pushButton_2 = QtWidgets.QPushButton(Form)
    self.pushButton_2.setGeometry(QtCore.QRect(300, 350, 101, 31))
    self.pushButton_2.setObjectName("pushButton_2")
    self.pushButton_2.clicked.connect(self.exitTheProcess)
    self.label_5 = QtWidgets.QLabel(Form)
    self.label_5.setGeometry(QtCore.QRect(300, 110, 51, 31))
    font = QtGui.QFont()
    font.setFamily("AcadEref")
    font.setPointSize(10)
    self.label_5.setFont(font)
    self.label_5.setObjectName("label_5")
    # ip输入框
    self.lineEdit = QtWidgets.QLineEdit(Form)
    self.lineEdit.setGeometry(QtCore.QRect(150, 110, 141, 31))
    self.lineEdit.setObjectName("lineEdit")
    self.lineEdit.setPlaceholderText('请输入IP地址')
    self.lineEdit.setText(self.mainDbConfig['ip'])
    # 端口
    self.lineEdit_2 = QtWidgets.QLineEdit(Form)
    self.lineEdit_2.setGeometry(QtCore.QRect(340, 110, 81, 31))
    self.lineEdit_2.setObjectName("lineEdit_2")
    self.lineEdit_2.setPlaceholderText('请输入端口')
    self.lineEdit_2.setText(self.mainDbConfig['port'])
    # 数据库账号
    self.lineEdit_3 = QtWidgets.QLineEdit(Form)
    self.lineEdit_3.setGeometry(QtCore.QRect(150, 210, 271, 31))
    self.lineEdit_3.setObjectName("lineEdit_3")
    self.lineEdit_3.setPlaceholderText("请输入账号")
    self.lineEdit_3.setText(self.mainDbConfig['user'])
    # 数据库密码
    self.lineEdit_4 = QtWidgets.QLineEdit(Form)
    self.lineEdit_4.setGeometry(QtCore.QRect(150, 270, 271, 31))
    self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
    self.lineEdit_4.setObjectName("lineEdit_4")
    self.lineEdit_4.setPlaceholderText("请输入密码")
    self.lineEdit_4.setText(self.mainDbConfig['password'])

    # 数据库名
    self.lineEdit_5 = QtWidgets.QLineEdit(Form)
    self.lineEdit_5.setGeometry(QtCore.QRect(150, 160, 271, 31))
    self.lineEdit_5.setObjectName("lineEdit_5")
    self.lineEdit_5.setText(self.mainDbConfig['dbname'])
    self.label_6 = QtWidgets.QLabel(Form)
    self.label_6.setGeometry(QtCore.QRect(20, 160, 121, 31))
    font = QtGui.QFont()
    font.setFamily("AcadEref")
    font.setPointSize(10)
    self.label_6.setFont(font)
    self.label_6.setObjectName("label_6")
    self.retranslateUi(Form)
    QtCore.QMetaObject.connectSlotsByName(Form)

  def retranslateUi(self, Form):
    _translate = QtCore.QCoreApplication.translate
    Form.setWindowTitle(_translate("Form", "Form"))
    self.label.setText(_translate("Form", "请输入数据库配置"))
    self.label_2.setText(_translate("Form", "主数据库服务器IP："))
    self.label_3.setText(_translate("Form", "管理账号："))
    self.label_4.setText(_translate("Form", "密码："))
    self.checkBox.setText(_translate("Form", "保存信息到配置文件"))
    self.pushButton.setText(_translate("Form", "连接"))
    self.pushButton_2.setText(_translate("Form", "关闭"))
    self.label_5.setText(_translate("Form", "端口:"))
    self.label_6.setText(_translate("Form", "数据库名："))

  # 关闭主程序事件（退出
  def exitTheProcess(self):
    sys.exit(0)

  # 确定连接？
  def onConfirmLinkClick(self):
    dbConfig = {}
    dbConfig['dbHost'] = self.lineEdit.text()
    dbConfig['port'] = self.lineEdit_2.text()
    dbConfig['dbName'] = self.lineEdit_5.text()
    dbConfig['dbUser'] = self.lineEdit_3.text()
    dbConfig['dbPass'] = self.lineEdit_4.text()
    # print(dbConfig)
    print(DBMainLinkController().dbMainLink(dbConfig))
    # self.isCheckBoxChecked = se
