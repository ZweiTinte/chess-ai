# coding: utf-8

def calculateKnightMoves(unit, player, game):
    position = game.getPositionOfUnit(unit)
    global x
    global y
    x, y = position
    if y < game.upperLimit - 1:
        calculateUpperMoves(unit, player, game)
    if y > game.lowerLimit:
        calculateLowerMoves(unit, player, game)

def calculateUpperMoves(unit, player, game):
    if x > 1:
        addMoveIfTargetFieldIsEmptyOrOpponentUnit(x - 2, y + 1, unit, player, game)
    if x < 6:
        addMoveIfTargetFieldIsEmptyOrOpponentUnit(x + 2, y + 1, unit, player, game)
    if y < game.upperLimit - 2:
        if x > game.lowerLimit:
            addMoveIfTargetFieldIsEmptyOrOpponentUnit(x - 1, y + 2, unit, player, game)
        if x < 7:
            addMoveIfTargetFieldIsEmptyOrOpponentUnit(x + 1, y + 2, unit, player, game)

def calculateLowerMoves(unit, player, game):
    if x > 1:
        addMoveIfTargetFieldIsEmptyOrOpponentUnit(x - 2, y - 1, unit, player, game)
    if x < 6:
        addMoveIfTargetFieldIsEmptyOrOpponentUnit(x + 2, y - 1, unit, player, game)
    if y > 1:
        if x > game.lowerLimit:
            addMoveIfTargetFieldIsEmptyOrOpponentUnit(x - 1, y - 2, unit, player, game)
        if x < 7:
            addMoveIfTargetFieldIsEmptyOrOpponentUnit(x + 1, y - 2, unit, player, game)

def addMoveIfTargetFieldIsEmptyOrOpponentUnit(targetX, targetY, unit, player, game):
    if game.fieldIsEmpty(targetX, targetY):
        unit.addMoveByPosition(targetX, targetY)
    elif game.board[targetX][targetY].owner == player.opponent:
        unit.addMoveByPosition(targetX, targetY)
