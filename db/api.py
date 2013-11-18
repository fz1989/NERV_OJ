#!/usr/bin/env python
#coding=utf-8
import sys
sys.path.insert(0, '../')
from models import *
from sqlalchemy import *
from config.config import *
import sys


class DBAPI:
    def sync_db(self):

        try:
            engine = create_engine(DATA_BASE_URI)
            Base.metadata.create_all(engine)
        except:
            create_sql = ("CREATE DATABASE IF NOT EXISTS %s") %\
                         (DATA_BASE_NAME)
            engine = create_engine(DATA_BASE_CONNECTION, echo=True)
            engine.execute(create_sql)
            engine.dispose()
            engine = create_engine(DATA_BASE_URI, echo=rue)
            Base.metadata.create_all(engine)

    def clean_up(self):
        drop_sql = ("DROP DATABASE IF EXISTS %s") % (DATA_BASE_NAME)
        engine = create_engine(DATA_BASE_CONNECTION)
        engine.execute(drop_sql)
        engine.dispose()

    def regist_user(self, username, userpassword, email):
        user = User(username=username,
                    userpassword=userpassword,
                    email=email,
                    )
        try:
            user.save()
        except:
            pass

DI = DBAPI()


def regist_user(username, userpassword, email):
    DI.regist_user(username, userpassword, email)


def add_user(username, userpassword, user_group):
    pass


def del_user(username):
    pass


def update_user(username, user_info):
    pass


def find_user(username):
    pass


def add_problem(problem_info):
    pass


def update_problem(preoblem_id, problem_info):
    pass


def add_contest():
    pass


def add_problem_for_contest(contest_id, preoblem_list):
    pass
