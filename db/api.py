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
        
        create_sql = ("CREATE DATABASE IF NOT EXISTS %s") % (DATA_BASE_NAME)
        engine = create_engine(DATA_BASE_CONNECTION)
        engine.execute(create_sql)
        engine.dispose()
        engine = create_engine(DATA_BASE_URI)
        Base.metadata.create_all(engine)

dbAPI = DBAPI()
dbAPI.sync_db()
