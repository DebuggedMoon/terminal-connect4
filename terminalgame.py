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
   
	def draw_gametitle(self):
		"""Draws the game title to the Terminal."""

		gametitle_lines = """
     _/_/_/                                                      _/      _/  _/
  _/          _/_/    _/_/_/    _/_/_/      _/_/      _/_/_/  _/_/_/_/  _/  _/ 
 _/        _/    _/  _/    _/  _/    _/  _/_/_/_/  _/          _/      _/_/_/_/
_/        _/    _/  _/    _/  _/    _/  _/        _/          _/          _/   
 _/_/_/    _/_/    _/    _/  _/    _/    _/_/_/    _/_/_/      _/_/      _/    
""".split("\n")

		for line in gametitle_lines:
			print(self.terminal.center(self.terminal.color_rgb(24, 116, 205) + line + self.terminal.normal))

	def draw_board(self):
		"""Draws the game board in its current state to the Terminal."""
		for column in self.game.board.columns:
			print(self.terminal.center(" ".join(column)))

	def draw_game(self) -> None:
		"""Draws the game in its current state to the Terminal."""
		if not self.game.board:
			return

		self.draw_gametitle()
		self.draw_board()
