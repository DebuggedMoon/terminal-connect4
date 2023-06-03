"""This module contains the terminal renderer class for the Connect4 game class"""

from blessed import Terminal
from game import Game


class TerminalGame():
	"""A class for handling how the Game object is drawn to the Terminal."""

	game: Game
	terminal = Terminal()

	def __init__(self, game: Game):
		self.game = game

	def draw_at_xy(self, x_position: int, y_position: int, content: str):
		"""Draws content string at the given x and y position to the Terminal."""
		with self.terminal.location(x_position, y_position):
			print(content)

	def render_board(self):
		"""Draws the game board in its current state to the Terminal."""
		for column in self.game.board.columns:
			print(self.terminal.center(" ".join(column)))

	def render_game(self) -> None:
		"""Draws the game in its current state to the Terminal."""
		if not self.game.board:
			return

		self.render_board()
