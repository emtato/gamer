# Description:
# Created by Emilia and Amanda on 2024-08-30
import sys
import pygame
import time
import random
import Button
#
#-----------------------------------------------------------------------------------------------------------------
#
from click._compat import WIN

pygame.font.init() #intializes fonts to display text

Width, Height = 1400, 1000
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("qwack")
#
#-----------------------------------------------------------------------------------------------------------------
#

#level selector functions
def level1():
    print("Level 1 selected")

def level2():
    print("Level 2 selected")

def level3():
    print("Level 3 selected")

#
#-----------------------------------------------------------------------------------------------------------------
#

#defining buttons

buttons = [
    Button.Button("Level 1", 300, 200, 200, 50, level1),
    Button.Button("Level 2", 300, 300, 200, 50, level2),
    Button.Button("Level 3", 300, 400, 200, 50, level3)
]


#
#-----------------------------------------------------------------------------------------------------------------
#

FONT = pygame.font.SysFont("arial", 30)
FONT2 = pygame.font.Font(None, 24)  # None means default font
#
#-----------------------------------------------------------------------------------------------------------------
#


def rendertext():

    quacker = FONT.render("quacker", True, "white") #defining each font
    desc = FONT2.render("a game by ayaka umbrella fans", True, "grey")

    Window.blit(quacker, (10,10)) #display text
    Window.blit(desc, (10,50))

    pygame.display.update()

#
#-----------------------------------------------------------------------------------------------------------------
#

#main game logic, while loop to run everything
def main():
    run = True
    while run:
        Window.fill('BLACK')

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #x in the corner pressed
                run = False
                break
        rendertext()

        for button in buttons:
            if button.is_clicked(event):
                button.callback()

        for button in buttons: #redraws every button every loop iteration
            button.draw(Window)

        pygame.display.flip() # Update the display

    pygame.quit()


#
#-----------------------------------------------------------------------------------------------------------------
#

#checks if run directly from this file (main), not when this is imported to another file, dont wanna run this window thingy
#when imported from another file ig
if __name__ == "__main__":
    main()




