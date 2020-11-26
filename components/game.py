import pygame

from utils.constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDHT,
    TITLE
)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))

    def run(self):
        self.create_components()
        # Game loop:
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()  # terminar juego

    def create_components(self):
        pass

    def update(self):
        pass

    def events(self):
    # pygame.events() : para traer eventos que hay
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def draw(self):
        pass
