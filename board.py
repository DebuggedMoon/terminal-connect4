"""This module contains the game board class"""

from typing import List, Dict

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

	def is_column_full(self, column_position: int) -> bool:
		"""Returns true of the column is full / doesn't have any Empty cells left."""
		return self.columns[column_position].count("Empty") == 0

	def get_surrounding_cells(self, column_position: int, row_position: int) -> Dict[str, str]:
		"""Returns a dict containing the cells surrounding the given position"""
		return {
			"TopLeft": self.columns[column_position - 1][row_position - 1],
			"Top": self.columns[column_position][row_position - 1],
			"TopRight": self.columns[column_position + 1][row_position - 1],
			"Right": self.columns[column_position + 1][row_position],
			"BottomRight": self.columns[column_position + 1][row_position + 1],
			"Bottom": self.columns[column_position][row_position + 1],
			"BottomLeft": self.columns[column_position - 1][row_position + 1],
			"Left": self.columns[column_position - 1][row_position]
		}
