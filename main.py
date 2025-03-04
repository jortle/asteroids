import sys
import pygame

# import pygame_menu
# from pygame_menu import themes
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from asteroid import Asteroid
from player import Player
from asteroidfield import AsteroidField
from bullets import Bullets
from powerups import PowerUp


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Bullets.containers = (bullets, updatable, drawable)
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    PowerUp.containers = (updatable, drawable)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    # time related
    Font = pygame.font.SysFont("Trebuchet MS", 25)
    Minute = 0
    Second = 0
    White = (255, 255, 255)
    TimeFont = Font.render(
        "Time:{0:02}".format(Minute), 1, White
    )  # zero-pad minutes to 2 digits
    TimeFontR = TimeFont.get_rect()
    TimeFontR.center = (int(SCREEN_WIDTH * 0.6), 20)

    # score related
    Score = 0
    ScoreFont = Font.render("Score: {0}".format(Score), 1, White)
    ScoreFontR = ScoreFont.get_rect()
    ScoreFontR.center = (int(SCREEN_WIDTH * 0.4), 20)
    time_multipler = 1

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        time_multipler += dt * 0.001

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if player.collision_detect(asteroid):
                print("Game over!")
                sys.exit()

            for bullet in bullets:
                if asteroid.collision_detect(bullet):
                    Score += asteroid.score * player.multiplier * time_multipler
                    bullet.kill()
                    asteroid.split()

        screen.fill("black")

        # time tracking
        Minute = pygame.time.get_ticks() // 1000 // 60
        Second = pygame.time.get_ticks() // 1000 % 60

        for obj in drawable:
            obj.draw(screen)

            # draw time
            TimeFont = Font.render(
                "Time {0:02}:{1:02}".format(Minute, Second),
                0,
                White,
            )
            screen.blit(TimeFont, TimeFontR)

            # draw score
            ScoreFont = Font.render("Score: {0:d}".format(int(Score)), 0, White)
            screen.blit(ScoreFont, ScoreFontR)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
