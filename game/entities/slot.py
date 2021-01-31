from cards import Card

class Slot:
	__init__(self):
		self.card = None
		self.locked = False

	isLocked():
		if self.locked:
			return True
		return False	

	isEmpty():
		if self.card == None:
			return True
		return False

	fill(card):
		self.card = card
		return

	clear():
		self.card = None
		return

	lock():
		self.locked = True
		return

	contents():
		return self.card
