#! /usr/bin/env python
# coding:utf-8

import tornado.web
import sys
from db.models import *
from db.api import *
import json


def authenticated(require):
    def actualDecorator(method):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            if not self.current_user:
                raise HTTPError(403)
            user = get_user(self.current_user.username)
            if user.level not in require:
                raise HTTPError(403)
            return method(self, *args, **kwargs)
        return wrapper
    return actualDecorator


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('user')

    def set_current_user(self, user_name):
        self.set_secure_cookie('user', username)


class UsersHandler(BaseHandler):
    '''
    get:
        get user status or range

    post:
        add a new user
    '''

    def get(self):
        users = User.get_all(order_by=["solved, submit"])
        self.write(json.dumps(users))

    def post(self):
        username = self.get_argument("username")
        email = self.get_argument("email")
        password = self.get_argument("password")
        regist_info = regist_user(username=username,
                                  email=email,
                                  password=password)
        self.write(regist_info)
