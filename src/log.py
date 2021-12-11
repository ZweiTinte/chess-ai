# coding: utf-8
from src.database import loadData
from src.databaseLocationString import generateDatabaseLocationString

LOG_FILE_NAME = "game_log.txt"

# appends text to the log file
def logToFile(text):
    f = open(LOG_FILE_NAME, "a")
    f.write(text + "\n")
    f.close()

# logs move to log file
def logMove(game, upx, upy, x, y):
    # preapare output string
    player = game.turn.getColor()
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
                logString += str(game.board[x][y].getPower())
            logString += " "
        logToFile(logString)

# logs the possible moves of a unit
def logPossibleMoves(game, x, y):
    possibleMoves = ""
    for m in game.board[x][y].moves:
        possibleMoves += m + ", "
    logToFile("\npossible moves: " + possibleMoves[:-2])

# logs the moveable units of the turn player
def logMoveableUnits(game):
    jsonFileString = generateDatabaseLocationString(game)
    data = loadData(jsonFileString)
    units = ""
    for u in data:
        units += u + ", "
    logToFile("moveable units: " + units[:-2])