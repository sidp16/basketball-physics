import pygame

from ball import Ball
from colours import WHITE, ORANGE, RED

pygame.init()
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill((64,64,64))
pygame.display.set_caption("Ball Physics Simulation")


basketball = Ball(400, 50, 35, ORANGE)
basketball.draw(gameDisplay)

def redrawWindow():
    gameDisplay.fill((64, 64, 64))
    basketball.draw(gameDisplay)
    pygame.draw.line(gameDisplay, (RED), line[0],line[1])
    pygame.display.update()


while True:
    pos = pygame.mouse.get_pos()
    line = [(basketball.x, basketball.y),pos]
    redrawWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()

