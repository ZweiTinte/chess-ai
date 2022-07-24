# coding: utf-8

from .unit import KING


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
                    if unit.power == KING and unit.owner == self:
                        return str(x) + str(y)

    # resets the player's game relevant attributes
    def reset(self):
        self.moves = []
        self.situations = []
        self.inCheck = False
        self.castling_permitted = True

    def addSituation(self, situation):
        self.situations.append(situation)

    def addMove(self, move):
        self.moves.append(move)
