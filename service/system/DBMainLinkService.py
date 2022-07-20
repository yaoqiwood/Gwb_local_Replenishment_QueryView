from dao.system.DBMainLinkMapper import DBMainLinkMapper


class DBMainLinkService:
  def __init__(self) -> None:
    pass

  def dbMainLink(self, dbConfigInf):
    return DBMainLinkMapper().dbMainLink(dbConfigInf)['success']
    # try:
    #   return DBMainLinkMapper().dbMainLink(dbConfigInf)['success']
    # except Exception as e:
    #   raise
# pass
