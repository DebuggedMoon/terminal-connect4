"""This module contains the Connect4 Game class"""

from board import Board

class Game():
	"""
	A class to represent a game of Connect4.
 	It modifies the given Board to match the game state.
	"""
 
	board: Board

	def __init__(self, board: Board):
		self.board = board
