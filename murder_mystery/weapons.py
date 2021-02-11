from .rooms import Room

class Weapon():
    is_the_murder_weapon = False
    location = Room
    def __init__(self, model, game):
        self.game = game
        for k, v in model.items():
            setattr(self, k, v)

    def pick_as_murder_weapon(self):
        choices = [self.game.end]
        text = "You identify %s as the murder weapon." % self.name
        self.game.murder_weapon_choice = self
        return text, choices

knife = {
    "name": "knife",
    "description": "This is the description of a knife.",
    "body_evidence": "There is a single deep stab wound to the man's chest. Right through the heart.",
    "hiding_place_evidence": "",
    "suspect_evidence": "!pos! hand is wrapped in a heavy white bandage. It seems like it could be a pretty nasty injury.",
}

