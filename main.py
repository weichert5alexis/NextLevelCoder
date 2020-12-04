from components.game import Game
import pygame

if __name__ == "__main__":
    game = Game()
    while game.running:
        if not game.playing:
            game.show_start_screen()
            game.run()

    pygame.quit() # terminar juego:cerrar pantalla

