from db.DBRunner import DBRunner
import pyodbc


class DBMainLinkMapper:
  def dbMainLink(self, dbConfigInf):
    try:
      db = DBRunner()
      return db.dbMainLink(dbConfigInf)
    except Exception as e:
      raise
      # print(e)
