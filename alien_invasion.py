import sys
import pygame

from settings import Settings


def run_game():
    # inicializa el juego
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("ALIEN INVASION")
    # Color de la ventana
    bg_color = (230, 230, 230)

    # crea el bucle principal
    while True:
        # espera eventos del rato o teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Pinta la pantalla
        screen.fill(ai_settings.bg_color)

        # hace visible la pantalla
        pygame.display.flip()


run_game()



