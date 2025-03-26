import pygame
from game.constants import ENEMY_SPEED, WIN_WIDTH


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_type, window):
        super().__init__()
        self.window = window
        self.enemy_type = enemy_type
        if enemy_type == 1:
            self.image_attack = pygame.image.load("./assets/images/enemy/enemy1_attack.png").convert_alpha()
            self.image_death = pygame.image.load("./assets/images/enemy/enemy1_death.png").convert_alpha()
        else:
            self.image_attack = pygame.image.load("./assets/images/enemy/enemy2_attack.png").convert_alpha()
            self.image_death = pygame.image.load("./assets/images/enemy/enemy2_death.png").convert_alpha()
        self.image = self.image_attack
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = ENEMY_SPEED
        self.health = 1

    def update(self, player_rect):
        self.rect.x -= self.speed
        if self.rect.colliderect(player_rect):
            self.image = self.image_attack
        else:
            self.image = self.image_death
        if self.rect.right < 0:
            self.kill()  # Remove o inimigo se sair da tela

    def draw(self):
        self.window.blit(self.image, self.rect)

    def take_damage(self):
        self.health -= 1
        return self.health <= 0