#!/usr/bin/env python
#coding=utf-8
import sys
sys.path.insert(0, '../')
from models import *
from sqlalchemy import *
from config.config import *
import sys
import hashlib


class DBAPI:
    def sync_db(self):

        try:
            engine = create_engine(DATA_BASE_URI)
            Base.metadata.create_all(engine)
        except:
            create_sql = ("CREATE DATABASE IF NOT EXISTS %s") %\
                         (DATA_BASE_NAME)
            engine = create_engine(DATA_BASE_CONNECTION)
            engine.execute(create_sql)
            engine.dispose()
            engine = create_engine(DATA_BASE_URI)
            Base.metadata.create_all(engine)

    def clean_up(self):
        drop_sql = ("DROP DATABASE IF EXISTS %s") % (DATA_BASE_NAME)
        engine = create_engine(DATA_BASE_CONNECTION)
        engine.execute(drop_sql)
        engine.dispose()

    def regist_user(self, username, password, email):
        user = User(username=username,
                    password=password,
                    email=email,
                    )
        if User.name_exist(username):
            return u"用户名已经存在！"
        user.save()
        return u"注册成功"

    def check_login(self, username, password):
        return User.get_by_name(name=username).password == password

    def soft_del_user(self, username):
        User.get_by_name(name=username).soft_delete()

    def update_user(self, user_info):
        User.get_by_name(name=username).update(user_info)

    def get_user(self, username):
        return User.get_by_name(name=username)

DI = DBAPI()


def regist_user(username, password, email):
    return DI.regist_user(username, password, email)


def check_login(username, password):
    return DI.check_login(username, password)


def del_user(username):
    return DI.soft_del_user(username)


def update_user(user_info):
    return DI.update_user(user_info)


def get_user(username):
    return DI.get_user(username)


def add_problem(problem_info):
    pass


def update_problem(preoblem_id, problem_info):
    pass


def add_contest():
    pass


def add_problem_for_contest(contest_id, preoblem_list):
    pass
