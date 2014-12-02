from models import Board, Hexagon, Vertex
from views import Display


def GameLoop():
    pass

def DrawBoardTest():
    board = Board(5)

    # Showing the Board
    display = Display()
    display.drawBoard(board)

    display.wait()
    display.close()

if __name__ == "__main__":
    # DrawBoardTest()

    GameLoop()
