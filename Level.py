# Description:
# Created by Emilia and Amanda on 2024-08-30
import sys
import pygame
import time
import random

from main import Window, clock, loadLevel


class Level:
    def __init__(self, levelNum):
        self.levelNum = levelNum
        fileName = "data"
        file = open(fileName, "r")
        for i in range(levelNum + 1):
            file.readline()
        List = file.readline().split()
        self.image = List[0]
        self.playerX = List[1]
        self.playerY = List[2]
        bulletData = List[3]
        self.bullets = list(bulletData)
        self.bulletPoof = List[4]
        obstacles = List[5].split('_')
        self.l = []
        for i in range(len(obstacles) // 3):
            self.l.append([obstacles[i * 3], obstacles[i * 3 + 1], obstacles[i * 3 + 2]])

    def printData(self):
        print(self.image)
        print(self.playerX)
        print(self.playerY)
        print(self.bullets)
        print(self.l)
        loadLevel()  # activate the loading screen sequence fade to white
