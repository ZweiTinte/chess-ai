# coding: utf-8
import unittest
from src.moveCalculations import playerIsInCheck
from src.unit import *
from src.game import *

class TestQueenMoves(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.clearBoard()
        self.kingUnit = Unit(KING, self.game.white)

    # --- OPPONENT UNITS ---

    def testNotInCheck(self):
        self.game.setUnitOnBoard(3, 4, self.kingUnit)
        self.game.setUnitOnBoard(0, 0, Unit(QUEEN, self.game.black))
        playerIsInCheck(self.game, self.game.turn)
        self.assertFalse(self.game.turn.inCheck)

    def testInCheck(self):
        self.game.setUnitOnBoard(3, 4, self.kingUnit)
        self.game.setUnitOnBoard(0, 1, Unit(QUEEN, self.game.black))
        playerIsInCheck(self.game, self.game.turn)
        self.assertTrue(self.game.turn.inCheck)
        