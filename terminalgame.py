"""This module contains the terminal renderer class for the Connect4 game class"""

from blessed import Terminal
from game import Game

GAMETITLE_ART = r"""
 ____                                           __        __ __      
/\  _`\                                        /\ \__    /\ \\ \     
\ \ \/\_\    ___     ___     ___      __    ___\ \ ,_\   \ \ \\ \    
 \ \ \/_/_  / __`\ /' _ `\ /' _ `\  /'__`\ /'___\ \ \/    \ \ \\ \_  
  \ \ \L\ \/\ \L\ \/\ \/\ \/\ \/\ \/\  __//\ \__/\ \ \_    \ \__ ,__\
   \ \____/\ \____/\ \_\ \_\ \_\ \_\ \____\ \____\\ \__\    \/_/\_\_/
    \/___/  \/___/  \/_/\/_/\/_/\/_/\/____/\/____/ \/__/       \/_/  
"""

TUTORIAL_TITLE_ART = r"""
 ______         __                                ___      
/\__  _\       /\ \__                __          /\_ \     
\/_/\ \/ __  __\ \ ,_\   ___   _ __ /\_\     __  \//\ \    
   \ \ \/\ \/\ \\ \ \/  / __`\/\`'__\/\ \  /'__`\  \ \ \   
    \ \ \ \ \_\ \\ \ \_/\ \L\ \ \ \/ \ \ \/\ \L\.\_ \_\ \_ 
     \ \_\ \____/ \ \__\ \____/\ \_\  \ \_\ \__/.\_\/\____\
      \/_/\/___/   \/__/\/___/  \/_/   \/_/\/__/\/_/\/____/
"""

TUTORIAL_TEXT = """
TODO: How to play
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. 
Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
"""

WELCOME_TEXT = """
Welcome to Connect 4,
the ultimate game of strategy and skill!

Brace yourself for intense battles against a bot opponent
as you strategically place your tokens to create an
unbreakable line of four.

Victory awaits those who can outwit and outmaneuver their adversaries!
"""

class TerminalGame(Terminal):
	"""A class for handling how the Game object is drawn to the Terminal."""

	game: Game

	def __init__(self, game: Game):
		super().__init__()
		self.game = game

	def draw_at_xy(self, x_position: int, y_position: int, content: str):
		"""Draws content string at the given x and y position to the Terminal."""
		with self.location(x_position, y_position):
			print(content)

	def draw_gametitle(self):
		"""Draws the game title to the Terminal."""

		for line in GAMETITLE_ART.split("\n"):
			print(self.center(self.color_rgb(24, 116, 205) + line + self.normal))

	def draw_tutorial_title(self) -> None:
		"""Draws the tutorial screen title to the Terminal."""

		for line in TUTORIAL_TITLE_ART.split("\n"):
			print(self.center(self.color_rgb(24, 116, 205) + line + self.normal))

	def draw_tutorial_text(self) -> None:
		"""Draws the tutorial text to the Terminal."""

		for line in TUTORIAL_TEXT.split("\n"):
			print(self.center(self.white + line + self.normal))

	def draw_welcome_text(self) -> None:
		"""Draws the welcome text to the Terminal."""

		for line in WELCOME_TEXT.split("\n"):
			print(self.center(self.white + line + self.normal))

	def draw_notification_message(self, message: str) -> None:
		"""Draws a given text notification at the bottom of the Terminal."""
		self.draw_at_xy(
        	0,
         	self.height - 2,
          	self.white_on_red(self.center(message))
        )

	def wait_for_input(self) -> None:
		"""Prompts user for input and waits until input is detected."""
		self.draw_at_xy(
        	0,
         	self.height - 3,
          	self.white_on_blue(
               self.center("> Press any Key to Continue <")
            )
        )

		with self.cbreak(), self.hidden_cursor():
			self.inkey()


	def get_player_move(self) -> int:
		"""Handles user input and returns a valid player move."""
		self.draw_at_xy(
        	0,
         	self.height - 3,
          	self.white_on_blue(
               self.center("> Press Column Number you wish to Select <")
            )
        )

		while True:

			with self.cbreak(), self.hidden_cursor():
				player_input = self.inkey()

			if not player_input.isdigit():
				self.draw_notification_message(f"Input must be a number! Got: {repr(player_input)}")
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
			print(self.center(" ".join(column)))

	def draw_game(self) -> None:
		"""Draws the game in its current state to the Terminal."""
		if not self.game.board:
			return

		self.draw_gametitle()
		self.draw_board()
		print(f"Player selected {self.get_player_move()}!")

	def draw_start_screen(self) -> None:
		"""Draws the welcome screen meant for program start."""
		print("")
		self.draw_gametitle()
		self.draw_welcome_text()
		self.wait_for_input()
		print(self.clear)

	def draw_tutorial_screen(self) -> None:
		"""Draws the tutorial screen which contains game controns and rules."""
		self.draw_tutorial_title()
		self.draw_tutorial_text()
		self.wait_for_input()
		print(self.clear)
