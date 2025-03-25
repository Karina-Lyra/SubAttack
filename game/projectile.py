import pygame
from game import constants

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, player_index):
        super().__init__()
        self.image = pygame.image.load("assets/images/projectile.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = constants.PROJECTILE_SPEED
        self.player_index = player_index

    def update(self):
        self.rect.x += self.speed

        # Remove o projétil se ele sair da tela
        if self.rect.right > constants.SCREEN_WIDTH:
            self.kill()