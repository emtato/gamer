# Description:
# Created by Emilia and Amanda on 2024-08-30
import sys
import pygame
import time
import random


class Level:
    def __init__(self, levelNum):
        self.levelNum = levelNum
        fileName = "data"
        file = open(fileName, "r")
        for i in range(levelNum+2):
            file.readline()
        List = (file.readLine()).split()
        self.imageName = List[0]
        self.playerX = List[1]
        self.playerY = List[2]
        self.bullets = List[3]
        self.
