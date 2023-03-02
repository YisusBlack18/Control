import os
import sys,pygame
from pygame import *

pygame.init()

clk = pygame.time.Clock()

if pygame.joystick.get_count() == 0:
    raise IOError("No joystick detected")
joy = pygame.joystick.Joystick(0)
joy.init()

def buttonX(boton):
    if(boton==0): return 298
    elif(boton==1): return 336
    elif(boton==2): return 260
    elif(boton==3): return 298
    elif(boton==4): return 75
    elif(boton==5): return 295
    elif(boton==6): return 160
    elif(boton==7): return 220
    elif(boton==8): return 154
    elif(boton==9): return 195

def buttonY(boton):
    if(boton==0): return 127
    elif(boton==1): return 98
    elif(boton==2): return 98
    elif(boton==3): return 70
    elif(boton==4 or boton==5): return 11
    elif(boton==6 or boton==7): return 98
    elif(boton==8): return 108
    elif(boton==9): return 110

size = width,height = 400,225
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Joystick Tester")
background_image = pygame.image.load(os.getcwd() + "\\sn.jpg")
background_image = background_image.convert_alpha()
background_image = pygame.transform.scale(background_image, (width, height))
frameRect = pygame.Rect((0,0),(width,height))

crosshair = pygame.Surface((10,10))
crosshair.fill(pygame.Color("magenta"))
pygame.draw.circle(crosshair, pygame.Color("blue"),(5,5),5,0)
crosshair.set_colorkey(pygame.Color("magenta"))

crosshairb = pygame.Surface((10,10))
crosshairb.fill(pygame.Color("magenta"))
pygame.draw.circle(crosshairb, pygame.Color("red"),(5,5),5,0)
crosshairb.set_colorkey(pygame.Color("magenta"))

buttons = {}
for b in range(joy.get_numbuttons()):
    buttons[b] = [crosshair,(buttonX(b),buttonY(b))]

while(True):
    pygame.event.pump()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill([255,255,255])
    screen.blit(background_image,(0,0))

    x = joy.get_axis(0)
    y = joy.get_axis(1)

    screen.blit(crosshairb,((x*20)+80-5,(y*20)+98))

    for b in range(joy.get_numbuttons()):
        if joy.get_button(b):
            screen.blit(buttons[b][0],buttons[b][1])

    pygame.display.flip()
    clk.tick(144) #mas FPS