# coding: utf-8
import unittest
from app.unit import *
from app.game import *
from test.testHelpers import assertExpectedMovesResults, assertNumberOfWhiteAndTotalUnits

class TestBishopMoves(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.clearBoard()

    # --- NO OTHER UNIT ---

    def testStartPositionWhiteLeftBishopMoves(self):
        bishopUnit = Unit(BISHOPL, self.game.white)
        self.game.setUnitOnBoard(2, 0, bishopUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["11", "02", "31", "42", "53", "64", "75"]
        assertExpectedMovesResults(expectedMoves, bishopUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testStartPositionWhiteRightBishopMoves(self):
        bishopUnit = Unit(BISHOPR, self.game.white)
        self.game.setUnitOnBoard(5, 0, bishopUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["05", "14", "23", "32", "41", "61", "72"]
        assertExpectedMovesResults(expectedMoves, bishopUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testStartPositionBlackLeftBishopMoves(self):
        bishopUnit = Unit(BISHOPL, self.game.white)
        self.game.setUnitOnBoard(5, 7, bishopUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["02", "13", "24", "35", "46", "66", "75"]
        assertExpectedMovesResults(expectedMoves, bishopUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testStartPositionBlackRightBishopMoves(self):
        bishopUnit = Unit(BISHOPR, self.game.white)
        self.game.setUnitOnBoard(2, 7, bishopUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["16", "05", "36", "45", "54", "63", "72"]
        assertExpectedMovesResults(expectedMoves, bishopUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testLeftBorderBishopMoves(self):
        bishopUnit = Unit(BISHOPL, self.game.white)
        self.game.setUnitOnBoard(0, 2, bishopUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["11", "20", "13", "24", "35", "46", "57"]
        assertExpectedMovesResults(expectedMoves, bishopUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testRightBorderBishopMoves(self):
        bishopUnit = Unit(BISHOPR, self.game.white)
        self.game.setUnitOnBoard(7, 2, bishopUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["61", "50", "63", "54", "45", "36", "27"]
        assertExpectedMovesResults(expectedMoves, bishopUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testLowerLeftCornerBishopMoves(self):
        bishopUnit = Unit(BISHOPL, self.game.white)
        self.game.setUnitOnBoard(0, 0, bishopUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["11", "22", "33", "44", "55", "66", "77"]
        assertExpectedMovesResults(expectedMoves, bishopUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testUpperRightCornerBishopMoves(self):
        bishopUnit = Unit(BISHOPL, self.game.white)
        self.game.setUnitOnBoard(7, 7, bishopUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["11", "22", "33", "44", "55", "66", "00"]
        assertExpectedMovesResults(expectedMoves, bishopUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testUpperLeftCornerBishopMoves(self):
        bishopUnit = Unit(BISHOPR, self.game.white)
        self.game.setUnitOnBoard(0, 7, bishopUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["16", "25", "34", "43", "52", "61", "70"]
        assertExpectedMovesResults(expectedMoves, bishopUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testLowerRightCornerBishopMoves(self):
        bishopUnit = Unit(BISHOPR, self.game.white)
        self.game.setUnitOnBoard(7, 0, bishopUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["16", "25", "34", "43", "52", "61", "07"]
        assertExpectedMovesResults(expectedMoves, bishopUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testMidGamePositionBishopMoves(self):
        bishopUnit = Unit(BISHOPR, self.game.white)
        self.game.setUnitOnBoard(3, 4, bishopUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["16", "25", "43", "52", "61", "07", "70", "45", "56", "67", "23", "12", "01"]
        assertExpectedMovesResults(expectedMoves, bishopUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    # --- OPPONENT UNITS ---

    def testMidGamePositionBishopHitMoves(self):
        bishopUnit = Unit(BISHOPR, self.game.white)
        self.game.setUnitOnBoard(3, 4, bishopUnit)
        self.game.setUnitOnBoard(4, 5, Unit(KNIGHT, self.game.black))
        self.game.setUnitOnBoard(5, 2, Unit(KNIGHT, self.game.black))
        self.game.setUnitOnBoard(2, 3, Unit(KNIGHT, self.game.black))
        self.game.setUnitOnBoard(1, 6, Unit(KNIGHT, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["16", "23", "45", "52", "43", "25"]
        assertExpectedMovesResults(expectedMoves, bishopUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 5)

    # --- ALLY UNITS ---

    def testMidGamePositionBishopNoHitMoves(self):
        bishopUnit = Unit(BISHOPR, self.game.white)
        self.game.setUnitOnBoard(3, 4, bishopUnit)
        self.game.setUnitOnBoard(4, 5, Unit(KNIGHT, self.game.white))
        self.game.setUnitOnBoard(5, 2, Unit(KNIGHT, self.game.white))
        self.game.setUnitOnBoard(2, 3, Unit(KNIGHT, self.game.white))
        self.game.setUnitOnBoard(1, 6, Unit(KNIGHT, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["43", "25"]
        assertExpectedMovesResults(expectedMoves, bishopUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 5, 5)