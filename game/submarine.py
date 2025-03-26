import pygame
from game.constants import SUBMARINE_SPEED, WIN_WIDTH, WIN_HEIGHT


class Submarine(pygame.sprite.Sprite):
    def __init__(self, x, y, player_index, window):
        super().__init__()
        self.window = window
        if player_index == 0:
            self.image = pygame.image.load("./assets/images/submarine/submarine.png").convert_alpha()
        else:
            self.image = pygame.image.load("./assets/images/submarine/submarine2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = SUBMARINE_SPEED
        self.player_index = player_index

    def update(self):
        keys = pygame.key.get_pressed()
        if self.player_index == 0:
            if keys[pygame.K_w]:
                self.rect.y -= self.speed
            if keys[pygame.K_s]:
                self.rect.y += self.speed
            if keys[pygame.K_a]:
                self.rect.x -= self.speed
            if keys[pygame.K_d]:
                self.rect.x += self.speed
        else:
            if keys[pygame.K_UP]:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed

        # Limita o submarino à tela
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(WIN_WIDTH, self.rect.right)
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(WIN_HEIGHT, self.rect.bottom)

    def draw(self):
        self.window.blit(self.image, self.rect)