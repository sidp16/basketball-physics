from math import degrees, sin, cos

import pygame
from ball import Ball
from colours import ORANGE
from config import DISPLAY_WIDTH, DISPLAY_HEIGHT

def clearScreen():
    gameDisplay.fill((255, 255, 255))

# force in newtons, angle in degrees
def shootBall(ball, totalForce, angle):
    print(f"Angle:  {angle}")
    y_force = sin(angle) * totalForce
    x_force = cos(angle) * totalForce
    print(f"X force: {x_force}, Y force: {y_force}")
    ball.addForce(x_force, y_force)


pygame.init()
bounce = 0.5 ** 0.5

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Ball Physics Simulation")
clearScreen()

basketball = Ball(x=832, y=680, radius=20, colour=ORANGE, bounciness=bounce)
basketball.draw(gameDisplay)
clock = pygame.time.Clock()

shootBall(basketball,500,70)
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
                basketball.addForce(y=-2000)


    dt = clock.tick(60) # in ms, e.g 2500ms is 2.5s (diff in time since last iteration)
    factor = 0.5/100
    basketball.update(dt * factor)
    clearScreen()
    basketball.draw(gameDisplay)
    pygame.display.update()