import ConfigParser
if __name__ == '__main__':
    import sys
    sys.path.insert(0, '../')
import os
import inspect
this_file = inspect.getfile(inspect.currentframe())
current_dir = os.path.abspath(os.path.dirname(this_file))
config = ConfigParser.ConfigParser()
config.read(current_dir + "/config.cfg")

DATA_BASE_BACKEND = config.get("db", "DATA_BASE_BACKEND")
DATA_BASE_USER = config.get("db", "DATA_BASE_USER")
DATA_BASE_PASSWORD = config.get("db", "DATA_BASE_PASSWORD")
DATA_BASE_NAME = config.get("db", "DATA_BASE_NAME")
DATA_BASE_IP = config.get("db", "DATA_BASE_IP")
DATA_BASE_CONNECTION = ("%s://%s:%s@%s") % (DATA_BASE_BACKEND, DATA_BASE_USER,
                DATA_BASE_PASSWORD, DATA_BASE_IP)
DATA_BASE_URI = ("%s/%s") % (DATA_BASE_CONNECTION, DATA_BASE_NAME)
        

