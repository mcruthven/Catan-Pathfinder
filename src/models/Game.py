import unittest

import numpy as np
import matplotlib.pyplot as plt

RESOURCES_STEP = [(2,1),(1,2),(-1,1),(-2,-1),(-1,-2),(1,-1)]
BUILDING_STEP = [(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]

class Board:
    def __init__(self, num_rings = 3):
        self.resources = dict()  
        self.buildings = dict()

        # Build the dictionaries
        if num_rings > 0:
            self.resources[(0,0)] = Resource()
            self.createGrid((0,0), num_rings)

    def createGrid(self, start, depth):
        for n_step in BUILDING_STEP:
            n_new = start[0] + n_step[0], start[1] + n_step[1]
            if n_new not in self.buildings:
                self.buildings[n_new] = Building()

        if depth < 2:
            return

        for h_step in RESOURCES_STEP:
                    h_new = start[0] + h_step[0], start[1] + h_step[1]
                    if h_new not in self.resources:
                        self.resources[h_new] = Resource()
                    self.createGrid(h_new, depth - 1)
                

class Building:
    def __init__(self):
        pass
        
class Resource:
    def __init__(self):
        pass

class TestGame(unittest.TestCase):
    def setUp(self):
        pass

    def test_building_function(self):
        ring0 = Board(0)
        ring1 = Board(1)
        ring2 = Board(2)
        ring3 = Board(3)
        ring4 = Board(4)

        self.assertEqual(len(ring0.resources), 0)
        self.assertEqual(len(ring1.resources), 1)
        self.assertEqual(len(ring2.resources), 7)
        self.assertEqual(len(ring3.resources), 19)
        self.assertEqual(len(ring4.resources), 37)

        self.assertEqual(len(ring0.buildings), 0)
        self.assertEqual(len(ring1.buildings), 6)
        self.assertEqual(len(ring2.buildings), 24)
        self.assertEqual(len(ring3.buildings), 54)
        self.assertEqual(len(ring4.buildings), 96)


def BoardGraphTest():
    board = Board()
    x = []
    y = []
    x1 = []
    y1 = []
    for key, item in board.resources.items():
        x.append(key[0])
        y.append(key[1])
    for key, item in board.buildings.items():
        x1.append(key[0])
        y1.append(key[1])
    plt.plot(x,y, 'ro')
    plt.plot(x1,y1, 'bo')
    plt.axis([-6, 6, -7, 7])
    plt.show()

if __name__ == "__main__":
    # BoardGraphTest()
    unittest.main()


