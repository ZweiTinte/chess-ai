# coding: utf-8
import unittest
from src.unit import *
from src.game import *
from test.testHelpers import assertExpectedMovesResults, assertNumberOfWhiteAndTotalUnits

class TestKnightMoves(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.clearBoard()
        self.knightUnit = Unit(KNIGHT, self.game.white)

    # --- NO OTHER UNIT ---

    def testStartPositionWhiteLeftKnightMoves(self):
        self.game.setUnitOnBoard(1, 0, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        expectedMoves = ["02", "22", "31"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testStartPositionWhiteRightKnightMoves(self):
        self.game.setUnitOnBoard(6, 0, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        expectedMoves = ["72", "52", "41"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testStartPositionBlackLeftKnightMoves(self):
        self.game.setUnitOnBoard(1, 7, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        expectedMoves = ["05", "25", "36"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testStartPositionBlackRightKnightMoves(self):
        self.game.setUnitOnBoard(6, 7, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        expectedMoves = ["75", "55", "46"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testMidGamePositionKnightMoves(self):
        self.game.setUnitOnBoard(3, 4, self.knightUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        expectedMoves = ["46", "42", "26", "22", "55", "53", "15", "13"]
        assertExpectedMovesResults(expectedMoves, self.knightUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)


    # --- OPPONENT UNITS ---



    # --- ALLY UNITS ---

