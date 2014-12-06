from models import Board, Hexagon, Vertex
from views import Display
from evaluators import EvaluatorA


def GameLoop():
    pass

def DrawBoardTest():
    board = Board(4)
    EvaluatorA().evaluateBoard(board)

    # Showing the Board
    display = Display()
    display.drawBoard(board)
    display.update()

    display.wait()
    display.close()

if __name__ == "__main__":
    DrawBoardTest()

    # GameLoop()
