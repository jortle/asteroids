import pygame
# from collision_math import circle_triangle_collision
# import math
# from constants import PLAYER_RADIUS


class TriangleShape(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        # use barycentric coordinates to find the point of intersection
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    # def triangle(self):
    #     angle = self.rotation
    #
    #     # Front vertex (pointing in the direction of angle)
    #     front_x = self.position[0] + PLAYER_RADIUS * math.cos(angle)
    #     front_y = self.position[1] + PLAYER_RADIUS * math.sin(angle)
    #
    #     # Back vertices (forming the base of the triangle)
    #     back_angle1 = angle + 2.5  # About 143° behind
    #     back_angle2 = angle - 2.5  # About 143° behind on the other side
    #
    #     back_x1 = self.position[0] + (PLAYER_RADIUS * 0.7) * math.cos(back_angle1)
    #     back_y1 = self.position[1] + (PLAYER_RADIUS * 0.7) * math.sin(back_angle1)
    #
    #     back_x2 = self.position[0] + (PLAYER_RADIUS * 0.7) * math.cos(back_angle2)
    #     back_y2 = self.position[1] + (PLAYER_RADIUS * 0.7) * math.sin(back_angle2)
    #
    #     front_point = (front_x, front_y)
    #     back_point1 = (back_x1, back_y1)
    #     back_point2 = (back_x2, back_y2)
    #     self.front_point = front_point
    #     self.back_point1 = back_point1
    #     self.back_point2 = back_point2
    #
    #     return [front_point, back_point1, back_point2]
    #
    # def collision_detect(self, asteroid):
    #     return circle_triangle_collision(
    #         asteroid.position, asteroid.radius, self.triangle()
    #     )
