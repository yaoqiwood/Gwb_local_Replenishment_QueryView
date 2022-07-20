from db.DBRunner import DBRunner


class DBListMapper:

  def findDBList(self):
    try:
      sql = 'SELECT * FROM db_list'
      db = DBRunner()
      return db.dbSelectMasterExecute(sql)
    except Exception as e:
      raise
