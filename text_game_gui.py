from tkinter import *
from tkinter import scrolledtext

from murder_mystery import gui_game as game

class GameWindow:
	def __init__(self, master, game_name):
		self.master = master
		self.game = game.Game(game_name)
		master.title(game_name)

		self.action_buttons = []

		self.game_text = scrolledtext.ScrolledText(window, width=120, height=40)
		self.game_text.grid(column=1, row=1, columnspan=5, sticky=W)
		self.display_actions([self.game.start])

	def update_game(self, action):
		"""
		Takes in a function as action that returns a string of text and then changes the game text to that
		text. 
		"""
		update = action()
		self.game_text.insert(INSERT, "\n...\n")
		self.game_text.insert(INSERT, update[0])
		self.game_text.yview_moveto(1)

	
		for b in self.action_buttons:
			b.destroy()
		self.action_buttons = [] 
		# The above line is essential to remove the action button reference in the list.
		# Otherwise the reference remains even though the object is destroyed, and causes an error.
		self.display_actions(update[1])


	def display_actions(self, functions):
		"""
		This function should take in a list of game action functions and create buttons on the bottom of 
		the window for them. The buttons are stored in the list action_buttons.
		"""
		for n, f in enumerate(functions):
			self.action_buttons.append(Button(window, text=f.__name__, command=lambda f=f: self.update_game(f)))
			self.action_buttons[n].grid(column=n+1, row=3)



window = Tk()
game_window = GameWindow(window, "palace_ball")

window.mainloop()
