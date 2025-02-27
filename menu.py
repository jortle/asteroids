from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes

main_menu = pygame_menu.Menu(
    "Asteroids", SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, theme=themes.THEME_SOLARIZED
)
main_menu.add_button("Choose profile", profiles_selector)
main_menu.add_button("Single player", single_player)
main_menu.add_button("Multiplayer", multiplayer)
main_menu.add_button("History", history_mode_selector)
main_menu.add_button("Leader board", leader_board_selector)
main_menu.add_button("Settings", settings)
main_menu.add_button("Quit", quit)

profiles_selector = main_menu.add_button("Profiles", profiles)


def profiles():
    pass


def single_player():
    pass


def multiplayer():
    pass


def history():
    pass


def leader_board():
    pass


def settings():
    pass


def quit():
    pygame.quit()
