"""
Vertex
Where players build settlements / cities
"""

class Vertex():
    def __init__(self, pos = (0,0), parity = False):
        """
        pos - coordinate points of the vertex
        """
        self.pos = pos
        self.parity = parity # even is true
        self.v_refs = [None] * 3
        self.h_refs = [None] * 3
        self.weight = None
        #order: wood, wheat, sheep, brick, stone, desert/none
        self.resources = [0,0,0,0,0,0]
        self.roll = {}

    def __str__(self):
        return "Vertex at " + str(self.pos)
