#! /usr/bin/env python
# coding:utf-8

import tornado.web
import sys
import db.
from models.user import User
from db.api import *
class RegistHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("regist.html")

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")

class show(tornado.web.RequestHandler):
    def get(self, user_id):
        user = get_user_by_id(user_id)
        self.render("user.html", user = user)
