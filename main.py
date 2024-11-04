# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants as c
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting asteroids!")
    print(c.SCREEN_HEIGHT)
    
    pygame.init()
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    
    
    #game objects
    player = Player(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2 )
    asteroidField = AsteroidField()
    
    itsOn = True
    while itsOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             return
         
        for up in updatable:
            up.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                pygame.QUIT
                return
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
         
        screen.fill((0, 0, 0))
        
        for draw in drawable:
            draw.draw(screen)
            
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()