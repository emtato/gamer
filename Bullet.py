# Description:
# Created by Emilia and Amanda on 2024-08-30
import sys
import pygame
import time
import random
import math
pygame.mixer.init()
bounce = pygame.mixer.Sound("files/bounce.mp3")


class Bullet:
    #SPEED = 3 useless attribute?
    RADIUS = 10
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
    speed_x: float
    speed_y: float
    win: bool

    def __init__(self, element, x, y, dx, dy):
        self.element = element
        self.colour = self.COLOURS[element]
        self.x = x
        self.y = y
        self.speed_x = dx
        self.speed_y = dy
        self.win = False

    def __repr__(self):
        return f"elm={self.element}"
    def __str__(self):
        return self.element

    #funky if added some amount of quirky randomness (the current amount of randomness is so the bullet doesnt form loops as i've tested)
    #the randomness i suggest above could be a level specific property where the bounces are chaotic
    def move(self, screen):
        rx, ry =random.uniform(0.5, 1), random.uniform(0.5, 1) #change to like 20 50 for fun
        # Change direction if collides with wall
        if self.collides(screen, self.x + self.speed_x, self.y):
            self.speed_x =- (self.speed_x + rx)# Reverse direction x
        if self.collides(screen, self.x, self.y + self.speed_y):
            self.speed_y = -(self.speed_y +ry) # Reverse direction y

        self.x += self.speed_x
        self.y += self.speed_y

    #change collides to bounding box way more efficient
    def collides(self, screen, new_x, new_y):
        for i in range(int(self.RADIUS/3), self.RADIUS):
            for j in range(int(self.RADIUS/3), self.RADIUS): #o(n^2) algorithm inneficient :nerd:
                if (math.sqrt((self.RADIUS - i) ** 2 + (self.RADIUS - j) ** 2)) <= self.RADIUS:
                    clr = screen.get_at((round(new_x - self.RADIUS + i), round(new_y - self.RADIUS + j)))
                    if clr == (0, 0, 0):  # Check if the color is black
                        pygame.mixer.Sound.play(bounce) #this sound gets anoying as shit very fast find another or no sound at all?
                        pygame.mixer.music.stop()
                        return True
                    if clr == (114, 245, 74): #check if bullet touches ending square = win
                        self.win = True
                        print('win!!!! :DDD')
        return False

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.RADIUS)

#pew pew
