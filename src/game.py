# coding: utf-8
from random import shuffle, randint
import sys
import json
import datetime
import os.path
from player import *
from unit import *
from database import *


class Game:
    def __init__(self):
        # setting players
        self.white = Player("white")
        self.black = Player("black")
        self.white.setOpponent(self.black)
        self.black.setOpponent(self.white)
        # generating the board
        self.board = self.generateBoard()
        # placing the units on the board
        self.setUnits()
        # who's turn is it?
        self.turn = self.white
        # border limit
        self.limit = 8

    # returns a unit's position
    def getUnitPosition(self, unitString):
        unitNumber = 1
        for x in range(8):
            for y in range(8):
                field = self.board[x][y]
                if field != None:
                    if field.getPower() == unitString[0]:
                        if unitNumber == unitString[2]:
                            return [x, y]
                        unitNumber += 1

    # ends the game and increments the win loss chances
    def endGame(self, winner):
        print("not implemented yet!")

    # resets the passant possible variable for the pawns
    def resetPassantPossible(self):
        for x in range(8):
            for y in range(8):
                if self.board[x][y] != None:
                    if self.board[x][y].getPower() == 1:
                        if self.board[x][y].getOwner() == self.turn:
                            self.board[x][y].en_passant_possible = False

    # moves a unit
    def moveUnit(self):
        move = self.getBestMove()
        unitPosition = self.getUnitPosition(move[0])
        upx = int(unitPosition[0])
        upy = int(unitPosition[1])
        x = move[1][0]
        y = move[1][1]

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

        # the target field gets set
        targetField = self.board[x][y]

        if targetField != None:
            # king is target
            if targetField.getPower() == 7:
                self.endGame()

        # sets our own unit to the target field
        targetField = self.board[upx][upy]

        # removes our unit from the previous field
        self.board[upx][upy] = None

        # pawn promotion
        if targetField.getOwner() == self.white:
            promotionRow = self.limit - 1
        else:
            promotionRow = 0
        if targetField.getPower() == 1 and y == promotionRow:
            targetField = Unit(move[1][2], self.turn)

        # reset passant possible variable for the turn player pawns
        self.resetPassantPossible()

        # sets passant variable True for opponent pawns nextby
        if move[0][0] == "1":
            if (self.turn == self.white and y == upy + 2) or (self.turn == self.black and y == upy - 2):
                if self.board[x - 1][y] != None:
                    if self.board[x - 1][y].getOwner() == self.black:
                        self.board[x - 1][y].en_passant_possible = True
                if self.board[x + 1][y] != None:
                    if self.board[x + 1][y].getOwner() == self.black:
                        self.board[x + 1][y].en_passant_possible = True

    # increments the win or loss value of a move in the json file
    def incrementMoveChance(self, unit, move, win):
        jsonFileString = self.generateDatabaseLocationString()
        data = loadData(jsonFileString)
        if win:
            data[unit][move]["w"] += 1
        else:
            data[unit][move]["l"] += 1
        writeData(jsonFileString, data)

    # returns the move with best win/loss chance
    def getBestMove(self):
        jsonFileString = self.generateDatabaseLocationString()
        data = loadData(jsonFileString)
        move = ""
        chance = 0
        unit = ""
        for u in data:
            for m in data[u]:
                moveChance = data[u][m]["w"] / \
                    (data[u][m]["w"] + data[u][m]["l"])
                # test line
                print(str(moveChance))
                if moveChance > chance:
                    chance = moveChance
                    unit = u
                    move = m
        result = [unit, move]
        return result

    # writes the possible moves to a json file
    def writeUnitMovesToFile(self, player):
        jsonFileString = self.generateDatabaseLocationString()
        data = {}
        # Go through all unit types and write the moves to the file
        for u in range(7):
            unitNumber = 1
            for x in range(self.limit):
                for y in range(self.limit):
                    if self.board[x][y] != None and self.board[x][y].getOwner() == player:
                        if self.board[x][y].getPower() == u:
                            jsonUnitString = str(u) + "_" + str(unitNumber)
                            data[jsonUnitString] = {}
                            for m in self.board[x][y].getMoves():
                                data[jsonUnitString][str(m)] = {}
                                data[jsonUnitString][str(m)]["w"] = 1
                                data[jsonUnitString][str(m)]["l"] = 1
                            unitNumber += 1
        # write the data to a json file
        writeData(jsonFileString, data)

    # calculates the possible moves for all units of a player

    def calculatePossibleMoves(self, player, initialCall):
        for x in range(self.limit):
            for y in range(self.limit):
                unit = self.board[x][y]
                if unit != None and unit.getOwner() == player:
                    # pawn moves
                    if unit.getPower() == 1:
                        if player == self.white:
                            if y + 1 < self.limit:
                                if self.board[x][y + 1] == None:
                                    if y + 2 == self.limit:
                                        unit.addMove(str(x) + str(y + 1) + "6")
                                        unit.addMove(str(x) + str(y + 1) + "3")
                                    else:
                                        unit.addMove(str(x) + str(y + 1))
                                        if self.board[x][y + 2] == None and y == 1:
                                            unit.addMove(str(x) + str(y + 2))
                                if x - 1 >= 0 and self.board[x - 1][y + 1] != None and self.board[x - 1][y + 1].getOwner() == self.black:
                                    if y + 2 == self.limit:
                                        unit.addMove(str(x) + str(y + 1) + "6")
                                        unit.addMove(str(x) + str(y + 1) + "3")
                                    else:
                                        unit.addMove(str(x - 1) + str(y + 1))
                                if x + 1 < self.limit and self.board[x + 1][y + 1] != None and self.board[x + 1][y + 1].getOwner() == self.black:
                                    if y + 2 == self.limit:
                                        unit.addMove(str(x) + str(y + 1) + "6")
                                        unit.addMove(str(x) + str(y + 1) + "3")
                                    else:
                                        unit.addMove(str(x + 1) + str(y + 1))
                        elif player == self.black:
                            if y - 1 >= 0:
                                if self.board[x][y - 1] == None:
                                    if y - 1 == 0:
                                        unit.addMove(str(x) + str(y - 1) + "6")
                                        unit.addMove(str(x) + str(y - 1) + "3")
                                    else:
                                        unit.addMove(str(x) + str(y - 1))
                                        if self.board[x][y - 2] == None and y == 6:
                                            unit.addMove(str(x) + str(y - 2))
                                if x - 1 >= 0 and self.board[x - 1][y - 1] != None and self.board[x - 1][y - 1].getOwner() == self.white:
                                    if y - 1 == 0:
                                        unit.addMove(str(x) + str(y - 1) + "6")
                                        unit.addMove(str(x) + str(y - 1) + "3")
                                    else:
                                        unit.addMove(str(x - 1) + str(y - 1))
                                if x + 1 < self.limit and self.board[x + 1][y - 1] != None and self.board[x + 1][y - 1].getOwner() == self.white:
                                    if y - 1 == 0:
                                        unit.addMove(str(x) + str(y - 1) + "6")
                                        unit.addMove(str(x) + str(y - 1) + "3")
                                    else:
                                        unit.addMove(str(x + 1) + str(y - 1))
                        # en_passant calculation
                        if (y == 4 and self.board[x][y].getOwner() == self.white) or (y == 3 and self.board[x][y].getOwner() == self.black):
                            if x < 7:
                                if self.board[x + 1][y] != None and self.board[x + 1][y].getPower() == 1 and self.board[x + 1][y].en_passant_pssible:
                                    unit.addMove("pr")
                            if x > 0:
                                if self.board[x - 1][y] != None and self.board[x - 1][y].getPower() == 1 and self.board[x - 1][y].en_passant_pssible:
                                    unit.addMove("pl")
                    # rook moves
                    elif unit.getPower() == 2:
                        if y < self.limit - 1:
                            for i in range(self.limit - (y + 1)):
                                if self.board[x][y + i + 1] == None:
                                    unit.addMove(str(x) + str(y + i + 1))
                                elif self.board[x][y + i + 1] != None and self.board[x][y + i + 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x) + str(y + i + 1))
                                    break
                                else:
                                    break
                        if y > 0:
                            for i in range(y):
                                if self.board[x][y - (i + 1)] == None:
                                    unit.addMove(str(x) + str(y - i - 1))
                                elif self.board[x][y - (i + 1)] != None and self.board[x][y - (i + 1)].getOwner() == player.getOpponent():
                                    unit.addMove(str(x) + str(y - i - 1))
                                    break
                                else:
                                    break
                        if x < self.limit - 1:
                            for i in range(self.limit - (x + 1)):
                                if self.board[x + i + 1][y] == None:
                                    unit.addMove(str(x + i + 1) + str(y))
                                elif self.board[x + i + 1][y] != None and self.board[x + i + 1][y].getOwner() == player.getOpponent():
                                    unit.addMove(str(x + i + 1) + str(y))
                                    break
                                else:
                                    break
                        if x > 0:
                            for i in range(x):
                                if self.board[x - (i + 1)][y] == None:
                                    unit.addMove(str(x - i - 1) + str(y))
                                elif self.board[x - (i + 1)][y] != None and self.board[x - (i + 1)][y].getOwner() == player.getOpponent():
                                    unit.addMove(str(x - i - 1) + str(y))
                                    break
                                else:
                                    break
                    # knight moves
                    elif unit.getPower() == 3:
                        if y < self.limit - 1:
                            if x > 1:
                                if self.board[x - 2][y + 1] == None:
                                    unit.addMove(str(x - 2) + str(y + 1))
                                elif self.board[x - 2][y + 1] != None and self.board[x - 2][y + 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x - 2) + str(y + 1))
                            if x < 6:
                                if self.board[x + 2][y + 1] == None:
                                    unit.addMove(str(x + 2) + str(y + 1))
                                elif self.board[x + 2][y + 1] != None and self.board[x + 2][y + 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x + 2) + str(y + 1))
                            if y < self.limit - 2:
                                if x > 0:
                                    if self.board[x - 1][y + 2] == None:
                                        unit.addMove(str(x - 1) + str(y + 2))
                                    elif self.board[x - 1][y + 2] != None and self.board[x - 1][y + 2].getOwner() == player.getOpponent():
                                        unit.addMove(str(x - 1) + str(y + 2))
                                if x < 7:
                                    if self.board[x + 1][y + 2] == None:
                                        unit.addMove(str(x + 1) + str(y + 2))
                                    elif self.board[x + 1][y + 2] != None and self.board[x + 1][y + 2].getOwner() == player.getOpponent():
                                        unit.addMove(str(x + 1) + str(y + 2))
                        if y > 0:
                            if x > 1:
                                if self.board[x - 2][y - 1] == None:
                                    unit.addMove(str(x - 2) + str(y - 1))
                                elif self.board[x - 2][y - 1] != None and self.board[x - 2][y - 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x - 2) + str(y - 1))
                            if x < 6:
                                if self.board[x + 2][y - 1] == None:
                                    unit.addMove(str(x + 2) + str(y + 1))
                                elif self.board[x + 2][y - 1] != None and self.board[x + 2][y - 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x + 2) + str(y - 1))
                            if y > 1:
                                if x > 0:
                                    if self.board[x - 1][y - 2] == None:
                                        unit.addMove(str(x - 1) + str(y - 2))
                                    elif self.board[x - 1][y - 2] != None and self.board[x - 1][y - 2].getOwner() == player.getOpponent():
                                        unit.addMove(str(x - 1) + str(y - 2))
                                if x < 7:
                                    if self.board[x + 1][y - 2] == None:
                                        unit.addMove(str(x + 1) + str(y - 2))
                                    elif self.board[x + 1][y - 2] != None and self.board[x + 1][y - 2].getOwner() == player.getOpponent():
                                        unit.addMove(str(x + 1) + str(y - 2))
                    # bishop moves
                    elif unit.getPower() == 4 or unit.getPower() == 5:
                        for i in range(self.limit - (y + 1)):
                            if y + i < self.limit - 1 and x + i < self.limit - 1:
                                if self.board[x + i + 1][y + i + 1] == None:
                                    unit.addMove(
                                        str(x + i + 1) + str(y + i + 1))
                                elif self.board[x + i + 1][y + i + 1] != None and self.board[x + i + 1][y + i + 1].getOwner() == player.getOpponent():
                                    unit.addMove(
                                        str(x + i + 1) + str(y + i + 1))
                                    break
                                else:
                                    break
                            if y + i < self.limit - 1 and x - i > 0:
                                if self.board[x - i - 1][y + i + 1] == None:
                                    unit.addMove(
                                        str(x - i - 1) + str(y + i + 1))
                                elif self.board[x - i - 1][y + i + 1] != None and self.board[x - i - 1][y + i + 1].getOwner() == player.getOpponent():
                                    unit.addMove(
                                        str(x - i - 1) + str(y + i + 1))
                                    break
                                else:
                                    break
                        for i in range(y):
                            if y - i > 0 and x + i < self.limit - 1:
                                if self.board[x + i + 1][y - i - 1] == None:
                                    unit.addMove(
                                        str(x + i + 1) + str(y - i - 1))
                                elif self.board[x + i + 1][y - i - 1] != None and self.board[x + i + 1][y - i - 1].getOwner() == player.getOpponent():
                                    unit.addMove(
                                        str(x + i + 1) + str(y - i - 1))
                                    break
                                else:
                                    break
                            if y - i > 0 and x - i > 0:
                                if self.board[x - i - 1][y - i - 1] == None:
                                    unit.addMove(
                                        str(x - i - 1) + str(y - i - 1))
                                elif self.board[x - i - 1][y - i - 1] != None and self.board[x - i - 1][y - i - 1].getOwner() == player.getOpponent():
                                    unit.addMove(
                                        str(x - i - 1) + str(y - i - 1))
                                    break
                                else:
                                    break
                    # queen moves
                    elif unit.getPower() == 6:
                        for i in range(self.limit - (y + 1)):
                            if y + i < self.limit - 1 and x + i < self.limit - 1:
                                if self.board[x + i + 1][y + i + 1] == None:
                                    unit.addMove(
                                        str(x + i + 1) + str(y + i + 1))
                                elif self.board[x + i + 1][y + i + 1] != None and self.board[x + i + 1][y + i + 1].getOwner() == player.getOpponent():
                                    unit.addMove(
                                        str(x + i + 1) + str(y + i + 1))
                                    break
                                else:
                                    break
                            if y + i < self.limit - 1 and x - i > 0:
                                if self.board[x - i - 1][y + i + 1] == None:
                                    unit.addMove(
                                        str(x - i - 1) + str(y + i + 1))
                                elif self.board[x - i - 1][y + i + 1] != None and self.board[x - i - 1][y + i + 1].getOwner() == player.getOpponent():
                                    unit.addMove(
                                        str(x - i - 1) + str(y + i + 1))
                                    break
                                else:
                                    break
                        for i in range(y):
                            if y - i > 0 and x + i < self.limit - 1:
                                if self.board[x + i + 1][y - i - 1] == None:
                                    unit.addMove(
                                        str(x + i + 1) + str(y - i - 1))
                                elif self.board[x + i + 1][y - i - 1] != None and self.board[x + i + 1][y - i - 1].getOwner() == player.getOpponent():
                                    unit.addMove(
                                        str(x + i + 1) + str(y - i - 1))
                                    break
                                else:
                                    break
                            if y - i > 0 and x - i > 0:
                                if self.board[x - i - 1][y - i - 1] == None:
                                    unit.addMove(
                                        str(x - i - 1) + str(y - i - 1))
                                elif self.board[x - i - 1][y - i - 1] != None and self.board[x - i - 1][y - i - 1].getOwner() == player.getOpponent():
                                    unit.addMove(
                                        str(x - i - 1) + str(y - i - 1))
                                    break
                                else:
                                    break
                        if y < self.limit - 1:
                            for i in range(self.limit - (y + 1)):
                                if self.board[x][y + i + 1] == None:
                                    unit.addMove(str(x) + str(y + i + 1))
                                elif self.board[x][y + i + 1] != None and self.board[x][y + i + 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x) + str(y + i + 1))
                                    break
                                else:
                                    break
                        if y > 0:
                            for i in range(y):
                                if self.board[x][y - (i + 1)] == None:
                                    unit.addMove(str(x) + str(y - i - 1))
                                elif self.board[x][y - (i + 1)] != None and self.board[x][y - (i + 1)].getOwner() == player.getOpponent():
                                    unit.addMove(str(x) + str(y - i - 1))
                                    break
                                else:
                                    break
                        if x < self.limit - 1:
                            for i in range(self.limit - (x + 1)):
                                if self.board[x + i + 1][y] == None:
                                    unit.addMove(str(x + i + 1) + str(y))
                                elif self.board[x + i + 1][y] != None and self.board[x + i + 1][y].getOwner() == player.getOpponent():
                                    unit.addMove(str(x + i + 1) + str(y))
                                    break
                                else:
                                    break
                        if x > 0:
                            for i in range(x):
                                if self.board[x - (i + 1)][y] == None:
                                    unit.addMove(str(x - i - 1) + str(y))
                                elif self.board[x - (i + 1)][y] != None and self.board[x - (i + 1)][y].getOwner() == player.getOpponent():
                                    unit.addMove(str(x - i - 1) + str(y))
                                    break
                                else:
                                    break
                    # king moves
                    elif unit.getPower() == 7:
                        if y < self.limit - 1:
                            if self.board[x][y + 1] == None:
                                unit.addMove(str(x) + str(y + 1))
                            elif self.board[x][y + 1] != None and self.board[x][y + 1].getOwner() == player.getOpponent():
                                unit.addMove(str(x) + str(y + 1))
                            if x < self.limit - 1:
                                if self.board[x + 1][y + 1] == None:
                                    unit.addMove(str(x + 1) + str(y + 1))
                                elif self.board[x + 1][y + 1] != None and self.board[x + 1][y + 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x + 1) + str(y + 1))
                            if x > 0:
                                if self.board[x - 1][y + 1] == None:
                                    unit.addMove(str(x - 1) + str(y + 1))
                                elif self.board[x - 1][y + 1] != None and self.board[x - 1][y + 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x - 1) + str(y + 1))
                        if y > 0:
                            if self.board[x][y - 1] == None:
                                unit.addMove(str(x) + str(y - 1))
                            elif self.board[x][y - 1] != None and self.board[x][y - 1].getOwner() == player.getOpponent():
                                unit.addMove(str(x) + str(y - 1))
                            if x < self.limit - 1:
                                if self.board[x + 1][y - 1] == None:
                                    unit.addMove(str(x + 1) + str(y - 1))
                                elif self.board[x + 1][y - 1] != None and self.board[x + 1][y - 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x + 1) + str(y - 1))
                            if x - i > 0:
                                if self.board[x - 1][y - 1] == None:
                                    unit.addMove(str(x - 1) + str(y - 1))
                                elif self.board[x - 1][y - 1] != None and self.board[x - 1][y - 1].getOwner() == player.getOpponent():
                                    unit.addMove(str(x - 1) + str(y - 1))
                        if x < self.limit - 1:
                            if self.board[x + 1][y] == None:
                                unit.addMove(str(x + 1) + str(y))
                            elif self.board[x + 1][y] != None and self.board[x + 1][y].getOwner() == player.getOpponent():
                                unit.addMove(str(x + 1) + str(y))
                        if x > 0:
                            if self.board[x - 1][y] == None:
                                unit.addMove(str(x - 1) + str(y))
                            elif self.board[x - 1][y] != None and self.board[x - 1][y].getOwner() == player.getOpponent():
                                unit.addMove(str(x - 1) + str(y))
                        # castling calculation
                        if initialCall:
                            playerIsInCheck(player)
                            if not player.isInCheck() and player.castlingIsPermitted():
                                if player == self.black:
                                    if self.board[0][7] != None and self.board[0][7].getPower() == 2 and not self.board[0][7].moved:
                                        if self.board[1][7] == None and self.board[2][7] == None and self.board[3][7] == None:
                                            unit.addMove("cl")
                                    if self.board[7][7] != None and self.board[7][7].getPower() == 2 and not self.board[7][7].moved:
                                        if self.board[6][7] == None and self.board[5][7] == None:
                                            unit.addMove("cr")
                                elif player == self.white:
                                    if self.board[0][0] != None and self.board[0][0].getPower() == 2 and not self.board[0][0].moved:
                                        if self.board[1][0] == None and self.board[2][0] == None and self.board[3][0] == None:
                                            unit.addMove("cl")
                                    if self.board[7][0] != None and self.board[7][0].getPower() == 2 and not self.board[7][0].moved:
                                        if self.board[6][0] == None and self.board[5][0] == None:
                                            unit.addMove("cr")

    # starts the game
    def start(self):
        print("--- NEW GAME ---")
        """for x in range(8):
			for y in range(8):
				if self.board[y][x] != None:
					print(self.board[y][x].getPowerString() + " " \
					+ self.board[y][x].getOwner().getColor())"""
        # self.calculatePossibleMoves(self.turn)
        """for m in self.board[0][1].getMoves():
			print(m)
		for m in self.board[0][0].getMoves():
			print(m)"""
        # self.writeUnitMovesToFile(self.turn)
        self.incrementMoveChance("3_2", "52", True)
        result = self.getBestMove()
        print(result[0] + " " + result[1])

    # return true if the player is in check
    def playerIsInCheck(self, player):
        self.calculatePossibleMoves(player.getOpponent(), False)
        king_position = player.getKingPosition()
        for x in range(self.limit):
            for y in range(self.limit):
                unit = self.board[x][y]
                if unit != None:
                    if unit.getOwner() == player.getOpponent():
                        for move in unit.getMoves():
                            if move == king_position:
                                player.setIsInCheck(True)
        player.setIsInCheck(False)

    # returns database location string for current state
    def generateDatabaseLocationString(self):
        dbLocationString = os.path.abspath(os.pardir) + "/db/"
        dbLocationString += str(self.getNumberOfUnits()) + "/"
        if not os.path.exists(dbLocationString):
            os.makedirs(dbLocationString)
        dbLocationString += str(self.getNumberOfWhiteUnits()) + "/"
        if not os.path.exists(dbLocationString):
            os.makedirs(dbLocationString)
        dbLocationString += self.getWhiteUnitsString() + "/"
        if not os.path.exists(dbLocationString):
            os.makedirs(dbLocationString)
        dbLocationString += self.getBlackUnitsString() + "/"
        if not os.path.exists(dbLocationString):
            os.makedirs(dbLocationString)
        dbLocationString += self.getWhiteUnitsPositionsString() + "/"
        if not os.path.exists(dbLocationString):
            os.makedirs(dbLocationString)
        dbLocationString += self.getBlackUnitsPositionsString() + "/"
        if not os.path.exists(dbLocationString):
            os.makedirs(dbLocationString)
        dbLocationString += self.turn.getColor() + "/"
        if not os.path.exists(dbLocationString):
            os.makedirs(dbLocationString)
        return dbLocationString + "data.json"

    # returns the black units positions string for the database
    def getBlackUnitsPositionsString(self):
        blackUnitsPositionsString = ""
        for p in range(7):
            for x in range(8):
                for y in range(8):
                    if self.board[x][y] != None:
                        if self.board[x][y].getOwner() == self.black:
                            if self.board[x][y].getPower() == p + 1:
                                blackUnitsPositionsString += str(x)
                                blackUnitsPositionsString += str(y)
        return blackUnitsPositionsString

    # returns the white units positions string for the database
    def getWhiteUnitsPositionsString(self):
        whiteUnitsPositionsString = ""
        for p in range(7):
            for x in range(8):
                for y in range(8):
                    if self.board[x][y] != None:
                        if self.board[x][y].getOwner() == self.white:
                            if self.board[x][y].getPower() == p + 1:
                                whiteUnitsPositionsString += str(x)
                                whiteUnitsPositionsString += str(y)
        return whiteUnitsPositionsString

    # returns the black units string for the database
    def getBlackUnitsString(self):
        blackUnitsString = ""
        for p in range(7):
            for x in range(8):
                for y in range(8):
                    if self.board[x][y] != None:
                        if self.board[x][y].getOwner() == self.black:
                            if self.board[x][y].getPower() == p + 1:
                                blackUnitsString += str(p + 1)
        return blackUnitsString

    # returns the white units string for the database
    def getWhiteUnitsString(self):
        whiteUnitsString = ""
        for p in range(7):
            for x in range(8):
                for y in range(8):
                    if self.board[x][y] != None:
                        if self.board[x][y].getOwner() == self.white:
                            if self.board[x][y].getPower() == p + 1:
                                whiteUnitsString += str(p + 1)
        return whiteUnitsString

    # returns number of units on the board
    def getNumberOfUnits(self):
        numberOfUnits = 0
        for x in range(8):
            for y in range(8):
                if self.board[x][y] != None:
                    numberOfUnits += 1
        return numberOfUnits

    # returns number of white units on the board
    def getNumberOfWhiteUnits(self):
        numberOfWhiteUnits = 0
        for x in range(8):
            for y in range(8):
                if self.board[x][y] != None:
                    if self.board[x][y].getOwner() == self.white:
                        numberOfWhiteUnits += 1
        return numberOfWhiteUnits

    # generates a blank chess board
    def generateBoard(self):
        board = []
        for x in range(8):
            board.append([])
            for y in range(8):
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

        # getters and setters
        def getWhite(self):
            return self.white

        def setWhite(self, white):
            self.white = white

        def getBlack(self):
            return self.black

        def setBlack(self, black):
            self.black = black

        def getBoard(self):
            return self.board

        def setBoard(self, board):
            self.board = board

        def getTurn(self):
            return self.turn

        def setTurn(self, turn):
            self.turn = turn

        def getLimit(self):
            return self.limit

        def setLimit(self, limit):
            self.limit = limit
