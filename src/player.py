# coding: utf-8
from random import shuffle, randint
import sys
import json
import datetime


class Player:
    def __init__(self, color):
        # setting the color (black | white)
        self.color = color
        # sets the opoonent of the player
        self.opponent = None
        # castling booleans
        self.castling_permitted = True
        # True if the player is in check
        self.inCheck = False
        # stores each move made in the game
        self.moves = []
        # stores the board situations of the game
        self.situations = []

    # getter and setter
    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getOpponent(self):
        return self.opponent

    def isInCheck(self):
        return self.inCheck

    def setIsInCheck(self, isInCheck):
        self.inCheck = isInCheck

    def setOpponent(self, opponent):
        self.opponent = opponent

    def castlingIsPermitted(self):
        return self.castling_permitted

    def setCastlingNotPermitted(self):
        self.castling_permitted = False

    def getSituations(self):
        return self.situations

    def addSituation(self, situation):
        self.situations.append(situation)

    def getMoves(self):
        return self.moves

    def addMove(self, move):
        self.moves.append(move)
