from connect4.terminalgame import TerminalGame
from connect4.board import Board
from connect4.game import Game

def main():

	board = Board(6, 7)
	game = Game(board)

	terminal = TerminalGame(game)
	terminal.render()

if __name__ == "__main__":
	main()