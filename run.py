"""Main Programm for Initiating and Managing the Connect4 Game"""

from terminalgame import TerminalGame
from board import Board
from game import Game

def main():
	"""Initiates a Connect4 Game for the Terminal"""

	board = Board(7, 6)
	game = Game(board)

	terminal = TerminalGame(game)
	terminal.draw_start_screen()
	terminal.draw_tutorial_screen()
	terminal.draw_game_screen()

	while True:
		player_move = terminal.get_player_move()
		player_won = game.place_token("Player", player_move)

		terminal.update_board()
		if player_won:
			terminal.draw_at_xy(
       			0,
          		int(terminal.height * 0.5),
				terminal.white_on_green + terminal.center("!!! You WON !!!")
            )
			terminal.draw_notification_message("> PRESS `RUN PROGRAM`TO PLAY AGAIN <")
			break

if __name__ == "__main__":
	main()
