from circleshape import CircleShape
import pygame
from constants import ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.score = 1000 // radius

    def draw(self, screen):
        pygame.draw.circle(screen, "brown", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        elif self.radius < ASTEROID_MAX_RADIUS:
            random_angle = random.uniform(20, 50)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = self.velocity.rotate(random_angle) * 1.2

            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2.velocity = self.velocity.rotate(-random_angle) * 1.2
        else:
            random_angle = random.uniform(20, 50)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = self.velocity.rotate(random_angle) * 1.2

            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2.velocity = self.velocity.rotate(-random_angle) * 1.2
