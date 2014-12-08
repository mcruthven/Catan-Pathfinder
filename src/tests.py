import unittest
from models import Board
from evaluators import EvaluatorA as EV

class TestEvaluators(unittest.TestCase):
    def setUp(self):
        self.board2 = Board(2)

    def test_evaluatorA(self):
        EV().evaluateBoard(self.board2)
        for vertex in self.board2.vertices.values():
            self.assertTrue(vertex.weight != None)


def DrawBoardTest():
    board = Board(4)
    EV().evaluateBoard(board)

    # Showing the Board
    display = Display()
    display.drawBoard(board)
    display.update()

    display.wait()
    display.close()

if __name__ == "__main__":
    # DrawBoardTest()
    unittest.main()