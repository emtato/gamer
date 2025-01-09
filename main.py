# Description:
# Created by Emilia and Amanda on 2024-08-30
import math
import sys
from typing import Optional

import pygame
import time
import random
from Level import Level
from Button import Button
from Bullet import Bullet

clock = pygame.time.Clock()
#
# -----------------------------------------------------------------------------------------------------------------
#
from click._compat import WIN

pygame.font.init()  # intializes fonts to display text

Width, Height = 1400, 900
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("qwack")


# move to Level.py
# duck_image = pygame.image.load('duck.png')  # reference for turret later

def scale_bg(image, window_width, window_height):
    return pygame.transform.scale(image, (window_width, window_height))

#
# -----------------------------------------------------------------------------------------------------------------
#

# level selector functions
def level1():
    print("Level 1 selected")
    global levela
    global level
    level = Level(1)
    levela = 1

    # testing purposes
    print('img', level.bg)
    print('x', level.playerX)
    print('y', level.playerY)
    print('bullets', level.bullets)
    print('obstaclelist', level.obstacle_data)
    loadLevel()  # activate the loading screen sequence fade to white

def level2():
    print("Level 2 selected")


def level3():
    print("Level 3 selected")

# change screen size
def screensmall():
    global size
    size = 'small'
    Width, Height = 1200, 836
    Window = pygame.display.set_mode((Width, Height))


def screenbig():
    global size
    size = 'big'
    Width, Height = 1400, 900
    Window = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption("qwack")

#
# -----------------------------------------------------------------------------------------------------------------
#

# loading screen
def loadLevel():
    for i in range(0, 255, 14):  # fade to white since maze is in (vomit) light mode
        Window.fill((i, i, i))
        pygame.display.flip()
        clock.tick(20)

#
# -----------------------------------------------------------------------------------------------------------------
#

# initializing buttons

buttons = [Button("Level 1", 300, 200, 200, 50, level1, is_level=True),
           Button("Level 2", 300, 300, 200, 50, level2, is_level=True),
           Button("Level 3", 300, 400, 200, 50, level3, is_level=True),
           Button('small', 400, 100, 200, 50, screensmall, is_level=False),
           Button('big', 700, 100, 200, 50, screenbig, is_level=False)]

#
# -----------------------------------------------------------------------------------------------------------------
#

# fonts
FONT = pygame.font.SysFont("arial", 30)
FONT2 = pygame.font.Font(None, 24)  # None means default font

# test

#
# -----------------------------------------------------------------------------------------------------------------
#

def rendertext():
    quacker = FONT.render("quacker", True, "white")  # defining each font
    desc = FONT2.render("a game by ayaka umbrella fans", True, "grey")
    SR = FONT2.render("select screen size", True, "grey")

    Window.blit(quacker, (10, 10))  # display text
    Window.blit(desc, (10, 50))
    Window.blit(SR, (50, 100))
    pygame.display.update()

#
# -----------------------------------------------------------------------------------------------------------------
#

# Initialize the level
level = None
# main game logic, while loop to run everything
levela = None


def main():
    clock = pygame.time.Clock()  # Initialize a clock to manage the frame rate
    run = True

    gamemode = 0
    while run:
        if gamemode <= 0:  # in the main menu
            Window.fill('BLACK')

        for event in pygame.event.get():  # Process all events in the event queue
            if event.type == pygame.QUIT:  # If the close button is clicked
                run = False
                break

            if gamemode <= 0:  # in the main menu
                for button in buttons:  # Check each button for clicks
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if button.is_clicked(event):  # is it?
                            if button.is_level:
                                gamemode = 1
                            button.callback()  # if button is pressed, button.callback (from button class,
                            # callback is an attribute/property)
                            '''in this case, we defined multiple buttons that should execute different things (
                            levels) but since were using
                            the same button press checker function, its hard to determine which function to execute 
                            IF the button is pressed.
                            Thus, we use a callback attribute in the Button class. (level1, level2... during 
                            initialization above)
                            This attribute stores a reference to the function that should be executed when the button 
                            is pressed..
                            '''
                            button.tick = 20  # set the greyed out timer

        mouse_pos = pygame.mouse.get_pos()
        if gamemode == 1:  # in the game
            speedmultiplier = 10  # can change!!
            level.draw(Window)
            # calculate dx and dy based on mouse pos vs player pos
            for event in pygame.event.get():  # Process all events in the event queue
                if event.type == pygame.QUIT:  # If the close button is clicked
                    run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:  # only if mouse button down calc angle and launch bullet
                    playerx, playery = level.playerX, level.playerY
                    mousex, mousey = mouse_pos[0], mouse_pos[1]

                    # Calculate differences in x and y coordinates
                    differencex, differencey = mousex - playerx, mousey - playery

                    # Normalize the difference to ensure constant bullet speed
                    # Check if the mouse is straight to the right or left or up/down
                    if differencex == 0:  # Straight up or down
                        differencex = 0
                        differencey = 1 if differencey > 0 else -1  # Up or down direction
                    elif differencey == 0:  # Straight left or right
                        differencey = 0
                        differencex = 1 if differencex > 0 else -1  # Right or left direction
                    else:
                        # Normalize the differences
                        length = math.sqrt(differencex ** 2 + differencey ** 2)
                        differencex /= length
                        differencey /= length

                    # this wouldve been my idea but it isnt copatible with the current thing
                    bullet = Bullet(0, playerx, playery, differencex, differencey)  # trying here to get bullet
                    # to launch at correct angle relative to where the mouseis aiiming, differencex and y are set to ≥1
                    # so speed is constant and theyre relative to ach other
                    Level.launch(level, speedmultiplier * differencex, speedmultiplier * differencey)

        if gamemode <= 0:

            for button in buttons:
                if button.tick == 0:  # when tick = 0, it means button not pressed. so it colors it grey for hover
                    button.is_hovered(mouse_pos)  # Update button hover state based on mouse position
                    button.draw(Window)
                else:
                    button.tick -= 1  # tick isnt 0 so it counts down a timer until it becomes 0 to resume the normal
                    # color.
                    button.draw(Window)
                    button.color = (100, 100, 100)  # temporary darker button to confirm you clicked button
            rendertext()
            # Render main menu text and subtitle. usually do this last otherwise might cause artifacts/flickering
            #but, if in rendertext the display update is removed, rendertext func call can be placed on top too.
            #probably has to do with how display update causes that if its not at the end of buttons being drawn?


        pygame.display.flip()  # Update the display with the drawn frame
        clock.tick(60)  # fps limit of 60 FPS so you dont burn your customers laptop

    pygame.quit()  # Quit pygame when the loop exits

#
# -----------------------------------------------------------------------------------------------------------------
#

# checks if run directly from this file (main), not when this is imported to another file, dont wanna run this window
# thingy
# when imported from another file ig
if __name__ == "__main__":
    main()
