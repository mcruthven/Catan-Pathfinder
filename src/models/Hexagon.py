"""
Resource 
Hexagon plate on board that contains 6 edges and 6 verticies
"""
class Hexagon:
    def __init__(self, pos = (0,0)):
        self.pos = pos
        self.vertices = [None] * 6