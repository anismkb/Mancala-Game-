import random
from math import inf
import time
import pygame
# from board import Game, Board
from copy import deepcopy

class Play:
    # def __init__(self, game):
    #     self.game = game

    def NegaMaxAlphaBetaPruning (self, game, player, depth, alpha, beta):
        #game est une instance de la classe Game et player = COMPUTER ou HUMAN
        if game.gameOver() or depth == 1:
            bestValue = game.evaluate()
            bestPit = None
            if player == 1:
                bestValue = - bestValue
            return bestValue, bestPit
        
        bestValue = -inf
        bestPit = None
        for pit in game.state.possibleMoves(player):
            
            child_game = deepcopy(game)
            player_turn =  child_game.state.doMove(player, pit)
            # print(game.state.board['A'])

            if player_turn == player:
                value, _ = self.NegaMaxAlphaBetaPruning (child_game, player, depth-1, -beta, -alpha) 
            else:
                value, _ = self.NegaMaxAlphaBetaPruning (child_game, -player, depth-1, -beta, -alpha) 
                
            value = - value
            if value > bestValue :
                bestValue = value
                bestPit =pit

            if bestValue > alpha :
                alpha = bestValue

            if beta <= alpha :
                break
        return bestValue, bestPit
    
    def humanTurn(self,cle,game):
        list = game.state.possibleMoves(1)
        if cle in list :
            game.state.doMove(1,cle)


    def computerTrun(self, game):
        game.state.doMove(self.NegaMaxAlphaBetaPruning(self,"COMPUTER", 10, -inf, +inf),-1)

# board = Board()
# game = Game(board)
# play = Play()
