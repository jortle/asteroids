import random
import pygame
from circleshape import CircleShape
from constants import POWERUP_BASE_RADIUS


class PowerUp(CircleShape):
    def __init__(self, x, y, radius=POWERUP_BASE_RADIUS):
        super().__init__(x, y, radius)
        self.position = (x, y)
        self.radius = radius
        self.effect = random.choice(
            [
                # "player_speed",
                # "rpm_up",
                # "shield",
                # "score_multiplier",
                # "turn_speed",
                "bullet_velocity_up",
            ]
        )

        # self.image_path = "./assets/Player-Damaged.png"
        # self.image = pygame.image.load(self.image_path).convert_alpha()
        # self.width = self.image.get_width()
        # self.height = self.image.get_height()
        # self.rect = pygame.Rect(
        #    self.position[0], self.position[1], self.width, self.height
        # )

    def draw(self, screen):
        if self.effect == "player_speed":
            pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        elif self.effect == "rpm_up":
            pygame.draw.circle(screen, "yellow", self.position, self.radius, 2)
        elif self.effect == "shield":
            pygame.draw.circle(screen, "blue", self.position, self.radius, 2)
        elif self.effect == "score_multiplier":
            pygame.draw.circle(screen, "green", self.position, self.radius, 2)
        elif self.effect == "turn_speed":
            pygame.draw.circle(screen, "red", self.position, self.radius, 2)
        elif self.effect == "bullet_velocity_up":
            pygame.draw.circle(screen, "purple", self.position, self.radius, 2)

    def apply(self, player):
        if self.effect == "player_speed":
            player.move_speed_mult += 0.1
        elif self.effect == "rpm_up":
            player.rpm_up()
        elif self.effect == "shield":
            player.shield = True
        elif self.effect == "score_multiplier":
            player.score_mult += 0.1
        elif self.effect == "turn_speed":
            player.turn_mult += 0.1
        elif self.effect == "bullet_velocity_up":
            player.bullet_velocity_mult -= 0.1
