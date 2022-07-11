import configparser

config = configparser.ConfigParser()

config.read("DBConfig.ini")

mainDBConfig = {}

mainDBConfig['ip'] = config.get("MainDB", "db_ip")
mainDBConfig['port'] = config.get("MainDB", "db_port")
mainDBConfig['user'] = config.get("MainDB", "db_user")
mainDBConfig['password'] = config.get("MainDB", 'db_pass')
