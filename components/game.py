import pygame

from components.ball import Ball
from components.player import Player
from utils.constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDHT,
    TITLE,
    BLACK
)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        self.create_components()
        # Game loop:

        self.playing = True

        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()
        pygame.quit()  # terminar juego

    def create_components(self):
        self.all_sprites = pygame.sprite.Group()
        player = Player()
        self.all_sprites.add(player)

        balls = pygame.sprite.Group()
        ball = Ball()
        self.all_sprites.add(ball)


    def update(self):
        self.all_sprites.update()

    def events(self):
    # pygame.events() : para traer eventos que hay
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
