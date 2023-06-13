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
		self.columns = [["Empty" for _ in range(heigth)] for _ in range(width)]

	def find_empty_column_index(self, column_position: int) -> int:
		"""Returns the next empty column cells index."""
		return self.columns[column_position].index("Empty")

	def is_column_full(self, column_position: int) -> bool:
		"""Returns true of the column is full / doesn't have any Empty cells left."""
		return self.columns[column_position].count("Empty") == 0

	def get_surrounding_cells(self, column_position: int, row_position: int) -> Dict[str, List[int]]:
		"""Returns a dict containing the cells surrounding the given position"""
		return {
			"TopLeft": [column_position - 1, row_position - 1],
			"Top": [column_position - 1, row_position - 1],
			"TopRight": [column_position - 1, row_position - 1] ,
			"Right": [column_position - 1, row_position - 1],
			"BottomRight": [column_position - 1, row_position - 1],
			"Bottom": [column_position - 1, row_position - 1],
			"BottomLeft": [column_position - 1, row_position - 1],
			"Left": [column_position - 1, row_position - 1]
		}
