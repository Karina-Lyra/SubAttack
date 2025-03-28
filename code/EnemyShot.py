import pygame

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class EnemyShot(Entity):
    # Creating sound for the EnemyShot
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shootEnemy_sound = pygame.mixer.Sound('asset/sound/shootEnemy.mp3')
        self.shootEnemy_sound.set_volume(0.3)
        self.shootEnemy_sound.play()

    # Differentiating Enemy3 movement
    def move(self, ):
        if self.name == 'Enemy3Shot':
            self.rect.centery -= ENTITY_SPEED[self.name]
        else:
            self.rect.centerx -= ENTITY_SPEED[self.name]
