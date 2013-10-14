import ConfigParser
if __name__ == '__main__':
    import sys
    sys.path.insert(0, '../')

config = ConfigParser.ConfigParser()
config.read("/home/fz/Project/Python/NERV_OJ/config/config.cfg")

DATA_BASE_BACKEND = config.get("db", "DATA_BASE_BACKEND")
DATA_BASE_USER = config.get("db", "DATA_BASE_USER")
DATA_BASE_PASSWORD = config.get("db", "DATA_BASE_PASSWORD")
DATA_BASE_NAME = config.get("db", "DATA_BASE_NAME")
DATA_BASE_IP = config.get("db", "DATA_BASE_IP")

