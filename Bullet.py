# Description:
# Created by Emilia and Amanda on 2024-08-30
import sys
import pygame
import time
import random
import math


class Bullet:
    SPEED = 3
    RADIUS = 20
    norm = (169,169,169)
    pyr = (239,122,53)
    hyd = (0, 191, 255)
    geo = (222, 189, 108)
    dend = (166,201,56)
    elec = (176,143,194)
    cry = (160,215,228)
    anem = (117,194,170)
    COLOURS = [norm, pyr, hyd, geo, dend, elec, cry, anem]
    element: int
    colour: tuple
    x: int
    y: int
    speed_x: int
    speed_y: int

    def __init__(self, element, x, y, dx, dy):
        self.element = element
        self.colour = self.COLOURS[element]
        self.x = x
        self.y = y
        self.speed_x = self.SPEED * dx
        self.speed_y = self.SPEED * dy

    def move(self, screen):
        # Change direction if collides with wall
        if self.collides(screen, self.x + self.speed_x, self.y):
            self.speed_x = -self.speed_x  # Reverse direction x
        if self.collides(screen, self.x, self.y + self.speed_y):
            self.speed_y = -self.speed_y  # Reverse direction y

        self.x += self.speed_x
        self.y += self.speed_y

    def collides(self, screen, new_x, new_y):
        for i in range(self.RADIUS * 2):
            for j in range(self.RADIUS * 2):
                if (math.sqrt((self.RADIUS - i) ** 2 + (self.RADIUS - j) ** 2)) <= self.RADIUS:
                    clr = screen.get_at((new_x - self.RADIUS + i, new_y - self.RADIUS + j))
                    if clr == (0, 0, 0):  # Check if the color is black
                        return True
        return False

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.RADIUS)

#pew pew
