# coding: utf-8
import unittest
from src.unit import *
from src.game import *
from test.testHelpers import assertExpectedMovesResults, assertNumberOfWhiteAndTotalUnits

class TestRookMoves(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.clearBoard()
        self.rookUnit = Unit(ROOK, self.game.white)

    # --- NO OTHER UNIT ---

    def testStartPositionWhiteLeftRookMoves(self):
        self.game.setUnitOnBoard(0, 0, self.rookUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        expectedMoves = ["01", "02", "03", "04", "05", "06", "07", "10", "20", "30", "40", "50", "60", "70"]
        assertExpectedMovesResults(expectedMoves, self.rookUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testStartPositionWhiteRightRookMoves(self):
        self.game.setUnitOnBoard(7, 0, self.rookUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        expectedMoves = ["71", "72", "73", "74", "75", "76", "77", "00", "10", "20", "30", "40", "50", "60"]
        assertExpectedMovesResults(expectedMoves, self.rookUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testStartPositionBlackLeftRookMoves(self):
        self.game.setUnitOnBoard(0, 7, self.rookUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        expectedMoves = ["01", "02", "03", "04", "05", "06", "00", "17", "27", "37", "47", "57", "67", "77"]
        assertExpectedMovesResults(expectedMoves, self.rookUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testStartPositionBlackRightRookMoves(self):
        self.game.setUnitOnBoard(7, 7, self.rookUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        expectedMoves = ["71", "72", "73", "74", "75", "76", "70", "07", "17", "27", "37", "47", "57", "67"]
        assertExpectedMovesResults(expectedMoves, self.rookUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testMidGamePositionRookMoves(self):
        self.game.setUnitOnBoard(3, 4, self.rookUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        expectedMoves = ["35", "36", "37", "33", "32", "31", "30", "04", "14", "24", "44", "54", "64", "74"]
        assertExpectedMovesResults(expectedMoves, self.rookUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)