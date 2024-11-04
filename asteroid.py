from constants import *
from circleshape import CircleShape
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20,50)
        left = self.velocity.rotate(angle)
        right = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        new_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_1.velocity = left * 1.2
        
        new_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_2.velocity = left * 1.2
        
    def update(self, dt):
        self.position += self.velocity * dt