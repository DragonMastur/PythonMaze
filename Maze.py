import pepper, mazechecker, random, time

arrows = {'left': '<--', 'right': '-->', 'up': '^\n|', 'down': '|\nv'}
arrowsl = ['left','right','up','down']
colorslist = ['red','gray','purple','blue','pink','white']

class MazeGenerator:
	def __init__(self):
		self.maze = pepper.Game(2, xaxis=8, yaxis=8, title='My Maze Program!')
		self.maze.GS.root.bind("<r>",self.doNew)
		self.maze.GS.root.bind("<Key>",self.keyPress)
		self.doNew()
		
	def doNew(self,event=None):
		self.generatenew()
		self.maze.postion=[0,0]
		self.maze.update()
		
	def generatenew(self, gb=None):
		if gb != None:
			self.maze.gameboard = gb
		else:
			mazepossible = False
			while mazepossible != True:
				self.teleporters={}
				for x in range(len(self.maze.gameboard)):
					for y in range(len(self.maze.gameboard[x])):
						r = random.choice(arrowsl)
						self.maze.gameboard[x][y] = pepper.GameSquare(color='green',text=arrows[r])
				for x in range(random.randint(1, 5)):
					coordsgood=False
					while coordsgood!=True:
						xi=random.randint(0,7);yi=random.randint(0,7);xq=random.randint(0,7);yq=random.randint(0,7);
						if xi==0 and yi==0 or xi==7 and yi==7: xi=random.randint(1,6); yi=random.randint(1,6);
						if xq==0 and yq==0 or xq==7 and yq==7: xq=random.randint(1,6); yq=random.randint(1,6);
						coordsgood=True
						for t in self.teleporters:
							if self.teleporters[t][0]==[xi,yi]: coordsgood=False;
							if self.teleporters[t][1]==[xq,yq]: coordsgood=False;
							if self.teleporters[t][1]==[xi,yi]: coordsgood=False;
							if self.teleporters[t][0]==[xq,yq]: coordsgood=False;
						if [xi,yi]==[xq,yq]: coordsgood=False;
					self.maze.gameboard[xi][yi] = pepper.GameSquare(color=colorslist[x], text="TEL")
					self.maze.gameboard[xq][yq] = pepper.GameSquare(color=colorslist[x], text="TEL")
					self.teleporters[colorslist[x]]=[[xi,yi],[xq,yq]]
				if mazechecker.checkifpossible(self.maze.gameboard,self.teleporters):
					mazepossible = True
			self.maze.gameboard[7][7] = pepper.GameSquare(color="yellow",text="END")
			self.maze.gameboard[0][0] = pepper.GameSquare(color="yellow",text="START")
	
	def checkwin(self):
		if self.maze.postion == [7, 7]:
			return True
		return False
	
	def keyPress(self,event):
		if event.char in ['w','s','a','d']:
			self.maze.keyPressed(event)
			self.maze.update()
			self.onMoveExc()
	
	def arrowMove(self, a):
		cursquare=[self.maze.postion[0],self.maze.postion[1]]
		if self.maze.gameboard[cursquare[0]][cursquare[1]].text==arrows[a]:
			if a=='right':
				self.maze.move(1,0)
			if a=='left':
				self.maze.move(-1,0)
			if a=='down':
				self.maze.move(0,1)
			if a=='up':
				self.maze.move(0,-1)
		if cursquare==[self.maze.postion[0],self.maze.postion[1]]:
			return False
		else:
			return True
	
	def checkBoardMove(self):
		pass
	
	def onMoveExc(self):
		cursquare=[self.maze.postion[0],self.maze.postion[1]];aa1=False
		for t in self.teleporters:
			if cursquare==self.teleporters[t][0]:
				self.maze.postion[0]=self.teleporters[t][1][0]
				self.maze.postion[1]=self.teleporters[t][1][1]
			if cursquare==self.teleporters[t][1]:
				self.maze.postion[0]=self.teleporters[t][0][0]
				self.maze.postion[1]=self.teleporters[t][0][1]
		for a in arrows:
			if self.arrowMove(a):
				aa1=True
				self.checkBoardMove()
		time.sleep(0.2)
		self.maze.update()
		if self.checkwin():
			print("YOU WIN!")
			time.sleep(1)
			self.doNew()
		try:
			if aa1==True:
				self.onMoveExc()
		except:
			print("STUCK?\nYOU'VE BEEN MOVED TO 0,0!")
			self.maze.postion=[0,0]
			self.maze.update()

if __name__ == '__main__':
	app = MazeGenerator()
	app.maze.root.mainloop()
