import pygame
from ball import Ball
from colours import ORANGE, GREEN, RED

pygame.init()
clock = pygame.time.Clock()
display_width = 800
display_height = 600
acceleration = 0.5
velocity = 0.1
bounce = 0.5**0.5

gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill((64, 64, 64))
pygame.display.set_caption("Ball Physics Simulation")

basketball = Ball(400, 40, 35, ORANGE)
basketball.draw(gameDisplay)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        basketball.update(velocity, acceleration, bounce, display_height, gameDisplay)

