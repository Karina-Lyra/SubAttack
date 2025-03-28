import pygame

from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent2, Player) and isinstance(ent1, Enemy):
            valid_interaction = True
        elif isinstance(ent2, Player) and isinstance(ent1, EnemyShot):
            valid_interaction = True
        elif isinstance(ent2, PlayerShot) and isinstance(ent1, Enemy):
            valid_interaction = True
        elif isinstance(ent2, PlayerShot) and isinstance(ent1, EnemyShot):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name
                # Replacing Enemy and EnemyShot with explosion
                if isinstance(ent1, PlayerShot):
                    ent2.surf = pygame.image.load('asset/image/EnemyExplosion.png').convert_alpha()
                    ent2.rect = ent2.surf.get_rect(center=ent2.rect.center)
                elif isinstance(ent2, PlayerShot):
                    ent1.surf = pygame.image.load('asset/image/EnemyExplosion.png').convert_alpha()
                    ent1.rect = ent1.surf.get_rect(center=ent1.rect.center)
                # Creating sound for collision with the Player
                else:
                    if (isinstance(ent1, Enemy) or
                            isinstance(ent2, Enemy) or
                            isinstance(ent1, EnemyShot) or
                            isinstance(ent2, EnemyShot)):
                        enemyDeath_sound = pygame.mixer.Sound('asset/sound/EnemyDeath.mp3')
                        enemyDeath_sound.set_volume(1)
                        enemyDeath_sound.play()

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
