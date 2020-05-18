import pygame
from ball import Ball
from colours import ORANGE
from config import DISPLAY_WIDTH, DISPLAY_HEIGHT

def clearScreen():
    gameDisplay.fill((255,255,255))

# force in newtons, angle in degrees
def shootBall(ball, force, angle):
    pass

pygame.init()
clock = pygame.time.Clock()
bounce = 0.5 ** 0.5

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Ball Physics Simulation")
clearScreen()

basketball = Ball(x=100, y=DISPLAY_HEIGHT-20, radius=20, colour=ORANGE, bounciness=bounce)
basketball.draw(gameDisplay)
basketball.addForceX(+100)
# timePassed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                basketball.addForceY(-200)
            if event.key == pygame.K_DOWN:
                basketball.addForceY(+200)
            if event.key == pygame.K_LEFT:
                basketball.addForceX(-200)
            if event.key == pygame.K_RIGHT:
                basketball.addForceX(+200)
            if event.key == pygame.K_SPACE:
                basketball.addForceY(-500)

    dt = clock.tick(60) # in ms, e.g 2500ms is 2.5s (diff in time since last iteration)

    # timePassed += dt
    # if timePassed > 1000:
    #     print(f"{timePassed} - {display_height - basketball.y:.2f}m at {basketball.velocity:.2f}m/s")
    #     timePassed = 0

    factor = 1/100
    basketball.update(dt * factor)
    clearScreen()
    basketball.draw(gameDisplay)
    pygame.display.update()