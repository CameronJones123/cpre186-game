# Import and initialize the pygame library
import pygame
pygame.init()
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

#Dan was here
