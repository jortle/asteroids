import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from asteroid import Asteroid
from player import Player
from asteroidfield import AsteroidField
from bullets import Bullets
from menu import main_menu


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Bullets.containers = (bullets, updatable, drawable)
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

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

    # Rate of Fire (RPM)
    Rate_of_Fire = 0.3 * 60

    # Accuracy (ACC)

    # menu shown
    Menu_Shown = False

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        if main_menu.is_enabled():
            main_menu.update(events)
            main_menu.draw(screen)

        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if obj.collision_detect(player):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for bullet in bullets:
                if asteroid.collision_detect(bullet):
                    Score += asteroid.score
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
            ScoreFont = Font.render("Score: {0}".format(Score), 0, White)
            screen.blit(ScoreFont, ScoreFontR)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
