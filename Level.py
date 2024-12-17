# Description:
# Created by Emilia and Amanda on 2024-08-30
import math
import sys
import pygame
import time
import random

from Bullet import Bullet


class Level:
    level_num: int
    image: pygame.Surface  # background image
    playerX: int
    playerY: int
    bullets: list
    bullet_poof: int
    obstacle_data: list
    duck_image = pygame.image.load('duck.png')

    def __init__(self, level_num):
        self.level_num = level_num

        # read data from file
        file_name = "data"
        file = open(file_name, "r")
        for i in range(level_num + 1):
            file.readline()
        lst = file.readline().split()

        # set attributes using data from file
        bg_img_filename = 'maps/level' + lst[0] + '.png'
        self.bg = pygame.image.load(bg_img_filename)
        self.playerX = int(lst[1])
        self.playerY = int(lst[2])
        bullet_data = lst[3]
        self.bullets = [Bullet(i, self.playerX, self.playerY, 0, 0) for i in range(7) for j in
                        range(int(bullet_data[i]))]
        self.bullet_poof = int(lst[4])
        obstacles = lst[5].split('_')
        self.obstacle_data = []
        for i in range(len(obstacles) // 3):
            self.obstacle_data.append([obstacles[i * 3], obstacles[i * 3 + 1], obstacles[i * 3 + 2]])

        # testing - delete later  # self.bullets[9].speed_x = self.bullets[9].SPEED  # self.bullets[9].speed_y =   #
        # self.bullets[9].SPEED

    # self.bullets[9].speed_x, self.bullets[9].speed_y = 4, 9 #i have no idea what SPEED does or what bullets list is

    """ move to main.py
    def printData(self):
        print('img', self.bg)
        print('x', self.playerX)
        print('y', self.playerY)
        print('bullets', self.bullets)
        print('obstaclelist', self.obstacle_data)
        loadLevel()  # activate the loading screen sequence fade to white
    """

    def rotate_image(self, image, angle, pos):
        rotated_image = pygame.transform.rotate(image, -angle)  # Rotate the image
        rotated_rect = rotated_image.get_rect(center=pos)  # Keep the center at the circle's center
        return rotated_image, rotated_rect

    def draw(self, screen):

        # car = pygame.transform.scale(self.bg, (Width, Height))
        car = pygame.transform.scale(self.bg, (1400, 900))  # assume large screen for now
        screen.blit(car, (0, 0))
        pygame.draw.circle(screen, 'grey', [int(self.playerX), int(self.playerY)], 30)

        #resizing window correctly in levels, size = input variable in function
        '''  if size == 'big':
                    car = pygame.transform.scale(self.bg, (1400, 900))  # assume large screen for now
                    screen.blit(car, (0, 0))
                else:
                    car = pygame.transform.scale(self.bg, (1200, 836))  # assume large screen for now
                    screen.blit(car, (0, 0))
        '''
        mousx, mousy = pygame.mouse.get_pos()
        locplayerx = int(self.playerX)
        locplayery = int(self.playerY)

        angle = math.degrees(math.atan2(mousy - locplayery, mousx - locplayerx))
        circle_center = (locplayerx, locplayery)
        rotated_image, rotated_rect = self.rotate_image(self.duck_image, angle, circle_center)
        screen.blit(rotated_image, rotated_rect)

        for bullet in self.bullets:
            bullet.move(screen)
            bullet.draw(screen)

    def launch(self, dx, dy):
        self.bullets[9].speed_x, self.bullets[9].speed_y = dx, dy
        #need to implement presence of multiple bullets on board at the same time but ifk how u did this so yeah
