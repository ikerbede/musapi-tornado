#!/usr/bin/python
#coding:utf-8

import datetime
import psycopg2

class Round:
  def __init__(self, team1Id, team2Id):
    self.team1Id = team1Id
    self.team2Id = team2Id
    self.startDate = datetime.date.now()
  
  def toDict(self):
    return {
      'roundId': self.roundId,
      'team1Id': self.team1Id,
      'team2Id': self.team2Id,
      'startDate': self.startDate.strftime('%c')
    }
  
  def insertToDB(self, connection):
    sql = """INSERT INTO Round(team1Id, team2Id, startDate)
             VALUES(%d, %d, %s) RETURNING roundId"""
    cursor = connection.cursor()
    cursor.execute(sql, (self.team1Id, self.team2Id, self.startDate))
    self.roundId = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
