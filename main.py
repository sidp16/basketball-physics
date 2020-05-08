import pygame
from ball import Ball
from colours import ORANGE

pygame.init()
clock = pygame.time.Clock()
display_width = 800
display_height = 600
acceleration = 0.5
velocity = 0
bounce = 0.5**0.5

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
        basketball.y = min(basketball.y + velocity, display_height - basketball.radius)
        velocity += acceleration
        gameDisplay.fill((64, 64, 64))
        basketball.draw(gameDisplay)
        clock.tick(60)
        pygame.display.update()
        print(f"speed: {velocity} | pos: {basketball.y} | going down")

    velocity = -velocity * bounce
    if abs(velocity) < 2.15:
        continue

    while velocity < 0:
        print(f"speed: {velocity} | pos: {basketball.y} | going up")
        basketball.y += velocity
        velocity += acceleration
        gameDisplay.fill((64, 64, 64))
        basketball.draw(gameDisplay)
        clock.tick(60)
        pygame.display.update()