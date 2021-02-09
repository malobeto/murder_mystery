from random import choice
from .characters import Investigator

class Game:
    def __init__(self, config):
        self.introduction = config.introduction
        self.rooms = config.rooms_master_list
        self.suspects = config.suspects_master_list
        self.weapons = config.weapons_master_list
        self.murderer = choice(config.suspects_master_list)
        self.murder_weapon = choice(config.weapons_master_list)
        self.murder_room = choice(config.rooms_master_list)
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
        self.playing = True
        self.good_end = config.good_end
        self.bad_end = config.bad_end
        self.missed_weapon_end = config.missed_weapon_end
        self.missed_murderer_end = config.missed_murderer_end
    
    def look_around(self):
        room = self.investigator.location
        text = room.description + "\n"
        for suspect in room.characters_present:
            text = text + suspect.description + "\n"
        if room.dead_body:
            text =  text + "And in the center of the room there is a dead body."
            text =  text + "Would you like to take a closer look? Yes or no?"

        def yes():
            weapon_evidence = self.murder_weapon.body_evidence
            suspect_evidence = self.murderer.body_evidence
            text = "The dead body lying in the center of the room has not been dead long. %s %s" % (weapon_evidence, suspect_evidence))
            choices = []
            return text, choices

        def no():
            text = "Ew gross who wants to see a dead body?!"
            choices = []
            return text, choices

        choices = [yes, no]
        return text, choices

    def search(self):
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
        choices = []
        return text, choices

    def move(self):
        current_location = self.investigator.location
        self.rooms.remove(current_location)
        r = 0
        for room in self.rooms:
            print("%d. %s" % (r, room.name))
            r += 1
        choice = int(input("Where to?"))
        self.investigator.location = self.rooms[choice]
        print("You move to the %s." % self.investigator.location.name)
        self.rooms.append(current_location)

    def talk(self):
        s = 0
        room = self.investigator.location
        if len(room.characters_present) == 0:
            print("There's no one here to talk to.")
            return 0
        for suspect in room.characters_present:
            print("%d. %s" % (s, suspect.name))
            s += 1
        choice = int(input("Who would you like to talk to?"))
        talking_to = room.characters_present[choice]
        if talking_to.is_the_murderer:
            description = talking_to.introduction + talking_to.insert_pronouns(self.murder_weapon.suspect_evidence) + talking_to.intro_end
        else:
            description = talking_to.introduction + talking_to.replacement_detail + talking_to.intro_end
        print(description)
        talking = True
        while talking:
            q = 0
            for question in talking_to.questions:
                print("%d. %s" % (q, question)) 
                q += 1
            print("%d. Leave" % q)
            choice = int(input("What do you ask?"))
            if choice == q:
                print(talking_to.insert_pronouns("You leave %s to !posadj! own designs." % talking_to.name))
                break
            else:
                print("%s you ask." % talking_to.questions[choice])
                print(talking_to.responses[choice])
    
    def accuse(self):
        s = 0
        room = self.investigator.location
        if len(room.characters_present) == 0:
            print("There's no one here to accuse!")
            return 0
        else:    
            for suspect in room.characters_present:
                print("%d. %s" % (s, suspect.name))
                s += 1
            suspect_choice = int(input("Who would you like to choose?"))
            suspect_accused = room.characters_present[suspect_choice]
        if len(self.investigator.inventory) == 0:
            print("You have not yet found any weapons.")
            return 0
        else:
            w = 0
            for weapon in self.investigator.inventory:
                print("%d. %s" % (w, weapon.name))
                w += 1
            weapon_choice = int(input("Which weapon did they do it with?"))
            weapon_accused = self.investigator.inventory[weapon_choice]
            print("Are you sure it was %s, with %s." % (suspect_accused.name, weapon_accused.name))
            confirm = input("Yes or no?")
            if confirm.lower() == "yes":
                self.end(suspect_accused, weapon_accused)
            else:
                print("It's too early to say for sure yet.")

    def end(self, suspect, weapon):
        self.playing = False
        if suspect.is_the_murderer and weapon.is_the_murder_weapon:
            ending =  self.good_end
        elif suspect.is_the_murderer and weapon.is_the_murder_weapon == False:
            ending =  self.missed_weapon_end
        elif suspect.is_the_murderer == False and weapon.is_the_murder_weapon:
            ending = self.missed_murderer_end
        elif suspect.is_the_murderer == False and weapon.is_the_murder_weapon == False:
            ending = self.bad_end
        print(ending.replace("!sus!", suspect.name).replace("!wep!", weapon.name))

    
    def main(self):
        print(self.introduction)
        room_actions = [self.look_around, self.search, self.move, self.talk, self.accuse]
        room_actions_names = ["Look Around", "Search", "Move", "Talk", "Accuse"]
        while self.playing:
            input()
            a = 0
            for action in room_actions_names:
                print("%d. %s" % (a, action))
                a += 1
            choice = int(input("What would you like to do?"))
            room_actions[choice]()

