import pygame as pg
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player

def main():
    pg.init()
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pg.time.Clock()
    
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    asteroids = pg.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        updatable.update(dt)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pg.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
pg.sprite