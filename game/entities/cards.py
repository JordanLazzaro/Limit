"""
Basic Card class 
"""
from enum import Enum, auto


class CardValue(Enum):
  RedKing   = -1
  Joker     = 0
  Ace       = 1
  Two       = 2
  Three     = 3
  Four      = 4
  Five      = 5
  Six       = 6
  Seven     = 7
  Eight     = 8
  Nine      = 9
  Ten       = 10
  Jack      = 11
  Queen     = 12
  BlackKing = 13

class CardSuit():
  Hearts   = auto()
  Diamonds = auto()
  Clovers  = auto()
  Spades   = auto()


class Card:
  """ A simple Card object
  Args:
    card_type: a tuple containing value and suite
  
  Raises: ValueError
  """
  def __init__(self, card_value=None, card_suit=None, is_visible=False):
    if card_value == None or not isinstance(card_value, CardValue):
      raise ValueError("card_type must by of type: CardValue")
    if card_suit == None or not isinstance(card_suit, CardSuit):
      raise ValueError("card_suit must by of type: CardSuit")
    self.card_value = card_value
    self.card_suit = card_suit
    self.is_visible = is_visible

  def __eq__(self, right):
    return self.card_value == right.card_value

  def __ne__(self, right):  
    return self.card_value != right.card_value

  def __lt__(self, right):
    return self.card_value < right.card_value

  def __le__(self, right):
    return self.card_value <= right.card_value

  def __gt__(self, right):
    return self.card_value > right.card_value

  def __ge__(self, right):
    return self.card_value >= right.card_value

