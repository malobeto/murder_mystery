import json
import os

from .rooms import Room
from .weapons import Weapon
from .characters import Suspect

class Config():
    suspects_master_list = []
    weapons_master_list = []
    rooms_master_list = []
    def __init__(self, game_set):
        with open("murder_mystery/game_sets/" + game_set, "r") as f:
            set_data = json.load(f)
        self.introduction = set_data["introduction"]
        self.good_end = set_data["good_end"]
        self.bad_end = set_data["bad_end"]
        self.missed_weapon_end = set_data["missed_weapon_end"]
        self.missed_murderer_end = set_data["missed_murderer_end"]
        for suspect in set_data["suspects"]:
            self.suspects_master_list.append(Suspect(suspect))
        for weapon in set_data["weapons"]:
            self.weapons_master_list.append(Weapon(weapon))
        for room in set_data["rooms"]:
            self.rooms_master_list.append(Room(room))



    