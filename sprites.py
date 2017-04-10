import pygame as pg
import numpy as np
from settings import *
vec = pg.math.Vector2

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("car.jpg")
        self.rect = self.image.get_rect()
        self.pos = vec(self.rect.center)
        self.vel = vec(0, 0)


    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.vel.x = -7
        if keys[pg.K_d]:
            self.vel.x = 7
        if keys[pg.K_s]:
            self.vel.y = 7
        if keys[pg.K_w]:
            self.vel.y = -7
        if self.pos.x > WIDTH - 50:
            self.pos.x = WIDTH - 50
        if self.pos.x < 10:
            self.pos.x = 10
        if self.pos.y < 10:
            self.pos.y = 10
        if self.pos.y > HEIGHT - 70:
            self.pos.y = HEIGHT - 70
       
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y


class bullet(pg.sprite.Sprite):
    def __init__(self, player, cursor):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("bull.png")
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.mass = BULLMASS
        self.pos = vec(player.pos)
        self.vel = .75*(cursor - player.pos)
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y


#figuring out how to remove bullets from sprite list to optimize memory usage/performance
    def update(self, blackholes):
        force = black_hole_force(self.pos, blackholes)
        self.vel += -2*force*(1./FPS)
        self.pos += self.vel*(1./FPS)
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

class Field(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("bhole3.jpg")
        self.rect = vec(x,y)

def black_hole_force(bullet_pos, blackholes):
    force = vec(0.0, 0.0)
    for hole in blackholes:
        const = g * (BULLMASS * GRAV_MASS)
        r = (bullet_pos - hole.rect)
        dx = np.linalg.norm(r)
        f = (const/dx**2)*(r/dx)
        force += f
    return force

class Villain(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("bad.jpg")
        self.rect = self.image.get_rect()
        self.pos = vec(1600, 50)
        self.vel = vec(0, 2)
    def update(self):
         self.pos.x += self.vel.x
         self.pos.y += self.vel.y
         self.rect.x = self.pos.x
         self.rect.y = self.pos.y
         if self.pos.x > WIDTH - 50:
             self.pos.x = WIDTH - 50
         if self.pos.x < 10:
             self.pos.x = 10
         if self.pos.y < 10:
             self.vel.y = -self.vel.y
         if self.pos.y > HEIGHT - 70:
             self.vel.y = -self.vel.y

        
        
class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y