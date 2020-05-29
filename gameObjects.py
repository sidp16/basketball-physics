
from colours import PURPLE
from vector import Vector
from wall import Wall

wall2 = Wall(startPos=(50,100), endPos=(1200,100), colour=PURPLE, width=1)
wall = Wall(startPos=(50,200), endPos=(1200,200), colour=PURPLE, width=1)

# wall3 = Wall(startPos=(600,600), endPos=(500,400), colour=PURPLE, width=1)
walls = [wall,wall2]