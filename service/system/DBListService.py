from dao.system.DBListMapper import DBListMapper


class DBListService:
  def __init__(self) -> None:
    self.dbListMapper = DBListMapper()

  def findDBList(self):
    return self.dbListMapper.findDBList()
