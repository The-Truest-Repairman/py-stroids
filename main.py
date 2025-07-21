# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
import circleshape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #Create new empty groups for objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Add new container to classes to help with organizing the main game loop
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    #Intialization of objects
    #Instantiate a new player object and spawn it in the middle of the screen
    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
   
   #Delta time is the time between frames, used to make sure the game runs at the same speed on all computers    dt = 0
    dt = 0

    #Main game loop
    while True:
        #This for loop checks if user has closed the window and exits if so
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
              
        
        
        #Update objects and then draw them individually
        updatable.update(dt)
       
        #Collision checker
        for asteroid in asteroids:
            #Check collision of player with asteroids
            if asteroid.check_collision(p1):
                exit("Game over!")
            #Check collision of bullets with asteroids
            for bullet in shots:
                if bullet.check_collision(asteroid):
                    bullet.kill()
                    asteroid.split()


        #Fill screen with black to start fresh each frame
        screen.fill("black")       
        for obj in drawable:
            obj.draw(screen)       

        #Refresh the game screen, this happens at the end!
        pygame.display.flip()
        
        #Enforce 60 FPS
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()