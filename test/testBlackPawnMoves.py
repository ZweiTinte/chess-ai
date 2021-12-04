# coding: utf-8
import unittest
from src.unit import *
from src.game import *
from test.testHelpers import assertExpectedMovesResults, assertNumberOfWhiteAndTotalUnits

class TestBlackPawnMoves(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.turn = self.game.black
        self.game.clearBoard()
        self.pawnUnit = Unit(PAWN, self.game.black)

    # --- NO OTHER UNIT ---

    def testStartPositionBlackPawnMoves(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["15", "14"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 0, 1)

    def testMidGameBlackPawnMoves(self):
        self.game.setUnitOnBoard(1, 5, self.pawnUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["14"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 0, 1)

    def testBlackPawnPromotion(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["103", "106"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 0, 1)
    
    # --- ONE OPPONENT UNIT ---

    def testStartPositionBlackPawnMovesBlockedFront(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        self.game.setUnitOnBoard(1, 5, Unit(PAWN, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults([], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 2)

    def testStartPositionBlackPawnMovesBlockedFront2(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        self.game.setUnitOnBoard(1, 4, Unit(PAWN, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["15"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 2)

    def testStartPositionBlackPawnMovesLeftHit(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        self.game.setUnitOnBoard(2, 5, Unit(PAWN, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["25", "15", "14"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 2)

    def testStartPositionBlackPawnMovesRightHit(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        self.game.setUnitOnBoard(0, 5, Unit(PAWN, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["05", "15", "14"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 2)

    def testMidGameWhiteBlackMovesBlockedFront2(self):
        self.game.setUnitOnBoard(1, 5, self.pawnUnit)
        self.game.setUnitOnBoard(1, 3, Unit(PAWN, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["14"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 2)

    def testBlackPawnPromotionBlockedFront(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        self.game.setUnitOnBoard(1, 0, Unit(ROOK, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults([], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 2)

    def testBlackPawnPromotionLeftHit(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        self.game.setUnitOnBoard(2, 0, Unit(ROOK, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["203", "103", "206", "106"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 2)

    def testBlackPawnPromotionRightHit(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        self.game.setUnitOnBoard(0, 0, Unit(ROOK, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["003", "103", "006", "106"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 1, 2)

    # --- ANOTHER BLACK UNIT ---

    def testStartPositionBlackPawnMovesBlockedFrontBlack(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        self.game.setUnitOnBoard(1, 5, Unit(PAWN, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults([], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 0, 2)

    def testStartPositionBlackPawnMovesBlockedFront2Black(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        self.game.setUnitOnBoard(1, 4, Unit(PAWN, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["15"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 0, 2)

    def testStartPositionBlackPawnMovesLeftBlocked(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        self.game.setUnitOnBoard(0, 5, Unit(PAWN, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["15", "14"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 0, 2)

    def testStartPositionBlackPawnMovesRightBlocked(self):
        self.game.setUnitOnBoard(1, 6, self.pawnUnit)
        self.game.setUnitOnBoard(2, 5, Unit(PAWN, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["15", "14"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 0, 2)

    def testMidGameBlackPawnMovesBlockedFront2Black(self):
        self.game.setUnitOnBoard(1, 5, self.pawnUnit)
        self.game.setUnitOnBoard(1, 3, Unit(PAWN, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["14"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 0, 2)

    def testBlackPawnPromotionBlockedFrontBlack(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        self.game.setUnitOnBoard(1, 0, Unit(ROOK, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults([], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 0, 2)

    def testBlackPawnPromotionLeftBlocked(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        self.game.setUnitOnBoard(0, 0, Unit(ROOK, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["103", "106"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 0, 2)

    def testBlackPawnPromotionRightBlocked(self):
        self.game.setUnitOnBoard(1, 1, self.pawnUnit)
        self.game.setUnitOnBoard(2, 0, Unit(ROOK, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn, True)
        assertExpectedMovesResults(["103", "106"], self.pawnUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 0, 2)