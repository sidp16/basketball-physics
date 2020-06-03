from math import radians

from colours import PURPLE, YELLOW, ORANGE, BLUE, GREEN, RED, BLACK
from vector import Vector
from wall import Wall

# wall2 = Wall(startPos=(50,300), endPos=(50,600), colour=PURPLE, width=1)
# wall = Wall(startPos=(500,300), endPos=(300,300), colour=PURPLE, width=1)
# wall3 = Wall(startPos=(50,600), endPos=(200,600), colour=PURPLE, width=1)

# v wall
# wall5 = Wall(Vector(450, 200), Vector(600,500), colour=RED, width=1)
# wall6 = Wall(Vector(600, 500), Vector(750,200), colour=BLACK, width=1)

# square wall
# wall1 = Wall(Vector(50, 200), Vector(250,200), colour=PURPLE, width=1)
# wall2 = Wall(Vector(250, 200), Vector(250,500), colour=BLUE, width=1)
# wall3 = Wall(Vector(250, 500), Vector(50,500), colour=BLACK, width=1)
# wall4 = Wall(Vector(50, 500), Vector(50,200), colour=ORANGE, width=1)

wall1 = Wall(Vector(800,200), Vector(1000,200), colour=BLACK, width=1)
wall2 = Wall(Vector(1000,200), Vector(1000,175), colour=BLACK, width=1)
wall3 = Wall(Vector(1000,175), Vector(800,175), colour=BLACK, width=1)
wall4 = Wall(Vector(800,175), Vector(800,200), colour=BLACK, width=1)

# walls = [wall1, wall2, wall3, wall4]
walls = []
def addRegularShape(center, radius, nSides):
    angleToTurn = 360 / nSides
    points = []
    radiusVector = Vector(radius, 0)
    for x in range(nSides):
        point = center + radiusVector
        points.append(point)
        radiusVector = radiusVector.rotate(radians(angleToTurn))

    for i in range(len(points)-1):
        walls.append(Wall(points[i], points[i+1], colour=BLACK, width=1))

    walls.append(Wall(points[-1], points[0], colour=BLACK, width=1))

addRegularShape(Vector(600,200), 50, 5)
addRegularShape(Vector(900,600), 100, 3)
addRegularShape(Vector(700,400), 200, 8)