#BP's Asteroid class
from constants import *
from circleshape import CircleShape 
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
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
            rnd_angle = random.uniform(20, 50)
            rnd_vector1 = self.velocity.rotate(rnd_angle)
            rnd_vector2 = self.velocity.rotate(-rnd_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_roid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_roid1.velocity = 1.2* rnd_vector1
            new_roid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_roid2.velocity = 1.2* rnd_vector2





