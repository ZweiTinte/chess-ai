# coding: utf-8
import unittest
from src.unit import *
from src.game import *
from test.testHelpers import *

class TestQueenMoves(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.clearBoard()
        self.queenUnit = Unit(QUEEN, self.game.white)

    # --- NO OTHER UNIT ---

    def testStartPositionWhiteQueenMoves(self):
        self.game.setUnitOnBoard(3, 0, self.queenUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        verticalMoves = ["31", "32", "33", "34", "35", "36", "37"]
        horizontalMoves = ["20", "10", "00", "40", "50", "60", "70"]
        diagonalMoves = ["21", "12", "03", "41", "52", "63", "74"]
        expectedMoves = verticalMoves + horizontalMoves + diagonalMoves
        assertExpectedMovesResults(expectedMoves, self.queenUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testStartPositionBlackQueenMoves(self):
        self.game.setUnitOnBoard(3, 7, self.queenUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        verticalMoves = ["31", "32", "33", "34", "35", "36", "30"]
        horizontalMoves = ["27", "17", "07", "47", "57", "67", "77"]
        diagonalMoves = ["26", "15", "04", "46", "55", "64", "73"]
        expectedMoves = verticalMoves + horizontalMoves + diagonalMoves
        assertExpectedMovesResults(expectedMoves, self.queenUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testUpperLeftCornerQueenMoves(self):
        self.game.setUnitOnBoard(0, 7, self.queenUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        verticalMoves = ["01", "02", "03", "04", "05", "06", "00"]
        horizontalMoves = ["27", "17", "37", "47", "57", "67", "77"]
        diagonalMoves = ["16", "25", "34", "43", "52", "61", "70"]
        expectedMoves = verticalMoves + horizontalMoves + diagonalMoves
        assertExpectedMovesResults(expectedMoves, self.queenUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testLowerLeftCornerQueenMoves(self):
        self.game.setUnitOnBoard(0, 0, self.queenUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        verticalMoves = ["01", "02", "03", "04", "05", "06", "07"]
        horizontalMoves = ["20", "10", "30", "40", "50", "60", "70"]
        diagonalMoves = ["11", "22", "33", "44", "55", "66", "77"]
        expectedMoves = verticalMoves + horizontalMoves + diagonalMoves
        assertExpectedMovesResults(expectedMoves, self.queenUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testLowerRightCornerQueenMoves(self):
        self.game.setUnitOnBoard(7, 0, self.queenUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        verticalMoves = ["71", "72", "73", "74", "75", "76", "77"]
        horizontalMoves = ["20", "10", "30", "40", "50", "60", "00"]
        diagonalMoves = ["16", "25", "34", "43", "52", "61", "07"]
        expectedMoves = verticalMoves + horizontalMoves + diagonalMoves
        assertExpectedMovesResults(expectedMoves, self.queenUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testUpperRightCornerQueenMoves(self):
        self.game.setUnitOnBoard(7, 7, self.queenUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        verticalMoves = ["71", "72", "73", "74", "75", "76", "70"]
        horizontalMoves = ["27", "17", "37", "47", "57", "67", "07"]
        diagonalMoves = ["11", "22", "33", "44", "55", "66", "00"]
        expectedMoves = verticalMoves + horizontalMoves + diagonalMoves
        assertExpectedMovesResults(expectedMoves, self.queenUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testMidGameQueenMoves(self):
        self.game.setUnitOnBoard(3, 4, self.queenUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        vMoves = ["31", "32", "33", "30", "35", "36", "37"]
        hMoves = ["24", "14", "44", "74", "54", "64", "04"]
        diagonalMovesUp = ["45", "56", "67", "25", "16", "07"]
        diagonalMovesDown = ["43", "52", "61", "70", "23", "12", "01"]
        expectedMoves = vMoves + hMoves + diagonalMovesUp + diagonalMovesDown
        assertExpectedMovesResults(expectedMoves, self.queenUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    # --- OPPONENT UNITS ---

    # --- ALLY UNITS ---