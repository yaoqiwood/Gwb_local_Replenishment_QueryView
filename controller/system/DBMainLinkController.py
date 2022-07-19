from service.system.DBMainLinkService import DBMainLinkService


class DBMainLinkController:
  def __init__(self) -> None:
    pass

  def dbMainLink(self, dbConfigInf):
    try:
      return DBMainLinkService().dbMainLink(dbConfigInf)
    except Exception as e:
      raise
