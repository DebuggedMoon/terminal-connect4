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

	def draw_notification_message(self, message: str) -> None:
		"""Draws a given text notification at the bottom of the Terminal."""
		self.draw_at_xy(
        	0,
         	self.terminal.height - 2,
          	self.terminal.white_on_red(self.terminal.center(message))
        )

	def get_player_move(self) -> int:
		"""Handles user input and returns a valid player move."""
		self.draw_at_xy(
        	0,
         	self.terminal.height - 3,
          	self.terminal.white_on_blue(
               self.terminal.center("> Press Column Number you wish to Select <")
            )
        )

		while True:

			with self.terminal.cbreak(), self.terminal.hidden_cursor():
				player_input = self.terminal.inkey()

			if not player_input.isdigit():
				self.draw_notification_message(f"Input must be a number! Got: {player_input}")
				continue

			board_width = self.game.board.width
			player_move = int(str(player_input))

			if player_move <= 0 or player_move > board_width:
				self.draw_notification_message(
                    f"Input must be within board width (1-{board_width})! Got: {player_input}"
                )
			else:
				return player_move

		return player_move

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
		print(f"Player selected {self.get_player_move()}!")
