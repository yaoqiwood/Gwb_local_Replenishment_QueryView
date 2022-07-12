from db.DBRunner import DBRunner


class DBMainLinkMapper:
  def dbMainLink(self, dbConfigInf):
    db = DBRunner()
    return db.dbMainLink(dbConfigInf)
