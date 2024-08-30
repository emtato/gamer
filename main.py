# Description:
# Created by Emilia and Amanda on 2024-08-30
import sys
import pygame
import time
import random

from click._compat import WIN

pygame.font.init()


Width, Height = 1400, 1000
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("qwack")

#main game logic, while loop to run everything
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()



#checks if run directly from this file (main), not when this is imported to another file, dont wanna run this window thingy
#when imported from another file ig
if __name__ == "__main__":
    main()



FONT = pygame.font.SysFont("arial", 30)

def rendertext():

    #this is the draw function in the video, finish later
    texttest = FONT.render("quacker", True, "white")
    WIN.blit(texttest, (10,10))

