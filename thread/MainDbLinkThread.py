from controller.system.DBMainLinkController import DBMainLinkController
import threading
import time


class MainDbLinkThread (threading.Thread):
  exitFlag = False
  sleepSec = 1
  other = None
  dbConfig = {}

  def __init__(self, name, sleepSec, other, dbConfig):
    threading.Thread.__init__(self)
    # self.threadID = threadID
    self.name = name
    self.sleepSec = sleepSec
    self.other = other
    self.dbConfig = dbConfig
    pass

  def run(self):
    self.other.label.setText("正在连接。。。。。")
    linkOut = DBMainLinkController().dbMainLink(self.dbConfig)
    if linkOut:
      self.other.closeFrame(self.other.frame)
    # self.play()
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
