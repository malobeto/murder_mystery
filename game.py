from random import choice
from rooms import rooms_master_list
from characters import suspects_master_list, Investigator
from weapons import weapons_master_list

class Game:
    def __init__(self):
        self.introduction = """There has been a murder at the old spooky mansion and you have been called in to investigate. The suspects have been ordered to stay where they are and the murder weapon has yet to be found."""
        self.rooms = rooms_master_list
        self.suspects = suspects_master_list
        self.weapons = weapons_master_list
        self.murderer = choice(suspects_master_list)
        self.murder_weapon = choice(weapons_master_list)
        self.murder_room = choice(rooms_master_list)
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
    
    def look_around(self):
        room = self.investigator.location
        print(room.description + "\n")
        for suspect in room.characters_present:
            print(suspect.description + "\n")
        if room.dead_body:
            print("And in the center of the room there is a dead body.")
            choice = input("Would you like to take a closer look? Yes or no?")
            if choice.lower() == "yes":
                self.inspect_body()
            else:
                print("Ew gross who wants to see a dead body?!")
    
    def inspect_body(self):
        weapon_evidence = self.murder_weapon.body_evidence
        suspect_evidence = self.murderer.body_evidence
        print("The dead body lying in the center of the room has not been dead long. %s %s" % (weapon_evidence, suspect_evidence))

    def search(self):
        room = self.investigator.location
        for weapon in room.items:
            print("You find a %s. %s/n" % (weapon.name, weapon.description))
            self.investigator.inventory.append(weapon)
        for weapon in room.hidden_items:
            print("%s you find a %s. %s %s" % (room.hiding_spot, weapon.name, weapon.description, self.murderer.weapon_evidence))
            self.investigator.inventory.append(weapon)

    def move(self):
        r = 0
        for room in self.rooms:
            print("%d. %s" % (r, room.name))
            r += 1
        choice = int(input("Where to?"))
        self.investigator.location = self.rooms[choice]
        print("You move to the %s." % self.investigator.location.name)

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
            description = talking_to.introduction + self.murder_weapon.suspect_evidence + talking_to.intro_end
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
                print("You leave %s to their own designs." % talking_to.name)
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
            if confirm == "Yes":
                self.end(suspect_accused, weapon_accused)
            else:
                print("It's too early to say for sure yet.")

    def end(self, suspect, weapon):
        self.playing = False
        if suspect.is_the_murderer and weapon.is_the_murder_weapon:
            ending = "Congratulations! You solved the mystery! %s is arrested and convicted of murder!" % (suspect.name)
        elif suspect.is_the_murderer and weapon.is_the_murder_weapon == False:
            ending = """You accuse %s, and they are arrested and taken away. However during trial is able to soundly disprove that
            %s was the weapon used. %s is set free perhaps to kill again.""" % (suspect.name, weapon.name, suspect.name)
        elif suspect.is_the_murderer == False and weapon.is_the_murder_weapon:
            ending = """You accuse %s, and they are quickly arrested and taken away. During trail there are many hole's in the prosecution's story. 
            %s continues to deny their guilt. However with the murder weapon on display, and with a confident accusation of an experienced investigator 
            the jury votes guilty and puts %s away for life.""" % (suspect.name, suspect.name, suspect.name)
        elif suspect.is_the_murderer == False and weapon.is_the_murder == False:
            ending = """You accuse %s and take them away in handcuffs. Later that night your boss calls you to fire you for such a ridiculous accusation. 
            You are now being sued by %s""" % (suspect.name, suspect.name)
        print(ending)
    
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

new_game = Game()
new_game.main()