#!/usr/bin/python
#coding:utf-8

import psycopg2

class Card:
  def __init__(self, color, value):
    if color not in ['bastoi', 'ezpata', 'kopa', 'urre']:
      raise ValueError("Color name must be one of: 'bastoi' | 'ezpata' | 'kopa' | 'urre'")
    if value not in [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]:
      raise ValueError('Card value is not valid')
    self.color = color
    self.value = value
  
  def toDict(self):
    return {
      'color': self.color,
      'value': self.value
    }
  