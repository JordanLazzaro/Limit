from cards import Card

class Slot:
	__init__(self):
		self.card = None
		self.locked = False

	is_locked():
		return self.locked	

	is_empty():
		self.card == None

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
