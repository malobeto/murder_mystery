from os import listdir

from game.py import Game
from config import Config

def new_game():
    game_sets = listdir("game_sets")
    g = 0
    for game_set in game_sets:
        print("%d. %s" % (g, game_set[:-5].title()))
        g += 1
    choice = int(input("Which set would you like to play with?"))
    config = Config(game_sets[choice])
    new_game = Game(config)
    new_game.main()