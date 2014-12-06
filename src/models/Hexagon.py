"""
Resource 
Hexagon plate on board that contains 6 edges and 6 verticies
"""
from Empty import Empty

class Hexagon():
    def __init__(self, pos = (0,0), resource = None, value = None):
        self.pos = pos
        self.vertices = [None] * 6
        self.resource = resource
        self.value = value

    def printVertices(self):
        print "\n" + "\n".join(map(str, self.vertices))

    def __int__(self):
        return 7 if self.resource == "desert" else abs(7 - self.value) 

    def __str__(self):
        return "Hexagon(" + self.resource + ") at " + str(self.pos) + " \nVertices:\n\t" + "\n\t".join(map(str, self.vertices))