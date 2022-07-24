# coding: utf-8
import unittest
from app.moveCalculations import playerIsInCheck
from app.unit import *
from app.game import *

class TestQueenMoves(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.clearBoard()
        self.kingUnit = Unit(KING, self.game.white)

    # --- OPPONENT UNITS ---

    def testNotInCheck(self):
        game = self.game
        game.setUnitOnBoard(3, 4, self.kingUnit)
        game.setUnitOnBoard(0, 0, Unit(QUEEN, game.black))
        playerIsInCheck(game, game.turn)
        self.assertFalse(game.turn.inCheck)

    def testInCheck(self):
        game = self.game
        game.setUnitOnBoard(3, 4, self.kingUnit)
        game.setUnitOnBoard(0, 1, Unit(QUEEN, game.black))
        playerIsInCheck(game, game.turn)
        self.assertTrue(game.turn.inCheck)
        