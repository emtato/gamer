# Description:
# Created by Emilia and Amanda on 2024-08-30
import sys
import pygame
import time
import random

class Button:
    def __init__(self, text, x, y, width, height, callback, is_level):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = "WHITE"
        self.callback = callback
        self.tick = 0
        self.is_level = is_level

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, 'BLACK')
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect) #render text on button (blit)

    def is_clicked(self, event):
        if self.rect.collidepoint(event.pos):
            self.color = (100,100,100)
            return True
        else:
            return False

    def is_hovered(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.color = (200, 200, 200)  # Light grey when hovered
            self.hovered = True
        else:
            self.color = 'WHITE'
            self.hovered = False
