from tkinter import *
from tkinter import scrolledtext

from murder_mystery import gui_game as game

window = Tk()

action_buttons = []

game_text = scrolledtext.ScrolledText(window, width=120, height=40)
game_text.grid(column=1, row=1, columnspan=5, sticky=W)

def update_game(action):
	"""
	Takes in a function as action that returns a string of text and then changes the game text to that
	text. 
	"""
	global action_buttons
	update = action()
	game_text.insert(INSERT, "\n...\n")
	game_text.insert(INSERT, update[0])
	game_text.yview_moveto(1)

	
	for b in action_buttons:
		b.destroy()
	action_buttons = [] 
	# The above line is essential to remove the action button reference in the list.
	# Otherwise the reference remains even though the object is destroyed, and causes an error.
	display_actions(update[1])

def display_actions(functions):
	"""
	This function should take in a list of game action functions and create buttons on the bottom of 
	the window for them. The buttons are stored in the list action_buttons.
	"""
	global action_buttons
	for n, f in enumerate(functions):
		action_buttons.append(Button(window, text=f.__name__, command=lambda f=f: update_game(f)))
		action_buttons[n].grid(column=n+1, row=3)

game = game.Game("palace_ball")
display_actions([game.start])

window.mainloop()
