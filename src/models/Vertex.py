"""
Vertex
Where players build settlements / cities
"""
class Vertex():
    def __init__(self, pos = (0,0)):
        self.pos = pos

    def __str__(self):
        return "Vertex at " + str(self.pos)
