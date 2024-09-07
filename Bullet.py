# Description:
# Created by Emilia and Amanda on 2024-08-30
import sys
import pygame
import pygame.Color
import time
import random
import math

class Bullet:
    SPEED = 3
    RADIUS = 20
    COLOURS = [(190,190,190)]
    def __init__(self, element, x, y,dX,dY):
        self.element = element
        self.colour = self.COLOURS[element]
        self.x = x
        self.y = y
        self.speedX = self.SPEED*dX
        self.speedY = self.SPEED*dY

    def move(self, screen):
        #self.react(self.getCollisions(screen),screen)
        self.x += self.speedX
        self.y += self.speedY
    '''
    def react(self,collisions,screen):
        xMoved = False
        yMoved = True
        for (x, y, clr) in self.getCollisions():
            if(clr==Color(0, 0, 0)):
                if (screen.get_at((x-4,y))==)
                if(not xMoved):
                    if (x<self.x and y<self.y)
            if(clr==self.COLOURS[-1]):
                if(not yMoved):
            if(clr==self.COLOURS[0]):
                return
    '''
    def getCollisions(self, screen):
        collided = []
        for i in range(self.RADIUS*2):
            for r in range(self.RADIUS*2):
                if(math.sqrt((self.RADIUS-i)**2+(self.RADIUS-r)**2))<=self.RADIUS:
                    clr = screen.get_at((self.x-self.RADIUS+i,self.y-self.RADIUS+r))
                    collided.append(((self.x-self.RADIUS+i,self.y-self.RADIUS+r,clr)))
        return collided
    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y),self.RADIUS)

#pew pew
