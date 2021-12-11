# coding: utf-8
import os.path

DB_DIR_NAME = "db"

# returns database location string for current state
def generateDatabaseLocationString(game):
    dbLocationString = DB_DIR_NAME + "/"
    dbLocationString += str(getNumberOfUnits(game)) + "/"
    if not os.path.exists(dbLocationString):
        os.makedirs(dbLocationString)
    dbLocationString += str(getNumberOfWhiteUnits(game)) + "/"
    if not os.path.exists(dbLocationString):
        os.makedirs(dbLocationString)
    dbLocationString += getWhiteUnitsString(game) + "/"
    if not os.path.exists(dbLocationString):
        os.makedirs(dbLocationString)
    dbLocationString += getBlackUnitsString(game) + "/"
    if not os.path.exists(dbLocationString):
        os.makedirs(dbLocationString)
    dbLocationString += getWhiteUnitsPositionsString(game) + "/"
    if not os.path.exists(dbLocationString):
        os.makedirs(dbLocationString)
    dbLocationString += getBlackUnitsPositionsString(game) + "/"
    if not os.path.exists(dbLocationString):
        os.makedirs(dbLocationString)
    dbLocationString += game.turn.getColor() + "/"
    if not os.path.exists(dbLocationString):
        os.makedirs(dbLocationString)
    return dbLocationString + "data.json"

# returns the black units positions string for the database
def getBlackUnitsPositionsString(game):
    blackUnitsPositionsString = ""
    for p in range(7):
        for x in range(8):
            for y in range(8):
                if game.board[x][y] != None:
                    if game.board[x][y].owner == game.black:
                        if game.board[x][y].getPower() == p + 1:
                            blackUnitsPositionsString += str(x)
                            blackUnitsPositionsString += str(y)
    return blackUnitsPositionsString

# returns the white units positions string for the database
def getWhiteUnitsPositionsString(game):
    whiteUnitsPositionsString = ""
    for p in range(7):
        for x in range(8):
            for y in range(8):
                if game.board[x][y] != None:
                    if game.board[x][y].owner == game.white:
                        if game.board[x][y].getPower() == p + 1:
                            whiteUnitsPositionsString += str(x)
                            whiteUnitsPositionsString += str(y)
    return whiteUnitsPositionsString

# returns the black units string for the database
def getBlackUnitsString(game):
    blackUnitsString = ""
    for p in range(7):
        for x in range(8):
            for y in range(8):
                if game.board[x][y] != None:
                    if game.board[x][y].owner == game.black:
                        if game.board[x][y].getPower() == p + 1:
                            blackUnitsString += str(p + 1)
    return blackUnitsString

# returns the white units string for the database
def getWhiteUnitsString(game):
    whiteUnitsString = ""
    for p in range(7):
        for x in range(8):
            for y in range(8):
                if game.board[x][y] != None:
                    if game.board[x][y].owner == game.white:
                        if game.board[x][y].getPower() == p + 1:
                            whiteUnitsString += str(p + 1)
    return whiteUnitsString

# returns number of units on the board
def getNumberOfUnits(game):
    numberOfUnits = 0
    for x in range(8):
        for y in range(8):
            if game.board[x][y] != None:
                numberOfUnits += 1
    return numberOfUnits

# returns number of white units on the board
def getNumberOfWhiteUnits(game):
    numberOfWhiteUnits = 0
    for x in range(8):
        for y in range(8):
            if game.board[x][y] != None:
                if game.board[x][y].owner == game.white:
                    numberOfWhiteUnits += 1
    return numberOfWhiteUnits
