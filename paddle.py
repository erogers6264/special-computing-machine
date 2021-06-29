import pygame

BLACK = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        
        # Pass in the color of the paddle
        # and its x and y position, w & h...
        self.surface = pygame.Surface([width, height])
        self.surface.fill(BLACK)
        self.surface.set_colorkey(BLACK)
        
        # Draw the paddle as a rectangle
        pygame.draw.rect(self.surface, color, [0, 0, width, height])
        
        # Fetch the rectangle object that has the dimensions of
        # the image
        self.rect = self.surface.get_rect()