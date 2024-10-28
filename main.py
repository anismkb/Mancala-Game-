import pygame
from pygame.locals import *
import pygame.gfxdraw
import time
from math import inf
import pygame, sys
from mancala.board import Board, Game
from mancala.play import Play
import math
pygame.init()

screen_width = 1000
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))

def get_fosse_from_mouse(pos,game, joueur):
    list = game.state.possibleMoves(joueur)
    for cle in list:
        Axis = game.state.boardAxis[cle]
        distance = math.sqrt((pos[0]-Axis[0])**2 + (pos[1]-Axis[1])**2)
        if distance <= 60 :
            return cle

bg = (204, 102, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
green = (50,205,50)
gris = (200,200,200)
backcolour = pygame.color.Color(100,0,0)
x = 1000/8
y = 80
board = Board()
game = Game(board)
play = Play()
player = 1
while True:
    # board.drawTurn(player, screen)
    screen.fill(backcolour)
    board.drawBoard(screen)
    if player == 1:
        board.colorPossibleMoves(screen,player)
    board.drawTurn(player, screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and player == 1:
            pos = pygame.mouse.get_pos()
            # if pos is not None :
            fosse = get_fosse_from_mouse(pos,game, player)
            # print(fosse)
            if fosse != None : 
                # board.drawTurn(player, screen)
                if game.gameOver() == False :
                    player = game.state.doMove(player, fosse)
                    board.drawBoard(screen)
                    pygame.display.update()
                    time.sleep(1)
                else:
                    print('game Over')
    
        
    if player == -1 :
        board.drawTurn(player, screen)
        bestValue, bestPit =play.NegaMaxAlphaBetaPruning(game, player, 2, -inf, inf)
        if bestPit != None :
            player =  game.state.doMove(player, bestPit)
            # print(player)
            # print(game.state.board['2'])
            board.drawBoard(screen)
            pygame.display.update()
            time.sleep(1)

    if game.gameOver():
        while True :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            winer, score = game.findWinner()
            screen.fill(backcolour)
            pygame.draw.rect(screen, gris, (150 , 30, 680, 500),  0,20)
            font = pygame.font.Font('freesansbold.ttf', 48)
            if winer == -1:
                text = font.render('You are Lose ! Your Score :'+str(game.state.board['1']), True, red )
                text4 = font.render('Computer Score: '+str(score), True, black)
                textRect4 = text4.get_rect()
                textRect4.center = (475,150)
                screen.blit(text4, textRect4)
            elif winer == 1:
                text = font.render('You are win ! Score: '+str(score), True, green )
                text2 = font.render('Congratulation .. !', True, black )
                text3 = font.render('Computer Score: '+str(game.state.board['2']), True, red)
                textRect3 = text3.get_rect()
                textRect3.center = (460,300)
                textRect2 = text2.get_rect()
                textRect2.center = (475,150)
                screen.blit(text2, textRect2)
                screen.blit(text3, textRect3)
            else:
                text = font.render('No one win ! Score : '+str(score), True, green )
            textRect = text.get_rect()
            textRect.center = (460,250)
            screen.blit(text, textRect)
            pygame.display.update()

    # print(bestPit)
    # player_turn =  game.state.doMove(1, bestPit)

    # time.sleep(1)

    # stop = True
    # while stop:
    #     pass