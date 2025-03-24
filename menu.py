import pygame
import pygame_menu
from pygame_menu import themes
from main import game_start
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


coop_menu = pygame_menu.Menu(
    "Co-op Mode - in progress",
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    theme=themes.THEME_SOLARIZED,
)
coop_menu.add.button(
    "Survival - in progress",
    lambda: game_start(2, 3, settings_dict),
)

coop_menu.add.button(
    "Time Trial - in progress",
    lambda: game_start(2, 4, settings_dict),
)


def coop_menu_loader():
    multiplayer_menu._open(coop_menu)


versus_menu = pygame_menu.Menu(
    "Versus Mode - in progress",
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    theme=themes.THEME_SOLARIZED,
)
versus_menu.add.button(
    "Survival - in progress",
    lambda: game_start(2, 5, settings_dict),
)

versus_menu.add.button(
    "Time Trial - in progress",
    lambda: game_start(2, 6, settings_dict),
)


def versus_menu_loader():
    multiplayer_menu._open(versus_menu)


single_player_menu = pygame_menu.Menu(
    "Single Player Modes", SCREEN_WIDTH, SCREEN_HEIGHT, theme=themes.THEME_SOLARIZED
)
single_player_menu.add.button(
    "Survival",
    lambda: game_start(1, 1, settings_dict),
)
single_player_menu.add.button(
    "Time Trial - in progress", lambda: game_start(1, 2, settings_dict)
)

multiplayer_menu = pygame_menu.Menu(
    "Multiplayer Modes - in progress",
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    theme=themes.THEME_SOLARIZED,
)
multiplayer_menu.add.button("Co-op - in progress", coop_menu_loader)
multiplayer_menu.add.button("Versus - in progress", versus_menu_loader)


def single_player():
    mainmenu._open(single_player_menu)


def multiplayer():
    mainmenu._open(multiplayer_menu)


def history():
    pass


def leaderboard():
    pass


def settings():
    mainmenu._open(settings_menu)


def update_display_time(widget):
    update_settings("time")


def update_display_score(widget):
    update_settings("score")


def update_display_accuracy(widget):
    update_settings("accuracy")


def update_display_rpm(widget):
    update_settings("rpm")


settings_dict = {
    "time": True,
    "score": True,
    "accuracy": True,
    "rpm": True,
}


def update_settings(toggle):
    if settings_dict[toggle]:
        settings_dict[toggle] = False
    else:
        settings_dict[toggle] = True


settings_menu = pygame_menu.Menu(
    "Settings", SCREEN_WIDTH, SCREEN_HEIGHT, theme=themes.THEME_SOLARIZED
)
settings_menu.add.label("Choose which stats to display")
settings_menu.add.toggle_switch("Time", True, update_display_time)
settings_menu.add.toggle_switch("Score", True, update_display_score)
settings_menu.add.toggle_switch("Accuracy", True, update_display_accuracy)
settings_menu.add.toggle_switch("RPM", True, update_display_rpm)


def choose_profile():
    pass


mainmenu = pygame_menu.Menu(
    "Asteroids by ChoccyMilk - In Development",
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    theme=themes.THEME_SOLARIZED,
)
mainmenu.add.button("Choose your profile - in progress", choose_profile)
mainmenu.add.button("Single Player", single_player)
mainmenu.add.button("Multiplayer - in progress", multiplayer)
mainmenu.add.button("History - in progress", history)
mainmenu.add.button("Leaderboard - in progress", leaderboard)
mainmenu.add.button("Settings", settings)
mainmenu.add.button("Quit", pygame_menu.events.EXIT)


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)

    pygame.display.update()
