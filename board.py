"""This module contains the game board class"""

class Board():
	"""
	A class to represent a game board.
	Allows modification to the board state.
	"""

	def __init__(self, width, heigth):
		self.width = width
		self.heigth = heigth
		self.columns = [["⬜"]*width]*heigth
