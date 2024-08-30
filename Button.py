# Description:
# Created by Emilia and Amanda on 2024-08-30
import sys
import pygame
import time
import random

class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = "WHITE"
        self.callback = callback
