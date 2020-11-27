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
        self.rect.centery = SCREEN_HEIGHT/2

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.rect.centerx += 5
        #self.rect.centerx = self.rect.centerx + 1

        if self.rect.right >= SCREEN_WIDHT:
            self.rect.right = SCREEN_WIDHT

