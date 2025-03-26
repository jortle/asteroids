import sys
import pygame
from pygame import time
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TIME_MULTIPLIER_MAGIC
from asteroid import Asteroid
from player import Player
from asteroidfield import AsteroidField
from bullets import Bullets
from powerups import PowerUp
import random
from render_hud import render_hud


def game_start(num_players, button_id, settings_dict):
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

    # creating players
    players = {}
    for i in range(num_players):
        player_name = f"player{i}"
        players[player_name] = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, player_name)

    dt = 0

    # hud variables
    minute = 0
    second = 0
    score = 0
    accuracy = 0
    rpm = 0

    # score related
    score = 0
    time_multipler = 1

    # accuracy related
    asteroids_destroyed = 0
    accuracy = 0

    hud_elements, HudRect = render_hud(
        settings_dict, minute, second, score, accuracy, rpm
    )

    # powerups
    current_powerups = []

    # background image
    background = pygame.image.load("./assets/SpaceBackground.png")

    # time limit for time trial game modes - in seconds
    # None by default so that survival doesn't have a time limit
    # gets changed if a time trial mode is chosen
    time_limit = None

    # button ids - odds for survival, evens for time trial
    if button_id % 2 == 1:
        time_limit = None
    elif button_id % 2 == 0:
        time_limit = 30

    # settings_dict hud manipulation

    for setting in settings_dict:
        if settings_dict[setting]:
            pass
        else:
            pass

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        screen.blit(background, (0, 0))

        time_multipler += dt * TIME_MULTIPLIER_MAGIC
        for player in players:
            if players[player].bullets_shot > 0:
                accuracy = int(asteroids_destroyed / players[player].bullets_shot * 100)
            else:
                accuracy = 0

            rpm = int(60 // players[player].rpm)

        for obj in updatable:
            obj.update(dt)

        # powerups
        if second % 12 == 0 and current_powerups == []:
            powerup = PowerUp(
                random.randint(100, SCREEN_WIDTH - 100),
                random.randint(100, SCREEN_HEIGHT - 100),
            )
            current_powerups.append(powerup)
        else:
            pass

        # collision detection
        for asteroid in asteroids:
            for player in players:
                if players[player].collision_detect(asteroid):
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

                splitting_happened = False
                if asteroid.collision_detect(bullet) and not splitting_happened:
                    score += int(
                        asteroid.score * players[player].score_mult * time_multipler
                    )
                    bullet.owner.pop(bullet)
                    asteroids_destroyed += 1
                    bullet.kill()
                    asteroid.split()
                    splitting_happened = True

        # powerup collision detection
        for player in players:
            for powerup in current_powerups:
                if players[player].collision_detect(powerup):
                    powerup.apply(players[player])
                    powerup.kill()
                    current_powerups.remove(powerup)

        # time tracking
        minute = pygame.time.get_ticks() // 1000 // 60
        second = pygame.time.get_ticks() // 1000 % 60

        if time_limit is not None:
            if time_limit <= second:
                sys.exit()

        for obj in drawable:
            obj.draw(screen)

            # draw top bar
        hud_elements, HudRect = render_hud(
            settings_dict, minute, second, score, accuracy, rpm
        )
        for element, rect in hud_elements:
            screen.blit(element, rect)

        # Optionally, draw the bounding rectangle for debugging
        pygame.draw.rect(screen, (255, 0, 0), HudRect, 2)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
