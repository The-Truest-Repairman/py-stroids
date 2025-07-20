# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
import circleshape
import player

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    #Delta time is the time between frames, used to make sure the game runs at the same speed on all computers    dt = 0
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Main game loop
    while True:
        #This for loop checks if user has closed the window and exits if so
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Fill screen with black to start fresh each frame
        screen.fill("black")
        
        #Instantiate a new player object and spawn it in the middle of the screen
        p1 = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        
        #Draw the player
                
        p1.draw(screen)

        #ENFORCE 60 FPS
        clock.tick(60)
        dt = clock.tick()/1000

        #Refresh the game screen, this happens at the end!
        pygame.display.flip()


if __name__ == "__main__":
    main()