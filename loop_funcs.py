from constants import TIME_MULTIPLIER_MAGIC
import pygame


def handle_events():
    evebts = pygame.event.get()
    for event in evebts:
        if event.type == pygame.QUIT:
            return True
    return False


def update(dt):
    global time_multipler, score
    time_multipler += dt * TIME_MULTIPLIER_MAGIC

    for obj in updatable:
        obj.update(dt)

    for asteroid in asteroids:
        if player.collision_detect(asteroid):
            print("Game over!")
            sys.exit()
        for bullet in bullets:
            if asteroid.collision_detect(bullet):
                score += asteroid.score * player.multiplier * time_multipler
                bullet.kill()
                asteroid.split()


def render():
    screen.fill("black")

    # time tracking
    current_time = pygame.time.get_ticks() // 1000
    minute = current_time // 60
    second = current_time % 60
    time_multipler += dt * TIME_MULTIPLIER_MAGIC

    for obj in drawable:
        obj.draw(screen)

        # draw time
        TimeFont = Font.render(
            "Time {0:02}:{1:02}".format(minute, second),
            0,
            White,
        )
        screen.blit(TimeFont, TimeFontR)

        # draw score
        ScoreFont = Font.render("Score: {0:d}".format(int(score)), 0, White)
        screen.blit(ScoreFont, ScoreFontR)

    pygame.display.flip()
    dt = clock.tick(60) / 1000
