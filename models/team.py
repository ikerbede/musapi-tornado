#!/usr/bin/python
#coding:utf-8

import psycopg2

class Team:
  def __init__(self, user1Id, user2Id):
    self.user1Id = user1Id
    self.user2Id = user2Id
  
  def toDict(self):
    return {
      'teamId': self.teamId,
      'user1Id': self.user1Id,
      'user2Id': self.user2Id
    }

  def insertToDB(self, connection):
    sql = """INSERT INTO Team(user1Id, user2Id)
             VALUES(%d, %d) RETURNING teamId"""
    cursor = connection.cursor()
    cursor.execute(sql, (self.user1Id, self.user2Id))
    self.teamId = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
