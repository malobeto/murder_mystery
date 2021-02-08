from tkinter import *
from tkinter import scrolledtext

window = Tk()

print("test")
action_buttons = []
print("testube")

game_text = scrolledtext.ScrolledText(window, width=40, height=10)
game_text.grid(column=1, row=1)

def update_game(action, action_buttons=action_buttons):
	"""
	Takes in a function as action that returns a string of text and then changes the game text to that
	text. 
	"""
	update = action()
	game_text.insert(INSERT, "...\n")
	game_text.insert(INSERT, update[0])
	#for b in action_buttons:
	#	b.destroy()
	display_actions(update[1])

def display_actions(functions, action_buttons=action_buttons):
	"""
	This function should take in a list of game action functions and create buttons on the bottom of 
	the window for them. The buttons are stored in the list action_buttons.
	"""
	action_buttons = []
	for n, f in enumerate(functions):
		action_buttons.append(Button(window, text=f.__name__, command=lambda f=f: update_game(f)))
		action_buttons[n].grid(column=n+1, row=3)

def another():
	responses = [test]
	return "Another test\n", responses

def test():
	responses = [another]
	return "This is a test\n", responses

actions = [test]
display_actions(actions)

window.mainloop()
