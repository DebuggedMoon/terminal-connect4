"""This module contains the game board class"""

from typing import List

class Board():
	"""
	A class to represent a game board.
	Allows modification to the board state.
	"""

	width: int
	heigth: int
	columns: List[List[str]]

	def __init__(self, width: int, heigth: int):
		self.width = width
		self.heigth = heigth
		self.columns = [["Empty"]*heigth]*width

	def find_empty_column_index(self, column_position: int) -> int:
		"""Returns the next empty column cells index."""
		return self.columns[column_position].index("Empty")
