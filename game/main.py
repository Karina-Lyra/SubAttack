import pygame
import os
from game.menu import Menu
from game.phase import Phase
from game.constants import WIN_WIDTH, WIN_HEIGHT


def main():
    # Inicializa o pygame
    pygame.init()
    pygame.mixer.init()

    # Define o diretório do projeto como diretório de trabalho
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Cria a janela do jogo
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Sub Attack")

    # Cria o objeto Menu
    game_menu = Menu(window)

    # Executa o menu e obtém a opção selecionada
    selected_option = game_menu.run()

    # Verifica a opção selecionada e inicia a fase correspondente
    if selected_option == "NEW GAME":
        num_players = 2  # Ou obtenha isso do menu se você adicionar a opção de 1 jogador
        game_mode = "competitive"  # Ou obtenha isso do menu se você tiver diferentes modos de jogo
        game_phase = Phase(window, num_players, game_mode)
        game_phase.run()
    elif selected_option == "SCORE":
        print("Mostrar Score")  # Adicione sua lógica para mostrar a pontuação
    elif selected_option == "EXIT":
        pygame.quit()

    # Finaliza o pygame
    pygame.quit()
