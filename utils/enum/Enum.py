from enum import Enum


class DBKey(Enum):
  MASTER = 'MASTER_DB'
  OTHER = 'LIST_DB'


def getName(enum, enum_name):
  return enum[enum_name]['name']


def getCode(enum, enum_name):
  return enum[enum_name]['code']
