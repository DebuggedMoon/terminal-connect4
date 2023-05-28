"""This module contains the terminal renderer class for the Connect4 game class"""

from game import Game
from blessed import Terminal

class TerminalGame():
	"""A class for handling how the Game object is drawn to the Terminal."""

	game: Game
	terminal = Terminal()

	def __init__(self, game: Game):
		self.game = game
  
	def draw_at_xy(self, x: int, y: int, content: str):
		with self.terminal.location(x, y):
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

