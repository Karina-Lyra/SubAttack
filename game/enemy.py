import pygame
from game import constants

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_type):
        super().__init__()
        self.enemy_type = enemy_type
        if enemy_type == 1:
            self.image_attack = pygame.image.load("assets/images/enemy1_attack.png").convert_alpha()
            self.image_death = pygame.image.load("assets/images/enemy1_death.png").convert_alpha()
        else:
            self.image_attack = pygame.image.load("assets/images/enemy2_attack.png").convert_alpha()
            self.image_death = pygame.image.load("assets/images/enemy2_death.png").convert_alpha()
        self.image = self.image_attack
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = constants.ENEMY_SPEED
        self.health = 1

    def update(self, player_rect):
        self.rect.x -= self.speed
        if self.rect.colliderect(player_rect):
            self.image = self.image_attack
        else:
            self.image = self.image_death

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            return True
        return False