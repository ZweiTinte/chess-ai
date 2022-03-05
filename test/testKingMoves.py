# coding: utf-8
import unittest
from src.unit import *
from src.game import *
from test.testHelpers import *

class TestKingMoves(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.clearBoard()
        self.kingUnit = Unit(KING, self.game.white)

    # --- NO OTHER UNIT ---

    def testStartPositionWhiteKingMoves(self):
        self.game.setUnitOnBoard(4, 0, self.kingUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["41", "30", "50", "51", "31"]
        assertExpectedMovesResults(expectedMoves, self.kingUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testStartPositionBlackKingMoves(self):
        self.game.setUnitOnBoard(4, 7, self.kingUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["46", "37", "57", "56", "36"]
        assertExpectedMovesResults(expectedMoves, self.kingUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testUpperLeftCornerKingMoves(self):
        self.game.setUnitOnBoard(0, 7, self.kingUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["06", "16", "17"]
        assertExpectedMovesResults(expectedMoves, self.kingUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)
    
    def testLowerLeftCornerKingMoves(self):
        self.game.setUnitOnBoard(0, 0, self.kingUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["01", "10", "11"]
        assertExpectedMovesResults(expectedMoves, self.kingUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testUpperRightCornerKingMoves(self):
        self.game.setUnitOnBoard(7, 7, self.kingUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["76", "67", "66"]
        assertExpectedMovesResults(expectedMoves, self.kingUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testLowerRightCornerKingMoves(self):
        self.game.setUnitOnBoard(7, 0, self.kingUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["71", "60", "61"]
        assertExpectedMovesResults(expectedMoves, self.kingUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testMidGameKingMoves(self):
        self.game.setUnitOnBoard(3, 4, self.kingUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["44", "24", "35", "33", "45", "23", "43", "25"]
        assertExpectedMovesResults(expectedMoves, self.kingUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    # --- OPPONENT UNITS ---

    def testKingHitMoves(self):
        self.game.setUnitOnBoard(3, 4, self.kingUnit)
        self.game.setUnitOnBoard(4, 4, Unit(QUEEN, self.game.black))
        self.game.setUnitOnBoard(2, 4, Unit(QUEEN, self.game.black))
        self.game.setUnitOnBoard(3, 5, Unit(QUEEN, self.game.black))
        self.game.setUnitOnBoard(3, 3, Unit(QUEEN, self.game.black))
        self.game.setUnitOnBoard(4, 5, Unit(QUEEN, self.game.black))
        self.game.setUnitOnBoard(2, 3, Unit(QUEEN, self.game.black))
        self.game.setUnitOnBoard(4, 3, Unit(QUEEN, self.game.black))
        self.game.setUnitOnBoard(2, 5, Unit(QUEEN, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["44", "24", "35", "33", "45", "23", "43", "25"]
        assertExpectedMovesResults(expectedMoves, self.kingUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 9)

    # --- ALLY UNITS ---

    def testKingAllyMoves(self):
        self.game.setUnitOnBoard(3, 4, self.kingUnit)
        self.game.setUnitOnBoard(4, 4, Unit(QUEEN, self.game.white))
        self.game.setUnitOnBoard(2, 4, Unit(QUEEN, self.game.white))
        self.game.setUnitOnBoard(3, 5, Unit(QUEEN, self.game.white))
        self.game.setUnitOnBoard(3, 3, Unit(QUEEN, self.game.white))
        self.game.setUnitOnBoard(4, 5, Unit(QUEEN, self.game.white))
        self.game.setUnitOnBoard(2, 3, Unit(QUEEN, self.game.white))
        self.game.setUnitOnBoard(4, 3, Unit(QUEEN, self.game.white))
        self.game.setUnitOnBoard(2, 5, Unit(QUEEN, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn)
        assertExpectedMovesResults([], self.kingUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 9, 9)