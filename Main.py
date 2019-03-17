"""
Instituto Tecnológico de Costa Rica (TEC)
Área Académica de Ingeniería en Computadores

Víctor Ignacio Castrillo Muñoz
Carné: 2017110244

Python 3.7.2
Pygame 1.9.3

Main File
"""

# Libraries
import pygame
from Game import *

# Settings
displayWidth = 760
displayHeight = 420
FPS = 32

# Initializing PyGame
pygame.init()

# ===== Main ===== #
def main():
    displayFlag = True

    frame = pygame.display.set_mode((displayWidth, displayHeight))
    pygame.display.set_caption('Game')
    clock = pygame.time.Clock()

    gameScreen = GameScreen(frame)

    while displayFlag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                displayFlag = False

            gameScreen.events(event)

        gameScreen.__update__()
        gameScreen.__draw__()

        pygame.display.flip()
        clock.tick(FPS)

# Executing
main()

# Quit
pygame.quit()
quit()
