import time
import pygame
from ball import Ball
from colours import ORANGE, WHITE

pygame.init()
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill((64,64,64))
pygame.display.set_caption("Ball Physics Simulation")

basketball = Ball(400, 10, 35, ORANGE)
basketball.draw(gameDisplay)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    basketball.y += 1
    time.sleep(0.005)
    basketball.draw(gameDisplay)
    pygame.display.update()
    gameDisplay.fill(WHITE)
