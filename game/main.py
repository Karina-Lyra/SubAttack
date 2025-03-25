import pygame
from game import menu
from game import phase
from game import constants

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Sub Attack")

game_menu = menu.Menu(screen)
num_players, game_mode = game_menu.run()

game_phase = phase.Phase(screen, num_players, game_mode)
game_phase.run()

pygame.quit()