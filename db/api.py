#!/usr/bin/env python
#coding=utf-8
import sys
sys.path.insert(0, '../')
from models import Base
from sqlalchemy import *
from config.config import *
import sys

class DBAPI:
    def sync_db(self):

        try:
            engine = create_engine(DATA_BASE_URI)
            Base.metadata.create_all(engine)
        except:
            create_sql = ("CREATE DATABASE IF NOT EXISTS %s") % (DATA_BASE_NAME)
            engine = create_engine(DATA_BASE_CONNECTION, echo = True)
            engine.execute(create_sql)
            engine.dispose()
            engine = create_engine(DATA_BASE_URI, echo = True)
            Base.metadata.create_all(engine)

    def clean_up(self):
        drop_sql = ("DROP DATABASE IF EXISTS %s") % (DATA_BASE_NAME)
        engine = create_engine(DATA_BASE_CONNECTION)
        engine.execute(drop_sql)
        engine.dispose()

dbAPI = DBAPI()
dbAPI.sync_db()

def registuser(username, userpassword, user_group):

