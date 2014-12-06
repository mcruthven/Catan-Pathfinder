import unittest
from models import Board
from evaluators import EvaluatorA

class TestEvaluators(unittest.TestCase):
    def setUp(self):
        self.board2 = Board(2)

    def test_evaluatorA(self):
        EvaluatorA().evaluateBoard(self.board2)
        for vertex in self.board2.vertices.values():
            self.assertTrue(vertex.weight != None)

if __name__ == "__main__":
    unittest.main()