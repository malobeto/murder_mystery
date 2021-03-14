import os
from pathlib import Path

from tkinter import *
from tkinter import scrolledtext

from murder_mystery import gui_game as game


#class MenuBar:
	#def __init__(self, master):
	#	self.master = master

	#	self.menu = Menu(self.master)
	#	self.master.config(menu=self.menu)

	#	self.file_menu = Menu(self.menu)
	#	self.file.add_command(label="Exit", command=self.quit)
	#	self.menu.add_cascade(label="File", menu=self.file_menu)

	#	self.game_menu = Menu(self.menu)
	#	self.file.add_command(label="New Game", command=self.new_game)
	#	self.menu.add_cascade(label="Game", menu=self.game_menu)

	#def new_game(self):
		# Need to figure out how to start a new game from this class that will clear widgets from whatever the active window is. I think I should move widgets in WindowTemplate to a class variable and then make sure clear sets the widgets
		# list to []. Also make the menu a subclass of WindowTemplate

	#def quit(self):
		#self.master.quit()


class WindowTemplate:
	def __init__(self, master):
		self.master = master

		self.widgets = []

	def display(self):
		for widget in self.widgets:
			widget.pack()
	
	def clear(self):
		for widget in self.widgets:
			widget.destroy()



class MainWindow(WindowTemplate):
	welcome_text = "Welcome to my game! What would you like to do?"
	def __init__(self, master):
		super().__init__(master)
		self.master.title("Welcome to the Murder Mystery game!")

		self.text = Label(master, text=self.welcome_text)
		self.widgets.append(self.text)

		self.choose_game_button = Button(master, text="Play a Game", command=self.choose_game)
		self.widgets.append(self.choose_game_button)

		self.create_game_button = Button(master, text="Write Your Own Game", command=self.create_game)
		self.widgets.append(self.create_game_button)

		#self.menu = MenuBar(self.master)

		self.display()

	def choose_game(self):
		game_choice_window = ChooseGameWindow(self.master)
		self.clear()

	def create_game(self):
		create_game_window = CreateGameSetWindow(self.master)
		self.clear()



class ChooseGameWindow(WindowTemplate):
	path_to_game_sets = Path('murder_mystery/game_sets/')
	game_sets = os.listdir(path_to_game_sets)
	game_titles = [game[:-5].title() for game in game_sets]
	def __init__(self, master):
		super().__init__(master)
		self.master.title("Choose a Game Set")

		self.text = Label(master, text="Please choose a game set to play with!")
		self.widgets.append(self.text)

		self.clicked = StringVar()
		self.drop = OptionMenu(master, self.clicked, *self.game_titles)
		self.widgets.append(self.drop)

		self.start_button = Button(master, text=f"Start {self.clicked.get()}", command=self.start)
		self.widgets.append(self.start_button)

		self.display()
	
	def start(self):
		game_window = GameWindow(self.master, self.clicked.get())
		self.clear()


class GameWindow(WindowTemplate):
	def __init__(self, master, game_name):
		super().__init__(master)
		self.game = game.Game(game_name)
		self.master.title(game_name)

		self.action_buttons = []

		self.game_text = scrolledtext.ScrolledText(window, width=120, height=40)
		self.widgets.append(self.game_text)

		self.display()
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
		super().clear()
		for b in self.action_buttons:
			b.destory()



if __name__ == "__main__":
	window = Tk()
	window.geometry("1000x800")
	main = MainWindow(window)
	window.mainloop()
