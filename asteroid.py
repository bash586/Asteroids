import random

import pygame

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x :float, y :float, radius :float):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            random_angle = random.uniform(20, 50)
            
            vector1 = self.velocity.rotate(random_angle) 
            vector2 = self.velocity.rotate(-random_angle)

            a1.velocity = vector1 * 1.2
            a2.velocity = vector2 * 1.2