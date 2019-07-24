import pygame

class Ship():

    def __init__(self, screen):
        # Inicializa la nave en la pantalla
        self.screen = screen

        # Carga la imagen de la nave
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Ubica la nave en la pantalla
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

