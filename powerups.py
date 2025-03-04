import pygame


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.position = (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, "red", self.position)
