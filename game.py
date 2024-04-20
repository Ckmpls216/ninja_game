import pygame
import os
from player import Player

#Initialize Pygame
pygame.init()

# Define Constants
window_width = 800
window_height = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setup the display using the above variables
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption ('Ninja Game')

# Initialize Player
player = Player(window_width // 2, window_height // 2)

# Main game loop
running = True
while running:
    # Check for Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update player and render
    player.update()
    window.fill(BLACK)
    player.draw(window)
    pygame.display.flip()

# Quit Pygame
pygame.quit()