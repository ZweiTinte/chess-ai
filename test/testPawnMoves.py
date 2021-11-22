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

    def assertExpectedMovesResults(self, expectedMoves):
        for move in expectedMoves:
            self.assertTrue(move in self.pawnUnit.moves)
        self.assertEqual(len(self.pawnUnit.moves), len(expectedMoves))

    # --- NO OPPONENT UNIT ---

    def testStartPositionWhitePawnMoves(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        self.assertExpectedMovesResults(["12", "13"])

    def testMidGameWhitePawnMoves(self):
        self.game.setUnitOnBoard(1, 2, self.pawnUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        self.assertExpectedMovesResults(["13"])

    def testPawnPromotion(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        self.assertExpectedMovesResults(["173", "176"])
    
    # --- ONE OPPONENT UNIT ---

    def testStartPositionWhitePawnMovesBlockedFront(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        self.game.setUnitOnBoard(1, 2, Unit(PAWN, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        self.assertExpectedMovesResults([])

    def testStartPositionWhitePawnMovesBlockedFront2(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        self.game.setUnitOnBoard(1, 3, Unit(PAWN, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        self.assertExpectedMovesResults(["12"])

    def testStartPositionWhitePawnMovesLeftHit(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        self.game.setUnitOnBoard(0, 2, Unit(PAWN, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        self.assertExpectedMovesResults(["02", "12", "13"])

    def testStartPositionWhitePawnMovesRightHit(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        self.game.setUnitOnBoard(2, 2, Unit(PAWN, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        self.assertExpectedMovesResults(["22", "12", "13"])

    def testMidGameWhitePawnMovesBlockedFront2(self):
        self.game.setUnitOnBoard(1, 2, self.pawnUnit)
        self.game.setUnitOnBoard(1, 4, Unit(PAWN, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        self.assertExpectedMovesResults(["13"])

    def testPawnPromotionBlockedFront(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        self.game.setUnitOnBoard(1, 7, Unit(ROOK, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        self.assertExpectedMovesResults([])

    def testPawnPromotionLeftHit(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        self.game.setUnitOnBoard(0, 7, Unit(ROOK, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        self.assertExpectedMovesResults(["073", "173", "076", "176"])

    def testPawnPromotionRightHit(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        self.game.setUnitOnBoard(2, 7, Unit(ROOK, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        self.assertExpectedMovesResults(["273", "173", "276", "176"])

    # --- TWO OPPONENT UNITS ---