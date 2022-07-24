# coding: utf-8
from app.log import getAllDbFiles, logLearningProgress, printAllDbFiles
from app.game import Game

game = Game()
game.start()

# print the learning progress of the AI to the console
#logLearningProgress()