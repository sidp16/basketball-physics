import pygame
from ball import Ball
from colours import ORANGE

pygame.init()
clock = pygame.time.Clock()
display_width = 800
display_height = 600
acceleration = 0.5
nAcceleration = 1
speed = 0

gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill((64, 64, 64))
pygame.display.set_caption("Ball Physics Simulation")

basketball = Ball(400, 10, 35, ORANGE)
basketball.draw(gameDisplay)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    while basketball.y < display_height - basketball.radius:
        basketball.y = min(basketball.y + speed, display_height - basketball.radius)
        speed += acceleration
        gameDisplay.fill((64, 64, 64))
        basketball.draw(gameDisplay)
        clock.tick(60)
        pygame.display.update()
        print("STOPPED: %s" % speed)
    speed = -speed
    while speed != 0:
        print("BOUNCE: %s" % speed)
        basketball.y += speed
        speed += nAcceleration
        gameDisplay.fill((64, 64, 64))
        basketball.draw(gameDisplay)
        clock.tick(60)
        pygame.display.update()



