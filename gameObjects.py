
from colours import PURPLE
from vector import Vector
from wall import Wall

wall = Wall(Vector(100,100), Vector(100,500), colour=PURPLE, width=1)
# wall2 = Wall(startPos=(1200,400), endPos=(900,100), colour=PURPLE, width=1)
# wall3 = Wall(startPos=(600,600), endPos=(500,400), colour=PURPLE, width=1)
walls = [wall]