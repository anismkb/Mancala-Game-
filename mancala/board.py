import random
from math import inf
import time
import pygame

screen_width = 1000
screen_height = 700
x = 1000/8
y = 80
bg = (204, 102, 0)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0,220,0)
gris = (200,200,200)
white = (255, 255, 255)
class Board:
    def __init__(self):
        self.board = {'1':0 ,'A':4 ,'B':4 ,'C':4 ,'D':4 ,'E':4 ,'F':4 , 
                      '2':0 ,'G':4 ,'H':4 ,'I':4 ,'J':4 ,'K':4 ,'L':4}

        self.boardAxis = {'1':(x*7+(120/2), 140+(330/2)) ,'A':(x*1+60,400) ,'B':(x*2+60,400) ,'C':(x*3+60,400) ,'D':(x*4+60,400) ,'E':(x*5+60,400) ,'F':(x*6+60,400) , 
                          '2':(2  +(120/2), 140+(330/2)) ,'G':(x*1+60,200) ,'H':(x*2+60,200) ,'I':(x*3+60,200) ,'J':(x*4+60,200) ,'K':(x*5+60,200) ,'L':(x*6+60,200)}

        self.joueur1 = ('A','B','C','D','E','F')
        self.joueur2 = ('G','H','I','J','K','L')

        self.FosseSuiv = {'1':'L' ,'A':'B', 'B':'C' ,'C':'D' ,'D':'E' ,'E':'F' ,'F':'1' , 
                          '2':'A' ,'G':'2', 'H':'G' ,'I':'H' ,'J':'I' ,'K':'J' ,'L':'K'}

        self.FosseOpos = {'A':'G', 'B':'H','C':'I' ,'D':'J' ,'E':'K' ,'F':'L' , 
                          'G':'A' ,'H':'B','I':'C' ,'J':'D' ,'K':'E' ,'L':'F'}

    def drawBoard(self, win):
        for cle in self.board:
            if cle != '1' and cle != '2':
                pygame.draw.circle(win, white, self.boardAxis[cle], 60)
                font = pygame.font.Font('freesansbold.ttf', 28)
                text = font.render(str(self.board[cle]), True, black )
                textRect = text.get_rect()
                textRect.center = self.boardAxis[cle]
                win.blit(text, textRect)

        pygame.draw.rect(win, white, (x*7, 140, 120, 330),  0,40)
        text = font.render(str(self.board['1']), True, black )
        textRect = text.get_rect()
        textRect.center = self.boardAxis['1']
        win.blit(text, textRect)

        pygame.draw.line(win, red, (x+20,300) , (x*7 - 20,300), 10)
        pygame.draw.rect(win, white, (2 , 140, 120, 330),  0,40)
        text = font.render(str(self.board['2']), True, black )
        textRect = text.get_rect()
        textRect.center = self.boardAxis['2']
        win.blit(text, textRect)

    def drawTurn(self,player,win):
        pygame.draw.rect(win, gris, (270 , 30, 400, 100),  0,20)
        font = pygame.font.Font('freesansbold.ttf', 50)
        if player == 1:
            text = font.render('Your Turn :', True, green )
        else:
            text = font.render('Computer Turn :', True, black )
        textRect = text.get_rect()
        textRect.center = (470,80)
        win.blit(text, textRect)

    def colorPossibleMoves(self,win,joueur):
        list = self.possibleMoves(joueur)
        for cle in list:
            pygame.draw.circle(win, green, self.boardAxis[cle], 60)
            font = pygame.font.Font('freesansbold.ttf', 28)
            text = font.render(str(self.board[cle]), True, black )
            textRect = text.get_rect()
            textRect.center = self.boardAxis[cle]
            win.blit(text, textRect)

    
    def possibleMoves(self,joueur):#return les indice des fosse du joueur qui contiennent des graines
        list = []
        for cle, valeur in self.board.items():
            if joueur == 1:
                if cle != '1' and cle != '2' and cle in self.joueur1 :
                    if valeur != 0:
                        list.append(cle)
            else :
                if cle != '1' and cle != '2' and cle in self.joueur2 :
                    if valeur != 0:
                        list.append(cle)
        return list

    def doMove(self,joueur,cle):
        val = self.board[cle]
        self.board[cle] = 0
        x = self.FosseSuiv[cle]
        if joueur == 1 and x == '2':
            x = self.FosseSuiv[x]
        if joueur == -1 and x == '1': 
            x = self.FosseSuiv[x]
        
        for i in range(val):
            if self.board[x] == 0 and i == (val-1) and x != '1' and x != '2': #lhaba lakhra dans une fosse vide
                # print('dkhol b fosse vide psq')
                if joueur == 1 and (x in self.joueur1):
                    opos = self.FosseOpos[x]
                    stones = self.board[opos]
                    self.board[opos] = 0
                    self.board['1'] = self.board['1'] + stones + 1
                elif joueur == -1 and (x in self.joueur2):
                    opos = self.FosseOpos[x]
                    stones = self.board[opos]
                    self.board[opos] = 0
                    self.board['2'] = self.board['2'] + stones + 1
                # else:
                #     self.board[x] = self.board[x] + 1
            else:
                # if(x == '2' and joueur == -1):
                #     print(self.board[x])
                self.board[x] = self.board[x] + 1
                

            y = x # garde trace de x
            x = self.FosseSuiv[x]
            if joueur == 1 and x == '2':
                x = self.FosseSuiv[x]
            if joueur == -1 and x == '1':
                x = self.FosseSuiv[x]
        
        if joueur == 1 :
            # print("laste ball was in "+str(y))
            if y == '1':
                return 1
            else:
                return -1

        elif joueur == -1:
            # print("laste ball was in "+str(y))
            if y == '2':
                return -1
            else:
                return 1

class Game: # represente le noeud de l'arbre de recherche
    def __init__(self, mancalaBoard):
        self.state = mancalaBoard
    
    def gameOver(self):
        vide1 = True
        vide2 = True
        for x in self.state.joueur1:
            if self.state.board[x] != 0:
                vide1 = False
                break
        for x in self.state.joueur2:
            if self.state.board[x] != 0:
                vide2 = False
                break
        som1 = 0
        som2 = 0
        if vide1 == True :
            #recolt tout les graines de l'adverssair et les met dans son magasin
            for x in self.state.joueur2:
                self.state.board[x] = 0
                som2 = som2 + self.state.board[x]
            self.state.board['2'] = self.state.board['2'] + som2
        
        if vide2 == True :
            for x in self.state.joueur1:
                self.state.board[x] = 0
                som1 = som1 + self.state.board[x]
            self.state.board['1'] = self.state.board['1'] + som1
        
        return vide1 or vide2

    def findWinner(self):
        if self.state.board['1'] > self.state.board['2']:
            return 1, self.state.board['1']
        elif self.state.board['2'] > self.state.board['1']:
            return -1, self.state.board['2']
        else:
            return 0, self.state.board['1']
    
    def evaluate(self):
        return self.state.board['1'] - self.state.board['2']

# class Play:
#     def __init__(self, mancalaBoard):
#         self.state = mancalaBoard

#     def humanTurn(self,cle, joueur):
#         turn = self.state.doMove(self,cle,joueur)
#         return turn

# board = Board()
# x = board.doMove(1,'A')

# print(board.board['A'])
# print(board.board['B'])
# print(board.board['C'])
# print(board.board['D'])
# print(board.board['E'])
# print(board.board['F'])
# print(board.board['G'])
# print(board.board['H'])
