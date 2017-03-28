# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:45:35 2017

@author: PET3RtheGreat
"""

import pygame as pg
import numpy as np
from settings import *
vec = pg.math.Vector2

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
#        or maybe append?
        self.image = pg.Surface((30, 50))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.pos = vec(self.rect.center)
        self.vel = vec(0, 0)


    def jump(self):
    # jump only if standing on a platform
        self.rect.x += 1
#        false means the sprite is not deleted upon collision

        self.rect.x -= 1
        if hits:
            self.vel.y = -20

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
#        for event in pg.event.get():
#            if event.type == pg.KEYDOWN:
#                if event.key == pg.K_a:
#                    self.vel.x = -10
#                elif event.key == pg.K_d:
#                    self.vel.x = 10
#                elif event.key == pg.K_w:
#                    self.jump()
#        else:
#        self.vel.x = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.vel.x = -10
        if keys[pg.K_d]:
            self.vel.x = 10
#        if keys[pg.K_w]:
#            self.jump()
        if self.pos.x > WIDTH - 55:
            self.pos.x = WIDTH - 55
        if self.pos.x < 55:
            self.pos.x = 55

#        self.pos += self.vel
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
#        self.rect.midbottom = self.pos
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y


class bullet(pg.sprite.Sprite):
    def __init__(self, player, cursor):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((4, 4))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.mass = BULLMASS
        self.pos = vec(player.pos)
        self.vel = 0.05*(cursor - player.pos)
#        self.rect.center = self.pos
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        #  self.pos = np.array([self.pos.x, self.pos.y])

#figuring out how to remove bullets from sprite list to optimize memory usage/performance
    def update(self, blackholes):
#        check what needs to be passed in (ie. field sprite group)
        force = black_hole_force(self.pos, blackholes)
        '''
        Check the vel, pos and force can be used in the calculation below, or
        if they all need converting to float before, then back to int
        '''
        # self.pos = vec(float(self.pos.x), float(self.pos.y))
        print(self.vel, self.pos, force)
        self.pos += force*(1./FPS**2.) + self.vel*(1./FPS)
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        # self.pos.x = 0.5*force.x + self.vel.x
        # self.pos.y = 0.5*force.y + self.vel.y
#        self.rect.midbottom = self.pos
        '''getting the following error: float() argument must be a string or a number, not 'pygame.math.Vector2'''

#also need to figure out collision detection between bullets and different bodies
#class Field(pg.sprite.Sprite):
#    def __init__(self, x, y, w, h):
#        pg.sprite.Sprite.__init__(self)
#        self.image = pg.Surface(x, y, w, h)
#        pg.draw.circle(self.image, CYAN, (x, y), w, 0)
#        self.image.fill(CYAN)
#        # self.rect = self.image.get_rect()
#        self.mass = GRAV_MASS
#        self.pos = self.rect.center
#        print ("running")
class Field(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(CYAN)
        # self.rect = self.image.get_rect()
        self.rect = vec(x,y)

def black_hole_force(bullet_pos, blackholes):
    force = vec(0.0, 0.0)
#        check how to loop over a sprite group here
    for hole in blackholes:
        const = g * (BULLMASS * GRAV_MASS)
        r = (bullet_pos - hole.rect)
        df_x= float(const)/(r[0])
        df_y= float(const)/(r[1])
        force += vec(df_x, df_y)
    return force

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
