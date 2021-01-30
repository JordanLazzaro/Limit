"""
Set of classes for all the game cards
"""

class Card:
  """ A simple Card object
  Args:
    card_type: a tuple containing value and suite
  
  Raises: NotImplementedError
  """
  def __init__(self, card_type=None, is_visible=False):
    if card_type == None:
      raise NotImplementedError()
    self.card_type = card_type
    self.is_visible = is_visible

  # TODO: Implement after finishing card_type enum
  def __eq__():
    pass 

  def __ne__():
    pass

  def __lt__():
    pass

  def __le__():
    pass

  def __gt__():
    pass

  def __ge__():
    pass
