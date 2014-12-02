import unittest
from Vertex import Vertex
from Hexagon import Hexagon

"""
Constants for Board Building
"""
ROOT3 = round(3**.5, 3)
ROOT3_2 = round(ROOT3/2.0, 3)

HEXAGONS = [
    (0, ROOT3),
    (1.5, ROOT3_2),
    (1.5, -ROOT3_2),
    (0, -ROOT3),
    (-1.5, -ROOT3_2),
    (-1.5, ROOT3_2)
]

VERTICES = [
    (.5, ROOT3_2),
    (1, 0),
    (.5, -ROOT3_2),
    (-.5, -ROOT3_2),
    (-1, 0),
    (-.5, ROOT3_2)
]

"""
Board Builder Class
Generates a dictionary of Resources (Hexagons) and a dictionary of vertices
"""
class Board():
    def __init__(self, num_rings = 3):
        self.hexagons = dict()
        self.vertices = dict()
        self.build(num_rings)

    def build(self,num_rings):
        start = Hexagon((0,0))
        self.hexagons[(0,0)] = start 
        self.buildRing(start, num_rings)

        return self.hexagons

    def buildRing(self, r, depth):
        for i, vertex in enumerate(VERTICES):
            if r.vertices[i] == None:
                newPos = round(r.pos[0] + vertex[0], 3), round(r.pos[1] + vertex[1], 3)
                newV = self.vertices.get(newPos, Vertex(pos = newPos))
                r.vertices[i] = newV
                if newPos not in self.vertices:
                    self.vertices[newPos] = newV

        if depth == 0:
            return

        for i, hexagon in enumerate(HEXAGONS):
            newPos = round(r.pos[0] + hexagon[0], 3), round(r.pos[1] + hexagon[1], 3)
            newR = self.hexagons.get(newPos, Hexagon(pos = newPos))
            newR.vertices[(i + 4) % 6], newR.vertices[(i + 3) % 6] = r.vertices[i], r.vertices[(i + 1) % 6]
            self.buildRing(newR, depth - 1)
            if newPos not in self.hexagons:
                self.hexagons[newPos] = newR

""" 
Testing
"""
class TestGame(unittest.TestCase):
    def setUp(self):
        pass

    def test_building_function(self):
        ring0 = Board(0)
        ring1 = Board(1)
        ring2 = Board(2)
        ring3 = Board(3)
        ring4 = Board(4)

        self.assertEqual(len(ring0.hexagons), 1)
        self.assertEqual(len(ring1.hexagons), 7)
        self.assertEqual(len(ring2.hexagons), 19)
        self.assertEqual(len(ring3.hexagons), 37)
        self.assertEqual(len(ring4.hexagons), 61)

        self.assertEqual(len(ring0.vertices), 6)
        self.assertEqual(len(ring1.vertices), 24)
        self.assertEqual(len(ring2.vertices), 54)
        self.assertEqual(len(ring3.vertices), 96)
        self.assertEqual(len(ring4.vertices), 150)

def TestGraphBoard(board):
    x = []
    y = []
    x1 = []
    y1 = []
    for key, item in board.hexagons.items():
        x.append(key[0])
        y.append(key[1])
        for vertex in item.vertices:
            x1.append(vertex.pos[0])
            y1.append(vertex.pos[1])

    plt.plot(x,y, 'ro')
    plt.plot(x1,y1, 'bo')
    plt.show()

if __name__ == "__main__":
     #Importing here to avoid importing when not testing
    import matplotlib.pyplot as plt

    # unittest.main()
    board = Board(3)
    # center = board.vertices[]
    TestGraphBoard(board)
