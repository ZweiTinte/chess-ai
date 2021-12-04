# coding: utf-8
import unittest
from src.unit import *
from src.game import *
from test.testHelpers import assertExpectedMovesResults, assertNumberOfWhiteAndTotalUnits

class TestWhitePawnMoves(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.clearBoard()
        self.pawnUnit = Unit(PAWN, self.game.white)

    # --- NO OTHER UNIT ---

    def testStartPositionWhitePawnMoves(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["12", "13"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testMidGameWhitePawnMoves(self):
        self.game.setUnitOnBoard(1, 2, self.pawnUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["13"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)

    def testWhitePawnPromotion(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["173", "176"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 1)
    
    # --- ONE OPPONENT UNIT ---

    def testStartPositionWhitePawnMovesBlockedFront(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        self.game.setUnitOnBoard(1, 2, Unit(PAWN, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults([], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 2)

    def testStartPositionWhitePawnMovesBlockedFront2(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        self.game.setUnitOnBoard(1, 3, Unit(PAWN, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["12"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 2)

    def testStartPositionWhitePawnMovesLeftHit(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        self.game.setUnitOnBoard(0, 2, Unit(PAWN, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["02", "12", "13"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 2)

    def testStartPositionWhitePawnMovesRightHit(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        self.game.setUnitOnBoard(2, 2, Unit(PAWN, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["22", "12", "13"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 2)

    def testMidGameWhitePawnMovesBlockedFront2(self):
        self.game.setUnitOnBoard(1, 2, self.pawnUnit)
        self.game.setUnitOnBoard(1, 4, Unit(PAWN, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["13"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 2)

    def testWhitePawnPromotionBlockedFront(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        self.game.setUnitOnBoard(1, 7, Unit(ROOK, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults([], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 2)

    def testWhitePawnPromotionLeftHit(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        self.game.setUnitOnBoard(0, 7, Unit(ROOK, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["073", "173", "076", "176"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 2)

    def testWhitePawnPromotionRightHit(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        self.game.setUnitOnBoard(2, 7, Unit(ROOK, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["273", "173", "276", "176"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 2)

    # --- ANOTHER WHITE UNIT ---

    def testStartPositionWhitePawnMovesBlockedFrontWhite(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        self.game.setUnitOnBoard(1, 2, Unit(PAWN, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults([], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 2, 2)

    def testStartPositionWhitePawnMovesBlockedFront2White(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        self.game.setUnitOnBoard(1, 3, Unit(PAWN, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["12"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 2, 2)

    def testStartPositionWhitePawnMovesLeftBlocked(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        self.game.setUnitOnBoard(0, 2, Unit(PAWN, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["12", "13"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 2, 2)

    def testStartPositionWhitePawnMovesRightBlocked(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        self.game.setUnitOnBoard(2, 2, Unit(PAWN, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["12", "13"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 2, 2)

    def testMidGameWhitePawnMovesBlockedFront2White(self):
        self.game.setUnitOnBoard(1, 2, self.pawnUnit)
        self.game.setUnitOnBoard(1, 4, Unit(PAWN, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["13"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 2, 2)

    def testWhitePawnPromotionBlockedFrontWhite(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        self.game.setUnitOnBoard(1, 7, Unit(ROOK, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults([], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 2, 2)

    def testWhitePawnPromotionLeftBlocked(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        self.game.setUnitOnBoard(0, 7, Unit(ROOK, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["173", "176"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 2, 2)

    def testWhitePawnPromotionRightBlocked(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        self.game.setUnitOnBoard(2, 7, Unit(ROOK, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["173", "176"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 2, 2)