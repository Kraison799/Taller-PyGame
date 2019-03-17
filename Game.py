"""
Instituto Tecnológico de Costa Rica (TEC)
Área Académica de Ingeniería en Computadores

Víctor Ignacio Castrillo Muñoz
Carné: 2017110244

Python 3.7.2
Pygame 1.9.3

Game File
"""

# Libraries
import pygame, time

# Settings
transColor = pygame.Color(255, 0, 255)

# Initializing PyGame
pygame.init()

# ===== Player ===== #
class Player:
    def __init__(self, x, y):
        # Settings
        self.rect = pygame.Rect(x, y, 64, 64)
        self.action = 'standing'
        self.direction = 'right'
        self.falling = True
        self.jump = 0

    def __update__(self):
        # Movement
        if self.action == 'walking':
            if self.direction == 'left':
                self.rect.left -= 10
            elif self.direction == 'right':
                self.rect.left += 10

        # Gravity and Jump
        if self.falling and self.jump <= 0:
            self.rect.top += 5
        elif self.jump > 0:
            self.rect.top -= 5
            self.jump -= 5

    def __draw__(self, frame):
        pygame.draw.rect(frame, (255, 0, 0), self.rect)
"""
# ===== Enemy ===== #
class Enemy:
    def __init__(self):

    def __update__(self):

    def __draw__(self):
"""
# ===== Platforms ===== #
class Platform:
    def __init__(self, x, y, width, height):
        # Settings
        self.rect = pygame.Rect(x, y, width, height)

    def __draw__(self, frame):
        pygame.draw.rect(frame, (0, 255, 0), self.rect)

# ===== Game Screen ===== #
class GameScreen:
    def __init__(self, frame):
        # Settings
        self.frame = frame
        self.player = Player(100, 100)
        self.platforms = [Platform(0, 404, 760, 16)]
        self.gameFlag = True

    def __update__(self):
        # Gravity for Player
        self.player.falling = True
        for platform in self.platforms:
            if self.player.rect.colliderect(platform.rect):
                self.player.falling = False
                break

        self.player.__update__()

    def __draw__(self):
        self.frame.fill((0, 0, 255))
        self.player.__draw__(self.frame)
        for platform in self.platforms:
            platform.__draw__(self.frame)

    # This function manage the keyboard during the Game Screen
    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.player.action = 'walking'
                self.player.direction = 'left'
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.player.action = 'walking'
                self.player.direction = 'right'
            elif event.key == pygame.K_SPACE and self.player.jump <= 0 and not self.player.falling:
                self.player.jump = 75

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.player.action = 'standing'
                self.player.direction = 'left'
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.player.action = 'standing'
                self.player.direction = 'right'

# Quit
pygame.quit()