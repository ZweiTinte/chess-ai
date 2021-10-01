# coding: utf-8
import os.path
from player import *
from unit import *
from log import *
from databaseLocationString import generateDatabaseLocationString
from database import loadData, writeData


class Game:
    def __init__(self):
        # setting players
        self.white = Player("white")
        self.black = Player("black")
        self.white.setOpponent(self.black)
        self.black.setOpponent(self.white)
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
    def getUnitPosition(self, unitString, color):
        unitNumber = 1
        for x in range(self.upperLimit):
            for y in range(self.upperLimit):
                if self.board[x][y] != None:
                    unit = self.board[x][y]
                    if unit.getOwner() == self.turn:
                        if unit.getPower() == int(unitString[0]):
                            if unitNumber == int(unitString[2]):
                                return [x, y]
                            else:
                                unitNumber += 1

    # ends the game and increments the win loss chances
    def endGame(self, winner):
        # increment winners win values
        for i in range(len(winner.getMoves())):
            unit = winner.getMoves()[i][0]
            move = winner.getMoves()[i][1]
            state = winner.getSituations()[i]
            self.incrementMoveChance(unit, move, True, state)
        # increment losers loss values
        for i in range(len(winner.getOpponent().getMoves())):
            unit = winner.getOpponent().getMoves()[i][0]
            move = winner.getOpponent().getMoves()[i][1]
            state = winner.getOpponent().getSituations()[i]
            self.incrementMoveChance(unit, move, False, state)

    # resets the passant possible variable for the pawns
    def resetPassantPossible(self):
        for x in range(8):
            for y in range(8):
                if self.board[x][y] != None:
                    if self.board[x][y].getPower() == 1:
                        if self.board[x][y].getOwner() == self.turn:
                            self.board[x][y].en_passant_possible = False

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
                    if self.board[x][y].getOwner() == self.turn:
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
        self.calculatePossibleMoves(self.turn, True)
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
        self.turn = self.turn.getOpponent()

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
        unitPosition = self.getUnitPosition(move[0], self.turn)
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
                if self.turn.getColor() == "black":
                    self.board[3][7] = self.board[0][7]
                    self.board[0][7] = None
                else:
                    self.board[3][0] = self.board[0][0]
                    self.board[0][0] = None
            else:
                x = upx + 2
                # move the rook
                if self.turn.getColor() == "black":
                    self.board[5][7] = self.board[7][7]
                    self.board[7][7] = None
                else:
                    self.board[5][0] = self.board[7][0]
                    self.board[7][0] = None
            # disallow castling for the rest of the match
            self.turn.setCastlingNotPermitted()
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
            if self.board[x][y].getPower() == 7:
                self.endGame(self.turn)
        else:
            # increase no hit counter of the game
            self.increaseNoHitCounter()
            # if the counter reaches the limit, the game ends
            if self.noHitTurns == self.noHitTurnsLimit:
                self.endGame(self.turn)
                self.endGame(self.turn.getOpponent())

        # set the rook varaiable for castling conditions to True
        if self.board[upx][upy].getPower() == 2:
            self.board[upx][upy].moved = True

        # sets our own unit to the target field
        self.board[x][y] = self.board[upx][upy]

        # removes our unit from the previous field
        self.board[upx][upy] = None

        # pawn promotion
        if self.board[x][y].getOwner() == self.white:
            promotionRow = self.upperLimit - 1
        else:
            promotionRow = self.lowerLimit
        if self.board[x][y].getPower() == 1 and y == promotionRow:
            self.board[x][y] = Unit(int(move[1][2]), self.turn)

        # log the board to the console
        logBoard(self)

        # reset passant possible variable for the turn player pawns
        self.resetPassantPossible()

        # sets passant variable True for opponent pawns nextby
        if move[0][0] == "1":
            if (self.turn == self.white and y == upy + 2) or (self.turn == self.black and y == upy - 2):
                if x - 1 > self.lowerLimit and self.board[x - 1][y] != None:
                    if self.board[x - 1][y].getOwner() == self.black:
                        self.board[x - 1][y].en_passant_possible = True
                if x + 1 < self.upperLimit and self.board[x + 1][y] != None:
                    if self.board[x + 1][y].getOwner() == self.black:
                        self.board[x + 1][y].en_passant_possible = True

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
                # test line
                # print(str(moveChance))
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
        for u in range(8):
            unitNumber = 1
            for x in range(self.upperLimit):
                for y in range(self.upperLimit):
                    if self.board[x][y] != None and self.board[x][y].getOwner() == player:
                        if self.board[x][y].getPower() == u:
                            if len(self.board[x][y].getMoves()) != 0:
                                jsonUnitString = str(u) + "_" + str(unitNumber)
                                data[jsonUnitString] = {}
                                for m in self.board[x][y].getMoves():
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

    # calculates the possible moves for all units of a player
    def calculatePossibleMoves(self, player, initialCall):
        for x in range(self.upperLimit):
            for y in range(self.upperLimit):
                unit = self.board[x][y]
                if unit != None and unit.getOwner() == player:
                    # pawn moves
                    if unit.getPower() == 1:
                        if player == self.white:
                            if y + 1 < self.upperLimit:
                                if self.fieldIsEmpty(x, y + 1):
                                    if y + 2 == self.upperLimit:
                                        self.addPromotionMovesToUnit(unit, x, y + 1)
                                    else:
                                        unit.addMove(str(x) + str(y + 1))
                                        if self.fieldIsEmpty(x, y + 2) and y == 1:
                                            unit.addMove(str(x) + str(y + 2))
                                if x - 1 >= self.lowerLimit and not self.fieldIsEmpty(x - 1, y + 1):
                                    if self.board[x - 1][y + 1].getOwner() == self.black:
                                        if y + 2 == self.upperLimit:
                                            self.addPromotionMovesToUnit(unit, x - 1, y + 1)
                                        else:
                                            unit.addMove(str(x - 1) + str(y + 1))
                                if x + 1 < self.upperLimit and not self.fieldIsEmpty(x + 1, y + 1):
                                    if self.board[x + 1][y + 1].getOwner() == self.black:
                                        if y + 2 == self.upperLimit:
                                            self.addPromotionMovesToUnit(unit, x + 1, y + 1)
                                        else:
                                            unit.addMove(str(x + 1) + str(y + 1))
                        elif player == self.black:
                            if y - 1 >= self.lowerLimit:
                                if self.fieldIsEmpty(x, y - 1):
                                    if y - 1 == self.lowerLimit:
                                        self.addPromotionMovesToUnit(unit, x, y - 1)
                                    else:
                                        unit.addMove(str(x) + str(y - 1))
                                        if self.fieldIsEmpty(x, y - 2) and y == 6:
                                            unit.addMove(str(x) + str(y - 2))
                                if x - 1 >= self.lowerLimit and not self.fieldIsEmpty(x - 1, y - 1):
                                    if self.board[x - 1][y - 1].getOwner() == self.white:
                                        if y - 1 == self.lowerLimit:
                                            self.addPromotionMovesToUnit(unit, x - 1, y - 1)
                                        else:
                                            unit.addMove(str(x - 1) + str(y - 1))
                                if x + 1 < self.upperLimit and not self.fieldIsEmpty(x + 1, y - 1):
                                    if self.board[x + 1][y - 1].getOwner() == self.white:
                                        if y - 1 == self.lowerLimit:
                                            self.addPromotionMovesToUnit(unit, x + 1, y - 1)
                                        else:
                                            unit.addMove(str(x + 1) + str(y - 1))
                        # en_passant calculation
                        if (y == 4 and self.board[x][y].getOwner() == self.white) or (y == 3 and self.board[x][y].getOwner() == self.black):
                            if x < 7:
                                if not self.fieldIsEmpty(x + 1, y):
                                    if self.board[x + 1][y].getPower() == 1:
                                        if self.board[x + 1][y].en_passant_possible:
                                            unit.addMove("pr")
                            if x > self.lowerLimit:
                                if not self.fieldIsEmpty(x - 1, y):
                                    if self.board[x - 1][y].getPower() == 1:
                                        if self.board[x - 1][y].en_passant_possible:
                                            unit.addMove("pl")
                    # rook moves
                    elif unit.getPower() == 2:
                        if y < self.upperLimit - 1:
                            for i in range(self.upperLimit - (y + 1)):
                                if self.fieldIsEmpty(x, y + i + 1):
                                    unit.addMove(str(x) + str(y + i + 1))
                                elif self.board[x][y + i + 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x) + str(y + i + 1))
                                    break
                                else:
                                    break
                        if y > self.lowerLimit:
                            for i in range(y):
                                if self.fieldIsEmpty(x, y - (i + 1)):
                                    unit.addMove(str(x) + str(y - i - 1))
                                elif self.board[x][y - (i + 1)].getOwner() == player.getOpponent():
                                    unit.addMove(str(x) + str(y - i - 1))
                                    break
                                else:
                                    break
                        if x < self.upperLimit - 1:
                            for i in range(self.upperLimit - (x + 1)):
                                if self.fieldIsEmpty(x + i + 1, y):
                                    unit.addMove(str(x + i + 1) + str(y))
                                elif self.board[x + i + 1][y].getOwner() == player.getOpponent():
                                    unit.addMove(str(x + i + 1) + str(y))
                                    break
                                else:
                                    break
                        if x > self.lowerLimit:
                            for i in range(x):
                                if self.fieldIsEmpty(x - (i + 1), y):
                                    unit.addMove(str(x - i - 1) + str(y))
                                elif self.board[x - (i + 1)][y].getOwner() == player.getOpponent():
                                    unit.addMove(str(x - i - 1) + str(y))
                                    break
                                else:
                                    break
                    # knight moves
                    elif unit.getPower() == 3:
                        if y < self.upperLimit - 1:
                            if x > 1:
                                if self.fieldIsEmpty(x - 2, y + 1):
                                    unit.addMove(str(x - 2) + str(y + 1))
                                elif self.board[x - 2][y + 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x - 2) + str(y + 1))
                            if x < 6:
                                if self.fieldIsEmpty(x + 2, y + 1):
                                    unit.addMove(str(x + 2) + str(y + 1))
                                elif self.board[x + 2][y + 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x + 2) + str(y + 1))
                            if y < self.upperLimit - 2:
                                if x > self.lowerLimit:
                                    if self.fieldIsEmpty(x - 1, y + 2):
                                        unit.addMove(str(x - 1) + str(y + 2))
                                    elif self.board[x - 1][y + 2].getOwner() == player.getOpponent():
                                        unit.addMove(str(x - 1) + str(y + 2))
                                if x < 7:
                                    if self.fieldIsEmpty(x + 1, y + 2):
                                        unit.addMove(str(x + 1) + str(y + 2))
                                    elif self.board[x + 1][y + 2].getOwner() == player.getOpponent():
                                        unit.addMove(str(x + 1) + str(y + 2))
                        if y > self.lowerLimit:
                            if x > 1:
                                if self.fieldIsEmpty(x - 2, y - 1):
                                    unit.addMove(str(x - 2) + str(y - 1))
                                elif self.board[x - 2][y - 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x - 2) + str(y - 1))
                            if x < 6:
                                if self.fieldIsEmpty(x + 2, y - 1):
                                    unit.addMove(str(x + 2) + str(y - 1))
                                elif self.board[x + 2][y - 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x + 2) + str(y - 1))
                            if y > 1:
                                if x > self.lowerLimit:
                                    if self.fieldIsEmpty(x - 1, y - 2):
                                        unit.addMove(str(x - 1) + str(y - 2))
                                    elif self.board[x - 1][y - 2].getOwner() == player.getOpponent():
                                        unit.addMove(str(x - 1) + str(y - 2))
                                if x < 7:
                                    if self.fieldIsEmpty(x + 1, y - 2):
                                        unit.addMove(str(x + 1) + str(y - 2))
                                    elif self.board[x + 1][y - 2].getOwner() == player.getOpponent():
                                        unit.addMove(str(x + 1) + str(y - 2))
                    # bishop moves
                    elif unit.getPower() == 4 or unit.getPower() == 5:
                        if y < 7:
                            for i in range(self.upperLimit - (y + 1)):
                                if y + i < self.upperLimit - 1 and x + i < self.upperLimit - 1:
                                    if self.fieldIsEmpty(x + i + 1, y + i + 1):
                                        unit.addMove(
                                            str(x + i + 1) + str(y + i + 1))
                                    elif self.board[x + i + 1][y + i + 1].getOwner() == player.getOpponent():
                                        unit.addMove(
                                            str(x + i + 1) + str(y + i + 1))
                                        break
                                    else:
                                        break
                            for i in range(self.upperLimit - (y + 1)):
                                if y + i < self.upperLimit - 1 and x - i > self.lowerLimit:
                                    if self.fieldIsEmpty(x - i - 1, y + i + 1):
                                        unit.addMove(
                                            str(x - i - 1) + str(y + i + 1))
                                    elif self.board[x - i - 1][y + i + 1].getOwner() == player.getOpponent():
                                        unit.addMove(
                                            str(x - i - 1) + str(y + i + 1))
                                        break
                                    else:
                                        break
                        if y > self.lowerLimit:
                            for i in range(y):
                                if y - i > self.lowerLimit and x + i < self.upperLimit - 1:
                                    if self.fieldIsEmpty(x + i + 1, y - i - 1):
                                        unit.addMove(
                                            str(x + i + 1) + str(y - i - 1))
                                    elif self.board[x + i + 1][y - i - 1].getOwner() == player.getOpponent():
                                        unit.addMove(
                                            str(x + i + 1) + str(y - i - 1))
                                        break
                                    else:
                                        break
                            for i in range(y):
                                if y - i > self.lowerLimit and x - i > self.lowerLimit:
                                    if self.fieldIsEmpty(x - i - 1, y - i - 1):
                                        unit.addMove(
                                            str(x - i - 1) + str(y - i - 1))
                                    elif self.board[x - i - 1][y - i - 1].getOwner() == player.getOpponent():
                                        unit.addMove(
                                            str(x - i - 1) + str(y - i - 1))
                                        break
                                    else:
                                        break
                    # queen moves
                    elif unit.getPower() == 6:
                        if y < 7:
                            for i in range(self.upperLimit - (y + 1)):
                                if y + i < self.upperLimit - 1 and x + i < self.upperLimit - 1:
                                    if self.fieldIsEmpty(x + i + 1, y + i + 1):
                                        unit.addMove(
                                            str(x + i + 1) + str(y + i + 1))
                                    elif self.board[x + i + 1][y + i + 1].getOwner() == player.getOpponent():
                                        unit.addMove(
                                            str(x + i + 1) + str(y + i + 1))
                                        break
                                    else:
                                        break
                            for i in range(self.upperLimit - (y + 1)):
                                if y + i < self.upperLimit - 1 and x - i > self.lowerLimit:
                                    if self.fieldIsEmpty(x - i - 1, y + i + 1):
                                        unit.addMove(
                                            str(x - i - 1) + str(y + i + 1))
                                    elif self.board[x - i - 1][y + i + 1].getOwner() == player.getOpponent():
                                        unit.addMove(
                                            str(x - i - 1) + str(y + i + 1))
                                        break
                                    else:
                                        break
                        if y > self.lowerLimit:
                            for i in range(y):
                                if y - i > self.lowerLimit and x + i < self.upperLimit - 1:
                                    if self.fieldIsEmpty(x + i + 1, y - i - 1):
                                        unit.addMove(
                                            str(x + i + 1) + str(y - i - 1))
                                    elif self.board[x + i + 1][y - i - 1].getOwner() == player.getOpponent():
                                        unit.addMove(
                                            str(x + i + 1) + str(y - i - 1))
                                        break
                                    else:
                                        break
                            for i in range(y):
                                if y - i > self.lowerLimit and x - i > self.lowerLimit:
                                    if self.fieldIsEmpty(x - i - 1, y - i - 1):
                                        unit.addMove(
                                            str(x - i - 1) + str(y - i - 1))
                                    elif self.board[x - i - 1][y - i - 1].getOwner() == player.getOpponent():
                                        unit.addMove(
                                            str(x - i - 1) + str(y - i - 1))
                                        break
                                    else:
                                        break
                        if y < 7:
                            for i in range(self.upperLimit - (y + 1)):
                                if self.fieldIsEmpty(x, y + i + 1):
                                    unit.addMove(str(x) + str(y + i + 1))
                                elif self.board[x][y + i + 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x) + str(y + i + 1))
                                    break
                                else:
                                    break
                        if y > self.lowerLimit:
                            for i in range(y):
                                if self.fieldIsEmpty(x, y - (i + 1)):
                                    unit.addMove(str(x) + str(y - i - 1))
                                elif self.board[x][y - (i + 1)].getOwner() == player.getOpponent():
                                    unit.addMove(str(x) + str(y - i - 1))
                                    break
                                else:
                                    break
                        if x < 7:
                            for i in range(self.upperLimit - (x + 1)):
                                if self.fieldIsEmpty(x + i + 1, y):
                                    unit.addMove(str(x + i + 1) + str(y))
                                elif self.board[x + i + 1][y].getOwner() == player.getOpponent():
                                    unit.addMove(str(x + i + 1) + str(y))
                                    break
                                else:
                                    break
                        if x > self.lowerLimit:
                            for i in range(x):
                                if self.fieldIsEmpty(x - (i + 1), y):
                                    unit.addMove(str(x - i - 1) + str(y))
                                elif self.board[x - (i + 1)][y].getOwner() == player.getOpponent():
                                    unit.addMove(str(x - i - 1) + str(y))
                                    break
                                else:
                                    break
                    # king moves
                    elif unit.getPower() == 7:
                        if y < 7:
                            if self.fieldIsEmpty(x, y + 1):
                                unit.addMove(str(x) + str(y + 1))
                            elif self.board[x][y + 1].getOwner() == player.getOpponent():
                                unit.addMove(str(x) + str(y + 1))
                            if x < self.upperLimit - 1:
                                if self.fieldIsEmpty(x + 1, y + 1):
                                    unit.addMove(str(x + 1) + str(y + 1))
                                elif self.board[x + 1][y + 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x + 1) + str(y + 1))
                            if x > self.lowerLimit:
                                if self.fieldIsEmpty(x - 1, y + 1):
                                    unit.addMove(str(x - 1) + str(y + 1))
                                elif self.board[x - 1][y + 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x - 1) + str(y + 1))
                        if y > self.lowerLimit:
                            if self.fieldIsEmpty(x, y - 1):
                                unit.addMove(str(x) + str(y - 1))
                            elif self.board[x][y - 1].getOwner() == player.getOpponent():
                                unit.addMove(str(x) + str(y - 1))
                            if x < self.upperLimit - 1:
                                if self.fieldIsEmpty(x + 1, y - 1):
                                    unit.addMove(str(x + 1) + str(y - 1))
                                elif self.board[x + 1][y - 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x + 1) + str(y - 1))
                            if x - i > self.lowerLimit:
                                if self.fieldIsEmpty(x - 1, y - 1):
                                    unit.addMove(str(x - 1) + str(y - 1))
                                elif self.board[x - 1][y - 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x - 1) + str(y - 1))
                        if x < self.upperLimit - 1:
                            if self.fieldIsEmpty(x + 1, y):
                                unit.addMove(str(x + 1) + str(y))
                            elif self.board[x + 1][y].getOwner() == player.getOpponent():
                                unit.addMove(str(x + 1) + str(y))
                        if x > self.lowerLimit:
                            if self.fieldIsEmpty(x - 1, y):
                                unit.addMove(str(x - 1) + str(y))
                            elif self.board[x - 1][y].getOwner() == player.getOpponent():
                                unit.addMove(str(x - 1) + str(y))
                        # castling calculation
                        if initialCall:
                            self.playerIsInCheck(player)
                            if not player.isInCheck() and player.castlingIsPermitted():
                                if player == self.black:
                                    if not self.fieldIsEmpty(self.lowerLimit, self.upperLimit - 1):
                                        if self.board[0][7].getPower() == 2:
                                            if not self.board[self.lowerLimit][self.upperLimit - 1].moved:
                                                if self.fieldIsEmpty(self.lowerLimit + 1, self.upperLimit - 1):
                                                    if self.fieldIsEmpty(self.lowerLimit + 2, self.upperLimit - 1):
                                                        if self.fieldIsEmpty(self.lowerLimit + 3, self.upperLimit - 1):
                                                            unit.addMove("cl")
                                    if not self.fieldIsEmpty(self.upperLimit - 1, self.upperLimit - 1):
                                        if self.board[self.upperLimit - 1][self.upperLimit - 1].getPower() == 2:
                                            if not self.board[self.upperLimit - 1][self.upperLimit - 1].moved:
                                                if self.fieldIsEmpty(self.upperLimit - 2, self.upperLimit - 1):
                                                    if self.fieldIsEmpty(self.upperLimit - 3, self.upperLimit - 1):
                                                        unit.addMove("cr")
                                elif player == self.white:
                                    if not self.fieldIsEmpty(self.lowerLimit, self.lowerLimit):
                                        if self.board[self.lowerLimit][self.lowerLimit].getPower() == 2:
                                            if not self.board[self.lowerLimit][self.lowerLimit].moved:
                                                if self.fieldIsEmpty(self.lowerLimit + 1, self.lowerLimit):
                                                    if self.fieldIsEmpty(self.lowerLimit + 2, self.lowerLimit):
                                                        if self.fieldIsEmpty(self.lowerLimit + 3, self.lowerLimit):
                                                            unit.addMove("cl")
                                    if not self.fieldIsEmpty(self.upperLimit - 1, self.lowerLimit):
                                        if self.board[self.upperLimit - 1][self.lowerLimit].getPower() == 2:
                                            if not self.board[self.upperLimit - 1][self.lowerLimit].moved:
                                                if self.fieldIsEmpty(self.upperLimit - 2, self.lowerLimit):
                                                    if self.fieldIsEmpty(self.upperLimit - 3, self.lowerLimit):
                                                        unit.addMove("cr")

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

    # return true if the player is in check
    def playerIsInCheck(self, player):
        self.calculatePossibleMoves(player.getOpponent(), False)
        king_position = player.getKingPosition(self.board)
        for x in range(self.upperLimit):
            for y in range(self.upperLimit):
                unit = self.board[x][y]
                if unit != None:
                    if unit.getOwner() == player.getOpponent():
                        for move in unit.getMoves():
                            if move == king_position:
                                player.setIsInCheck(True)
        player.setIsInCheck(False)

    # generates a blank chess board
    def generateBoard(self):
        board = []
        for x in range(self.upperLimit):
            board.append([])
            for _ in range(self.upperLimit):
                board[x].append(None)
        return board

    # sets units on the board
    def setUnits(self):
        # black pawns
        for x in range(8):
            self.board[x][6] = Unit(1, self.black)
        # white pawns
        for x in range(8):
            self.board[x][1] = Unit(1, self.white)
        # black rooks
        self.board[0][7] = Unit(2, self.black)
        self.board[7][7] = Unit(2, self.black)
        # white rooks
        self.board[0][0] = Unit(2, self.white)
        self.board[7][0] = Unit(2, self.white)
        # black knights
        self.board[1][7] = Unit(3, self.black)
        self.board[6][7] = Unit(3, self.black)
        # white knights
        self.board[1][0] = Unit(3, self.white)
        self.board[6][0] = Unit(3, self.white)
        # black bishops
        self.board[2][7] = Unit(5, self.black)
        self.board[5][7] = Unit(4, self.black)
        # white bishops
        self.board[2][0] = Unit(4, self.white)
        self.board[5][0] = Unit(5, self.white)
        # black queen
        self.board[3][7] = Unit(6, self.black)
        # white queen
        self.board[3][0] = Unit(6, self.white)
        # black king
        self.board[4][7] = Unit(7, self.black)
        # white king
        self.board[4][0] = Unit(7, self.white)