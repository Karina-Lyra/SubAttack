from code.Const import ENTITY_SPEED
from code.Entity import Entity


class EnemyShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        if self.name == 'Enemy3Shot':
            self.rect.centery -= ENTITY_SPEED[self.name]
        else:
            self.rect.centerx -= ENTITY_SPEED[self.name]
