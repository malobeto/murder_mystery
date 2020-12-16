from .rooms import Room
from .sentence_formatting import capitalize_first


class Investigator():
    location = Room
    notes = []
    inventory = []

    def take_note(self, note):
        self.notes.append(note)
        return "You scribbled down a note in your notepad."
    
    def read_notes(self):
        for note in self.notes:
            pirnt("%s\n" % note)
        return "That's the end of your notes."

class Suspect():
    is_the_murderer = False
    location = Room
    def __init__(self, model):
        for k, v in model.items():
            setattr(self, k, v)
    
    def insert_pronouns(self, string):
        new_string = string.replace("!sub!", self.pronouns[0]).replace("!obj!", self.pronouns[1]).replace("!posadj!", self.pronouns[2]).replace("!pos!", self.pronouns[3]).replace("!ref!", self.pronouns[4])
        return capitalize_first(new_string)


miss_scarlett = {
    "name": "Miss Scarlett",
    "pronouns": ["she", "her", "her", "hers", "herself"],
    "description": "Next to the window stands a beautiful woman in red.",
    "weapon_evidence": "If you look closely you can see flecks of red fingernail polish.",
    "body_evidence": "There is a smudge of red lipstick on the man's lip.",
    "introduction": "The woman in red greets you with a dismissive smile and a half glance.",
    "replacement_detail": "gloves are covered in a dusting of some kind of fine powder. Your keen eyes barely manage to detect it.",
    "intro_end": "\"I suppose you'll have to question all of us detective. Well let's get it on with.\"",
    "questions": ["question1", "question2"],
    "responses": ["response1", "response2"]
}

colonel_mustard = {
    "name": "Colonel Mustard",
    "pronouns": ["he", "him", "his", "his", "himself"],
    "description": "In a large comfortable chair there sits an older man in millitary attire.",
    "weapon_evidence": "It smells strongly of pipe tobbaco.",
    "body_evidence": "This man was killed with millitary efficiency.",
    "introduction": "Colonel intro",
    "replacement_detail": "detail",
    "intro_end": "end",
    "questions": ["question1", "question2"],
    "responses": ["response1", "response2"]
}

professor_plum = {
    "name": "Professor Plum",
    "pronouns": ["he", "him", "his", "his", "himself"],
    "description": "In the corner stands a professor with a book open.",
    "weapon_evidence": "It is engraved with the insignia of a prominant college.",
    "body_evidence": "The murderer clearly knew how to kill in theory but perhaps not in practice.",
    "introduction": "",
    "replacement_detail": "",
    "intro_end": "",
    "questions": ["question1", "question2"],
    "responses": ["response1", "response2"]
}

suspects_master_list = [Suspect(miss_scarlett), Suspect(colonel_mustard), Suspect(professor_plum)]