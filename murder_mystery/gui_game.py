from random import choice
import json
import os

from .rooms import Room
from .weapons import Weapon
from .characters import Suspect
from .characters import Investigator

class Game:
    def __init__(self, game_set):
        self.rooms = []
        self.suspects = []
        self.weapons = []
        with open("murder_mystery/game_sets/" + game_set + ".json", "r") as f:
            set_data = json.load(f)
        self.introduction = set_data["introduction"]
        self.good_end = set_data["good_end"]
        self.bad_end = set_data["bad_end"]
        self.missed_weapon_end = set_data["missed_weapon_end"]
        self.missed_murderer_end = set_data["missed_murderer_end"]
        for suspect in set_data["suspects"]:
            self.suspects.append(Suspect(suspect, self))
        for weapon in set_data["weapons"]:
            self.weapons.append(Weapon(weapon, self))
        for room in set_data["rooms"]:
            self.rooms.append(Room(room, self))
        self.murderer = choice(self.suspects)
        self.murder_weapon = choice(self.weapons)
        self.murder_room = choice(self.rooms)
        self.murder_room.dead_body = True
        self.murder_weapon.is_the_murder_weapon = True
        self.murderer.is_the_murderer = True
        #randomly place suspects in rooms
        for suspect in self.suspects:
            location = choice(self.rooms)
            location.characters_present.append(suspect)
            suspect.location = location
        #randomly place weapons in rooms. If the weapon is the murder weapon make it hidden
        for weapon in self.weapons:
            location = choice(self.rooms)
            weapon.location = location
            if weapon.is_the_murder_weapon:
                location.hidden_items.append(weapon)
            else:
                location.items.append(weapon)
        self.investigator = Investigator()
        self.investigator.location = self.murder_room
        self.murderer_choice = None
        self.murder_weapon_choice = None
        self.playing = True
        self.base_actions = []

    
    def look_around(self):
        room = self.investigator.location
        text = room.description + "\n"
        choices = self.base_actions
        for suspect in room.characters_present:
            text = text + suspect.description + "\n"

        def yes():
            weapon_evidence = self.murder_weapon.body_evidence
            suspect_evidence = self.murderer.body_evidence
            text = "The dead body lying in the center of the room has not been dead long. %s %s" % (weapon_evidence, suspect_evidence)
            choices = self.base_actions
            return text, choices

        def no():
            text = "Ew gross who wants to see a dead body?!"
            choices = self.base_actions
            return text, choices

        if room.dead_body:
            text =  text + "And in the center of the room there is a dead body."
            text =  text + "Would you like to take a closer look? Yes or no?"
            choices = [yes, no]

        return text, choices

    def search(self):
        text = ""
        room = self.investigator.location
        if len(room.items) < 1:
            text = "You don't find anything of note when you search %s" % room.name
        else:
            for weapon in room.items:
                text = text + "You find a %s." % weapon.description
                self.investigator.inventory.append(weapon)
                room.items.remove(weapon)
            for weapon in room.hidden_items:
                text = text + "%s you find a %s. %s" % (room.hiding_spot, weapon.description, self.murderer.weapon_evidence)
                self.investigator.inventory.append(weapon)
                room.hidden_items.remove(weapon)
        choices = self.base_actions
        return text, choices

    def move(self):
        current_location = self.investigator.location
        self.rooms.remove(current_location)
        choices = []
        for room in self.rooms:
            choice = lambda r=room: r.move_to()
            choice.__name__ = room.name
            choices.append(choice)
        self.rooms.append(current_location)
        text = "Which room would you like to move to?"
        return text, choices

    def talk(self):
        room = self.investigator.location
        choices = []
        text = "Who would you like to talk to?"
        if len(room.characters_present) == 0:
            text = "There's no one here to talk to."
            choices = self.base_actions
            return text, choices
        for suspect in room.characters_present:
            choice = lambda s=suspect: s.talk_to()
            choice.__name__ = suspect.name
            choices.append(choice)
        return text, choices
    
    def accuse(self):
        choices = []
        for suspect in self.suspects:
            choice = lambda s=suspect: s.accuse_murderer()
            choice.__name__ = suspect.name
            choices.append(choice)
        text = "Who do you think dunit?"
        return text, choices

    def end(self):
        text = "Are you sure that it was %s with %s." % (self.murderer_choice.name, self.murder_weapon_choice.name)
        
        def yes():
            choices = []
            self.playing = False
            if self.murderer_choice.is_the_murderer and self.murder_weapon_choice.is_the_murder_weapon:
                text =  self.good_end
            elif self.murderer_choice.is_the_murderer and self.murder_weapon_choice.is_the_murder_weapon == False:
                text =  self.missed_weapon_end
            elif self.murderer_choice.is_the_murderer == False and self.murder_weapon_choice.is_the_murder_weapon:
                text = self.missed_murderer_end
            elif self.murderer_choice.is_the_murderer == False and self.murder_weapon_choice.is_the_murder_weapon == False:
                text = self.bad_end
            text = text.replace("!sus!", self.murderer_choice.name).replace("!wep!", self.murder_weapon_choice.name)
            return text, choices

        def no():
            choices = self.base_actions
            text = "You're not sure. You better gather more evidence."
            return text, choices

        choices = [yes, no]
        return text, choices
    
    def start(self):
        text = self.introduction
        self.base_actions = [self.look_around, self.search, self.move, self.talk, self.accuse]
        choices = self.base_actions
        return text, choices
        
