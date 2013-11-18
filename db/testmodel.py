from models import User
from api import DBAPI
import sys
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
    print User.get_all()
    for user in User.get_all():
        print user
