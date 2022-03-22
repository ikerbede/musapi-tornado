#!/usr/bin/python
#coding:utf-8

import psycopg2

class Score:
  def __init__(self, teamId, roundId, value):
    self.teamId = teamId
    self.roundId = roundId
    self.value = value
  
  def toDict(self):
    return {
      'scoreId': self.scoreId,
      'teamId': self.teamId,
      'roundId': self.roundId,
      'value': self.value
    }

  def insertToDB(self, connection):
    sql = """INSERT INTO Score(teamId, roundId, value)
             VALUES(%d, %d, %d) RETURNING scoreId"""
    cursor = connection.cursor()
    cursor.execute(sql, (self.teamId, self.roundId, self.value))
    self.scoreId = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
