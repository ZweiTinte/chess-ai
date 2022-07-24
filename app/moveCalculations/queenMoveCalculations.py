# coding: utf-8

def calculateQueenMoves(unit, player, game):
    position = game.getPositionOfUnit(unit)
    global x
    global y
    x = position[0]
    y = position[1]
    if y < game.upperLimit - 1:
        calculateUpMoves(unit, player, game)
    if y > game.lowerLimit:
        calculateDownMoves(unit, player, game)
    if x < game.upperLimit - 1:
        calculateRightMoves(unit, player, game)
    if x > game.lowerLimit:
        calculateLeftMoves(unit, player, game)
    if y < game.upperLimit - 1:
        calculateUpperMoves(unit, player, game)
    if y > game.lowerLimit:
        calculateLowerMoves(unit, player, game)

def calculateUpMoves(unit, player, game):
    for i in range(game.upperLimit - (y + 1)):
        targetY = y + i + 1
        if game.fieldIsEmpty(x, targetY):
            unit.addMoveByPosition(x, targetY)
        elif game.board[x][targetY].owner == player.opponent:
            unit.addMoveByPosition(x, targetY)
            break
        else:
            break

def calculateDownMoves(unit, player, game):
    for i in range(y):
        targetY = y - i - 1
        if game.fieldIsEmpty(x, targetY):
            unit.addMoveByPosition(x, targetY)
        elif game.board[x][targetY].owner == player.opponent:
            unit.addMoveByPosition(x, targetY)
            break
        else:
            break

def calculateRightMoves(unit, player, game):
    for i in range(game.upperLimit - (x + 1)):
        targetX = x + i + 1
        if game.fieldIsEmpty(targetX, y):
            unit.addMoveByPosition(targetX, y)
        elif game.board[targetX][y].owner == player.opponent:
            unit.addMoveByPosition(targetX, y)
            break
        else:
            break

def calculateLeftMoves(unit, player, game):
    for i in range(x):
        targetX = x - i - 1
        if game.fieldIsEmpty(targetX, y):
            unit.addMoveByPosition(targetX, y)
        elif game.board[targetX][y].owner == player.opponent:
            unit.addMoveByPosition(targetX, y)
            break
        else:
            break

def calculateUpperMoves(unit, player, game):
    for i in range(game.upperLimit - (y + 1)):
        if y + i < game.upperLimit - 1 and x + i < game.upperLimit - 1:
            targetX = x + i + 1
            targetY = y + i + 1
            if game.fieldIsEmpty(targetX, targetY):
                unit.addMoveByPosition(targetX, targetY)
            elif game.board[targetX][targetY].owner == player.opponent:
                unit.addMoveByPosition(targetX, targetY)
                break
            else:
                break
    for i in range(game.upperLimit - (y + 1)):
        if y + i < game.upperLimit - 1 and x - i > game.lowerLimit:
            targetX = x - i - 1
            targetY = y + i + 1
            if game.fieldIsEmpty(targetX, targetY):
                unit.addMoveByPosition(targetX, targetY)
            elif game.board[targetX][targetY].owner == player.opponent:
                unit.addMoveByPosition(targetX, targetY)
                break
            else:
                break

def calculateLowerMoves(unit, player, game):
    for i in range(y):
        if y - i > game.lowerLimit and x + i < game.upperLimit - 1:
            targetX = x + i + 1
            targetY = y - i - 1
            if game.fieldIsEmpty(targetX, targetY):
                unit.addMoveByPosition(targetX, targetY)
            elif game.board[targetX][targetY].owner == player.opponent:
                unit.addMoveByPosition(targetX, targetY)
                break
            else:
                break
    for i in range(y):
        if y - i > game.lowerLimit and x - i > game.lowerLimit:
            targetX = x - i - 1
            targetY = y - i - 1
            if game.fieldIsEmpty(targetX, targetY):
                unit.addMoveByPosition(targetX, targetY)
            elif game.board[targetX][targetY].owner == player.opponent:
                unit.addMoveByPosition(targetX, targetY)
                break
            else:
                break