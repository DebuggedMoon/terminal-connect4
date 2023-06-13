"""This module contains the Connect4 Game class"""

from random import randint
from board import Board

class Game():
	"""
	A class to represent a game of Connect4.
 	It modifies the given Board to match the game state.
	"""

	board: Board

	def __init__(self, board: Board):
		self.board = board

	def place_token(self, owner: str, column_position: int) -> bool:
		"""Places player token at lowest available row in column on the game board."""
		row_position = self.board.find_empty_column_index(column_position)
		self.board.columns[column_position][row_position] = owner
		return self.does_move_win(owner, column_position, row_position)

	def does_move_win(self, owner: str,column_position: int, row_position: int) -> bool:
		"""Returns true of placing a token at given cell causes the player to win."""
		surrounding_cells = self.board.get_surrounding_cells(column_position, row_position)
		for direction in surrounding_cells:
			matched_tokens = 1
			coordinates = surrounding_cells[direction]
			try:
				while owner == self.board.columns[coordinates[0]][coordinates[1]]:
					matched_tokens += 1
					coordinates = self.board.get_surrounding_cells(coordinates[0], coordinates[1])[direction]

					if matched_tokens == 4:
						return True
			except IndexError:
				pass # Cell is outside the game board.

		return False

	def get_bot_move(self) -> int:
		"""Returns a random board column that is not full."""
		move = None
		while not move or self.board.is_column_full(move):
			move = randint(0, self.board.width - 1)
		return move
