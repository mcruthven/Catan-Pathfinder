from models import Board, Hexagon, Vertex
from views import Display


def GameLoop():
    pass

def DrawBoardTest():
    board = Board(4)

    # Showing the Board
    display = Display()
    display.drawBoard(board)
    display.update()

    display.wait()
    display.close()

if __name__ == "__main__":
    DrawBoardTest()

    # GameLoop()
