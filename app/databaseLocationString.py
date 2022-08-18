# coding: utf-8
import os.path

DB_DIR_NAME = "db"

def makeDir(location):
    if not os.path.exists(location):
        os.makedirs(location)

# returns database location string for current state
def generateDatabaseLocationString(game):
    (   numberOfUnits, numberOfWhiteUnits, whiteUnitsString, 
        blackUnitsString, whiteUnitsPositionsString, blackUnitsPositionsString
    ) = getBoardInformation(game)
    paths = [
        f"{str(numberOfWhiteUnits)}/",
        f"{whiteUnitsString}/",
        f"{blackUnitsString}/",
        f"{whiteUnitsPositionsString}/",
        f"{blackUnitsPositionsString}/",
        f"{game.turn.color}/",
        "data.json"
    ]
    dbLocationString = f"{DB_DIR_NAME}/{str(numberOfUnits)}/"
    for path in paths:
        makeDir(dbLocationString)
        dbLocationString += path
    return dbLocationString

def getBoardInformation(game):
    numberOfUnits = numberOfWhiteUnits = 0
    whiteUnitsString = blackUnitsString = whiteUnitsPositionsString = blackUnitsPositionsString = ""
    for p in range(7):
        for x in range(8):
            for y in range(8):
                unit = game.board[x][y]
                if unit is not None:
                    numberOfUnits += 1
                    if unit.owner is game.white:
                        numberOfWhiteUnits += 1
                        if unit.power is p + 1:
                            whiteUnitsPositionsString += str(x) + str(y)
                            whiteUnitsString += str(p + 1)
                    if unit.owner is game.black:
                        if unit.power is p + 1:
                            blackUnitsPositionsString += str(x) + str(y)
                            blackUnitsString += str(p + 1)
    return (
        numberOfUnits, numberOfWhiteUnits, whiteUnitsString,
        blackUnitsString, whiteUnitsPositionsString, blackUnitsPositionsString
    )

def getNumberOfUnits(game):
    numberOfUnits = numberOfWhiteUnits = 0
    for x in range(8):
        for y in range(8):
            unit = game.board[x][y]
            if unit is not None:
                numberOfUnits += 1
                if unit.owner is game.white:
                    numberOfWhiteUnits += 1
    return (numberOfUnits, numberOfWhiteUnits)
