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

    # returns the players king position
    def getKingPosition(self, board):
        for x in range(8):
            for y in range(8):
                if board[x][y] != None:
                    unit = board[x][y]
                    if unit.getPower() == 7 and unit.getOwner() == self.color:
                        move_string = str(x) + str(y)
                        return move_string

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
