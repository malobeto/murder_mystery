import os
from pathlib import Path

from .game import Game

def new_game():
    path = Path('.\murder_mystery\game_sets')
    games = os.listdir(path)
    g = 0
    for game in games:
        print("%d. %s" % (g, game[:-5].title()))
        g += 1
    choice = int(input("Which set would you like to play with?"))
    new_game = Game(games[choice])
    new_game.main()
