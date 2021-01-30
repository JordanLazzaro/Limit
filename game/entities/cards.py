"""
Basic Card class with 
"""
import enum


class CardType(enum.Enum):
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

class CardColor(enum.Enum):
  Red
  Black

class Card:
  """ A simple Card object
  Args:
    card_type: a tuple containing value and suite
  
  Raises: NotImplementedError
  """
  def __init__(self, card_type=None, is_visible=False):
    if card_type == None:
      raise NotImplementedError()
    self.card_type = card_type # tuple: (CardType, CardColor)
    self.is_visible = is_visible

  def __eq__(self, right):
    return self.card_type == right.card_type

  def __ne__(self, right):  
    return self.card_type != right.card_type

  def __lt__(self, right):
    return self.card_value < right.card_value

  def __le__(self, right):
    return self.card_value <= right.card_value

  def __gt__(self, right):
    return self.card_value > right.card_value

  def __ge__(self, right):
    return self.card_value >= right.card_value

