import pyodbc as db
import logging
# dbConfig = {
#     'driverName': '{SQL Server}',
#     'dbHost': '127.0.0.1',
#     'dbName': 'fzsc_local',
#     'port': '',
#     'dbUser': 'pub',
#     'dbPass': 'root'
# }

# cursor = None
con = None
logger = logging.getLogger(__name__)


class DB:

  def dbConnect(self, dbConfig):
    try:
      # dbHostAddr = dbConfig['dbHost'] + ':' + dbConfig['port']
      conConfigInf = ('DRIVER='+dbConfig['driverName'] + '; ' if dbConfig['driverName'] else '') + 'SERVER=' + \
          dbConfig['dbHost'] + ((',' + dbConfig['port']) if dbConfig['port'] else '') + '; DATABASE=' + \
          dbConfig['dbName'] + '; UID=' + \
          dbConfig['dbUser'] + '; PWD=' + dbConfig['dbPass']
      print(conConfigInf)
      con = db.connect(conConfigInf)
      return {'success': True, 'con': con}
      # cursor = con.cursor()
      # Sample select query
      # cursor.execute("SELECT * FROM AccountModel")
      # row = cursor.fetchone()
      # while row:
      #   print(row)
      #   row = cursor.fetchone()
    except db.Error as e:
      # print(e)
      # logger.error('wrong:' + e)
      raise
    finally:
      print('The try except is finished')

  def dbSelectExecute(self, cursor, sql):
    try:
      return cursor.execute(sql)
    except Exception as sqlError:
      logger.error('sql wrong:' + sqlError)
      raise Exception({'success': False, 'error': sqlError})
    finally:
      if (con is not None):
        con.close()

  def dbModifyExecute(self, cursor, sql):
    try:
      count = cursor.execute(sql)
      con.commit()
      return count
    except Exception as sqlError:
      logger.error('sql wrong:' + sqlError)
      raise Exception({'success': False, 'error': sqlError})
    finally:
      if (con is not None):
        con.close()
