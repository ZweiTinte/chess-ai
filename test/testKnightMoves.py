# coding: utf-8
import unittest
from src.unit import *
from src.game import *
from test.testHelpers import *

class TestKnightMoves(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.clearBoard()
        self.knightUnit = Unit(KNIGHT, self.game.white)

    # --- NO OTHER UNIT ---

    def testStartPositionWhiteLeftKnightMoves(self):
        self.game.setUnitOnBoard(1, 0, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["02", "22", "31"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testStartPositionWhiteRightKnightMoves(self):
        self.game.setUnitOnBoard(6, 0, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["72", "52", "41"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testStartPositionBlackLeftKnightMoves(self):
        self.game.setUnitOnBoard(1, 7, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["05", "25", "36"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testStartPositionBlackRightKnightMoves(self):
        self.game.setUnitOnBoard(6, 7, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["75", "55", "46"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testMidGamePositionKnightMoves(self):
        self.game.setUnitOnBoard(3, 4, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["46", "42", "26", "22", "55", "53", "15", "13"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testUpperLeftBorderKnightMoves(self):
        self.game.setUnitOnBoard(0, 6, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["27", "14", "25"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testLowerLeftBorderKnightMoves(self):
        self.game.setUnitOnBoard(0, 1, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["20", "13", "22"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testUpperRightBorderKnightMoves(self):
        self.game.setUnitOnBoard(7, 6, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["57", "64", "55"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testLowerRightBorderKnightMoves(self):
        self.game.setUnitOnBoard(7, 1, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["50", "63", "52"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testUpperLeftCornerKnightMoves(self):
        self.game.setUnitOnBoard(0, 7, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["15", "26"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testLowerLeftCornerKnightMoves(self):
        self.game.setUnitOnBoard(0, 0, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["21", "12"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testUpperRightCornerKnightMoves(self):
        self.game.setUnitOnBoard(7, 7, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["56", "65"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testLowerRightCornerKnightMoves(self):
        self.game.setUnitOnBoard(7, 0, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["51", "62"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testUpperLeftPositionKnightMoves(self):
        self.game.setUnitOnBoard(1, 6, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["04", "24", "35", "37"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testLowerLeftPositionKnightMoves(self):
        self.game.setUnitOnBoard(1, 1, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["03", "23", "32", "30"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testUpperRightPositionKnightMoves(self):
        self.game.setUnitOnBoard(6, 6, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["74", "54", "45", "47"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testLowerRightPositionKnightMoves(self):
        self.game.setUnitOnBoard(6, 1, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["73", "53", "42", "40"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    # --- OPPONENT UNITS ---

    def testMidGamePositionKnightHitMoves(self):
        self.game.setUnitOnBoard(3, 4, self.knightUnit)
        self.game.setUnitOnBoard(4, 6, Unit(KNIGHT, self.game.black))
        self.game.setUnitOnBoard(2, 6, Unit(KNIGHT, self.game.black))
        self.game.setUnitOnBoard(4, 2, Unit(KNIGHT, self.game.black))
        self.game.setUnitOnBoard(2, 2, Unit(KNIGHT, self.game.black))
        self.game.setUnitOnBoard(5, 5, Unit(KNIGHT, self.game.black))
        self.game.setUnitOnBoard(5, 3, Unit(KNIGHT, self.game.black))
        self.game.setUnitOnBoard(1, 5, Unit(KNIGHT, self.game.black))
        self.game.setUnitOnBoard(1, 3, Unit(KNIGHT, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["46", "42", "26", "22", "55", "53", "15", "13"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 9)

    # --- ALLY UNITS ---

    def testMidGamePositionKnightBlockedMoves(self):
        self.game.setUnitOnBoard(3, 4, self.knightUnit)
        self.game.setUnitOnBoard(4, 6, Unit(KNIGHT, self.game.white))
        self.game.setUnitOnBoard(2, 6, Unit(KNIGHT, self.game.white))
        self.game.setUnitOnBoard(4, 2, Unit(KNIGHT, self.game.white))
        self.game.setUnitOnBoard(2, 2, Unit(KNIGHT, self.game.white))
        self.game.setUnitOnBoard(5, 5, Unit(KNIGHT, self.game.white))
        self.game.setUnitOnBoard(5, 3, Unit(KNIGHT, self.game.white))
        self.game.setUnitOnBoard(1, 5, Unit(KNIGHT, self.game.white))
        self.game.setUnitOnBoard(1, 3, Unit(KNIGHT, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn)
        assertExpectedMovesResults([], self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 9, 9)