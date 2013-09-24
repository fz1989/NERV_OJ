#! /usr/bin/env python
# coding: UTF-8
import tornado.ioloop
import tornado.web

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


application = tornado.web.Application([
    (r"/home", HomeHandler),
])

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
