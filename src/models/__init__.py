import unittest, random
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
# Relations for vertices across hexagons
RELATIONS = [
    (0,2,5,3),
    (0,4,1,3),
    (1,5,2,4),
    (3,5,2,0),
    (4,0,3,1),
    (4,2,5,1)
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

    """
    Building the Board
    """
    def build(self,num_rings):
        start = Hexagon(pos = (0,0))
        self.hexagons[(0,0)] = start 
        self.buildRing(start, num_rings)
        self.buildVertexRelations()

        materials, resourceValues = self.makeMaterialsArray(num_rings)
        random.shuffle(materials)
        random.shuffle(resourceValues)
        for i in self.hexagons:
            self.hexagons[i].resource = materials.pop()
            if self.hexagons[i].resource != "desert":
                self.hexagons[i].value = resourceValues.pop()
            else:
                self.hexagons[i].value = 7

        return self.hexagons

    def calc_resources_from_rings(self, num_rings):
        """
        Calculate number of resources from number of rings
        Rings are number of rings from the center of the board
        """
        # non positive number of rings - returns 0 resources
        if num_rings <= 0:
            return 0
        if num_rings == 1:
            return 7
        
        return 1 + 3 * num_rings * (num_rings + 1)

    def makeMaterialsArray(self,num_rings):
        manyResources = ["wood", "sheep", "wheat"]
        fewResources = ["brick","stone"]
        materials = []
        desertValue = 0

        if num_rings <= 2:
            materials.append("desert")
            desertValue = desertValue + 1
        else:
            for i in range(num_rings-1):
                materials.append("desert")
                desertValue = desertValue + 1
        for resource in manyResources:
            for i in range((self.calc_resources_from_rings(num_rings)-desertValue)/5+1):
                materials.append(resource)
        for resource in fewResources:
            for i in range((self.calc_resources_from_rings(num_rings)-desertValue)/5):
                materials.append(resource)

        manyNumbers = range(3,12)
        manyNumbers = [x for x in manyNumbers if x != 7]
        fewNumbers = [2,12]
        resourceValues = []

        for val in manyNumbers:
            for i in range((self.calc_resources_from_rings(num_rings)-desertValue)/11+1):
                resourceValues.append(val)
        for val in fewNumbers:    
            for i in range((self.calc_resources_from_rings(num_rings)-desertValue)/11):
                resourceValues.append(val)    

        return materials, resourceValues

    def buildRing(self, r, depth):
        for i, vertex in enumerate(VERTICES):
            if r.vertices[i] == None:
                newPos = round(r.pos[0] + vertex[0], 3), round(r.pos[1] + vertex[1], 3)
                newV = self.vertices.get(newPos, Vertex(pos = newPos, parity = (i % 2) == 0))
                r.vertices[i] = newV
                if newPos not in self.vertices:
                    self.vertices[newPos] = newV

        if depth == 0:
            return

        for i, hexagon in enumerate(HEXAGONS):
            newPos = round(r.pos[0] + hexagon[0], 3), round(r.pos[1] + hexagon[1], 3)
            newR = self.hexagons.get(newPos, Hexagon(pos = newPos))
            rel = RELATIONS[i]
            newR.vertices[rel[1]], newR.vertices[rel[3]] = r.vertices[rel[0]], r.vertices[rel[2]]
            self.buildRing(newR, depth - 1)
            if newPos not in self.hexagons:
                self.hexagons[newPos] = newR

    def buildVertexRelations(self):
        map(self.get_vertex_ref, self.vertices.values())

    """
    Helpers for Navigation
    """
    def get_vertex_ref(self, vertex):
        for i,j in enumerate(xrange(1 - vertex.parity, 6, 2)):
            pos = vertex.pos[0] + VERTICES[j][0], vertex.pos[1] + VERTICES[j][1]
            if vertex.v_refs[i] == None:
                vertex.v_refs[i] = self.vertices.get(pos, None)

    """
    Helpers for printing
    """
    def print_vertices(self):
        print sorted([vertex.pos for vertex in self.vertices.values()])

""" 
Testing
"""
class TestGame(unittest.TestCase):
    def setUp(self):
        self.ring0 = Board(0)
        self.ring1 = Board(1)
        self.ring2 = Board(2)
        self.ring3 = Board(3)
        self.ring4 = Board(4)

    def test_building_function(self):
        self.assertEqual(len(self.ring0.hexagons), 1)
        self.assertEqual(len(self.ring1.hexagons), 7)
        self.assertEqual(len(self.ring2.hexagons), 19)
        self.assertEqual(len(self.ring3.hexagons), 37)
        self.assertEqual(len(self.ring4.hexagons), 61)

        self.assertEqual(len(self.ring0.vertices), 6)
        self.assertEqual(len(self.ring1.vertices), 24)
        self.assertEqual(len(self.ring2.vertices), 54)
        self.assertEqual(len(self.ring3.vertices), 96)
        self.assertEqual(len(self.ring4.vertices), 150)

    def test_vertex_ref_builder(self):
        # Even Vertices
        testVertex = self.ring3.vertices[VERTICES[0]]

        self.assertEqual(testVertex.v_refs[0], self.ring3.vertices[2 * VERTICES[0][0], 2 * VERTICES[0][1]])
        self.assertEqual(testVertex.v_refs[1], self.ring3.vertices[VERTICES[1]])
        self.assertEqual(testVertex.v_refs[2], self.ring3.vertices[VERTICES[5]])

        # Odd Vertices
        testVertex = self.ring3.vertices[VERTICES[1]]

        self.assertEqual(testVertex.v_refs[0], self.ring3.vertices[2 * VERTICES[1][0], 2 * VERTICES[1][1]])
        self.assertEqual(testVertex.v_refs[1], self.ring3.vertices[VERTICES[2]])
        self.assertEqual(testVertex.v_refs[2], self.ring3.vertices[VERTICES[0]])

    def test_vertex_ref(self):
        # For Even Vertices
        testVertex = self.ring3.vertices[VERTICES[0]]

        self.ring3.get_vertex_ref(testVertex)

        self.assertEqual(testVertex.v_refs[0], self.ring3.vertices[2 * VERTICES[0][0], 2 * VERTICES[0][1]])
        self.assertEqual(testVertex.v_refs[1], self.ring3.vertices[VERTICES[1]])
        self.assertEqual(testVertex.v_refs[2], self.ring3.vertices[VERTICES[5]])

        # For Odd Vertices
        testVertex = self.ring3.vertices[VERTICES[1]]

        self.ring3.get_vertex_ref(testVertex)

        self.assertEqual(testVertex.v_refs[0], self.ring3.vertices[2 * VERTICES[1][0], 2 * VERTICES[1][1]])
        self.assertEqual(testVertex.v_refs[1], self.ring3.vertices[VERTICES[2]])
        self.assertEqual(testVertex.v_refs[2], self.ring3.vertices[VERTICES[0]])

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

    unittest.main()

    # board = Board(3)
    # TestGraphBoard(board)
