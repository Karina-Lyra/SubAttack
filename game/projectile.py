import pygame
from game.constants import PROJECTILE_SPEED, WIN_WIDTH


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, player_index, window):
        super().__init__()
        self.window = window
        self.image = pygame.image.load("./assets/images/projectile/projectile.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = PROJECTILE_SPEED
        self.player_index = player_index

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIN_WIDTH:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)