from triangleshape import TriangleShape
import pygame
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
    BULLET_RADIUS,
)
from bullets import Bullets
import math
from collision_math import circle_triangle_collision


class Player(TriangleShape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.rotation = 0
        self.timer = 0

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def draw(self, screen):
        pygame.draw.polygon(screen, "green", self.triangle(), 2)

        # below lines are used for debugging
        # uncomment to see them
        # red line shows bullet/actual player orientation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        end_pos = self.position + forward * PLAYER_RADIUS * 1.5
        pygame.draw.line(screen, "red", self.position, end_pos, 2)

        # blue line shows player position to front of triangle
        triangle_points = self.triangle()
        pygame.draw.line(screen, "blue", self.position, triangle_points[0], 2)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.timer > 0:
            pass
        else:
            bullet = Bullets(self.position.x, self.position.y, BULLET_RADIUS)
            bullet.velocity = (
                pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            )
            self.timer = PLAYER_SHOOT_COOLDOWN

    def triangle(self):
        math_rotation = math.radians(self.rotation + 90)
        # Front vertex (pointing in the direction of angle)
        front_x = self.position[0] + PLAYER_RADIUS * math.cos(math_rotation)
        front_y = self.position[1] + PLAYER_RADIUS * math.sin(math_rotation)

        # Back vertices (forming the base of the triangle)
        back_angle1 = math_rotation + 2.5  # About 143° behind
        back_angle2 = math_rotation - 2.5  # About 143° behind on the other side

        back_x1 = self.position[0] + (PLAYER_RADIUS * 0.7) * math.cos(back_angle1)
        back_y1 = self.position[1] + (PLAYER_RADIUS * 0.7) * math.sin(back_angle1)

        back_x2 = self.position[0] + (PLAYER_RADIUS * 0.7) * math.cos(back_angle2)
        back_y2 = self.position[1] + (PLAYER_RADIUS * 0.7) * math.sin(back_angle2)

        front_point = (front_x, front_y)
        back_point1 = (back_x1, back_y1)
        back_point2 = (back_x2, back_y2)

        return [front_point, back_point1, back_point2]

    def collision_detect(self, asteroid):
        return circle_triangle_collision(
            asteroid.position, asteroid.radius, self.triangle()
        )
