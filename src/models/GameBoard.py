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

class TestGameBoardHelpers(unittest.TestCase):
    def setUp(self):
        self.board = GameBoard()

    def test_resources_from_rings(self):
        self.assertEqual(self.board.calc_resources_from_rings(-1), 0)
        self.assertEqual(self.board.calc_resources_from_rings(0), 0)
        self.assertEqual(self.board.calc_resources_from_rings(1), 1)
        self.assertEqual(self.board.calc_resources_from_rings(2), 7)
        self.assertEqual(self.board.calc_resources_from_rings(3), 19)

if __name__ == "__main__":
    unittest.main()