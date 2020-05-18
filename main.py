import pygame
from ball import Ball
from colours import ORANGE, GREEN, RED
from config import display_width, display_height


def clearScreen():
    gameDisplay.fill((255,255,255))


pygame.init()

clock = pygame.time.Clock()
bounce = 0.3 ** 0.5

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Ball Physics Simulation")

clearScreen()
basketball = Ball(x=450, y=150, radius=50, colour=ORANGE, bounciness=bounce)
tennis = Ball(x=350, y=150, radius=30, colour=GREEN, bounciness=0.6 ** 0.5)
cricket = Ball(x=550, y=150, radius=30, colour=RED, bounciness=0.07 ** 0.5)

basketball.draw(gameDisplay)
tennis.draw(gameDisplay)
cricket.draw(gameDisplay)
# print("ORIGINAL HEIGHT :", display_height - basketball.y)
# timePassed = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            basketball.addForce(-300)
            tennis.addForce(-300)
            cricket.addForce(-300)

    dt = clock.tick(60) # in ms, e.g 2500ms is 2.5s

    # timePassed += dt
    # if timePassed > 1000:
    #     print(f"{timePassed} - {display_height - basketball.y:.2f}m at {basketball.velocity:.2f}m/s")
    #     timePassed = 0

    factor = 1/100
    basketball.update(dt * factor)
    tennis.update(dt * factor)
    cricket.update(dt * factor)
    clearScreen()
    basketball.draw(gameDisplay)
    tennis.draw(gameDisplay)
    cricket.draw(gameDisplay)
    pygame.display.update()