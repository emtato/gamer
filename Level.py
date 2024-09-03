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
        for i in range(levelNum-1):
            file.readline()
        List = file.readLine().split()
        self.image = List[0]
        self.playerX = List[1]
        self.playerY = List[2]
        bulletData = List[3]
        self.bullets = list(bulletData)
        obstacles = List[4].split('_')
        self.l = []
        for i in range(len(obstacles)//3):
            self.l.append([obstacles[i*3],obstacles[i*3+1],obstacles[i*3+2]])
        self.endX = List[5]
        self.endY = List[6]

    def printData(self):
        print(self.image)
        print(self.playerX)
        print(self.playerY)
        print(self.bullets)
        print(self.l)
        print(self.endX)
        print(self.endY)


