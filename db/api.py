#!/usr/bin/env python
#coding=utf-8
if __name__ == '__main__':
    import sys
    sys.path.insert(0, '../')
from models import Base
from sqlalchemy import *
from config.config import *
import sys

class DBAPI:
    def sync_db(self):
        DATA_BASE_ENGIN = ("%s://%s:%s@%s/%s") % (DATA_BASE_BACKEND, DATA_BASE_USER,
                DATA_BASE_PASSWORD, DATA_BASE_IP, DATA_BASE_NAME)
        engine = create_engine(DATA_BASE_ENGIN)
        Base.metadata.create_all(engine)

dbAPI = DBAPI()
dbAPI.sync_db()
