# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 17:30:44 2017

@author: Peter Kyriakopoulos
"""

''' Imports '''
import pygame as pg
from settings import *
vec = pg.math.Vector2

''' Creating the player class '''
class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        ''' Player visual reresentation '''
        self.image = pg.Surface((30, 50))
        self.image.fill(YELLOW)
        ''' Player position '''
        self.rect = self.image.get_rect()
        self.pos = vec(self.rect.center)
        ''' Player velocity and acceleration '''
        self.vel = vec(0, 0)
        self.acc = vec(0, PLAYER_GRAV)
        
    ''' Giving the player the ability to jump '''      
    def jump(self):
    # jump only if standing on a platform
#        self.rect.y += 1
#        false means the sprite is not deleted upon collision
#        hits = pg.sprite.spritecollide(self, Platform, False)
#        self.rect.y -= 1
#        if hits:
            self.vel.y = -20


    '''calculate position w/ collisions'''    
    def get_position(self, obstacles):
#        keys = pg.key.get_pressed()
        ''' check if buttons are pressed '''
        for event in pg.event.get():
            ''' player moves while key is pressed, not once pressed '''
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    self.vel.x = -10
                elif event.key == pg.K_d:
                    self.vel.x = 10
                elif event.key == pg.K_w:
                    self.jump()
        else:
            ''' if no key is pressed player doesnt move '''
            self.vel.x = 0
            self.vel.y = 0
        ''' prevent player from going off screen '''
        if self.pos.x > WIDTH - 55:
            self.pos.x = WIDTH - 55
        if self.pos.x < 55:
            self.pos.x = 55
        if self.pos.y > HEIGHT - 65:
            self.pos.x = HEIGHT - 65
        if self.pos.y < 65:
            self.pos.y = 65
        ''' x position changed by velocity, y position takes acceleration into account '''
        self.pos.x += self.vel.x
        self.pos.y += self.acc.y + self.vel.y
        self.rect.center = self.pos
        
        ''' check if player stands on a platform '''
        if not self.fall:
            self.check_falling(obstacles)
        else:
            self.fall = self.check_collisions((0, self.vel.y), 1, obstacles)
        if self.vel.x:
            self.check_collisions((self.vel.x, 0), 0, obstacles)
        
    def check_falling(self, obstacles):
        ''' Fall if not on ground '''
        self.rect.move_ip((0, 1))
        collisions = pg.sprite.spritecollide(self, obstacles, False)
        collidable = pg.sprite.collide_mask
        if not pg.sprite.spritecollideany(self, collisions, collidable):
            self.fall = True
        self.rect.move_ip((0, -1))
    
    def check_collisions(self, offset, index, obstacles):

        ''' Checking if collision occurs after moving offset pixels. If yes
        repeat after reducing by one pixel until the exact distance that
        can be moved is found '''

        unaltered = True
        self.rect.move_ip(offset)
        collisions = pg.sprite.spritecollide(self, obstacles, False)
        collidable = pg.sprite.collide_mask
        while pg.sprite.spritecollideany(self, collisions, collidable):
            self.rect[index] += (1 if offset[index]<0 else -1)
            unaltered = False
        return unaltered
    ''' update position of player '''
    def update(self, obstacles):
        self.get_position(obstacles)

''' creating a new class for bullets '''
class bullet(pg.sprite.Sprite):
    def __init__(self, player, cursor):
        pg.sprite.Sprite.__init__(self)
        ''' visual representation of bullets '''
        self.image = pg.Surface((4, 4))
        self.image.fill(PURPLE)
        ''' bullet properties '''
        self.rect = self.image.get_rect()
        self.mass = BULLMASS
        self.pos = vec(player.pos)
        self.vel = 0.05*(cursor - player.pos)
        self.rect.center = self.pos
        self.rect.center = (100, 100)
#figure out how to remove bullets from sprite list to optimize memory usage/performance    
    
    ''' update bullet position '''
    def update(self):
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

''' new class for platforms '''
class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        ''' visual representation of sprites, width and height as defined in settings '''
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y