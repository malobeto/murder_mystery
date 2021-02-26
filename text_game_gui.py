import os
from pathlib import Path

from tkinter import *
from tkinter import scrolledtext

from murder_mystery import gui_game as game


class MainWindow:
	welcome_text = "Welcome to my game! What would you like to do?"
	def __init__(self, master):
		self.master = master
		master.title("Welcome to the Murder Mystery game!")

		self.text = Label(master, text=self.welcome_text)
		self.text.pack()

		self.choose_game_button = Button(master, text="Play a Game", command=self.choose_game)
		self.choose_game_button.pack()

		self.create_game_button = Button(master, text="Write Your Own Game", command=self.create_game)
		self.create_game_button.pack()

	def choose_game(self):
		game_choice_window = ChooseGameWindow(self.master)
		self.clear()

	def create_game(self):
		create_game_window = CreateGameSetWindow(self.master)
		self.clear()

	def clear(self):
		self.text.destroy()
		self.choose_game_button.destroy()
		self.create_game_button.destroy()


class ChooseGameWindow:
	path_to_game_sets = Path('.\murder_mystery\game_sets')
	game_sets = os.listdir(path_to_game_sets)
	game_titles = [game[:-5].title() for game in game_sets]
	def __init__(self, master):
		self.master = master
		master.title("Choose a Game Set")

		self.text = Label(master, text="Please choose a game set to play with!")
		self.text.pack()

		self.clicked = StringVar()
		self.drop = OptionMenu(master, self.clicked, *self.game_titles)
		self.drop.pack()

		self.start_button = Button(master, text=f"Start {self.clicked.get()}", command=self.start)
		self.start_button.pack()
	
	def start(self):
		game_window = GameWindow(self.master, self.clicked.get())
		self.clear()

	def clear(self):
		self.text.destroy()
		self.drop.destroy()
		self.start_button.destroy()


class GameWindow:
	def __init__(self, master, game_name):
		self.master = master
		self.game = game.Game(game_name)
		master.title(game_name)

		self.action_buttons = []

		self.game_text = scrolledtext.ScrolledText(window, width=120, height=40)
		self.game_text.pack()

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
			button = Button(window, text=f.__name__, command=lambda f=f: self.update_game(f))
			self.action_buttons.append(button)
			button.pack(side=LEFT, padx=30)

	def clear(self):
		for b in self.action_buttons:
			b.destory()
		self.game_text.destory()


class CreateGameSetWindow:
	explaination = (
	"This is where you can write your own murder mystery! " 
	"Fill out each category. Some categories have a button to add additional entries into that category."
	)
	def __init__(self, master):
		self.master = master
		master.title("Write your own murder mystery!")

		self.game_dict = {
			"introduction": "",
			"suspects": [],
			"weapons": [],
			"rooms": [],
			"good_end": "",
			"bad_end": "",
			"missed_weapon_end": "",
			"missed_murderer_end": ""
		}

		self.text = Label(master, text=self.explaination)
		self.text.pack()


#class EditGameSetWindow:



if __name__ == "__main__":
	window = Tk()
	window.geometry("1000x800")
	main = MainWindow(window)
	window.mainloop()
