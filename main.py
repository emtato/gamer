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
    global level
    level = Level(1, size)

    # testing purposes
    print('img', level.bg)
    print('x', level.playerX)
    print('y', level.playerY)
    print('bullets', level.bullets)
    print('obstaclelist', level.obstacle_data)
    loadLevel()  # activate the loading screen sequence fade to white


def levels(level: int):
    print(f"Level {level} selected")


# change screen size
def screensmall():
    global size, Width, Height, Window
    size = 'small'
    Width, Height = 1200, 771
    Window = pygame.display.set_mode((Width, Height))
    for i, button in enumerate(buttons):
        button.width = 160
        button.height = 40
        button.x = 100  # move buttons more to the left
        button.y = 200 + i * 70  # tighter vertical spacing
        if i > len(buttons) - 4:
            break  # don't reposition screen size buttons


def screenbig():
    global size, Width, Height, Window
    size = 'big'
    Width, Height = 1400, 900
    Window = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption("qwack")
    for i, button in enumerate(buttons):
        button.width = 200
        button.height = 50
        button.x = 120  # move buttons more to the left
        button.y = 220 + i * 90  # more vertical spacing
        if i > len(buttons) - 4:
            break  # don't reposition screen size buttons


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

buttons = [Button("Level 1", 120, 220, 200, 50, level1, is_level=True),
           Button("Level 2", 120, 310, 200, 50, lambda: levels(2), is_level=True),
           Button("Level 3", 120, 400, 200, 50, lambda: levels(3), is_level=True),
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
    desc = FONT2.render("By Amanda and Emilia", True, "grey")
    SR = FONT2.render("select screen size", True, "grey")

    Window.blit(quacker, (10, 10))  # display text
    Window.blit(desc, (10, 50))
    Window.blit(SR, (50, 100))
    pygame.display.update()

def winwindow():
    popup_width, popup_height = 300, 200
    popup_x = (Width - popup_width) // 2
    popup_y = (Height - popup_height) // 2

    popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)
    pygame.draw.rect(Window, (240, 240, 240), popup_rect)  # light grey popup
    pygame.draw.rect(Window, (100, 100, 100), popup_rect, 4)  # border
    text = FONT.render("win :DD", True, (50, 50, 50))
    Window.blit(text, (popup_x + 60, popup_y + 80))

#
# -----------------------------------------------------------------------------------------------------------------
#

# Initialize the level
level = None
# main game logic, while loop to run everything
size = 'big'


def main():
    bulletslaunched = 0
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
                        if button.is_clicked(event, Window):  # is it?
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
            level.draw(Window, size)

            if any(bul.win for bul in level.bullets):
                print('fouind you!! :DD')
                winwindow()
                pygame.display.update()
                time.sleep(1.3)
                gamemode = 0

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

                    bullet = Bullet(0, playerx, playery, differencex, differencey)
                    Level.launch(level, bulletslaunched, speedmultiplier * differencex, speedmultiplier * differencey)
                    bulletslaunched += 1

                    '''avoid drawing all bullets at once (happens in Level.py. currently on level.draw, it iterates 
                    bullets list and draws all
                    
                    
                    code in progress for this goal:
                    
                     bulletlist = level.bullets
                    if bulletslaunched < len(bulletlist):
                        bullet = Bullet(bulletlist[bulletslaunched].element, playerx, playery, differencex, differencey)
                        Level.launch(level, bulletslaunched, speedmultiplier * differencex, speedmultiplier * 
                        differencey)
                        bulletslaunched+=1
                        bullet.draw(Window)
                    '''

        if gamemode <= 0:

            for button in buttons:
                if button.tick == 0:  # when tick = 0, it means button not pressed. so it colors it grey for hover
                    button.is_hovered(mouse_pos, Window)  # Update button hover state based on mouse position
                    button.draw(Window)
                else:
                    button.tick -= 1  # tick isnt 0 so it counts down a timer until it becomes 0 to resume the normal
                    # color.
                    button.draw(Window)
                    button.color = (100, 100, 100)  # temporary darker button to confirm you clicked button
            rendertext()  # Render main menu text and subtitle. usually do this last otherwise might cause
            # artifacts/flickering  # but, if in rendertext the display update is removed, rendertext func call can
            # be placed on top too.  # probably has to do with how display update causes that if its not at the end
            # of buttons being drawn?

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
