#! /usr/bin/env python
# coding: UTF-8

import tornado
import tornado.ioloop
import tornado.web
import os
import tornado.httpserver
from controllers import user_controller


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/users", user_controller.UsersHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "statics"),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    application = Application()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
