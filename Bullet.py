# Description:
# Created by Emilia and Amanda on 2024-08-30
import sys
import pygame
import time
import random
from main import Window, clock, loadLevel

class Bullet:
    BULLET_SPEED = 10
    BULLET_RADIUS = 5
    COLOURS = [Color(r, g, b),Color(r, g, b),Color(r, g, b),Color(r, g, b),[],[],[]]
    def __init__(self, element, x, y):
        self.element = element
        self.colour = self.COLOURS[element]
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0

    def collision(self):

    def draw(self, screen):
        pygame.draw.circle(Window, 'grey', [600, 600], 30)





#pew pew
