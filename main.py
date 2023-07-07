#import stuff
import pygame
import sys
import os

from pygame.locals import *


class PlayerSprite:

    def __init__(self, screenheight, screenwidth, imagefile):

        self.shape = pygame.image.load(os.path.join('./', imagefile))

        self.top = screenheight - self.shape.get_height()

        self.left = screenwidth / 2 - self.shape.get_width() / 2

    def Show(self, surface):
        surface.blit(self.shape, (self.left, self.top))

    def UpdateCoords(self, x, y):

        self.left = x - self.shape.get_width() / 2
        self.top = y - self.shape.get_height() / 2
    def Collision(self):
        print("h")


class Background:

    def __init__(self, screenheight, imagefile):

        self.img = pygame.image.load(os.path.join('./', imagefile))
        self.coord = [0, 0]
        self.coord2 = [0, -screenheight]
        self.y_original = self.coord[1]
        self.y2_original = self.coord2[1]

    def Show(self, surface):

        surface.blit(self.img, self.coord)
        surface.blit(self.img, self.coord2)

    # def UpdateCoords(self, speed_y, time):

    #     distance_y = speed_y * time
    #     self.coord[1] += distance_y
    #     self.coord2[1] += distance_y

    #     if self.coord2[1] >= 0:


    #         self.coord[1] = self.y_original
    #         self.coord2[1] = self.y2_original
def setup():

    global ismove
    global direction
    global x
    global y
    global accelx
    global friction
    global gravity
    global accely
    global moveup
    global moveleft
    global moveright
    ismove = False
    direction = "n/a"
    x = 571
    y = 345
    accelx = 0
    friction = 0.5
    gravity = 2
    accely = 0
    moveup = False
    moveleft = False
    moveright = False


setup()
pygame.init()

#Setup Screen
screenwidth, screenheight = (950, 670)
screen = pygame.display.set_mode((screenwidth, screenheight))

#Setup Sprites
bg = Background(screenheight, "BG2.png")
plyer = PlayerSprite(screenheight, screenwidth, "Player.png")
#Setup Title
pygame.display.set_caption('Platformer thingy?')

#test ignore
print(
    "Platformer Game made by Patch32 (aka ilikestealingurbred on discord [dm me for questions or just wanna fwend :)])"
)
#variables
clock = pygame.time.Clock()
dt = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                ismove = True
                moveleft = True
            elif event.key == K_d:
                ismove = True
                moveright = True
            elif event.key == K_w:
                ismove = True
                moveup = True
            elif event.key == K_w and event.key == K_a:
                ismove = True
                moveup = True
                moveleft = True
            elif event.key == K_w and event.key == K_d:
                ismove = True
                moveup = True
                moveright = True
        elif event.type == pygame.KEYUP:
            ismove = False
            moveleft = False
            moveright = False

    if ismove == True:
        if moveleft == True:
            accelx -= 10
        elif moveright == True:
            accelx += 10
        elif moveup == True:
            accely = 25
        
    
    accely -= gravity
    y -= accely
    accelx = accelx * friction
    x += accelx
    if y > 574:
      y = 574
    plyer.UpdateCoords(x, y)
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(pygame.mouse.get_pos())
    # print(pygame.mouse.get_pos())
    bg.Show(screen)
    plyer.Show(screen)
    pygame.display.update()
    clock.tick(60)
