"""This module contains the terminal renderer class for the Connect4 game class"""

class TerminalGame():
	"""A class for handling how the Game object is drawn to the Terminal."""

	def __init__(self, game):
		self.game = game

	def render(self) -> None:
		"""Draws the game board in its current state to the Terminal."""
		if not self.game.board:
			return

		for column in self.game.board.columns:
			print(" ".join(column))
