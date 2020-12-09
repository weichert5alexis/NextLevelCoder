import pygame
import random
from os import path

from utils.constants import (
    SCREEN_WIDHT,
    SCREEN_HEIGHT,
    BLACK,
    IMG_DIR,
)

class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMG_DIR, "cherry.png"))
        self.image = pygame.transform.scale(self.image, (10, 20))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDHT - self.rect.width)
        self.rect.bottom = 0

    def update(self):
        self.rect.y = self.rect.y +2


