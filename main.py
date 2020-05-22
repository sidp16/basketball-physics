import pygame

from actions import shootBall
from ball import Ball
from colours import RED
from config import DISPLAY_WIDTH, DISPLAY_HEIGHT
from gameObjects import walls


def clearScreen():
    gameDisplay.fill((236,240,241))

basketball = Ball(x=1000, y=680, radius=18, colour=RED, bounciness=0.5**0.5)
clock = pygame.time.Clock()
pygame.init()

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Ball Physics Simulation")
clearScreen()

basketball.draw(gameDisplay)
for w in walls:
    w.draw(gameDisplay)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                basketball.addForce(y=-500)
            if event.key == pygame.K_DOWN:
                basketball.addForce(y=350)
            if event.key == pygame.K_LEFT:
                basketball.addForce(x=-350)
            if event.key == pygame.K_RIGHT:
                basketball.addForce(x=350)
            if event.key == pygame.K_SPACE:
                shootBall(basketball, 10000, 90)

    dt = clock.tick(60) # in ms, e.g 2500ms is 2.5s (diff in time since last iteration)
    factor = 0.5/100
    basketball.update(dt * factor)
    clearScreen()
    basketball.draw(gameDisplay)
    for w in walls:
        w.draw(gameDisplay)
    pygame.display.update()