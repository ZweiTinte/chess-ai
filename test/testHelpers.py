# coding: utf-8
from unittest.case import TestCase
from app.log import LOG_FILE_NAME
from app.databaseLocationString import DB_DIR_NAME, getNumberOfUnits, getNumberOfWhiteUnits
from unittest import TestCase
import shutil
import os

tc = TestCase()

def assertNumberOfWhiteAndTotalUnits(game, expectedWhite, expectedTotal):
    tc.assertEqual(getNumberOfWhiteUnits(game), expectedWhite)
    tc.assertEqual(getNumberOfUnits(game), expectedTotal)

def assertExpectedMovesResults(expectedMoves, unit):
    for move in expectedMoves:
        tc.assertTrue(move in unit.moves)
    tc.assertEqual(len(unit.moves), len(expectedMoves))

def removeLogFileAndDatabase():
    os.remove(LOG_FILE_NAME)
    shutil.rmtree(DB_DIR_NAME)