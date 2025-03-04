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
    minute = 0
    second = 0
    White = (255, 255, 255)
    TimeFont = Font.render(
        "Time:{0:02}".format(minute), 1, White
    )  # zero-pad minutes to 2 digits
    TimeFontR = TimeFont.get_rect()
    TimeFontR.center = (int(SCREEN_WIDTH * 0.3), 20)

    # score related
    score = 0
    time_multipler = 1

    # accuracy related
    asteroids_destroyed = 0
    accuracy = 0

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        time_multipler += dt * 0.001
        if asteroids_destroyed > 0:
            accuracy = asteroids_destroyed / player.bullets_shot * 100
        else:
            accuracy = 0

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if player.collision_detect(asteroid):
                print("Game over!")
                sys.exit()

            for bullet in bullets:
                if (
                    bullet.position[0] < 0
                    or bullet.position[1] < 0
                    or bullet.position[0] > SCREEN_WIDTH
                    or bullet.position[1] > SCREEN_HEIGHT
                ):
                    bullet.kill()
                if asteroid.collision_detect(bullet):
                    score += asteroid.score * player.multiplier * time_multipler
                    bullet.owner.pop(bullet)
                    asteroids_destroyed += 1
                    bullet.kill()
                    asteroid.split()

        screen.fill("black")

        # time tracking
        minute = pygame.time.get_ticks() // 1000 // 60
        second = pygame.time.get_ticks() // 1000 % 60

        for obj in drawable:
            obj.draw(screen)

            # draw time
            TimeFont = Font.render(
                "Time {0:02}:{1:02}        Score {2:d}     Accuracy {3:d}%".format(
                    minute, second, int(score), int(accuracy)
                ),
                0,
                White,
            )
            screen.blit(TimeFont, TimeFontR)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
