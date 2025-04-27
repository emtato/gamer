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
    bulletslaunched: int

    def __init__(self, level_num, size):  # Added size parameter
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
        if size == 'small':
            self.playerX = int(self.playerX * (1200 / 1400))
            self.playerY = int(self.playerY * (771 / 900))
        bullet_data = str(lst[3])
        self.bullets = [Bullet(i, self.playerX, self.playerY, 0, 0, int(lst[4])) for i in range(8) for j in
                        range(int(bullet_data[i]))]
        self.bullet_poof = int(lst[4])
        obstacles = lst[5].split('_')
        self.obstacle_data = []
        for i in range(len(obstacles) // 3):
            self.obstacle_data.append([obstacles[i * 3], obstacles[i * 3 + 1], obstacles[i * 3 + 2]])
        self.bulletslaunched = 0

    def rotate_image(self, image, angle, pos):
        rotated_image = pygame.transform.rotate(image, -angle)  # Rotate the image
        rotated_rect = rotated_image.get_rect(center=pos)  # Keep the center at the circle's center
        return rotated_image, rotated_rect

    def draw(self, screen, size):
        car = pygame.transform.scale(self.bg, (
        1400 if size == 'big' else 1200, 900 if size == 'big' else 771))  # assume large screen for now
        screen.blit(car, (0, 0))
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
        if len(self.bullets) > self.bulletslaunched:
            self.bullets[self.bulletslaunched].speed_x, self.bullets[self.bulletslaunched].speed_y = dx, dy
