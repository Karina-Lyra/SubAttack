import sys

import pygame
from pygame import Surface

from code.Const import WIN_WIDTH, WIN_HEIGHT, C_WHITE, C_BLUE, C_GREY, C_ORANGE


class GameOver:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/image/GameOver.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))

    def show(self):
        pygame.mixer_music.load('./asset/sound/gameOver.mp3')
        pygame.mixer_music.set_volume(2)
        pygame.mixer_music.play(-1)

        self.window.blit(self.surf, (0, 0))
        self.display_text(48, "GAME OVER", C_ORANGE, (WIN_WIDTH // 2 - 150, WIN_HEIGHT // 3))
        self.display_text(18, "[Press any key to return]", C_GREY, (WIN_WIDTH // 2 - 155,
                                                                   WIN_HEIGHT // 2 - 5))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False
                    pygame.mixer_music.stop()  # Stop music

    def display_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
