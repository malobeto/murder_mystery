from rooms import Room

class Weapon():
    is_the_murder_weapon = False
    location = Room
    def __init__(self, model):
        for k, v in model.items():
            setattr(self, k, v)

knife = {
    "name": "knife",
    "description": "This is the description of a knife.",
    "body_evidence": "There is a single deep stab wound to the man's chest. Right through the heart.",
    "hiding_place_evidence": "",
    "suspect_evidence": " hand is wrapped in a heavy white bandage. It seems like it could be a pretty nasty injury.",
}

weapons_master_list = [Weapon(knife)]