# Import the pygame library and intialize the game engine.
import pygame
pygame.init()

# Define some colors
GREEN = (0, 255, 0)
PURPLE = (255, 255, 255)
DARKBLUE = (16, 23, 99)
YELLOW = (255, 255, 255)
RED = (255, 255, 255)
WHITE = (255, 255, 255)
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
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20, 10))

    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650, 10))

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
