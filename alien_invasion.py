import sys
import pygame

from settings import Settings
from ship import Ship


def run_game():
    # inicializa el juego
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("ALIEN INVASION")

    # crea una nave
    ship = Ship(screen)

    # crea el bucle principal
    while True:
        # espera eventos del rato o teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Pinta la pantalla
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # hace visible la pantalla
        pygame.display.flip()


run_game()



