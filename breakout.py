# Import the pygame library and intialize the game engine.
import pygame
pygame.init()

# Define some colors
GREEN = (255, 255, 255)
PURPLE = (255, 255, 255)
DARKBLUE = (255, 255, 255)
YELLOW = (255, 255, 255)
RED = (255, 255, 255)
ORANGE = (255, 255, 255)

score = 0
lives = 3

# Open a new window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")
