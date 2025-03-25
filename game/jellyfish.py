import pygame

from game import constants


class Jellyfish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_attack = pygame.image.load("assets/images/jellyfish_attack.png").convert_alpha()
        self.image_death = pygame.image.load("assets/images/jellyfish_death.png").convert_alpha()
        self.image = self.image_attack
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = constants.JELLYFISH_SPEED
        self.health = 1
        self.direction = -1  # Move para cima
        self.initial_y = y  # Rastreia a posição inicial

    def update(self, player_rect):
        self.rect.y += self.speed * self.direction  # Move para cima

        # Lógica de mudança de direção
        if self.rect.y <= 0:  # Se atingir o topo da tela
            self.direction = 1  # Move para baixo
        elif self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height:  # Se atingir a parte inferior da tela
            self.direction = -1  # Move para cima

        if self.rect.colliderect(player_rect):
            self.image = self.image_attack
        else:
            self.image = self.image_death

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            return True
        return False

