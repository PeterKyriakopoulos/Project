# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:46:21 2016

@author: Peter Kyriakopoulos
"""

''' Screen settings and framerate '''
WIDTH = 1600
HEIGHT = 900
FPS = 60

''' Game window title '''
TITLE = "Platform Demo v2."


PLAYER_GRAV = 5
PLAYERMASS = 100

BULLET_SPEED = 50
BULLET_LIFETIME = 2000
BULLET_RATE = 150
BULLMASS = 1

GRAV_MASS = 50
g = 1

''' Platform coordinates '''
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH // 2 - 50, HEIGHT * 3 // 4, 100, 20),
                 (0, 0, 40, HEIGHT),
                 (WIDTH - 40, 0, 40, HEIGHT),
                 (0, 0, WIDTH, 40)]

''' Color presets '''
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PINK = (255,0,255)
CYAN = (0,255,255)
PURPLE = (100,0,255)