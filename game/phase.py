import random

import pygame

from game import constants
from game.jellyfish import Jellyfish
from game.projectile import Projectile
from game.submarine import Submarine


class Phase:
    def __init__(self, screen, num_players, game_mode):
        self.screen = screen
        self.num_players = num_players
        self.game_mode = game_mode
        self.players = [Submarine(100, 300, 0), Submarine(100, 400, 1)]
        self.enemies = pygame.sprite.Group()
        self.jellyfish = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.phase_num = 1
        self.scores = [0, 0]
        self.load_background()
        self.load_music()
        self.player_health = [100, 100]

    def load_background(self):
        try:
            self.background_images = [
                pygame.image.load("assets/images/backgrounds/phase1.png").convert(),
                pygame.image.load("assets/images/backgrounds/phase2.png").convert(),
                pygame.image.load("assets/images/backgrounds/phase3.png").convert()
            ]
            self.background = self.background_images[self.phase_num - 1]
        except pygame.error as e:
            print(f"Erro ao carregar imagens de fundo: {e}")

    def load_music(self):
        try:
            self.music = pygame.mixer.Sound("assets/sounds/phase1_music.mp3")
            self.music.play(-1)
        except pygame.error as e:
            print(f"Erro ao carregar música: {e}")

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        projectile = Projectile(self.players[0].rect.right, self.players[0].rect.centery, 0)
                        self.projectiles.add(projectile)

            # Desenha o background
            self.screen.blit(self.background, (0, 0))

            # Atualiza e desenha jogadores
            for i, player in enumerate(self.players):
                player.update()
                self.screen.blit(player.image, player.rect)

            # Atualiza e desenha inimigos
            for enemy in self.enemies:
                enemy.update(self.players[0].rect)
                self.screen.blit(enemy.image, enemy.rect)

            # Atualiza e desenha águas-vivas
            for jellyfish in self.jellyfish:
                jellyfish.update(self.players[0].rect)
                self.screen.blit(jellyfish.image, jellyfish.rect)

            # Atualiza e desenha projéteis
            for projectile in self.projectiles:
                projectile.update()
                self.screen.blit(projectile.image, projectile.rect)

            # Lógica de colisões e pontuação
            for projectile in self.projectiles:
                projectile.update()
                self.screen.blit(projectile.image, projectile.rect)
                for enemy in self.enemies:
                    if projectile.rect.colliderect(enemy.rect):
                        self.projectiles.remove(projectile)
                        if enemy.take_damage():
                            self.enemies.remove(enemy)
                        if projectile.player_index == 0:
                            self.scores[0] += 1
                        else:
                            self.scores[1] += 1
                for jellyfish in self.jellyfish:
                    if projectile.rect.colliderect(jellyfish.rect):
                        self.projectiles.remove(projectile)
                        if jellyfish.take_damage():
                            self.jellyfish.remove(jellyfish)
                        if projectile.player_index == 0:
                            self.scores[0] += 1
                        else:
                            self.scores[1] += 1

            # Lógica de colisão com inimigos/águas-vivas (perda de saúde)
            for i, player in enumerate(self.players):
                for enemy in self.enemies:
                    if player.rect.colliderect(enemy.rect):
                        self.player_health[i] -= 10
                        if self.player_health[i] <= 0:
                            font = pygame.font.Font(None, 72)
                            game_over_text = font.render("Game Over", True, constants.RED)
                            game_over_rect = game_over_text.get_rect(
                                center=(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2))
                            self.screen.blit(game_over_text, game_over_rect)
                            pygame.display.flip()
                            pygame.time.delay(3000)
                            pygame.quit()
                            return
                for jellyfish in self.jellyfish:
                    if player.rect.colliderect(jellyfish.rect):
                        self.player_health[i] -= 5
                        if self.player_health[i] <= 0:
                            font = pygame.font.Font(None, 72)
                            game_over_text = font.render("Game Over", True, constants.RED)
                            game_over_rect = game_over_text.get_rect(
                                center=(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2))
                            self.screen.blit(game_over_text, game_over_rect)
                            pygame.display.flip()
                            pygame.time.delay(3000)
                            pygame.quit()
                            return

            # Exibe a pontuação e a saúde de cada jogador
            font = pygame.font.Font(None, 36)
            for i, player in enumerate(self.players):
                score_text = font.render(f"P{i + 1} Score: {self.scores[i]}", True, constants.WHITE)
                self.screen.blit(score_text, (10, 10 + i * 40))
                health_text = font.render(f"P{i + 1} Health: {self.player_health[i]}", True, constants.WHITE)
                self.screen.blit(health_text, (10, 50 + i * 40))

            # Lógica de geração de águas-vivas na segunda fase
            if self.phase_num == 2 and random.randint(0, 100) < 2:
                jellyfish = Jellyfish(random.randint(0, constants.SCREEN_WIDTH - 50), constants.SCREEN_HEIGHT)
                self.jellyfish.add(jellyfish)

            pygame.display.flip()
