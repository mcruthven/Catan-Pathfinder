"""
Resource 
Hexagon plate on board that contains 6 edges and 6 verticies
"""
class Hexagon():
    def __init__(self, pos = (0,0), resource = "wood"):
        self.pos = pos
        self.vertices = [None] * 6
        self.resource = resource

    def printVertices(self):
            print "\n" + "\n".join(map(str, self.vertices))

    def __str__(self):
        return "Hexagon(" + self.resource + ") at " + str(self.pos) + " \nVertices:\n\t" + "\n\t".join(map(str, self.vertices))