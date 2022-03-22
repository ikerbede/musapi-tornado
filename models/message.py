#!/usr/bin/python
#coding:utf-8

import datetime

class Message:
  def __init__(self, author, content):
    self.id = id(self)
    self.author = author
    self.content = content
    self.date = datetime.datetime.now()
  
  def toDict(self):
    return {
      'id': self.id,
      'author': self.author,
      'content': self.content,
      'date': self.date.strftime('%c')
    }