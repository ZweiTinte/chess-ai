# coding: utf-8

def calculateBishopMoves(unit, player, game):
    position = game.getPositionOfUnit(unit)
    global x
    global y
    x = position[0]
    y = position[1]
    if y < game.upperLimit - 1:
        calculateUpperMoves(unit, player, game)
    if y > game.lowerLimit:
        calculateLowerMoves(unit, player, game)

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
