# coding: utf-8
import unittest
from src.unit import *
from src.game import *
from src.databaseLocationString import getNumberOfWhiteUnits

class TestWhitePawnMoves(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.clearBoard()
        self.pawnUnit = Unit(PAWN, self.game.white)

    def tearDown(self):
        self.assertTrue(getNumberOfWhiteUnits(self.game), 1)

    def setUnit(self, posX, posY):
        self.game.board[posX][posY] = self.pawnUnit

    # --- NO OPPONENT UNIT ---

    def testStartPositionWhitePawnMoves(self):
        self.setUnit(1, 1)
        calculatePossibleMoves(self.game, self.game.turn, True)
        expectedMoves = ["12", "13"]
        for move in expectedMoves:
            self.assertTrue(move in self.pawnUnit.moves)
        self.assertEqual(len(self.pawnUnit.moves), len(expectedMoves))

    def testMidGameWhitePawnMoves(self):
        self.setUnit(1, 2)
        calculatePossibleMoves(self.game, self.game.turn, True)
        expectedMoves = ["13"]
        for move in expectedMoves:
            self.assertTrue(move in self.pawnUnit.moves)
        self.assertEqual(len(self.pawnUnit.moves), len(expectedMoves))

    def testPawnPromotion(self):
        self.setUnit(1, 6)
        calculatePossibleMoves(self.game, self.game.turn, True)
        expectedMoves = ["173", "176"]
        for move in expectedMoves:
            self.assertTrue(move in self.pawnUnit.moves)
        self.assertEqual(len(self.pawnUnit.moves), len(expectedMoves))