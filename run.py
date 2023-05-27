from terminalgame import TerminalGame
from board import Board
from game import Game

def main():

	board = Board(6, 7)
	game = Game(board)

	terminal = TerminalGame(game)
	terminal.render()

if __name__ == "__main__":
	main()