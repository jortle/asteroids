from circleshape import CircleShape
import pygame


class Bullets(CircleShape):
    def __init__(self, x, y, radius, owner):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.owner = owner
        self.image_path = "./assets/Rocket.png"
        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(
            self.position[0], self.position[1], self.width, self.height
        )

    def draw(self, screen):
        # screen.blit(self.image, (self.position[0], self.position[1]))
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
