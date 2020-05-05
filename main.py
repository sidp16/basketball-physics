import pygame

pygame.init()

display_width = 800
display_height = 600

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))#
gameDisplay.fill(white)

pixAr = pygame.PixelArray(gameDisplay)

pixAr[10][20] = green

pygame.draw.line(gameDisplay, blue, (100,200), (300,450),5)
pygame.draw.rect(gameDisplay,red, (400,400,50,25))
pygame.draw.circle(gameDisplay, green, (150,150),75)
pygame.draw.polygon(gameDisplay,blue, ((25,75),(76,125),(700,120)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()