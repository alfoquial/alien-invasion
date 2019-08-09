import pygame

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    # Init backgrounds need pygame
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("ALIEN INVASION")

    # init an instance of class ship
    ship = Ship(screen)

    # Init loop
    while True:
        # Get mouse and keyboards events
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
