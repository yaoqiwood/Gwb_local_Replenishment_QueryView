from db.DBRunner import DBRunner


class DBListMapper:

  def findDBList(self):
    sql = 'SELECT * FROM db_list'
    db = DBRunner()
    db.dbSelectMasterExecute(sql)
