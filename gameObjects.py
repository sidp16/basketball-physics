
from colours import PURPLE
from vector import Vector
from wall import Wall

wall = Wall((100,100), (100,500), colour=PURPLE, width=1)
wall2 = Wall(startPos=(1200,800), endPos=(500,500), colour=PURPLE, width=1)
# wall3 = Wall(startPos=(600,600), endPos=(500,400), colour=PURPLE, width=1)
walls = [wall,wall2]