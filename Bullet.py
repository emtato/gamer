# Description:
# Created by Emilia and Amanda on 2024-08-30
import sys
import pygame
import time
import random

class Bullet:
    SPEED = 10
    RADIUS = 5
    COLOURS = [(190,190,190)]
    def __init__(self, element, x, y):
        self.element = element
        self.colour = self.COLOURS[element]
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0

    def collision(self):
        return True
    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y),self.RADIUS)


#pew pew
