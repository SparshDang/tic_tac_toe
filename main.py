#Importing Modules
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.core.window import Window

#Definig Window Size
Window.size = (300,600)

#Main Class
class logic(Screen):
	def __init__(self):
		super().__init__()

		#Declaring Variables
		self.dict_win = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
		self.player = 0
		self.win = False

	#Function on Click
	def click_(self, event, n):
		if self.win:
			return

		#Decides Whose Turn and Changes The Turn 
		if self.dict_win[n] not  in ['x', '0']:
			event.text = 'X' if  self.player%2 == 0 else '0'
			self.dict_win[n] =  'x' if  self.player%2 == 0 else '0'
			self.player +=1
			event.width = self.width/3

			#Check For Turn
			self.check()
	

	#Check For Win or Draw
	def check(self):

		#Check Win
		for i in range(1,4): 
			if self.dict_win[i*3] == self.dict_win[i*3-1] == self.dict_win[i*3-2] or  self.dict_win[i] == self.dict_win[i+3] == self.dict_win[i+6] or self.dict_win[1] == self.dict_win[5] == self.dict_win[9] or  self.dict_win[3] == self.dict_win[5] == self.dict_win[7]:
				self.ids['reset'].text = 'New Game'
				self.ids['text'].text = f"Winner: X" if self.player%2 == 1 else f"Winner: 0"
				self.win = True	

		#Check Draw	
		if self.player == 9:
			self.ids['text'].text = 'Draw'
			self.win = True
			self.ids['reset'].text = 'New Game'

	#Reset Game
	def reset(self):
		if self.ids['reset'].text  == 'New Game':
			self.ids['reset'].text = 'Reset' 
		lay = self.ids['mainlayout']
		for w in lay.children:
			w.text = ''
		for i,v in self.dict_win.items():
			self.dict_win[i] = i
		self.win = False
		self.player = 0
		self.ids['text'].text = 'TIC-TAC-TOE'

#Main App
class tictactoe(MDApp):
	def build(self):
		return logic()


if __name__ == '__main__':
	game = tictactoe()
	game.run()
