import pygame

from game import constants


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font_title = pygame.font.Font(None, 72)
        self.font_button = pygame.font.Font(None, 36)
        self.menu_bg = pygame.image.load("assets/images/menu_bg.png").convert()
        self.menu_music = pygame.mixer.Sound("assets/sounds/menu_music.mp3")
        self.button_width = 200
        self.button_height = 50
        self.button_margin = 20

    def draw_button(self, text, rect, color, text_color):
        pygame.draw.rect(self.screen, color, rect)
        text_surface = self.font_button.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def run(self):
        running = True
        num_players = 2  # Sempre 2 jogadores
        game_mode = "competitive"  # Sempre modo competitivo

        self.menu_music.play(-1)

        title_text = self.font_title.render("Sub Attack", True, constants.WHITE)  # Título correto
        title_rect = title_text.get_rect(center=(constants.SCREEN_WIDTH // 2, 100))

        button_1p_rect = pygame.Rect(
            constants.SCREEN_WIDTH // 2 - self.button_width // 2,
            constants.SCREEN_HEIGHT // 2 - self.button_height - self.button_margin,
            self.button_width,
            self.button_height,
        )
        button_2p_rect = pygame.Rect(
            constants.SCREEN_WIDTH // 2 - self.button_width // 2,
            constants.SCREEN_HEIGHT // 2,
            self.button_width,
            self.button_height,
        )
        button_score_rect = pygame.Rect(
            constants.SCREEN_WIDTH // 2 - self.button_width // 2,
            constants.SCREEN_HEIGHT // 2 + self.button_height + self.button_margin,
            self.button_width,
            self.button_height,
        )
        button_exit_rect = pygame.Rect(
            constants.SCREEN_WIDTH // 2 - self.button_width // 2,
            constants.SCREEN_HEIGHT // 2 + 2 * (self.button_height + self.button_margin),
            self.button_width,
            self.button_height,
        )

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if button_1p_rect.collidepoint(mouse_pos):
                        num_players = 1
                        running = False
                    elif button_2p_rect.collidepoint(mouse_pos):
                        num_players = 2
                        running = False
                    elif button_score_rect.collidepoint(mouse_pos):
                        pass
                    elif button_exit_rect.collidepoint(mouse_pos):
                        running = False

            self.screen.blit(self.menu_bg, (0, 0))
            self.screen.blit(title_text, title_rect)
            self.draw_button("NEW GAME 1P", button_1p_rect, constants.BLUE, constants.WHITE)
            self.draw_button("NEW GAME 2P", button_2p_rect, constants.RED, constants.WHITE)
            self.draw_button("SCORE", button_score_rect, constants.WHITE, constants.BLACK)
            self.draw_button("EXIT", button_exit_rect, constants.WHITE, constants.BLACK)

            pygame.display.flip()

        self.menu_music.stop()
        return num_players, game_mode
