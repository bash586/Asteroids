import pygame as pg

from circleshape import CircleShape
from constants import *

class Gift(CircleShape):
    def __init__(self, x, y, type="asteroid-immunity"):
        super().__init__(x, y, GIFT_RADIUS) # type: "extraLife"|"timedshield"|"extra player speed"| "asteroid-immunity"|
        self.type = type
        self.speed = GIFT_SPEED

    def draw(self, screen):
        pg.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
