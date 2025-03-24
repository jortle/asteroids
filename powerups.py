import pygame
from circleshape import CircleShape
from constants import POWERUP_BASE_RADIUS


class PowerUp(CircleShape):
    def __init__(self, x, y, radius=POWERUP_BASE_RADIUS):
        super().__init__(x, y, radius)
        self.position = (x, y)
        self.radius = radius

        # self.image_path = "./assets/Player-Damaged.png"
        # self.image = pygame.image.load(self.image_path).convert_alpha()
        # self.width = self.image.get_width()
        # self.height = self.image.get_height()
        # self.rect = pygame.Rect(
        #    self.position[0], self.position[1], self.width, self.height
        # )

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)
