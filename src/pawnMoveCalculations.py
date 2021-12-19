# coding: utf-8

from src.unit import PAWN

PASSANT_RIGHT = "pr"
PASSANT_LEFT = "pl"

def calculatePawnMoves(unit, player, game):
    position = game.getPositionOfUnit(unit)
    x = position[0]
    y = position[1]
    if player == game.white:
        calculateWhitePawnMoves(unit, game, x, y)
    elif player == game.black:
        calculateBlackPawnMoves(unit, game, x, y)
    calculateEnPassantMoves(unit, game, x, y)

def calculateWhitePawnMoves(unit, game, x, y):
    if y + 1 < game.upperLimit:
        if game.fieldIsEmpty(x, y + 1):
            if y + 2 == game.upperLimit:
                game.addPromotionMovesToUnit(unit, x, y + 1)
            else:
                unit.addMove(str(x) + str(y + 1))
                if game.fieldIsEmpty(x, y + 2) and y == 1:
                    unit.addMove(str(x) + str(y + 2))
        if x - 1 >= game.lowerLimit and not game.fieldIsEmpty(x - 1, y + 1):
            if game.board[x - 1][y + 1].owner == game.black:
                if y + 2 == game.upperLimit:
                    game.addPromotionMovesToUnit(unit, x - 1, y + 1)
                else:
                    unit.addMove(str(x - 1) + str(y + 1))
        if x + 1 < game.upperLimit and not game.fieldIsEmpty(x + 1, y + 1):
            if game.board[x + 1][y + 1].owner == game.black:
                if y + 2 == game.upperLimit:
                    game.addPromotionMovesToUnit(unit, x + 1, y + 1)
                else:
                    unit.addMove(str(x + 1) + str(y + 1))

def calculateBlackPawnMoves(unit, game, x, y):
    if y - 1 >= game.lowerLimit:
        if game.fieldIsEmpty(x, y - 1):
            if y - 1 == game.lowerLimit:
                game.addPromotionMovesToUnit(unit, x, y - 1)
            else:
                unit.addMove(str(x) + str(y - 1))
                if game.fieldIsEmpty(x, y - 2) and y == 6:
                    unit.addMove(str(x) + str(y - 2))
        if x - 1 >= game.lowerLimit and not game.fieldIsEmpty(x - 1, y - 1):
            if game.board[x - 1][y - 1].owner == game.white:
                if y - 1 == game.lowerLimit:
                    game.addPromotionMovesToUnit(unit, x - 1, y - 1)
                else:
                    unit.addMove(str(x - 1) + str(y - 1))
        if x + 1 < game.upperLimit and not game.fieldIsEmpty(x + 1, y - 1):
            if game.board[x + 1][y - 1].owner == game.white:
                if y - 1 == game.lowerLimit:
                    game.addPromotionMovesToUnit(unit, x + 1, y - 1)
                else:
                    unit.addMove(str(x + 1) + str(y - 1))

def calculateEnPassantMoves(unit, game, x, y):
    owner = unit.owner
    if (y == 4 and owner == game.white) or (y == 3 and owner == game.black):
        if x < game.upperLimit - 1:
            opponentUnit = game.board[x + 1][y]
            if opponentUnit != None and opponentUnit.isPassantUnit:
                unit.addMove(PASSANT_RIGHT)
        if x > game.lowerLimit:
            opponentUnit = game.board[x - 1][y]
            if opponentUnit != None and opponentUnit.isPassantUnit:
                unit.addMove(PASSANT_LEFT)