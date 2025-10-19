import pygame as pg

from constants import *
from gift import Gift
import random

class GiftField(pg.sprite.Sprite):
    typs = ["shield", "extra life"]
    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0

    def spawn(self):
        position = pg.Vector2(random.randint(10, SCREEN_WIDTH -10), 0)
        gift = Gift(position.x, position.y)
        gift.velocity = pg.Vector2(0, 1) * GIFT_SPEED

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > GIFT_SPAWN_RATE:
            # Reset Timer
            self.spawn_timer = 0
            #spawn from upper edge
            self.spawn()
            
    