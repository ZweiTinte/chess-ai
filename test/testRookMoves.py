# coding: utf-8
import unittest
from src.unit import *
from src.game import *
from test.testHelpers import *

class TestRookMoves(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.clearBoard()
        self.rookUnit = Unit(ROOK, self.game.white)

    # --- NO OTHER UNIT ---

    def testStartPositionWhiteLeftRookMoves(self):
        self.game.setUnitOnBoard(0, 0, self.rookUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        verticalMoves = ["01", "02", "03", "04", "05", "06", "07"]
        horizontalMoves = ["10", "20", "30", "40", "50", "60", "70"]
        expectedMoves = horizontalMoves + verticalMoves
        assertExpectedMovesResults(expectedMoves, self.rookUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testStartPositionWhiteRightRookMoves(self):
        self.game.setUnitOnBoard(7, 0, self.rookUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        verticalMoves = ["71", "72", "73", "74", "75", "76", "77"]
        horizontalMoves = ["00", "10", "20", "30", "40", "50", "60"]
        expectedMoves = horizontalMoves + verticalMoves
        assertExpectedMovesResults(expectedMoves, self.rookUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testStartPositionBlackLeftRookMoves(self):
        self.game.setUnitOnBoard(0, 7, self.rookUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        verticalMoves = ["01", "02", "03", "04", "05", "06", "00"]
        horizontalMoves = ["17", "27", "37", "47", "57", "67", "77"]
        expectedMoves = horizontalMoves + verticalMoves
        assertExpectedMovesResults(expectedMoves, self.rookUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testStartPositionBlackRightRookMoves(self):
        self.game.setUnitOnBoard(7, 7, self.rookUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        verticalMoves = ["71", "72", "73", "74", "75", "76", "70"]
        horizontalMoves = ["07", "17", "27", "37", "47", "57", "67"]
        expectedMoves = horizontalMoves + verticalMoves
        assertExpectedMovesResults(expectedMoves, self.rookUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testMidGamePositionRookMoves(self):
        self.game.setUnitOnBoard(3, 4, self.rookUnit)
        calculatePossibleMoves(self.game, self.game.turn)
        verticalMoves = ["35", "36", "37", "33", "32", "31", "30"]
        horizontalMoves = ["04", "14", "24", "44", "54", "64", "74"]
        expectedMoves = horizontalMoves + verticalMoves
        assertExpectedMovesResults(expectedMoves, self.rookUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    # --- OPPONENT UNITS ---

    def testMidGamePositionSurroundedByOpponentRookMoves(self):
        self.game.setUnitOnBoard(3, 4, self.rookUnit)
        self.game.setUnitOnBoard(3, 5, Unit(ROOK, self.game.black))
        self.game.setUnitOnBoard(3, 3, Unit(ROOK, self.game.black))
        self.game.setUnitOnBoard(4, 4, Unit(ROOK, self.game.black))
        self.game.setUnitOnBoard(2, 4, Unit(ROOK, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["35", "33", "44", "24"]
        assertExpectedMovesResults(expectedMoves, self.rookUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 5)

    def testMidGamePositionFarSurroundedByOpponentRookMoves(self):
        self.game.setUnitOnBoard(3, 4, self.rookUnit)
        self.game.setUnitOnBoard(0, 4, Unit(ROOK, self.game.black))
        self.game.setUnitOnBoard(7, 4, Unit(ROOK, self.game.black))
        self.game.setUnitOnBoard(3, 0, Unit(ROOK, self.game.black))
        self.game.setUnitOnBoard(3, 7, Unit(ROOK, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn)
        verticalMoves = ["35", "36", "37", "33", "32", "31", "30"]
        horizontalMoves = ["04", "14", "24", "44", "54", "64", "74"]
        expectedMoves = horizontalMoves + verticalMoves
        assertExpectedMovesResults(expectedMoves, self.rookUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 5)

    # --- ALLY UNITS ---

    def testMidGamePositionSurroundedByAllyRookMoves(self):
        self.game.setUnitOnBoard(3, 4, self.rookUnit)
        self.game.setUnitOnBoard(3, 5, Unit(ROOK, self.game.white))
        self.game.setUnitOnBoard(3, 3, Unit(ROOK, self.game.white))
        self.game.setUnitOnBoard(4, 4, Unit(ROOK, self.game.white))
        self.game.setUnitOnBoard(2, 4, Unit(ROOK, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn)
        assertExpectedMovesResults([], self.rookUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 5, 5)

    def testMidGamePositionFarSurroundedByAllyRookMoves(self):
        self.game.setUnitOnBoard(3, 4, self.rookUnit)
        self.game.setUnitOnBoard(0, 4, Unit(ROOK, self.game.white))
        self.game.setUnitOnBoard(7, 4, Unit(ROOK, self.game.white))
        self.game.setUnitOnBoard(3, 0, Unit(ROOK, self.game.white))
        self.game.setUnitOnBoard(3, 7, Unit(ROOK, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["35", "36", "33", "32", "31", "14", "24", "44", "54", "64"]
        assertExpectedMovesResults(expectedMoves, self.rookUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 5, 5)

    # --- MIXED ROWS AND COLS ---

    def testMidGamePositionFarSurroundedByMultipleUnitsRookMoves(self):
        self.game.setUnitOnBoard(3, 4, self.rookUnit)
        self.game.setUnitOnBoard(0, 4, Unit(ROOK, self.game.white))
        self.game.setUnitOnBoard(1, 4, Unit(ROOK, self.game.black))
        self.game.setUnitOnBoard(7, 4, Unit(ROOK, self.game.black))
        self.game.setUnitOnBoard(6, 4, Unit(ROOK, self.game.white))
        self.game.setUnitOnBoard(3, 0, Unit(ROOK, self.game.white))
        self.game.setUnitOnBoard(3, 1, Unit(ROOK, self.game.black))
        self.game.setUnitOnBoard(3, 7, Unit(ROOK, self.game.black))
        self.game.setUnitOnBoard(3, 6, Unit(ROOK, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = ["35", "33", "32", "31", "14", "24", "44", "54"]
        assertExpectedMovesResults(expectedMoves, self.rookUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 5, 9)