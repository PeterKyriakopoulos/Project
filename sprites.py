# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 17:30:44 2017

@author: PET3RtheGreat
"""

import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
#        or  pg.sprite.Sprite.__init__(self)
#        or maybe append?
        self.image = pg.Surface((30, 50))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.pos = self.rect.center
        print(self.rect.center)
        
    def jump(self):
    # jump only if standing on a platform
        self.rect.x += 1
#        false means the sprite is not deleted upon collision
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20
    
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.vel.x = -20
        if keys[pg.K_d]:
            self.vel.x = 20
        if keys[pg.K_w]:
            self.player.jump()
        if self.pos.x > WIDTH - 55:
            self.pos.x = WIDTH - 55
        if self.pos.x < 55:
            self.pos.x = 55

        self.rect.midbottom = self.pos
        
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

class bullet(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((4, 4))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.mass = BULLMASS
        self.rect.center = self.pos

#figuring out how to remove bullets from sprite list to optimize memory usage/performance    
    def update(self):
        if self.pos.x > 1610:
            pass
        if self.pos.x < -10:
            pass
        if self.pos.y > 910:
            pass
        if self.pos.y < -10:
            pass
#also need to figure out collision detection between bullets and different bodies    
class field(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.draw.circle((10))
        self.image.fill(CYAN)
        self.rect = self.image.get_rect()
        self.mass = GRAV_MASS
        self.pos = self.rect.center


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y