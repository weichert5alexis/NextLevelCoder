import pygame

from utils.constants import(
    BLUE,
    SCREEN_HEIGHT,
    SCREEN_WIDHT,
)

import random

allowed_speed = list(range(3,5))

class Ball(pygame.sprite.Sprite):

    def __init__(self, size):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

        #aparicion de bola a los dos lados de la pantalla

        self.rect.x = random.randrange(SCREEN_WIDHT - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.choice(allowed_speed)
        self.speedx = random.choice(allowed_speed)
        self.size = size

    def update(self):
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy

        # La bola rebota de izquierda a la derecha

        if self.rect.right > SCREEN_WIDHT:
            self.rect.right = SCREEN_WIDHT
            self.speedx = random.choice(allowed_speed) * -1

        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = random.choice(allowed_speed)

            # Bola rebota en la parte superior e inferior.

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom > SCREEN_HEIGHT
                            #=
            self.speedy = random.choice(allowed_speed) * -1

        if self.rect.top < 0:
            self.rect.top = 0
            self.speedy = random.choice(allowed_speed) + 1