from models import User
from api import DBAPI
import sys
from api import *
sys.path.insert(0, '../')

DB = DBAPI()


def init():
    DB.clean_up()
    DB.sync_db()
    a = User(password="19891001",
             email="fz1989fz@test.com",
             username="fz1989")
    a.save()
    b = User(password="19891001",
             email="fz1989afz@test.com",
             username="fza1989")
    b.save()

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "init":
        init()
    print "111", regist_user(username="fz198ss11", email="fz19@1.com", password="te")
