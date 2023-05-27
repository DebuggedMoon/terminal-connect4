
class TerminalGame():

	def __init__(self, game):
		
		self.game = game

	def render(self):

		if not self.game.board:
			return

		for column in self.game.board.columns:
			print(" ".join(column))
