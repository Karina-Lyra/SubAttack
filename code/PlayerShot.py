import pygame

from code.Const import ENTITY_SPEED, PLAYER_KEY_SHOOT
from code.Entity import Entity


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shoot_sound = pygame.mixer.Sound('asset/sound/shoot.mp3')
        self.shoot_sound.set_volume(0.2)
        self.shoot_sound.play()

    def move(self, ):
        self.rect.centerx += ENTITY_SPEED[self.name]