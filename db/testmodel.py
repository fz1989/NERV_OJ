from  models import User
from api import DBAPI
import sys
sys.path.insert(0, '../')

DB = DBAPI()
DB.clean_up()
DB.sync_db()
a = User(password = "19891001", email = "fz1989fz@test.com", username = "fz1989")
a.save()
b = User(password = "19891001", email = "fz1989fz@test.com", username = "fz1989")
b.save()
c = User(password = "19891001", email = "fz1989afz@test.com", username = "fza1989")
c.save()
