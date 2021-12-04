# coding: utf-8
from unittest.case import TestCase
from src.databaseLocationString import getNumberOfUnits, getNumberOfWhiteUnits
from unittest import TestCase

tc = TestCase()

def assertNumberOfWhiteAndTotalUnits(game, expectedWhite, expectedTotal):
    tc.assertEqual(getNumberOfWhiteUnits(game), expectedWhite)
    tc.assertEqual(getNumberOfUnits(game), expectedTotal)

def assertExpectedMovesResults(expectedMoves, unit):
    for move in expectedMoves:
        tc.assertTrue(move in unit.moves)
    tc.assertEqual(len(unit.moves), len(expectedMoves))