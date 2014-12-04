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
        self.parity = parity
        self.v_refs = [None] * 3
        self.h_refs = [None] * 3

    def __str__(self):
        return "Vertex at " + str(self.pos)
