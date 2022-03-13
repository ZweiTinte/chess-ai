# coding: utf-8

# unit power values
PAWN = 1
ROOK = 2
KNIGHT = 3
BISHOPL = 4
BISHOPR = 5
QUEEN = 6
KING = 7

CASTLING_LEFT = "cl"
CASTLING_RIGHT = "cr"

class Unit:
    def __init__(self, power, owner):
        # setting owner of the unit (black | white)
        self.owner = owner
        self.power = power
        self.moves = []
        # special pawn move
        self.isPassantUnit = False
        # rook castling variable
        self.moved = False

    # add a move to the list
    def addMove(self, move):
        self.moves.append(move)

    def addMoveByPosition(self, x, y):
        self.addMove(str(x) + str(y))

    # returns the power of a unit as word
    def getPowerString(self):
        if self.power == 1:
            return "pawn"
        elif self.power == 2:
            return "rook"
        elif self.power == 3:
            return "knight"
        elif self.power == 4:
            return "bishop"
        elif self.power == 5:
            return "bishop"
        elif self.power == 6:
            return "queen"
        elif self.power == 7:
            return "king"
        else:
            return "ERROR"

    # resets the moves array
    def resetMoves(self):
        self.moves = []

    # getter and setter
    def getMoves(self):
        return self.moves

    def setMoves(self, moves):
        self.moves = moves

    def getPower(self):
        return self.power

    def setPower(self, power):
        self.power = power

    def isInGame(self):
        return self.inGame

    def setInGame(self, inGame):
        self.inGame = inGame
