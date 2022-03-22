#!/usr/bin/python
#coding:utf-8

import tornado.websocket
import json
from models.message import Message

class ChatHandler(tornado.websocket.WebSocketHandler):
  """docstring for SocketHandler"""
  clients = set()

  @staticmethod
  def send_to_all(message):
    for c in ChatHandler.clients:
        c.write_message(json.dumps(message))

  def open(self):
    #joinedMsg = Message('MUS', 'Ongi etorri mus solaserat !')
    #self.write_message(joinedMsg.toDict())
    ChatHandler.clients.add(self)

  def on_close(self):
    ChatHandler.clients.remove(self)

  def on_message(self, data):
    dataDict = json.loads(data)
    userMsg = Message(dataDict['author'], dataDict['content'])
    ChatHandler.send_to_all(userMsg.toDict())
  
  def check_origin(self, origin):
    return True
