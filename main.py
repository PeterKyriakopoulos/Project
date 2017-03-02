# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 17:18:15 2017

@author: Peter Kyriakopoulos
"""

''' Imports and other files '''
import numpy as np
import pygame as pg
import random
from settings import *
from sprites import Player, bullet, field, Platform

''' Starting the game '''
class Game:
    def __init__(self):
        ''' Game Window '''
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
    ''' Starting a new game, making new groups ''' 
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        ''' Setting up platforms, adding them to all_sprites '''
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)    

    ''' Running the Game '''   
    def run(self):
        ''' Game loop '''
        self.playing = True
        while self.playing:
            ''' Set framerate, update, and draw '''
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
               
    ''' Shooting function '''
    def shoot(self, cursor):
        ''' Create bullet sprite and add it to all_sprites '''
        b = bullet(self.player, cursor)
        self.all_sprites.add(b)

    ''' Gravity '''   
    def gravity(self):
        self.gravity = gravity(self)
        diff2 = np.abs(self.bullet.pos - self.field.pos)
        self.force = g * (BULLMASS * GRAV_MASS)//diff2

    ''' Updating all sprites '''   
    def update(self):
        self.all_sprites.update(self.platforms)

    ''' Getting mouse position and mouse click status, shoot when clicking '''   
    def events(self):
        mouse = pg.mouse.get_pressed()
        ''' If mouse is clicked '''
        if mouse[0]:
            ''' Get cursor position '''
            cur = pg.mouse.get_pos()
            ''' Shoot '''
            self.shoot(cur)
        ''' Quit game if red x clicked '''            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                ''' Stop running the game when quitting '''
                if self.playing:
                    self.playing  = False
                self.running = False

    ''' Draw all sprites on screen '''                
    def draw(self):
        ''' Fill screen with black before drawing '''
        self.screen.fill(BLACK)
        ''' Draw sprites '''
        self.all_sprites.draw(self.screen)
        pg.display.flip()

''' Running the game '''
g = Game()
g.new()
while g.running:
    g.run()

pg.quit()