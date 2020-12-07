import pygame

from utils.text_utils import draw_text

from components.ball import Ball
from os import path
from components.player import Player
from utils.constants import (
    SCREEN_WIDHT,
    SCREEN_HEIGHT,
    TITLE,
    BLACK,
    IMG_DIR
)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
        self.background_img = pygame.image.load(path.join(IMG_DIR, "desierto.jpg")).convert()
        self.background_img = pygame.transform.scale(self.background_img, (SCREEN_WIDHT, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = True
        pygame.mixer.init()
        pygame.mixer.music.load(path.join(IMG_DIR, "town4.mp3"))
        pygame.mixer.music.play(-1)



    def run(self):
        self.create_components()
        # Game loop: events - update - draw

        self.playing = True

        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()


    def create_components(self):
        self.all_sprites = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()


        self.player = Player(self)
        self.all_sprites.add(self.player)

        ball = Ball(1)
        self.all_sprites.add(ball)
        self.balls.add(ball)


    def update(self):
        self.all_sprites.update()


        hits = pygame.sprite.spritecollide(self.player, self.balls, False)
        if hits:
            self.playing = False


        hits = pygame.sprite.groupcollide(self.balls, self.player.bullets, True, True)


        for hit in hits:
            if hit.size < 4:
                for i in range (0, 2):
                    ball = Ball(hit.size + 1)
                    self.all_sprites.add(ball)
                    self.balls.add(ball)



    def events(self):
    # pygame.events() : para traer eventos que hay
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()


    def draw(self):
        background_rect = self.background_img.get_rect()
        self.screen.blit(self.background_img, background_rect)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def show_start_screen(self):
        self.screen.blit(self.background_img, self.background_img.get_rect())
        draw_text(self.screen, "Game working", 64, SCREEN_WIDHT/2, SCREEN_HEIGHT/4)
        draw_text(self.screen, "Presione las flechas para moverse y SPACE para disparar", 20, SCREEN_WIDHT / 2, SCREEN_HEIGHT / 2)
        draw_text(self.screen, "Prsionar Enter para iniciar", 20, SCREEN_WIDHT / 2, SCREEN_HEIGHT*3/5)

        pygame.display.flip()

        waiting = True
        while waiting:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        waiting = False