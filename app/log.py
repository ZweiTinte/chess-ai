# coding: utf-8
from .database import loadData, writeData
from .databaseLocationString import DB_DIR_NAME, generateDatabaseLocationString
import os

LOG_FILE_NAME = "game_log.txt"
STATISTICS_DATA_FILE = "stats.json"
WARNINGS_FILE = "warnings.txt"

# appends text to the log file
def logToFile(text, fileName = LOG_FILE_NAME):
    f = open(fileName, "a")
    f.write(text + "\n")
    f.close()

# logs move to log file
def logMove(game, upx, upy, x, y):
    # preapare output string
    player = game.turn.color
    unit = game.board[upx][upy].getPowerString()
    position_x = game.getCharacterOfNumber(upx)
    position_y = str(upy + 1)
    target_x = game.getCharacterOfNumber(x)
    target_y = str(y + 1)

    # log to log file
    logToFile(player + " moves " + unit + " from " + position_x + position_y + " to " + target_x + target_y)

# logs the chess board to log file
def logBoard(game):
    for y in range(game.upperLimit):
        logString = ""
        for x in range(game.upperLimit):
            if game.board[x][y] == None:
                logString += "__"
            else:
                logString += game.board[x][y].owner.color[0].upper()
                logString += str(game.board[x][y].power)
            logString += " "
        logToFile(logString)

# logs the possible moves of a unit
def logPossibleMoves(game, x, y):
    possibleMoves = ""
    for m in game.board[x][y].moves:
        possibleMoves += m + ", "
    logToFile("possible moves: " + possibleMoves[:-2])

# logs the moveable units of the turn player
def logMoveableUnits(game):
    jsonFileString = generateDatabaseLocationString(game)
    data = loadData(jsonFileString)
    units = ""
    for u in data:
        units += u + ", "
    logToFile("moveable units: " + units[:-2])

def printAllDbFiles():
    for subdir, dirs, files in os.walk(DB_DIR_NAME):
        for file in files:
            print(os.path.join(subdir, file))

def getAllDbFiles():
    allFiles = []
    for subdir, dirs, files in os.walk(DB_DIR_NAME):
        for file in files:
            allFiles.append(os.path.join(subdir, file))
    return allFiles

def getAllWinChances():
    winChances = []
    for file in getAllDbFiles():
        data = loadData(file)
        for unit in data:
            for move in data[unit]:
                chances = data[unit][move]
                winChances.append(chances["w"] / (chances["w"] + chances["l"]))
    return winChances

def logTurnsTaken(turns):
    data = {}
    if os.path.exists(STATISTICS_DATA_FILE):
        data = loadData(STATISTICS_DATA_FILE)
    else:
        data["turns"] = []
    data["turns"].append(turns)
    writeData(STATISTICS_DATA_FILE, data)

def logLearningProgress(console = False):
    winChances = getAllWinChances()
    topTenAmount = 0
    bottomTenAmount = 0
    totalAmount = len(winChances)
    dataAvailable = totalAmount > 0

    if dataAvailable:
        for chance in winChances:
            if chance >= 0.9:
                topTenAmount += 1
            elif chance <= 0.1:
                bottomTenAmount += 1

        topTenPercentage = round(100 * topTenAmount / totalAmount, 2)
        bottomTenPercentage = round(100 * bottomTenAmount / totalAmount, 2)

    if console:
        if dataAvailable:
            print("Total amount of moves stored: " + str(totalAmount))
            print("Amount of moves with win chance >= 90%: " + str(topTenAmount))
            print("Amount of moves with win chance <= 10%: " + str(bottomTenAmount))
            print("Percentage of moves with win chance >= 90%: " + str(topTenPercentage) + "%")
            print("Percentage of moves with win chance <= 10%: " + str(bottomTenPercentage) + "%")
        else:
            print("Sorry, the database is empty :(")
    else:
        return {
            "Total amount of moves stored: ": str(totalAmount), 
            "Amount of moves with win chance >= 90%: ": str(topTenAmount),
            "Amount of moves with win chance <= 10%: ": str(bottomTenAmount),
            "Percentage of moves with win chance >= 90%: ": str(topTenPercentage) + "%",
            "Percentage of moves with win chance <= 10%: ": str(bottomTenPercentage) + "%"
        } if dataAvailable else {}