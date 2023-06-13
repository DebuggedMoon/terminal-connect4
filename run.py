"""Main Programm for Initiating and Managing the Connect4 Game"""

from terminalgame import TerminalGame
from board import Board
from game import Game

def main():
	"""Initiates a Connect4 Game for the Terminal"""

	board = Board(6, 7)
	game = Game(board)

	terminal = TerminalGame(game)
	terminal.draw_start_screen()
	terminal.draw_game()

if __name__ == "__main__":
	main()
