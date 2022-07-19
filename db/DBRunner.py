from .DBConfig import dbConfig
from .DBDrive import DB
import pyodbc


class DBRunner:
  def dbMainLink(self, dbConfigInf):
    try:
      db = DB()
      dbConfigInf['driverName'] = '{SQL Server Native Client 10.0}'
      return db.dbConnect(dbConfigInf)
    except Exception as e:
      raise

  def dbSelectMasterExecute(self, sql):
    db = DB()
    dbConfig['driverName'] = '{SQL Server Native Client 10.0}'
    dbConfig['dbHost'] = '192.168.0.101'
    dbConfig['dbName'] = 'fzsc_local'
    dbConfig['port'] = ''
    dbConfig['dbUser'] = 'gwb'
    dbConfig['dbPass'] = 'root'

    con = db.dbConnect(dbConfig)
    cursor = con.cursor()
    return db.dbSelectExecute(cursor, sql).fetchall()
