# coding: utf-8

def calculateKingMoves(unit, player, game):
    position = game.getPositionOfUnit(unit)
    global x
    global y
    x = position[0]
    y = position[1]
    if y < 7:
        calculateUpperMoves(unit, player, game)
    if y > game.lowerLimit:
        calculateLowerMoves(unit, player, game)
    calculateHorizontalMoves(unit, player, game)

def calculateUpperMoves(unit, player, game):
    targetX = x
    targetY = y + 1
    addMoveIfTargetFieldIsEmptyOrOpponentUnit(targetX, targetY, unit, player, game)
    if x < game.upperLimit - 1:
        targetX = x + 1
        addMoveIfTargetFieldIsEmptyOrOpponentUnit(targetX, targetY, unit, player, game)
    if x > game.lowerLimit:
        targetX = x - 1
        addMoveIfTargetFieldIsEmptyOrOpponentUnit(targetX, targetY, unit, player, game)

def calculateLowerMoves(unit, player, game):
    targetX = x
    targetY = y - 1
    addMoveIfTargetFieldIsEmptyOrOpponentUnit(targetX, targetY, unit, player, game)
    if x < game.upperLimit - 1:
        targetX = x +1
        addMoveIfTargetFieldIsEmptyOrOpponentUnit(targetX, targetY, unit, player, game)
    if x - 1 > game.lowerLimit:
        targetX = x - 1
        addMoveIfTargetFieldIsEmptyOrOpponentUnit(targetX, targetY, unit, player, game)

def calculateHorizontalMoves(unit, player, game):
    targetY = y
    if x < game.upperLimit - 1:
        targetX = x + 1
        addMoveIfTargetFieldIsEmptyOrOpponentUnit(targetX, targetY, unit, player, game)
    if x > game.lowerLimit:
        targetX = x -1
        addMoveIfTargetFieldIsEmptyOrOpponentUnit(targetX, targetY, unit, player, game)

def addMoveIfTargetFieldIsEmptyOrOpponentUnit(targetX, targetY, unit, player, game):
    if game.fieldIsEmpty(targetX, targetY):
        unit.addMoveByPosition(targetX, targetY)
    elif game.board[targetX][targetY].owner == player.opponent:
        unit.addMoveByPosition(targetX, targetY)