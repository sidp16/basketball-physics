import pygame

pygame.init()

display_width = 800
display_height = 600

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
orange = (255,165,0)

gameDisplay = pygame.display.set_mode((800,600))#
gameDisplay.fill(white)
pygame.display.set_caption("Ball Physics Simulation")

pixAr = pygame.PixelArray(gameDisplay)

pygame.draw.circle(gameDisplay, orange, (400,300),50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()