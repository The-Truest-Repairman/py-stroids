# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
import circleshape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #Delta time is the time between frames, used to make sure the game runs at the same speed on all computers    dt = 0
    dt = 0

    #Create new empty groups for objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
     
    #Add new container to classes to help with organizing the main game loop
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    
    #Intialization of objects
    #Instantiate a new player object and spawn it in the middle of the screen
    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    a_field = AsteroidField()

    #Main game loop
    while True:
        #This for loop checks if user has closed the window and exits if so
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Fill screen with black to start fresh each frame
        screen.fill("black")
        
        #Enforce 60 FPS
        dt = clock.tick(60)/1000
        
        #Update objects and then draw them individually
        updatable.update(dt)       
        for object in drawable:
            object.draw(screen)       

        #Refresh the game screen, this happens at the end!
        pygame.display.flip()


if __name__ == "__main__":
    main()