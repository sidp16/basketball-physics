import pygame

from ball import Ball
from colours import WHITE, ORANGE, BLUE

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill(WHITE)
pygame.display.set_caption("Ball Physics Simulation")

#pygame.draw.circle(gameDisplay, ORANGE, (400, 300), 50)

myBall = Ball(400, 300, 70, ORANGE)

myBall.draw(gameDisplay)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
