#!/usr/bin/python
#coding:utf-8
  
from random import choice
from .color import Color

class Hand():
  def __init__(self):
    self.id = id(self)
    self.cards = []
  
  def addCard(self, card):
    if (len(self.cards) == 4):
      raise IndexError('The Hand is full already!')
    else:
      self.cards.append(card)

  def getPairValuesAndPoints(self):
    vap = []
    value = 0
    points = 0
    cardValues = []
    for card in self.cards:
      cardValues.append(card.value)
    for card in self.cards:
      if (card.value != value):
        nbOccurences = cardValues.count(card.value)
        if (nbOccurences > 1):
          value = card.value
          if (nbOccurences == 2):
            points = 1
          elif (nbOccurences == 3):
            points = 2
          elif (nbOccurences == 4):
            points = 3
          else:
            raise ValueError('Unexpected number of occurences: ' + nbOccurences)
          vap.append([value, points])
    
    return vap
  
  def getGameValueAndPoints(self):
    vap = []
    value = 0
    for card in self.cards:
      if (card.value in [11, 12]):
        value += 10
      else:
        value += card.value
    vap.append(value)

    if (value < 31):
      vap.append(1)
    elif (value > 31):
      vap.append(2)
    elif (value == 31):
      vap.append(3)
    
    return vap
  
  def toDict(self):
    cardDicts = []
    for card in self.cards:
      cardDicts.append(card.toDict())
    return {
      'id': self.id,
      'cards': cardDicts,
      'pairs': self.getPairValuesAndPoints(),
      'game': self.getGameValueAndPoints()
    }
