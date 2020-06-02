
from colours import PURPLE, YELLOW, ORANGE, BLUE, GREEN, RED, BLACK
from vector import Vector
from wall import Wall

# wall2 = Wall(startPos=(50,300), endPos=(50,600), colour=PURPLE, width=1)
# wall = Wall(startPos=(500,300), endPos=(300,300), colour=PURPLE, width=1)
# wall3 = Wall(startPos=(50,600), endPos=(200,600), colour=PURPLE, width=1)

# v wall
wall5 = Wall(Vector(450, 200), Vector(600,500), colour=RED, width=20)
wall6 = Wall(Vector(600, 500), Vector(750,200), colour=BLACK, width=20)
wall1 = Wall(Vector(50, 200), Vector(250,200), colour=PURPLE, width=20)
wall2 = Wall(Vector(250, 200), Vector(250,500), colour=BLUE, width=20)
wall3 = Wall(Vector(250, 500), Vector(50,500), colour=BLACK, width=20)
wall4 = Wall(Vector(50, 500), Vector(50,200), colour=ORANGE, width=20)


walls = [wall1, wall2, wall3, wall4, wall5, wall6]