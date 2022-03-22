#!/usr/bin/python
#coding:utf-8

from random import choice
from .color import Color
from .hand import Hand

class Deck:
  cards = []
  recycleBin = []
  hands = []

  def __init__(self):
    self.cards = (Color('bastoi').cards + Color('ezpata').cards) + (Color('kopa').cards + Color('urre').cards)
    self.dealCards()

  def pickUpCard(self):
    if len(self.cards) == 0:
      self.cards = self.recycleBin
      self.recycleBin = []
    card = choice(self.cards)
    self.cards.remove(card)
    self.recycleBin.append(card)
    return card

  def removeCard(self, card):
    self.cards.remove(card)
    self.recycleBin.append(card)

  def dealCards(self):
    self.hands = [Hand(), Hand(), Hand(), Hand()]
    for hand in self.hands:
      for i in range (1, 5):
        hand.addCard(self.pickUpCard())

  def getCards(self, nb):
    cards = []
    if (nb > len(self.cards)):
      raise IndexError('You try to remove more cards than it remains in card deck!')
    for i in range(0, nb):
      cards.append(self.pickUpCard())
    return cards
  
  def replaceCardsFromHand(self, handId, cards):
    # Remove cards from the hand
    hand = self.getHandById(handId)
    for card in cards:
      hand.cards.remove(card)

    # Replace by new cards from the deck
    newCards = self.getCards(len(cards))
    for newCard in newCards:
      hand.addCard(newCard)
  
  def getHandById(self, handId):
    for hand in self.hands:
      if hand.id == handId:
        return hand
    return None

  def getHandDicts(self):
    handDicts = []
    for hand in self.hands:
      print('ya')
      handDicts.append(hand.toDict())
    return handDicts
