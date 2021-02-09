class Room():
    dead_body = False

    def __init__(self, model, game):
        self.game = game
        self.items = []
        self.hidden_items = []
        self.characters_present = []
        for k, v in model.items():
            setattr(self, k, v)

    def move_to(self):
        self.game.investigator.location = self
        text = "You move to %s." % self.name
        choices = game.base_actions
        return text, choices

library = {
    "name": "library",
    "description": "This is a classic library.",
    "hiding_spot": "Shoved behind a row of books",
}

kitchen = {
    "name": "kitchen",
    "description": "This kitchen looks like a dangerous place.",
    "hiding_spot": "Burried in the ice tray in the freezer.",
}


rooms_master_list = [Room(library), Room(kitchen)]