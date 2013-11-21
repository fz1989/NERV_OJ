#! /usr/bin/env python
# coding:utf-8

import tornado.web
import sys
from models.user import User
from db.api import *


def authenticated(req):
    def actualDecorator(method):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            user = DI.get_user(self.current_user.username)
            if not user:
                raise HTTPError(403)
            return method(self, *args, **kwargs)
        return wrapper
    return actualDecorator


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('user')

    def set_current_user(self, user_name):
        self.set_secure_cookie('user', username)


class UsersHandle(BaseHandler):
    '''
    get:
        get user status or range

    post:
        add a new user

    del:
        del all user
    '''
    pass
