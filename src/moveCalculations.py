# coding: utf-8

from src.kingMoveCalculations import calculateKingMoves
from src.queenMoveCalculations import calculateQueenMoves
from src.bishopMoveCalculations import calculateBishopMoves
from src.knightMoveCalculations import calculateKnightMoves
from src.rookMoveCalculations import calculateRookMoves
from src.pawnMoveCalculations import calculatePawnMoves
from src.unit import BISHOPL, BISHOPR, KNIGHT, PAWN, QUEEN, ROOK

# calculates the possible moves for all units of a player
def calculatePossibleMoves(game, player, initialCall = True):
    for x in range(game.upperLimit):
        for y in range(game.upperLimit):
            unit = game.board[x][y]
            if unit != None and unit.owner == player:
                if unit.power == PAWN:
                    calculatePawnMoves(unit, player, game)
                elif unit.power == ROOK:
                    calculateRookMoves(unit, player, game)
                elif unit.power == KNIGHT:
                    calculateKnightMoves(unit, player, game)
                elif unit.power == BISHOPL or unit.power == BISHOPR:
                    calculateBishopMoves(unit, player, game)
                elif unit.power == QUEEN:
                    calculateQueenMoves(unit, player, game)
                elif unit.power == 7:
                    calculateKingMoves(unit, player, game)
                    if initialCall:
                        calculateCastling(game, player, unit)
                            
# castling calculation
def calculateCastling(game, player, unit):
    playerIsInCheck(game, player)
    if not player.inCheck and player.castlingIsPermitted():
        if player == game.black:
            if not game.fieldIsEmpty(game.lowerLimit, game.upperLimit - 1):
                if game.board[0][7].getPower() == 2:
                    if not game.board[game.lowerLimit][game.upperLimit - 1].moved:
                        if game.fieldIsEmpty(game.lowerLimit + 1, game.upperLimit - 1):
                            if game.fieldIsEmpty(game.lowerLimit + 2, game.upperLimit - 1):
                                if game.fieldIsEmpty(game.lowerLimit + 3, game.upperLimit - 1):
                                    unit.addMove("cl")
            if not game.fieldIsEmpty(game.upperLimit - 1, game.upperLimit - 1):
                if game.board[game.upperLimit - 1][game.upperLimit - 1].getPower() == 2:
                    if not game.board[game.upperLimit - 1][game.upperLimit - 1].moved:
                        if game.fieldIsEmpty(game.upperLimit - 2, game.upperLimit - 1):
                            if game.fieldIsEmpty(game.upperLimit - 3, game.upperLimit - 1):
                                unit.addMove("cr")
        elif player == game.white:
            if not game.fieldIsEmpty(game.lowerLimit, game.lowerLimit):
                if game.board[game.lowerLimit][game.lowerLimit].getPower() == 2:
                    if not game.board[game.lowerLimit][game.lowerLimit].moved:
                        if game.fieldIsEmpty(game.lowerLimit + 1, game.lowerLimit):
                            if game.fieldIsEmpty(game.lowerLimit + 2, game.lowerLimit):
                                if game.fieldIsEmpty(game.lowerLimit + 3, game.lowerLimit):
                                    unit.addMove("cl")
            if not game.fieldIsEmpty(game.upperLimit - 1, game.lowerLimit):
                if game.board[game.upperLimit - 1][game.lowerLimit].getPower() == 2:
                    if not game.board[game.upperLimit - 1][game.lowerLimit].moved:
                        if game.fieldIsEmpty(game.upperLimit - 2, game.lowerLimit):
                            if game.fieldIsEmpty(game.upperLimit - 3, game.lowerLimit):
                                unit.addMove("cr")

def playerIsInCheck(game, player):
    calculatePossibleMoves(game, player.opponent, False)
    kingPosition = player.getKingPosition(game.board)
    for x in range(game.upperLimit):
        for y in range(game.upperLimit):
            unit = game.board[x][y]
            if unit != None:
                if unit.owner == player.opponent:
                    for move in unit.moves:
                        if move == kingPosition:
                            player.inCheck = True
                            return
    player.inCheck = False