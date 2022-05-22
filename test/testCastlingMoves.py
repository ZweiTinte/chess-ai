# coding: utf-8
import unittest
from src.unit import *
from src.game import *
from test.testHelpers import *

WHITE_KING_MOVES = ["41", "30", "50", "51", "31"]
BLACK_KING_MOVES = ["46", "37", "57", "56", "36"]

class TestKingMoves(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.clearBoard()
        self.whiteKingUnit = Unit(KING, self.game.white)
        self.blackKingUnit = Unit(KING, self.game.black)

# --- CASTLING POSSIBLE ---

    def testStartPositionWhiteKingLeftCastlingMove(self):
        self.game.setUnitOnBoard(4, 0, self.whiteKingUnit)
        self.game.setUnitOnBoard(0, 0, Unit(ROOK, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = WHITE_KING_MOVES + [CASTLING_LEFT]
        assertExpectedMovesResults(expectedMoves, self.whiteKingUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 2, 2)

    def testStartPositionWhiteKingRightCastlingMove(self):
        self.game.setUnitOnBoard(4, 0, self.whiteKingUnit)
        self.game.setUnitOnBoard(7, 0, Unit(ROOK, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = WHITE_KING_MOVES + [CASTLING_RIGHT]
        assertExpectedMovesResults(expectedMoves, self.whiteKingUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 2, 2)

    def testStartPositionWhiteKingCastlingMoves(self):
        self.game.setUnitOnBoard(4, 0, self.whiteKingUnit)
        self.game.setUnitOnBoard(7, 0, Unit(ROOK, self.game.white))
        self.game.setUnitOnBoard(0, 0, Unit(ROOK, self.game.white))
        calculatePossibleMoves(self.game, self.game.turn)
        expectedMoves = WHITE_KING_MOVES + [CASTLING_LEFT, CASTLING_RIGHT]
        assertExpectedMovesResults(expectedMoves, self.whiteKingUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 3, 3)

    def testStartPositionBlackKingLeftCastlingMove(self):
        self.game.setUnitOnBoard(4, 7, self.blackKingUnit)
        self.game.setUnitOnBoard(0, 7, Unit(ROOK, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn.opponent)
        expectedMoves = BLACK_KING_MOVES + [CASTLING_LEFT]
        assertExpectedMovesResults(expectedMoves, self.blackKingUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 0, 2)

    def testStartPositionBlackKingRightCastlingMove(self):
        self.game.setUnitOnBoard(4, 7, self.blackKingUnit)
        self.game.setUnitOnBoard(7, 7, Unit(ROOK, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn.opponent)
        expectedMoves = BLACK_KING_MOVES + [CASTLING_RIGHT]
        assertExpectedMovesResults(expectedMoves, self.blackKingUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 0, 2)

    def testStartPositionBlackKingCastlingMoves(self):
        self.game.setUnitOnBoard(4, 7, self.blackKingUnit)
        self.game.setUnitOnBoard(7, 7, Unit(ROOK, self.game.black))
        self.game.setUnitOnBoard(0, 7, Unit(ROOK, self.game.black))
        calculatePossibleMoves(self.game, self.game.turn.opponent)
        expectedMoves = BLACK_KING_MOVES + [CASTLING_LEFT, CASTLING_RIGHT]
        assertExpectedMovesResults(expectedMoves, self.blackKingUnit)
        assertNumberOfWhiteAndTotalUnits(self.game, 0, 3)

# --- CASTLING NOT POSSIBLE ---

    def testStartPositionWhiteKingMoved(self):
        game = self.game
        game.setUnitOnBoard(4, 0, self.whiteKingUnit)
        # move forward
        calculatePossibleMoves(game, game.turn, True)
        self.whiteKingUnit.moves = ["41"]
        game.writeUnitMovesToFile(game.turn)
        game.moveUnit()
        # move back
        self.game.resetPossibleMoves()
        calculatePossibleMoves(game, game.turn, True)
        self.whiteKingUnit.moves = ["40"]
        game.writeUnitMovesToFile(game.turn)
        game.moveUnit()
        # set the rook units
        game.setUnitOnBoard(7, 0, Unit(ROOK, game.white))
        game.setUnitOnBoard(0, 0, Unit(ROOK, game.white))
        # assertions
        game.resetPossibleMoves()
        calculatePossibleMoves(game, game.turn)
        assertExpectedMovesResults(WHITE_KING_MOVES, self.whiteKingUnit)
        assertNumberOfWhiteAndTotalUnits(game, 3, 3)
        # clean up database and logfile
        removeLogFileAndDatabase()