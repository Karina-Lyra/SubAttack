import pygame
from game import constants

class Submarine(pygame.sprite.Sprite):
    def __init__(self, x, y, player_index):
        super().__init__()
        if player_index == 0:
            self.image = pygame.image.load("assets/images/submarine.png").convert_alpha()
        else:
            self.image = pygame.image.load("assets/images/submarine2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = constants.SUBMARINE_SPEED
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
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > constants.SCREEN_WIDTH:
            self.rect.right = constants.SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > constants.SCREEN_HEIGHT:
            self.rect.bottom = constants.SCREEN_HEIGHT