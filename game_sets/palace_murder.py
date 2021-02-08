introduction = "This should be the opening lines of your mystery."

characters = [
    {
        "name": "the name of the character",
        "description": "This is a brief description that will pop up when the investigator first enters a room they are in",
        "weapon_evidence": "This is the evidence that they will leave on the weapon",
        "body_evidence": "This is the evidence that they will leave on the body",
        "introduction": "This is an introduction used when the you first talk to the character.",
        "replacement_detail": "This is a detail that is inserted between the two intro halves if the character is not the murderer. Make sure it makes sense with the rest of the sentence.",
        "intro_end": "This is the end of the intro and the start of your conversation with the character. Use \" to make quotation marks inside the string quotes.",
        "questions": [
            "These are questions you may ask this character",
            "They should be lined up so the first question gets the first response",
            ],
        "responses": [
            "These are responses to the questions",
            "For instance this will be how the suspect replies to the second question"
            ]
    },
]

weapons = [
    {
        "name": "the name of the weapon",
        "description": "A short description of the weapon",
        "body_evidence": "This is the method of death that will indicate what sort of weapon you should be looking for",
        "suspect_evidence": "This is the evidence that the weapon will leave on the guilty suspect. Make sure it lines up gramatically with the replacement_detail",
    }
]

rooms = [
    {
        "name": "rame of the room",
        "description": "A description for when you enter a room.",
        "hiding_spot": "where items may be hidden in the room",
    }
]

good_end = "This is the outcome if you've guessed the murderer and the murder weapon correctly."
bad_end = "This is the ending if you missed both murderer and murder weapon."
missed_weapon_end = "This is the end if you missed the murder weapon but picked the right murderer"
missed_murderer_end = "This is the end if you accused the wrong person but found the right murder weapon"