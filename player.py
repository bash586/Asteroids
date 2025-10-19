import pygame as pg
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):

    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = - PLAYER_SHOOT_COOLDOWN

    def triangle(self):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        right = pg.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pg.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rotate(-dt)
        if keys[pg.K_d]:
            self.rotate(dt)
        if keys[pg.K_w]:
            self.move(dt)
        if keys[pg.K_s]:
            self.move(-dt)
        if keys[pg.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        # prevent player movement out of screen scope
        self.position.x = min(SCREEN_WIDTH - PLAYER_RADIUS, max(PLAYER_RADIUS, self.position.x + forward.x * PLAYER_SPEED * dt))
        self.position.y = min(SCREEN_HEIGHT - PLAYER_RADIUS, max(PLAYER_RADIUS, self.position.y + forward.y * PLAYER_SPEED * dt))

    def shoot(self):
        if (pg.time.get_ticks()/1000 - self.timer) >= PLAYER_SHOOT_COOLDOWN:
            shot = Shot(self.position.x, self.position.y)
            shot.rotation = self.rotation
            shot.velocity = pg.Vector2(0, 1).rotate(shot.rotation) * PLAYER_SHOOT_SPEED
            self.timer = pg.time.get_ticks()/1000
            return shot