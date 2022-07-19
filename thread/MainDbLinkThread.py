from PyQt5 import QtCore
import threading
import time
import logging
import sys

logger = logging.getLogger(__name__)


class MainDbLinkThread (QtCore.QObject):
  exitFlag = False
  sleepSec = 1
  other = None
  dbConfig = {}

  # 信号收发
  # signal = QtCore.pyqtSignal(object)

  def __init__(self, name, sleepSec, other, dbConfig):
    super(MainDbLinkThread, self).__init__()
    # threading.Thread.__init__(self)
    # self.threadID = threadID
    self.name = name
    self.sleepSec = sleepSec
    self.other = other
    self.dbConfig = dbConfig
    pass

  def run(self):
    pass
    try:
      pass
      # self.other.label.setText("正在连接。。。。。")
      # linkOut = DBMainLinkController().dbMainLink(self.dbConfig)
      # if linkOut:
      #   self.other.closeFrame(self.other.frame)
      # self.play()
    except Exception as e:
      pass
      # self.other.signal.emit(e)
      # self.callBack(e)

      # self.bucket.put(sys.exc_info())
      # raise
      # print(e)
      # logger.error('数据库错误：' + str(e['error']))
    finally:
      # logger.info('查询结束')
      pass

  def play(self):
    i = 1
    while True:
      if self.exitFlag:
        break
      text = ''
      for j in range(i):
        i += 1
        if (i == 5):
          i = 1
          text = ''
        text += '。'
        print(text)
      self.other.label.setText("正在连接。" + text)
      time.sleep(self.sleepSec)
