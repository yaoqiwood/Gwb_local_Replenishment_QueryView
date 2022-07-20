from service.system.DBListService import DBListService


class DBListController:
  def __init__(self) -> None:
    self.dbListService = DBListService()

  def findDBList(self):
    return self.dbListService.findDBList()
