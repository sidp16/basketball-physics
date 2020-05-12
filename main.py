import pygame
from ball import Ball
from colours import ORANGE
from config import display_width, display_height


def clearScreen():
    gameDisplay.fill((64, 64, 64))


pygame.init()
clock = pygame.time.Clock()
bounce = 0.5 ** 0.5

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Ball Physics Simulation")

clearScreen()
basketball = Ball(x = 400, y = 40, radius = 35, colour = ORANGE, bounciness = bounce)
basketball.draw(gameDisplay)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        dit = clock.tick(60)
        basketball.update(dit / 100)
        clearScreen()
        basketball.draw(gameDisplay)
        pygame.display.update()
