import pygame

from components.bullet import Bullet
from utils.constants import (
    BLACK,
    SCREEN_HEIGHT,
    SCREEN_WIDHT,
    IMG_DIR
)
from os import path


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(path.join(IMG_DIR, "sheriff.png")).convert()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(BLACK) #fondo
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDHT/2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.bullets = pygame.sprite.Group()


    def update(self):                                                    #def update(self):
                                                                            #self.movement_on_x = 10
        key = pygame.key.get_pressed()                                      # key = pygame.key.get_pressed()
                                                                            #if key[pygame.K_LEFT]:
        # asigna movimiento al tocar una tecla en especifico                #self.rect.x = self.rect.x - self.movement_on_x
                                                                            #if key[pygame.K_RIGHT]:
        if key[pygame.K_RIGHT]:                                             #self.rect.x = self.rect.x + self.movement_on_x
            self.rect.x += 5                                                #
        #self.rect.centerx = self.rect.centerx + 1                          #if self.rect.right > SCREEN_WIDHT:
        if self.rect.right >= SCREEN_WIDHT:                                 #  self.rect.right = SCREEN_WIDHT
            self.rect.right = SCREEN_WIDHT                                  #if self.rect.left < 0:
                                                                            #  self.rect.left = 0
        if key[pygame.K_LEFT]:                                              #
                self.rect.x -=5                                             #
        if self.rect.left >= SCREEN_WIDHT:                                  #
            self.rect.left = SCREEN_WIDHT                                   #
                                                                            #
        # Jugador no salga de la pantalla por el lado izquierdo             #
                                                                            #
        if self.rect.x <= 0:                                             #
            self.rect.x = 0                                              #

    def shoot(self):

        sound_rifle = pygame.mixer.Sound(path.join(IMG_DIR, "rifle.ogg"))
        pygame.mixer.Sound.play(sound_rifle)
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.game.all_sprites.add(bullet)
        self.bullets.add(bullet)






