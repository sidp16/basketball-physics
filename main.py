import pygame

from actions import shootBall
from ball import Ball
from colours import ORANGE
from config import DISPLAY_WIDTH, DISPLAY_HEIGHT

def clearScreen():
    gameDisplay.fill((236,240,241))

pygame.init()
bounce = 0.5 ** 0.5
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Ball Physics Simulation")
clearScreen()

basketball = Ball(x=832, y=680, radius=20, colour=ORANGE, bounciness=bounce)
basketball.draw(gameDisplay)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                basketball.addForce(y=-350)
            if event.key == pygame.K_DOWN:
                basketball.addForce(y=350)
            if event.key == pygame.K_LEFT:
                basketball.addForce(x=-350)
            if event.key == pygame.K_RIGHT:
                basketball.addForce(x=350)
            if event.key == pygame.K_SPACE:
                shootBall(basketball, 5000, 45)

    dt = clock.tick(60) # in ms, e.g 2500ms is 2.5s (diff in time since last iteration)
    factor = 0.5/100
    basketball.update(dt * factor)
    clearScreen()
    basketball.draw(gameDisplay)
    pygame.display.update()