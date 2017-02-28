# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 17:30:44 2017

@author: PET3RtheGreat
"""

import pygame as pg
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
#        super().__init__()
        pg.sprite.Sprite.__init__(self)
#        or maybe append?
        self.image = pg.Surface((30, 50))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.pos = vec(self.rect.center)
        self.vel = vec(0, 0)
        self.acc = vec(0, PLAYER_GRAV)
        self.fall = True


    def jump(self):
    # jump only if standing on a platform
#        false means the sprite is not deleted upon collision
        self.vel.y = -20

    def get_position(self, obstacles):
        """Calculate the player's position this frame, including collisions."""
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.vel.x = -10
        elif keys[pg.K_d]:
            self.vel.x = 10
        elif keys[pg.K_w]:
            print('jump')
            self.jump()
        else:
            self.vel.x = 0
            self.vel.y = 0
        if self.pos.x > WIDTH - 55:
            self.pos.x = WIDTH - 55
        if self.pos.x < 55:
            self.pos.x = 55
        if self.pos.y > HEIGHT - 65:
            self.pos.y = HEIGHT - 65
        if self.pos.y < 65:
            self.pos.y = 65

        self.pos.x += self.vel.x
        self.pos.y += self.acc.y + self.vel.y
        self.rect.center = self.pos
        if not self.fall:
            self.check_falling(obstacles)
        else:
            self.fall = self.check_collisions((0,self.vel.y), 1, obstacles)
        if self.vel.x:
            self.check_collisions((self.vel.x,0), 0, obstacles)

    def check_falling(self, obstacles):
        """If player is not contacting the ground, enter fall state."""
        self.rect.move_ip((0,1))
        collisions = pg.sprite.spritecollide(self, obstacles, False)
        collidable = pg.sprite.collide_mask
        if not pg.sprite.spritecollideany(self, collisions, collidable):
            self.fall = True
        self.rect.move_ip((0,-1))

    def check_collisions(self, offset, index, obstacles):
        """
        This function checks if a collision would occur after moving offset
        pixels.  If a collision is detected position is decremented by one
        pixel and retested. This continues until we find exactly how far we can
        safely move, or we decide we can't move.
        """
        unaltered = True
        self.rect.move_ip(offset)
        collisions = pg.sprite.spritecollide(self, obstacles, False)
        collidable = pg.sprite.collide_mask
        while pg.sprite.spritecollideany(self, collisions, collidable):
            self.rect[index] += (1 if offset[index]<0 else -1)
            unaltered = False
        return unaltered


    def update(self, obstacles):
        self.get_position(obstacles)


class bullet(pg.sprite.Sprite):
    def __init__(self, player, cursor):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((4, 4))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.mass = BULLMASS
        self.pos = vec(player.pos)
        self.vel = 0.05*(cursor - player.pos)
        self.rect.center = self.pos

#figuring out how to remove bullets from sprite list to optimize memory usage/performance
    def update(self, platforms):
#        if self.pos.x > 1610:
#            pass
#        if self.pos.x < -10:
#            pass
#        if self.pos.y > 910:
#            pass
#        if self.pos.y < -10:
#            pass
        self.pos += self.vel
        self.rect.midbottom = self.pos

#also need to figure out collision detection between bullets and different bodies
class field(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.draw.circle((10))
        self.image.fill(CYAN)
        self.rect = self.image.get_rect()
        self.mass = GRAV_MASS
        self.pos = self.rect.center


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
