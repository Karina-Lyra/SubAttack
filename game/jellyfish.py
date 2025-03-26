import pygame
from game.constants import JELLYFISH_SPEED, WIN_WIDTH, WIN_HEIGHT


class Jellyfish(pygame.sprite.Sprite):
    def __init__(self, x, y, window):
        super().__init__()
        self.window = window
        self.image_attack = pygame.image.load("./assets/images/jellyfish/jellyfish_attack.png").convert_alpha()
        self.image_death = pygame.image.load("./assets/images/jellyfish/jellyfish_death.png").convert_alpha()
        self.image = self.image_attack
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = JELLYFISH_SPEED
        self.health = 1
        self.direction = -1  # Começa movendo para cima
        self.initial_y = y

    def update(self, player_rect):
        self.rect.y += self.speed * self.direction

        if self.rect.y <= 0:
            self.direction = 1
        elif self.rect.y >= WIN_HEIGHT - self.rect.height:
            self.direction = -1

        if self.rect.colliderect(player_rect):
            self.image = self.image_attack
        else:
            self.image = self.image_death

    def draw(self):
        self.window.blit(self.image, self.rect)

    def take_damage(self):
        self.health -= 1
        return self.health <= 0