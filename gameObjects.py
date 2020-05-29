
from colours import PURPLE
from vector import Vector
from wall import Wall

# wall2 = Wall(startPos=(50,300), endPos=(50,600), colour=PURPLE, width=1)
# wall = Wall(startPos=(500,300), endPos=(300,300), colour=PURPLE, width=1)
# wall3 = Wall(startPos=(50,600), endPos=(200,600), colour=PURPLE, width=1)

# v wall
wall1 = Wall((50, 200), (200,500), colour=PURPLE, width=1)
wall2 = Wall((200, 500), (350,200), colour=PURPLE, width=1)

#square
wall1 = Wall((50, 200), (250,200), colour=PURPLE, width=1)
wall2 = Wall((250, 200), (250,500), colour=PURPLE, width=1)
wall3 = Wall((250, 500), (50,500), colour=PURPLE, width=1)
wall4 = Wall((50, 500), (50,200), colour=PURPLE, width=1)


walls = [wall1, wall2, wall3, wall4]