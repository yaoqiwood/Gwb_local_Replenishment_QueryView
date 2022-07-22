DBKey = {
    'MASTER': {
        'name': 'MASTER',
        'code': 'MASTER_DB'
    },
    'OTHER': {
        'name': 'OTHER',
        'code': 'LIST_DB'
    }
}


def getName(enum, enum_name):
  return enum[enum_name]['name']


def getCode(enum, enum_name):
  return enum[enum_name]['code']
