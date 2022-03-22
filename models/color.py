#!/usr/bin/python
#coding:utf-8

from .card import Card

class Color:
  def __init__(self, name):
    if name not in ['bastoi', 'ezpata', 'kopa', 'urre']:
      raise ValueError("Color name must be one of: 'bastoi' | 'ezpata' | 'kopa' | 'urre'")
    self.name = name
    self.cards = []
    for i in [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]:
      self.cards.append(Card(name, i))
  