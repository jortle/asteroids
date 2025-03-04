import sys
import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TIME_MULTIPLIER_MAGIC
from collision_math import circle_triangle_collision


# Class definitions should take containers as parameters or use a different pattern
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Asteroid Game")
        self.clock = pygame.time.Clock()

        # Game state
        self.running = True
        self.score = 0
        self.time_multiplier = 1
        self.dt = 0

        # Initialize sprite groups
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()

        # Set up containers for sprite classes
        from asteroid import Asteroid
        from player import Player
        from asteroidfield import AsteroidField
        from bullets import Bullets
        from powerups import PowerUp

        # Initialize the player at center screen
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.updatable.add(self.player)
        self.drawable.add(self.player)

        # Initialize asteroid field
        self.asteroid_field = AsteroidField()
        self.updatable.add(self.asteroid_field)

        # UI setup
        self.font = pygame.font.SysFont("Trebuchet MS", 25)
        self.white = (255, 255, 255)

        # Time display setup
        self.time_font = self.font.render("Time: 00:00", 1, self.white)
        self.time_font_rect = self.time_font.get_rect()
        self.time_font_rect.center = (int(SCREEN_WIDTH * 0.6), 20)

        # Score display setup
        self.score_font = self.font.render("Score: 0", 1, self.white)
        self.score_font_rect = self.score_font.get_rect()
        self.score_font_rect.center = (int(SCREEN_WIDTH * 0.4), 20)

    def run(self):
        while self.running:
            if self.handle_events():
                break

            self.update()
            self.render()

            # Update delta time for next frame
            self.dt = self.clock.tick(60) / 1000

        pygame.quit()
        sys.exit()

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return True
        return False

    def update(self):
        # Update time multiplier
        self.time_multiplier += self.dt * TIME_MULTIPLIER_MAGIC

        # Update all objects
        self.updatable.update(self.dt)

        # Check collisions
        self.check_collisions()

    def triangle_collision(self, asteroid):
        circle_triangle_collision(
            asteroid.position, asteroid.radius, self.player.triangle()
        )

    def check_collisions(self):
        # Check player-asteroid collisions
        for asteroid in self.asteroids:
            if self.triangle_collision(asteroid):
                print("Game over!")
                self.running = False

        # Check bullet-asteroid collisions
        for asteroid in self.asteroids:
            for bullet in self.bullets:
                if asteroid.collision_detect(bullet):
                    self.score += int(
                        asteroid.score * self.player.multiplier * self.time_multiplier
                    )
                    bullet.kill()
                    asteroid.split()

    def render(self):
        self.screen.fill("black")

        # Calculate time for display
        total_seconds = pygame.time.get_ticks() // 1000
        minutes = total_seconds // 60
        seconds = total_seconds % 60

        # Draw all sprites
        for obj in self.drawable:
            obj.draw(self.screen)

        # Draw time
        time_text = f"Time: {minutes:02}:{seconds:02}"
        self.time_font = self.font.render(time_text, 1, self.white)
        self.screen.blit(self.time_font, self.time_font_rect)

        # Draw score
        score_text = f"Score: {self.score:d}"
        self.score_font = self.font.render(score_text, 1, self.white)
        self.screen.blit(self.score_font, self.score_font_rect)

        pygame.display.flip()


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
