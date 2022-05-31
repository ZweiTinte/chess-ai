# coding: utf-8
from src.game import Game

# Consider using a while loop instead...
for i in range(100000):
    game = Game()
    game.start()
    print("Game ", i, " finished")
