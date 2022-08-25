# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 07:57:05 2021

@author: Casa
"""

import pygame 
from pygame.locals import *

pygame.init()

PANTALLA = pygame.display.set_mode((500,400))

pygame.display.set_caption("mi primer juego :D")

BLANCO = (255,255,255)

PANTALLA.fill(BLANCO)

BUTTON = pygame.draw.rect(PANTALLA,(255,0,0),(100,50,100,50))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
    pygame.display.update()