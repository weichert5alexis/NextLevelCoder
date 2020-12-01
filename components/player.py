import pygame

from utils.constants import (
    GREEN,
    SCREEN_HEIGHT,
    SCREEN_WIDHT
)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDHT/2
        self.rect.bottom = SCREEN_HEIGHT - 10



    def update(self):
        #self.movement_on_x = 10
        key = pygame.key.get_pressed()

        # asigna movimiento al tocar una tecla en especifico

        if key[pygame.K_RIGHT]:
            self.rect.x += 5
        #self.rect.centerx = self.rect.centerx + 1
        if self.rect.right >= SCREEN_WIDHT:
            self.rect.right = SCREEN_WIDHT

        if key[pygame.K_LEFT]:
                self.rect.x -=5
        if self.rect.left >= SCREEN_WIDHT:
            self.rect.left = SCREEN_WIDHT

        # Jugador no salga de la pantalla por el lado izquierdo

        if self.rect.left <= 0:
            self.rect.left = 0

