import time
import pygame
from ball import Ball
from colours import ORANGE, WHITE

pygame.init()
clock = pygame.time.Clock()
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill((64,64,64))
pygame.display.set_caption("Ball Physics Simulation")

basketball = Ball(400, 10, 35, ORANGE)
basketball.draw(gameDisplay)

speed = 0.2
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    while basketball.y < display_height - basketball.radius:
        basketball.y = min(basketball.y + speed, display_height - basketball.radius)
        speed += 0.6
        basketball.draw(gameDisplay)
        pygame.display.update()
        clock.tick(60)
        gameDisplay.fill((64,64,64))
        print(basketball.y)

