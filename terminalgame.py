"""This module contains the terminal renderer class for the Connect4 game class"""

from game import Game

class TerminalGame():
	"""A class for handling how the Game object is drawn to the Terminal."""

	game: Game

	def __init__(self, game: Game):
		self.game = game

	def render(self) -> None:
		"""Draws the game board in its current state to the Terminal."""
		if not self.game.board:
			return

		for column in self.game.board.columns:
			print(" ".join(column))
