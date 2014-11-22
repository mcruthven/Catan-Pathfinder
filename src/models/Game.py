import unittest

class GameBoard:
    def __init__(self, num_rings = 3):
        self.num_resources = self.calc_resources_from_rings(num_rings)


    """
    Helpers
    """
    def calc_resources_from_rings(self, num_rings):
        """
        Calculate number of resources from number of rings
        Rings are number of rings from the center of the board
        """
        # non positive number of rings - returns 0 resources
        if num_rings <= 0:
            return 0
        if num_rings == 1:
            return 1
        
        return 1 + 3 * num_rings * (num_rings - 1)

class Hexagon:
    """
    Coordinate System: 
    (Index)
    0   1   2   3   4   5
    z,  y,  x, -z, -y, -x - Vertices
    zy, yx, x_z, _z_y, _y_x, _xz  - Edges, Hexagons
    """
    def __init__(self, pos = (0,0,0), vertices = [0,0,0,0,0,0], edges = [0,0,0,0,0,0]):
        self.pos = pos
        self.vertices = vertices
        self.edges = edges
        self.adjacents = [None, None, None, None, None, None]

    def ref(self, other):
        """
        Reference another hexagon as an adjacent

        other - another hexagon
        returns success boolean
        """
        dx = other.pos[0] - self.pos[0]
        dy = other.pos[1] - self.pos[1]
        dz = other.pos[2] - self.pos[2]

        if dx > 1 or dx < -1 or dy > 1 or dy < -1 or dz > 1 or dz < -1:
            return False

        if dx == 1:
            pos = 1 - dz
        elif dx == -1:
            pos = -1 + dy
        else:
            if dy == 1:
                pos = 0
            else:
                pos = 3
        if self.adjacents[pos] != None:
            return False

        self.adjacents[pos] = other
        other.adjacents[(pos + 3) % 6] = self
        return True




class TestGameBoardHelpers(unittest.TestCase):
    def setUp(self):
        self.board = GameBoard()

    def test_resources_from_rings(self):
        self.assertEqual(self.board.calc_resources_from_rings(-1), 0)
        self.assertEqual(self.board.calc_resources_from_rings(0), 0)
        self.assertEqual(self.board.calc_resources_from_rings(1), 1)
        self.assertEqual(self.board.calc_resources_from_rings(2), 7)
        self.assertEqual(self.board.calc_resources_from_rings(3), 19)


class TestHexagon(unittest.TestCase):
    def setUp(self):
        self.hexagon = Hexagon(pos = (0,0,0))

    def test_resources_from_rings(self):
        testzy = Hexagon(pos = (0, 1, 1))
        testyx = Hexagon(pos = (1, 1, 0))
        testx_z = Hexagon(pos = (1, 0, -1))
        test_z_y = Hexagon(pos = (0, -1, -1)) 
        test_y_x = Hexagon(pos = (-1, -1, 0))
        test_xz = Hexagon(pos = (-1, 0, 1))

        self.hexagon.ref(testzy)
        self.hexagon.ref(testyx)
        self.hexagon.ref(testx_z)
        self.hexagon.ref(test_z_y)
        self.hexagon.ref(test_y_x)
        self.hexagon.ref(test_xz)

        self.assertEqual(self.hexagon.adjacents[0], testzy)
        self.assertEqual(self.hexagon.adjacents[1], testyx)
        self.assertEqual(self.hexagon.adjacents[2], testx_z)
        self.assertEqual(self.hexagon.adjacents[3], test_z_y)
        self.assertEqual(self.hexagon.adjacents[4], test_y_x)
        self.assertEqual(self.hexagon.adjacents[5], test_xz)

        self.assertEqual(testzy.adjacents[3], self.hexagon)
        self.assertEqual(testyx.adjacents[4], self.hexagon)
        self.assertEqual(testx_z.adjacents[5], self.hexagon)
        self.assertEqual(test_z_y.adjacents[0], self.hexagon)
        self.assertEqual(test_y_x.adjacents[1], self.hexagon)
        self.assertEqual(test_xz.adjacents[2], self.hexagon)

if __name__ == "__main__":
    unittest.main()