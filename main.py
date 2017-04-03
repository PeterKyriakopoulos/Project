"""
Created on Tue Mar 21 20:45:16 2017
@author: PET3RtheGreat
"""

#imports and other files
import numpy as np
import pygame as pg
import random
from settings import *
from sprites import Player, bullet, Field, Platform

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
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.field_sprites = pg.sprite.Group()
        self.all_bullets = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player()
        self.field = Field(500, 500, 30, 30)
        self.all_sprites.add(self.player)
        self.field_sprites.add(self.field)


#        for plat in PLATFORM_LIST:
#            p = Platform(*plat)
#            self.all_sprites.add(p)
#            self.platform.add(p)
        # self.run



    def run(self):
#        Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def shoot(self, cursor):
        b = bullet(self.player, cursor)
        self.all_bullets.add(b)



    def update(self):
#        self.rect.midbottom = self.pos
#        if self.vel.y > 0:
#            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
#            if hits:
#                self.pos.y = hits[0].rect.top
#                self.vel.y = 0
        self.all_sprites.update()
        self.all_bullets.update(self.field_sprites)
        # self.field_sprites.update(bullet)

    def events(self):
        mouse = pg.mouse.get_pressed()
        if mouse[0]:
            cur = pg.mouse.get_pos()
            self.shoot(cur)
        keys = pg.key.get_pressed()
        if keys[pg.K_h]:
           cur = pg.mouse.get_pos()
           print(cur)
           self.shoot(cur)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing  = False
                self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.field_sprites.draw(self.screen)
        self.all_bullets.draw(self.screen)
        pg.display.flip()



#    def show_start_screen(self):
#        pass
#    def show_go_screen(self):
#        pass

g = Game()
#g.show_start_screen
g.new()
while g.running:
    g.run()
#    g.show_go_screen()

pg.quit()