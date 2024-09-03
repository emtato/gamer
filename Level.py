# Description: MAKE SAVE FILES LATER!!!!! replace "filename, r" with 'w' or 'a' in a new file
# Created by Emilia and Amanda on 2024-08-30
import sys
import pygame
import time
import random


class Level:
    def __init__(self, levelNum, imageName, playerX, playerY, bullets):
        self.levelNum = levelNum
        fileName = "data"
        file = open(fileName, "r")
        for i in range(levelNum-1):
            file.readline()
        List = map(int, file.readLine().split())
        self.image = List[0]
        self.playerX = List[1]
        self.playerY = List[2]



