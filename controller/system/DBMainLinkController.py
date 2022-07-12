from service.system.DBMainLinkService import DBMainLinkService


class DBMainLinkController:
  def __init__(self) -> None:
    pass

  def dbMainLink(self, dbConfigInf):
    return DBMainLinkService().dbMainLink(dbConfigInf)
