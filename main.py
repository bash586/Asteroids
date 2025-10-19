import pygame as pg

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from giftfield import GiftField
from gift import Gift
from constants import *

def main():
    pg.init()
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pg.time.Clock()

    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    asteroids = pg.sprite.Group()
    shots = pg.sprite.Group()
    gifts = pg.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Gift.containers = (gifts, updatable, drawable)
    GiftField.containers = updatable

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    gift_field = GiftField()
    
    dt = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
    
        updatable.update(dt)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        for a in asteroids:
            if a.detectCollision(player):
                print("Game Over")
                pg.quit()
            for shot in shots:
                if a.detectCollision(shot):
                    a.split()
                    shot.kill()

        pg.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
pg.sprite