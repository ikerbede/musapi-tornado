#!/usr/bin/python
#coding:utf-8

import tornado.web
import json
import psycopg2
from handlers.base import BaseHandler
from models.user import User

class UsersHandler(BaseHandler):
  def get(self):
    if self.current_user.name == "admin":
      cursor = self.application.dbConnection.cursor()
      # TODO: cursor.execute(sql, (self.name, self.password, psycopg2.Binary(self.avatar)))
      self.userId = cursor.fetchone()[0]
      cursor.close()

  def post(self):
    credentials = json.loads(self.request.body)
    newUser = User(credentials.name, credentials.password, credentials.avatar)
    newUser.insertToDB(self.application.dbConnection)
    self.write(newUser.toDict())

class AuthenticationHandler(tornado.web.RequestHandler):
  def __init__(self):
    self.hands = self.application.deck.hands[:]
    self.users = []

  def post(self):
    credentials = json.loads(self.request.body)
    self.users.append(User(credentials.name, credentials.password, None))
    handId = self.hands.pop(0).id
    self.write({'handId': handId})
