import pepper, mazechecker, random

arrows = {'left': '<--', 'right': '-->', 'up': '^\n|', 'down': '|\nv'}
arrowsl = ['left','right','up','down']
colorslist = ['red','orange','purple','blue','pink']

class MazeGenerator:
	def __init__(self):
		self.maze = pepper.Game(2, xaxis=8, yaxis=8, title='My Maze Program!')
		self.generatenew()
		self.maze.update()
		
	def generatenew(self, gb=None):
		if gb != None:
			self.maze.gameboard = gb
		else:
			mazepossible = False
			while mazepossible != True:
				for x in range(len(self.maze.gameboard)):
					for y in range(len(self.maze.gameboard[x])):
						r = random.choice(arrowsl)
						self.maze.gameboard[x][y] = pepper.GameSquare(color='green', text=arrows[r])
						if mazechecker.checkifpossible(self.maze.gameboard):
							mazepossible = True
			self.maze.gameboard[7][7] = pepper.GameSquare(color="yellow")
			mazepossible = False
			while mazepossible != True:
				for x in range(random.randint(1, 5)):
					self.maze.gameboard[x][random.randint(0,7)] = pepper.GameSquare(color=colorslist[x], text="TEL")
					self.maze.gameboard[random.randint(0,7)][random.randint(0,7)] = pepper.GameSquare(color=colorslist[x], text="TEL")
					if mazechecker.checkifpossible(self.maze.gameboard):
						mazepossible = True
	
	def checkwin(self):
		if self.maze.postion == [7, 7]:
			return True
		return False
	
	def onMoveExc(self, x, y):
		pass

if __name__ == '__main__':
	app = MazeGenerator()
	app.maze.root.mainloop()
