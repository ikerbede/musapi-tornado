#!/usr/bin/python
#coding:utf-8

import os.path
import psycopg2
import tornado.web
import tornado.ioloop
import tornado.options
from handlers.index import IndexHandler
from handlers.users import UsersHandler, AuthenticationHandler
from handlers.chat import ChatHandler
from handlers.hands import HandsHandler, HandHandler
from models.deck import Deck

tornado.options.define("port", default=5000, help="run on the given port", type=int)

class Application(tornado.web.Application):
  def __init__(self):
    self.deck = Deck()
    self.dbConnection = psycopg2.connect(host="localhost", port=5432, database="musdb", user="iker", password="iker")

    # WEB APP
    handlers = [
      (r"/mus", IndexHandler),
      (r"/chat", ChatHandler),
      (r"/users", UsersHandler),
      (r"/users/login", AuthenticationHandler),
      (r"/hands", HandsHandler),
      (r"/hands/([0-9]+)", HandHandler)
    ]
    settings = dict(
      cookie_secret = "__MUS_BY_IKER__",
      login_url = "/login",
      xsrf_cookies = True,
      template_path = os.path.join(os.path.dirname(__file__), "templates"),
      static_path = os.path.join(os.path.dirname(__file__), "static")
    )
    super(Application, self).__init__(handlers, **settings)


def main():
  tornado.options.parse_command_line()
  app = Application()
  app.listen(tornado.options.options.port)
  tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
  main()