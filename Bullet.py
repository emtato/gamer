# Description:
# Created by Emilia and Amanda on 2024-08-30
import sys
import pygame
import pygame.Color
import time
import random

class Bullet:
    BULLET_SPEED = 10
    BULLET_RADIUS = 5
    COLOURS = [Color(100, 100, 100),Color(r, g, b),Color(r, g, b),Color(r, g, b),Color(r, g, b),Color(r, g, b),Color(r, g, b)]
    def __init__(self, element, x, y):
        self.element = element
        self.colour = self.COLOURS[element]
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0

    def collision(self):

    def draw(self, screen):
        pygame.draw.circle(screen, )



#pew pew
