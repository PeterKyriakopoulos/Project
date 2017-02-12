# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 17:18:15 2017

@author: PET3RtheGreat
"""

#imports and other files
import numpy as np
import pygame as pg
import random
from settings import *
from sprites import *

#starting the game
class Game:
    def __init__(self):
#        game window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self):
        self.all_sprites = pg.sprite.Group()
#        self.player = Player(self)
        self.run
    
    
    def run(self):
#        Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def shoot(self):
        self.bullet = bullet(self)
        cur = pg.mouse.get_pos()
        diff = cur - self.player.pos
        self.bullet.move = diff * BULLET_SPEED
    
    def gravity(self):
        self.gravity = gravity(self)
        diff2 = np.abs(self.bullet.pos - self.field.pos)
        self.force = g * (BULLMASS * GRAV_MASS)//diff2
    
    def update(self):
        self.all_sprites.update()
    
    def events(self): 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing  = False
                self.running = False
                
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    
    
    
    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

g = Game()
g.show_start_screen
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()