from  models import User
from api import DBAPI
import sys
sys.path.insert(0, '../')

DB = DBAPI()
DB.clean_up()
DB.sync_db()
a = User(password = "19891001", email = "fz1989fz@test.com", username = "fz1989")
a.save()
