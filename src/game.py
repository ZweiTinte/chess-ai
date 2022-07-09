# coding: utf-8
import os.path
from src.player import *
from src.unit import *
from src.log import *
from src.databaseLocationString import generateDatabaseLocationString
from src.database import loadData, writeData
from src.moveCalculations.moveCalculations import calculatePossibleMoves

class Game:
    def __init__(self):
        # setting players
        self.white = Player("white")
        self.black = Player("black")
        self.white.opponent = self.black
        self.black.opponent = self.white
        # border limit
        self.upperLimit = 8
        self.lowerLimit = 0
        # when a game reaches this limit, both players lose
        self.noHitTurnsLimit = 20
        self.resetGame()

    # resets the game
    def resetGame(self):
        # generating the board
        self.board = self.generateBoard()
        # placing the units on the board
        self.setUnits()
        # a counter for turns in a row without any hit
        self.noHitTurns = 0
        # reset moves and situations
        self.white.reset()
        self.black.reset()
        # who's turn is it?
        self.turn = self.white

    # returns a unit's position
    def getUnitPosition(self, unitString):
        unitNumber = 1
        for x in range(self.upperLimit):
            for y in range(self.upperLimit):
                if self.board[x][y] != None:
                    unit = self.board[x][y]
                    if unit.owner == self.turn:
                        if unit.power == int(unitString[0]):
                            if unitNumber == int(unitString[2]):
                                return [x, y]
                            else:
                                unitNumber += 1

    # ends the game and increments the win loss chances
    def endGame(self, winner):
        # increment winners win values
        for i in range(len(winner.moves)):
            unit = winner.moves[i][0]
            move = winner.moves[i][1]
            state = winner.situations[i]
            self.incrementMoveChance(unit, move, True, state)
        # increment losers loss values
        for i in range(len(winner.opponent.moves)):
            unit = winner.opponent.moves[i][0]
            move = winner.opponent.moves[i][1]
            state = winner.opponent.situations[i]
            self.incrementMoveChance(unit, move, False, state)

    # resets the passant possible units of the turn player
    def resetPassantPossible(self):
        for x in range(8):
            for y in range(8):
                unit = self.board[x][y]
                if unit != None:
                    if unit.power == PAWN:
                        if unit.owner == self.turn:
                            unit.isPassantUnit = False

    # checks if the json file for this turn already exists or not
    def jsonFileExists(self):
        dbLocationString = generateDatabaseLocationString(self)
        if not os.path.exists(dbLocationString):
            return False
        return True

    # resets the possible moves of all turn player units
    def resetPossibleMoves(self):
        for x in range(8):
            for y in range(8):
                if self.board[x][y] != None:
                    if self.board[x][y].owner == self.turn:
                        self.board[x][y].resetMoves()

    # returns True if the move/state combination already exists for this game
    def situationWithMoveAlreadyExists(self, situation, move):
        for s in range(len(self.turn.situations)):
                if self.turn.situations[s] == situation:
                    if self.turn.moves[s] == move:
                        return True

    # makes a turn
    def makeATurn(self):
        # prepare the possible moves file if it doesn't exist
        self.resetPossibleMoves()
        self.resetPassantPossible()
        calculatePossibleMoves(self, self.turn, True)
        if not self.jsonFileExists():
            self.writeUnitMovesToFile(self.turn)
        # add move and situation for the learning process
        dbLocationString = generateDatabaseLocationString(self)
        bestMove = self.getBestMove()
        if not self.situationWithMoveAlreadyExists(dbLocationString, bestMove):
            self.turn.addSituation(dbLocationString)
            self.turn.addMove(bestMove)
        # make the best move for the turn
        self.moveUnit()
        # set the opponent player as turn
        self.turn = self.turn.opponent

    # returns the character for the field number (A1, C5...)
    def getCharacterOfNumber(self, number):
        if number == 0:
            return "A"
        elif number == 1:
            return "B"
        elif number == 2:
            return "C"
        elif number == 3:
            return "D"
        elif number == 4:
            return "E"
        elif number == 5:
            return "F"
        elif number == 6:
            return "G"
        elif number == 7:
            return "H"

    # increases the counter of turns without hits
    def increaseNoHitCounter(self):
        self.noHitTurns += 1

    # resets the counter of turns without hits
    def resetNoHitTurns(self):
        self.noHitTurns = 0

    # moves a unit
    def moveUnit(self):
        move = self.getBestMove()
        unitPosition = self.getUnitPosition(move[0])
        upx = unitPosition[0]
        upy = unitPosition[1]
        x = move[1][0]
        y = move[1][1]

        logPossibleMoves(self, upx, upy)
        logMoveableUnits(self)

        # en passant move setup
        if x == "p":
            if y == "l":
                x = upx - 1
            else:
                x = upx + 1
            if self.turn == self.black:
                y = upy - 1
            else:
                y = upy + 1
            # remove opponent pawn from the board
            self.board[x][upy] = None
        # castling move setup
        elif x == "c":
            if y == "l":
                x = upx - 2
                # move the rook
                if self.turn.color == "black":
                    self.board[3][7] = self.board[0][7]
                    self.board[0][7] = None
                else:
                    self.board[3][0] = self.board[0][0]
                    self.board[0][0] = None
            else:
                x = upx + 2
                # move the rook
                if self.turn.color == "black":
                    self.board[5][7] = self.board[7][7]
                    self.board[7][7] = None
                else:
                    self.board[5][0] = self.board[7][0]
                    self.board[7][0] = None
            # disallow castling for the rest of the match
            self.turn.castling_permitted = False
            y = upy
        # set up the target coordinates
        else:
            x = int(x)
            y = int(y)

        # log the move to the console
        logMove(self, upx, upy, x, y)

        if self.board[x][y] != None:
            self.resetNoHitTurns()
            # king is target
            if self.board[x][y].power == 7:
                self.endGame(self.turn)
        else:
            # increase no hit counter of the game
            self.increaseNoHitCounter()
            # if the counter reaches the limit, the game ends
            if self.noHitTurns == self.noHitTurnsLimit:
                self.endGame(self.turn)
                self.endGame(self.turn.opponent)

        # set the rook/king variable for castling conditions to True
        if self.board[upx][upy].power in (ROOK, KING):
            self.board[upx][upy].moved = True

        # sets our own unit to the target field
        self.board[x][y] = self.board[upx][upy]

        # removes our unit from the previous field
        self.board[upx][upy] = None

        # pawn promotion
        if self.board[x][y].owner == self.white:
            promotionRow = self.upperLimit - 1
        else:
            promotionRow = self.lowerLimit
        if self.board[x][y].power == 1 and y == promotionRow:
            self.board[x][y] = Unit(int(move[1][2]), self.turn)

        # log the board to the console
        logBoard(self)

        # update en passant
        self.setEnPassant(move, x, y, upy)

    # sets passant variable True for opponent pawns nextby
    def setEnPassant(self, move, x, y, upy):
        if move[0][0] == str(PAWN):
            if (self.turn == self.white and y == upy + 2) or (self.turn == self.black and y == upy - 2):
                # passant right
                if x > self.lowerLimit:
                    opponentUnit = self.board[x - 1][y]
                    if opponentUnit != None:
                        if opponentUnit.owner == self.turn.opponent:
                            self.board[x][y].isPassantUnit = True
                # passant left
                if x + 1 < self.upperLimit:
                    opponentUnit = self.board[x + 1][y]
                    if opponentUnit != None:
                        if opponentUnit.owner == self.turn.opponent:
                            self.board[x][y].isPassantUnit = True

    # increments the win or loss value of a move in the json file
    def incrementMoveChance(self, unit, move, win, jsonFileString):
        data = loadData(jsonFileString)
        if win:
            data[unit][move]["w"] += 1
        else:
            data[unit][move]["l"] += 1
        # reduce json file size with dividing by 2
        while data[unit][move]["l"] % 2 == 0 and data[unit][move]["w"] % 2 == 0:
            data[unit][move]["l"] /= 2
            data[unit][move]["w"] /= 2
        # update the json file
        writeData(jsonFileString, data)

    # returns the move with best win/loss chance
    def getBestMove(self):
        jsonFileString = generateDatabaseLocationString(self)
        data = loadData(jsonFileString)
        move = ""
        chance = 0
        unit = ""
        for u in data:
            for m in data[u]:
                moveChance = data[u][m]["w"] / \
                    (data[u][m]["w"] + data[u][m]["l"])
                if moveChance > chance:
                    chance = moveChance
                    unit = u
                    move = m
        result = [unit, move]
        return result

    # writes the possible moves to a json file
    def writeUnitMovesToFile(self, player):
        jsonFileString = generateDatabaseLocationString(self)
        data = {}
        # Go through all unit types and write the moves to the file
        for u in range(PAWN, KING + 1):
            unitNumber = 1
            for x in range(self.upperLimit):
                for y in range(self.upperLimit):
                    if not self.fieldIsEmpty(x, y):
                        unit = self.board[x][y]
                        if unit.owner == player:
                            if unit.power == u:
                                if len(unit.moves) != 0:
                                    jsonUnitString = str(u) + "_" + str(unitNumber)
                                    data[jsonUnitString] = {}
                                    for m in unit.moves:
                                        data[jsonUnitString][str(m)] = {}
                                        data[jsonUnitString][str(m)]["w"] = 1
                                        data[jsonUnitString][str(m)]["l"] = 1
                                unitNumber += 1
        # write the data to a json file
        writeData(jsonFileString, data)

    # checks if a field of the chess board is empty
    def fieldIsEmpty(self, x, y):
        return True if self.board[x][y] == None else False

    # adds promotion moves to a unit
    def addPromotionMovesToUnit(self, unit, x, y):
        unit.addMove(str(x) + str(y) + "6")
        unit.addMove(str(x) + str(y) + "3")

    # starts the game
    def start(self):
        logToFile("\n--- NEW GAME ---")
        # using a number because we're still in test
        turns = 0
        while True:
            self.makeATurn()
            turns += 1
            if turns == 50:
                break
        logToFile("--- GAME END ---")

    # generates a blank chess board
    def generateBoard(self):
        return [[None for _ in range(self.upperLimit)] for _ in range(self.upperLimit)]

    # sets units on the board
    def setUnits(self):
        # black pawns
        for x in range(8):
            self.setUnitOnBoard(x, 6, Unit(PAWN, self.black))
        # white pawns
        for x in range(8):
            self.setUnitOnBoard(x, 1, Unit(PAWN, self.white))
        # black rooks
        self.setUnitOnBoard(0, 7, Unit(ROOK, self.black))
        self.setUnitOnBoard(7, 7, Unit(ROOK, self.black))
        # white rooks
        self.setUnitOnBoard(0, 0, Unit(ROOK, self.white))
        self.setUnitOnBoard(7, 0, Unit(ROOK, self.white))
        # black knights
        self.setUnitOnBoard(1, 7, Unit(KNIGHT, self.black))
        self.setUnitOnBoard(6, 7, Unit(KNIGHT, self.black))
        # white knights
        self.setUnitOnBoard(1, 0, Unit(KNIGHT, self.white))
        self.setUnitOnBoard(6, 0, Unit(KNIGHT, self.white))
        # black bishops
        self.setUnitOnBoard(2, 7, Unit(BISHOPR, self.black))
        self.setUnitOnBoard(5, 7, Unit(BISHOPL, self.black))
        # white bishops
        self.setUnitOnBoard(2, 0, Unit(BISHOPL, self.white))
        self.setUnitOnBoard(5, 0, Unit(BISHOPR, self.white))
        # black queen
        self.setUnitOnBoard(3, 7, Unit(QUEEN, self.black))
        # white queen
        self.setUnitOnBoard(3, 0, Unit(QUEEN, self.white))
        # black king
        self.setUnitOnBoard(4, 7, Unit(KING, self.black))
        # white king
        self.setUnitOnBoard(4, 0, Unit(KING, self.white))

    # clears the board
    def clearBoard(self):
        for x in range(self.upperLimit):
            for y in range(self.upperLimit):
                self.board[x][y] = None
    
    # sets a unit on the chess board
    def setUnitOnBoard(self, posX, posY, unit):
        self.board[posX][posY] = unit

    def getPositionOfUnit(self, unit):
        for x in range(self.upperLimit):
            for y in range(self.upperLimit):
                field = self.board[x][y]
                if not self.fieldIsEmpty(x, y) and field == unit:
                    return (x, y)