import pygame


# a class for the ship

class Ship:

    def __init__(self, screen):
        # Init the screen for the ship
        self.screen = screen
        # Movement Flag
        self.moving_right = False
        self.moving_left = False

        # Loads image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Center the ship on the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def update(self):
        """Update the position of the ship"""
        if self.moving_right:
            self.rect.centerx += 1

        if self.moving_left:
            self.rect.centerx -= 1


    def blitme(self):
        self.screen.blit(self.image, self.rect)
