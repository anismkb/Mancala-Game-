import pygame
from pygame.locals import *
import pygame.gfxdraw
import time
from math import inf
import pygame, sys
from board import Board


screen_width = 1000
screen_height = 700

x = 1000/8
y = 80

class noeud():
    def __init__(self, value):
        self.x = 0
        self.y = 0
        self.calPos()
        self.value = value
        pass

    def drawFosse(self):
        pass
    
    def calPos(self):
        pass
