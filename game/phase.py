import pygame
import random
from game.constants import WIN_WIDTH, WIN_HEIGHT, C_WHITE, C_RED
from game.submarine import Submarine
from game.enemy import Enemy
from game.jellyfish import Jellyfish
from game.projectile import Projectile


class Phase:
    def __init__(self, window, num_players, game_mode):
        self.window = window
        self.num_players = num_players
        self.game_mode = game_mode
        self.players = [Submarine(100, 300, 0, window), Submarine(100, 400, 1, window)]
        self.enemies = pygame.sprite.Group()
        self.jellyfish = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.phase_num = 1
        self.scores = [0, 0]
        self.player_health = [100, 100]
        self.font_score = pygame.font.SysFont("Lucida Sans Typewriter", 36)
        self.font_game_over = pygame.font.SysFont("Lucida Sans Typewriter", 72)
        try:
            self.background_images = [
                pygame.image.load("./assets/images/phase1_bg.png").convert(),
                # Adicione outros backgrounds para fases 2 e 3 aqui
                pygame.image.load("./assets/images/phase1_bg.png").convert(),  # Placeholder para fase 2
                pygame.image.load("./assets/images/phase1_bg.png").convert(),  # Placeholder para fase 3
            ]
            self.background = self.background_images[self.phase_num - 1]
        except FileNotFoundError:
            print("Erro ao carregar imagem de fundo da fase. Usando fundo preto.")
            self.background = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
            self.background.fill(C_BLACK)
        self.music_path = './assets/sounds/phase1_music.mp3'

    def load_music(self):
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(-1)

    def run(self):
        running = True
        self.load_music()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # Exemplo: Espaço para atirar (jogador 1)
                        projectile = Projectile(self.players[0].rect.right, self.players[0].rect.centery, 0, self.window)
                        self.projectiles.add(projectile)
                    if event.key == pygame.K_RETURN: # Exemplo: Enter para atirar jogador 2
                        if self.num_players > 1:
                            projectile = Projectile(self.players[1].rect.right, self.players[1].rect.centery, 1, self.window)
                            self.projectiles.add(projectile)

            # Desenha o background
            self.window.blit(self.background, (0, 0))

            # Atualiza e desenha jogadores
            for player in self.players:
                player.update()
                player.draw()

            # Atualiza e desenha inimigos
            for enemy in self.enemies:
                enemy.update(self.players[0].rect)  # Passa a posição do jogador para o inimigo
                enemy.draw()

            # Atualiza e desenha águas-vivas
            for jellyfish in self.jellyfish:
                jellyfish.update(self.players[0].rect)
                jellyfish.draw()

            # Atualiza e desenha projéteis
            self.projectiles.update()
            self.projectiles.draw(self.window)

            # Lógica de colisões e pontuação
            self.handle_collisions()

            # Lógica de geração de inimigos e águas-vivas
            self.spawn_enemies()
            self.spawn_jellyfish()

            # Exibe a pontuação e a saúde de cada jogador
            self.draw_scores_and_health()

            pygame.display.flip()
        pygame.mixer.music.stop()

    def handle_collisions(self):
        for projectile in self.projectiles:
            for enemy in self.enemies:
                if projectile.rect.colliderect(enemy.rect):
                    self.projectiles.remove(projectile)
                    if enemy.take_damage():
                        self.enemies.remove(enemy)
                        if projectile.player_index == 0:
                            self.scores[0] += 10  # Pontuação para o jogador 1
                        else:
                            self.scores[1] += 10  # Pontuação para o jogador 2

            for jellyfish in self.jellyfish:
                if projectile.rect.colliderect(jellyfish.rect):
                    self.projectiles.remove(projectile)
                    if jellyfish.take_damage():
                        self.jellyfish.remove(jellyfish)
                        if projectile.player_index == 0:
                            self.scores[0] += 5  # Pontuação para o jogador 1
                        else:
                            self.scores[1] += 5  # Pontuação para o jogador 2

        for player in self.players:
            for enemy in self.enemies:
                if player.rect.colliderect(enemy.rect):
                    self.player_health[player.player_index] -= 10
                    self.enemies.remove(enemy)  # Remove o inimigo após a colisão
                    if self.player_health[player.player_index] <= 0:
                        self.game_over()
            for jellyfish in self.jellyfish:
                if player.rect.colliderect(jellyfish.rect):
                    self.player_health[player.player_index] -= 5
                    self.jellyfish.remove(jellyfish)
                    if self.player_health[player.player_index] <= 0:
                        self.game_over()

    def spawn_enemies(self):
        if random.randint(0, 100) < 5:  # Controla a frequência de geração de inimigos
            enemy_type = random.randint(1, 2)  # 1 ou 2
            enemy_x = WIN_WIDTH + 50  # Spawn à direita da tela
            enemy_y = random.randint(50, WIN_HEIGHT - 50)
            enemy = Enemy(enemy_x, enemy_y, enemy_type, self.window)
            self.enemies.add(enemy)

    def spawn_jellyfish(self):
        if self.phase_num == 2 and random.randint(0, 100) < 3:  # Ajuste a probabilidade
            jellyfish_x = random.randint(0, WIN_WIDTH - 50)
            jellyfish_y = WIN_HEIGHT  # Spawn na parte inferior
            jellyfish = Jellyfish(jellyfish_x, jellyfish_y, self.window)
            self.jellyfish.add(jellyfish)

    def draw_scores_and_health(self):
        for i, player in enumerate(self.players):
            score_text = self.font_score.render(f"P{i + 1} Score: {self.scores[i]}", True, C_WHITE)
            self.window.blit(score_text, (10, 10 + i * 40))
            health_text = self.font_score.render(f"P{i + 1} Health: {self.player_health[i]}", True, C_WHITE)
            self.window.blit(health_text, (10, 50 + i * 40))

    def game_over(self):
        pygame.mixer.music.stop()
        self.window.fill(C_BLACK)  # Preenche a tela com preto
        game_over_text = self.font_game_over.render("Game Over", True, C_RED)
        text_rect = game_over_text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        self.window.blit(game_over_text, text_rect)
        pygame.display.flip()
        pygame.time.delay(3000)  # Mostra a mensagem por 3 segundos
        pygame.quit()
        exit()