#!/usr/bin/python
#coding:utf-8

import tornado.web
import json
from handlers.base import BaseHandler
from models.deck import Deck
from models.card import Card

class HandsHandler(BaseHandler):
  @tornado.web.authenticated
  def get(self):
    self.write({'hands': self.application.deck.getHandDicts()})

class HandHandler(BaseHandler):
  @tornado.web.authenticated
  def get(self, handId):
    hand = self.application.deck.getHandById(int(handId))
    self.write({'hand': hand.toDict()})
  
  @tornado.web.authenticated
  def put(self, handId):
    cards = []
    for cardDict in json.loads(self.request.body):
      cards.append(Card(cardDict['color'], cardDict['value']))
    self.application.deck.replaceCardsFromHand(int(handId), cards)
    hand = self.application.deck.getHandById(int(handId))
    self.write({'hand': hand.toDict()})
