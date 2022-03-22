#!/usr/bin/python
#coding:utf-8

import datetime
import psycopg2

class User:
  def __init__(self, name, password, avatar):
    self.name = name
    self.password = password
    self.avatar = avatar
  
  def toDict(self):
    return {
      'userId': self.userId,
      'name': self.name,
      'password': self.password,
      'avatar': self.avatar
    }

  def insertToDB(self, connection):
    sql = """INSERT INTO User(name, password, avatar)
             VALUES(%s, %s, %s) RETURNING userId"""
    cursor = connection.cursor()
    cursor.execute(sql, (self.name, self.password, psycopg2.Binary(self.avatar)))
    self.userId = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
