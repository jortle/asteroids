from circleshape import CircleShape
import pygame


class Bullets(CircleShape):
    def __init__(self, x, y, radius, owner):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.owner = owner

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
