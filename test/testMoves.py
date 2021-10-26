# coding: utf-8
import unittest
from src.unit import *
from src.game import *

class TestPawnMoves(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.clearBoard()

    # test start position moves of pawns
    def testBasicWhitePawnMoves(self):
        self.game.board[1][1] = Unit(1, self.game.white)
        calculatePossibleMoves(self.game, self.game.turn, True)
        self.assertTrue("12" in self.game.board[1][1].moves)
        self.assertTrue("13" in self.game.board[1][1].moves)
        self.assertEqual(len(self.game.board[1][1].moves), 2)