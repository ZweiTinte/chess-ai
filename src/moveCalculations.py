# coding: utf-8

from src.knightMoveCalculations import calculateKnightMoves
from src.rookMoveCalculations import calculateRookMoves
from src.pawnMoveCalculations import calculatePawnMoves
from src.unit import PAWN, ROOK

# calculates the possible moves for all units of a player
def calculatePossibleMoves(game, player, initialCall):
    for x in range(game.upperLimit):
        for y in range(game.upperLimit):
            unit = game.board[x][y]
            if unit != None and unit.owner == player:
                # pawn moves
                if unit.power == PAWN:
                    calculatePawnMoves(unit, player, game)
                # rook moves
                elif unit.getPower() == ROOK:
                    calculateRookMoves(unit, player, game)
                # knight moves
                elif unit.getPower() == 3:
                    calculateKnightMoves(unit, player, game)
                # bishop moves
                elif unit.getPower() == 4 or unit.getPower() == 5:
                    if y < 7:
                        for i in range(game.upperLimit - (y + 1)):
                            if y + i < game.upperLimit - 1 and x + i < game.upperLimit - 1:
                                if game.fieldIsEmpty(x + i + 1, y + i + 1):
                                    unit.addMove(
                                        str(x + i + 1) + str(y + i + 1))
                                elif game.board[x + i + 1][y + i + 1].owner == player.opponent:
                                    unit.addMove(
                                        str(x + i + 1) + str(y + i + 1))
                                    break
                                else:
                                    break
                        for i in range(game.upperLimit - (y + 1)):
                            if y + i < game.upperLimit - 1 and x - i > game.lowerLimit:
                                if game.fieldIsEmpty(x - i - 1, y + i + 1):
                                    unit.addMove(
                                        str(x - i - 1) + str(y + i + 1))
                                elif game.board[x - i - 1][y + i + 1].owner == player.opponent:
                                    unit.addMove(
                                        str(x - i - 1) + str(y + i + 1))
                                    break
                                else:
                                    break
                    if y > game.lowerLimit:
                        for i in range(y):
                            if y - i > game.lowerLimit and x + i < game.upperLimit - 1:
                                if game.fieldIsEmpty(x + i + 1, y - i - 1):
                                    unit.addMove(
                                        str(x + i + 1) + str(y - i - 1))
                                elif game.board[x + i + 1][y - i - 1].owner == player.opponent:
                                    unit.addMove(
                                        str(x + i + 1) + str(y - i - 1))
                                    break
                                else:
                                    break
                        for i in range(y):
                            if y - i > game.lowerLimit and x - i > game.lowerLimit:
                                if game.fieldIsEmpty(x - i - 1, y - i - 1):
                                    unit.addMove(
                                        str(x - i - 1) + str(y - i - 1))
                                elif game.board[x - i - 1][y - i - 1].owner == player.opponent:
                                    unit.addMove(
                                        str(x - i - 1) + str(y - i - 1))
                                    break
                                else:
                                    break
                # queen moves
                elif unit.getPower() == 6:
                    if y < 7:
                        for i in range(game.upperLimit - (y + 1)):
                            if y + i < game.upperLimit - 1 and x + i < game.upperLimit - 1:
                                if game.fieldIsEmpty(x + i + 1, y + i + 1):
                                    unit.addMove(
                                        str(x + i + 1) + str(y + i + 1))
                                elif game.board[x + i + 1][y + i + 1].owner == player.opponent:
                                    unit.addMove(
                                        str(x + i + 1) + str(y + i + 1))
                                    break
                                else:
                                    break
                        for i in range(game.upperLimit - (y + 1)):
                            if y + i < game.upperLimit - 1 and x - i > game.lowerLimit:
                                if game.fieldIsEmpty(x - i - 1, y + i + 1):
                                    unit.addMove(
                                        str(x - i - 1) + str(y + i + 1))
                                elif game.board[x - i - 1][y + i + 1].owner == player.opponent:
                                    unit.addMove(
                                        str(x - i - 1) + str(y + i + 1))
                                    break
                                else:
                                    break
                    if y > game.lowerLimit:
                        for i in range(y):
                            if y - i > game.lowerLimit and x + i < game.upperLimit - 1:
                                if game.fieldIsEmpty(x + i + 1, y - i - 1):
                                    unit.addMove(
                                        str(x + i + 1) + str(y - i - 1))
                                elif game.board[x + i + 1][y - i - 1].owner == player.opponent:
                                    unit.addMove(
                                        str(x + i + 1) + str(y - i - 1))
                                    break
                                else:
                                    break
                        for i in range(y):
                            if y - i > game.lowerLimit and x - i > game.lowerLimit:
                                if game.fieldIsEmpty(x - i - 1, y - i - 1):
                                    unit.addMove(
                                        str(x - i - 1) + str(y - i - 1))
                                elif game.board[x - i - 1][y - i - 1].owner == player.opponent:
                                    unit.addMove(
                                        str(x - i - 1) + str(y - i - 1))
                                    break
                                else:
                                    break
                    if y < 7:
                        for i in range(game.upperLimit - (y + 1)):
                            if game.fieldIsEmpty(x, y + i + 1):
                                unit.addMove(str(x) + str(y + i + 1))
                            elif game.board[x][y + i + 1].owner == player.opponent:
                                unit.addMove(str(x) + str(y + i + 1))
                                break
                            else:
                                break
                    if y > game.lowerLimit:
                        for i in range(y):
                            if game.fieldIsEmpty(x, y - (i + 1)):
                                unit.addMove(str(x) + str(y - i - 1))
                            elif game.board[x][y - (i + 1)].owner == player.opponent:
                                unit.addMove(str(x) + str(y - i - 1))
                                break
                            else:
                                break
                    if x < 7:
                        for i in range(game.upperLimit - (x + 1)):
                            if game.fieldIsEmpty(x + i + 1, y):
                                unit.addMove(str(x + i + 1) + str(y))
                            elif game.board[x + i + 1][y].owner == player.opponent:
                                unit.addMove(str(x + i + 1) + str(y))
                                break
                            else:
                                break
                    if x > game.lowerLimit:
                        for i in range(x):
                            if game.fieldIsEmpty(x - (i + 1), y):
                                unit.addMove(str(x - i - 1) + str(y))
                            elif game.board[x - (i + 1)][y].owner == player.opponent:
                                unit.addMove(str(x - i - 1) + str(y))
                                break
                            else:
                                break
                # king moves
                elif unit.getPower() == 7:
                    if y < 7:
                        if game.fieldIsEmpty(x, y + 1):
                            unit.addMove(str(x) + str(y + 1))
                        elif game.board[x][y + 1].owner == player.opponent:
                            unit.addMove(str(x) + str(y + 1))
                        if x < game.upperLimit - 1:
                            if game.fieldIsEmpty(x + 1, y + 1):
                                unit.addMove(str(x + 1) + str(y + 1))
                            elif game.board[x + 1][y + 1].owner == player.opponent:
                                unit.addMove(str(x + 1) + str(y + 1))
                        if x > game.lowerLimit:
                            if game.fieldIsEmpty(x - 1, y + 1):
                                unit.addMove(str(x - 1) + str(y + 1))
                            elif game.board[x - 1][y + 1].owner == player.opponent:
                                unit.addMove(str(x - 1) + str(y + 1))
                    if y > game.lowerLimit:
                        if game.fieldIsEmpty(x, y - 1):
                            unit.addMove(str(x) + str(y - 1))
                        elif game.board[x][y - 1].owner == player.opponent:
                            unit.addMove(str(x) + str(y - 1))
                        if x < game.upperLimit - 1:
                            if game.fieldIsEmpty(x + 1, y - 1):
                                unit.addMove(str(x + 1) + str(y - 1))
                            elif game.board[x + 1][y - 1].owner == player.opponent:
                                unit.addMove(str(x + 1) + str(y - 1))
                        if x - i > game.lowerLimit:
                            if game.fieldIsEmpty(x - 1, y - 1):
                                unit.addMove(str(x - 1) + str(y - 1))
                            elif game.board[x - 1][y - 1].owner == player.opponent:
                                unit.addMove(str(x - 1) + str(y - 1))
                    if x < game.upperLimit - 1:
                        if game.fieldIsEmpty(x + 1, y):
                            unit.addMove(str(x + 1) + str(y))
                        elif game.board[x + 1][y].owner == player.opponent:
                            unit.addMove(str(x + 1) + str(y))
                    if x > game.lowerLimit:
                        if game.fieldIsEmpty(x - 1, y):
                            unit.addMove(str(x - 1) + str(y))
                        elif game.board[x - 1][y].owner == player.opponent:
                            unit.addMove(str(x - 1) + str(y))
                    # castling calculation
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

# return true if the player is in check
def playerIsInCheck(game, player):
    calculatePossibleMoves(game, player.opponent, False)
    king_position = player.getKingPosition(game.board)
    for x in range(game.upperLimit):
        for y in range(game.upperLimit):
            unit = game.board[x][y]
            if unit != None:
                if unit.owner == player.opponent:
                    for move in unit.getMoves():
                        if move == king_position:
                            player.inCheck = True
    player.inCheck = False