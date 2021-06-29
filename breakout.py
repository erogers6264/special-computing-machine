# Import the pygame library and intialize the game engine.
import pygame
pygame.init()

# Define some colors
GREEN = (0, 255, 0)
PURPLE = (255, 255, 255)
DARKBLUE = (16, 23, 99)
YELLOW = (255, 255, 255)
RED = (255, 255, 255)
ORANGE = (255, 255, 255)

score = 0
lives = 3

# Open a new window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

# The main program loop
carryOn = True

clock = pygame.time.Clock()

while carryOn:
    # Capturing Events
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT:
            carryOn = False
    # Implementing Game Logic

    # Refreshing Screen
    screen.fill(DARKBLUE)
    
    pygame.display.flip()