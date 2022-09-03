# coding: utf-8
from app.log import logLearningProgress
from app.game import Game

TURN_LIMIT = 100
GAME_RUNS = 1

def runAILearning(runs=GAME_RUNS):
    games = 0
    while games < runs:
        game = Game()
        game.start(TURN_LIMIT)
        games += 1

runAILearning(1)

# print the learning progress of the AI to the console
#logLearningProgress()