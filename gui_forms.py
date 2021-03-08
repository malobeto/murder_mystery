class SuspectForm:
	def __init__(self, master):
		self.master = master

		self.name_lable = Label(master, text="Name:")
		self.name_label.pack()
		self.name_form = Entry(master)
		self.name_form.pack()

		self.description_label = Label(master, text="Description:")
		self.description_label.pack()
		self.description_form = Text(master)
		self.description_form.pack()


class WeaponForm:


class RoomForm:


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

		self.expl = Label(master, text=self.explaination)
		self.expl.pack()

		self.title_lable = Label(master, text="Title:")
		self.title_label.pack()
		self.title_form = Entry(master)
		self.title_form.pack()

		self.intro_label = Label(master, text="Type the intro to your mystery here:")
		self.intro_label.pack()
		self.intro_form = Text(master)
		self.intro_form.pack()

		self.good_end_label = Label(master, text="This is the ending to your game if the player finds both the murderer and the murder weapon used.")
		self.good_end_label.pack()
		self.good_end_form = Text(master)
		self.good_end_form.pack()

		self.bad_end_label = Label(master, text="This is the ending to your game if the player gets both the murderer and the murder weapon wrong:")
		self.bad_end_label.pack()
		self.bad_end_form = Text(master)
		self.bad_end_form.pack()

		self.missed_wep_label = Label(master, text="This is the ending to your game if the player found the murderer but did not choose the correct murder weapon:")
		self.missed_wep_label.pack()
		self.missed_wep_form = Text(master)
		self.missed_wep_form.pack()

		self.missed_sus_label = Label(master, text="This is the ending to your game if the player found the correct murder weapon but didn't choose the right suspect:")
		self.missed_sus_label.pack()
		self.missed_sus_form = Text(master)
		self.missed_sus_form.pack()

		self.suspects = []
		self.weapons = []
		self.rooms = []


#class EditGameSetWindow: