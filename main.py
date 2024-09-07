# Description:
# Created by Emilia and Amanda on 2024-08-30
import math
import sys
import pygame
import time
import random

import Level
import Button

clock = pygame.time.Clock()
#
# -----------------------------------------------------------------------------------------------------------------
#
from click._compat import WIN

pygame.font.init()  # intializes fonts to display text

Width, Height = 1400, 900
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("qwack")

duck_image = pygame.image.load('duck.png')  # reference for turret later


#
# -----------------------------------------------------------------------------------------------------------------
#


# level selector functions
def level1():
    print("Level 1 selected")
    global levela
    lol = Level.Level(1)
    levela = 1
    lol.printData()


def level2():
    print("Level 2 selected")


def level3():
    print("Level 3 selected")


# change screen size
def screensmall():
    Width, Height = 1200, 836
    Window = pygame.display.set_mode((Width, Height))


def screenbig():
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

buttons = [
    Button.Button("Level 1", 300, 200, 200, 50, level1),
    Button.Button("Level 2", 300, 300, 200, 50, level2),
    Button.Button("Level 3", 300, 400, 200, 50, level3),
    Button.Button('small', 400, 100, 200, 50, screensmall),
    Button.Button('big', 700, 100, 200, 50, screenbig)

]

#
# -----------------------------------------------------------------------------------------------------------------
#

FONT = pygame.font.SysFont("arial", 30)
FONT2 = pygame.font.Font(None, 24)  # None means default font
#test

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


# rotate duck to face mouse
def rotate_image(image, angle, pos):
    rotated_image = pygame.transform.rotate(image, -angle)  # Rotate the image
    rotated_rect = rotated_image.get_rect(center=pos)  # Keep the center at the circle's center
    return rotated_image, rotated_rect


#
# -----------------------------------------------------------------------------------------------------------------
#

# main game logic, while loop to run everything
levela = None


def main():
    clock = pygame.time.Clock()  # Initialize a clock to manage the frame rate
    run = True

    gamemode = 0
    while run:
        if gamemode <= 0:
            Window.fill('BLACK')

        for event in pygame.event.get():  # Process all events in the event queue
            if event.type == pygame.QUIT:  # If the close button is clicked
                run = False
                break
            if gamemode <= 0:
                for button in buttons:  # Check each button for clicks
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if button.is_clicked(event):  # is it?
                            if levela != None:
                                gamemode = 1
                            button.callback()  # if button is pressed, button.callback (from button class, callback is an attribute/property)
                            '''in this case, we defined multiple buttons that should execute different things (levels) but since were using
                            the same button press checker function, its hard to determine which function to execute IF the button is pressed.
                            Thus, we use a callback attribute in the Button class. (level1, level2... during initialization above)
                            This attribute stores a reference to the function that should be executed when the button is pressed..
                            '''
                            button.tick = 20  # set the greyed out timer

        if gamemode == 1:
            levelnum = 'maps/level' + str(levela) + '.png'
            car = pygame.image.load(levelnum)
            Window.blit(car, (0, 0))
            levelData = Level.Level(levela)
            pygame.draw.circle(Window, 'grey', [int(levelData.playerX), int(levelData.playerY)], 30)

            levelData = Level.Level(levela)

            mousx, mousy = pygame.mouse.get_pos()
            locplayerx = int(levelData.playerX)
            locplayery = int(levelData.playerY)

            angle = math.degrees(math.atan2(mousy - locplayery, mousx - locplayerx))
            circle_center = (locplayerx, locplayery)
            rotated_image, rotated_rect = rotate_image(duck_image, angle, circle_center)
            Window.blit(rotated_image, rotated_rect)

        mouse_pos = pygame.mouse.get_pos()
        if gamemode <= 0:
            for button in buttons:
                if button.tick == 0:  # when tick = 0, it means button not pressed. so it colors it grey for hover
                    button.is_hovered(mouse_pos)  # Update button hover state based on mouse position
                    button.draw(Window)
                else:
                    button.tick -= 1  # tick isnt 0 so it counts down a timer until it becomes 0 to resume the normal color.
                    button.color = (100, 100, 100)  # temporary darker button to confirm you clicked button
                    button.draw(Window)
        """ testing bullet movement
        bullet = Bullet.Bullet(0, 400, 400)
        bullet.draw(Window)
        bullet.move()
        """

        if gamemode <= 0:
            rendertext()  # Render main menu text and subtitle. usually do this last otherwise might cause artifacts/flickering
        pygame.display.flip()  # Update the display with the drawn frame
        clock.tick(60)  # fps limit of 60 FPS so you dont burn your customers laptop

    pygame.quit()  # Quit pygame when the loop exits


#
# -----------------------------------------------------------------------------------------------------------------
#

# checks if run directly from this file (main), not when this is imported to another file, dont wanna run this window thingy
# when imported from another file ig
if __name__ == "__main__":
    main()
